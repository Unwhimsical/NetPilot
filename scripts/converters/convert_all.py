#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
NetPilot 格式转换器：Shadowrocket .sgmodule -> Surge / Loon / Clash(Mihomo)

设计原则：
- 只读源文件（modules/*.module），绝不修改源文件与现有更新流水线。
- 纯标准库、无时间戳、无随机因素：相同输入必产生相同输出（幂等）。
- 每个格式独立生成，单个格式失败不影响其他格式；失败在汇总中醒目标记。
- 所有丢弃/降级都有计数，汇总输出为 Markdown 表格（供 CI 日志与 Step Summary 使用）。

用法：
  python3 convert_all.py [--root .] [--verify-idempotent]
"""

import argparse
import csv
import io
import os
import re
import sys
import tempfile

# ---------------------------------------------------------------- 源解析

SECTION_ORDER = ["Rule", "URL Rewrite", "Script", "MITM", "Host", "General"]

KNOWN_RULE_TYPES = {
    "DOMAIN", "DOMAIN-SUFFIX", "DOMAIN-KEYWORD", "DOMAIN-REGEX",
    "IP-CIDR", "IP-CIDR6", "GEOIP", "USER-AGENT", "URL-REGEX",
    "PROCESS-NAME", "PROTOCOL", "DEST-PORT", "SRC-IP-CIDR",
    "FINAL", "AND", "OR", "NOT", "SUBNET", "HOSTNAME-TYPE",
}

REJECT_FAMILY = {"REJECT", "REJECT-DROP", "REJECT-NO-DROP", "REJECT-200", "REJECT-DICT", "REJECT-IMG", "REJECT-ARRAY"}


class Module:
    """一个 .sgmodule 源文件的解析结果（保留原始行，转换时不重新序列化规则行）。"""

    def __init__(self, path):
        self.path = path
        self.name = ""
        self.desc = ""
        self.sections = {}  # section -> [raw line, ...]（含注释与空行）
        self._parse()

    def _parse(self):
        with open(self.path, "r", encoding="utf-8", errors="replace") as f:
            lines = f.read().splitlines()
        current = None
        for line in lines:
            m = re.match(r"^\[(.+)\]\s*$", line.strip())
            if m:
                current = m.group(1).strip()
                self.sections.setdefault(current, [])
                continue
            if current is None:
                if line.startswith("#!name="):
                    self.name = line[len("#!name="):].strip()
                elif line.startswith("#!desc="):
                    self.desc = line[len("#!desc="):].strip()
                continue
            self.sections[current].append(line)

    def data_lines(self, section):
        """某段的有效数据行：去掉空行与注释行，保留原始文本。"""
        out = []
        for line in self.sections.get(section, []):
            s = line.strip()
            if not s or s.startswith("#") or s.startswith(";") or s.startswith("//"):
                continue
            out.append(line.rstrip())
        return out

    def raw_section(self, section):
        """某段原始行（供直通格式使用）：去掉“# 更新时间”行以保证输出稳定。"""
        out = []
        for line in self.sections.get(section, []):
            if line.strip().startswith("# 更新时间"):
                continue
            out.append(line.rstrip())
        while out and not out[-1].strip():
            out.pop()
        return out


def parse_rule_line(line):
    """按 CSV 规则解析一条规则行（URL-REGEX 等值中可能带引号与逗号）。
    返回 dict(type, value, policy, extras) 或 None。"""
    try:
        row = next(csv.reader(io.StringIO(line.strip())))
    except Exception:
        return None
    row = [c.strip() for c in row]
    if len(row) < 3:
        return None
    return {"type": row[0].upper(), "value": row[1], "policy": row[2].upper(), "extras": row[3:]}


class Stats:
    def __init__(self):
        self.rows = []  # (模块, 段/类别, 输入, 输出, 丢弃说明)

    def add(self, module, category, in_n, out_n, note=""):
        dropped = in_n - out_n
        note = note or ("丢弃 %d" % dropped if dropped else "-")
        self.rows.append((module, category, in_n, out_n, note))


# ---------------------------------------------------------------- Surge

def emit_surge(mod, out_path, stats):
    """Surge 与源同语法：直通 + 合规校验。源 [MITM] 已是 %APPEND% 写法。"""
    lines = []
    lines.append("#!name=" + (mod.name or os.path.basename(mod.path)))
    if mod.desc:
        lines.append("#!desc=" + mod.desc)
    lines.append("# 由 NetPilot 转换器自 Shadowrocket 模块自动生成（Surge 合规版），源更新后自动同步，请勿手动编辑。")
    lines.append("")
    for sec in SECTION_ORDER:
        if sec not in mod.sections:
            continue
        lines.append("[%s]" % ("URL Rewrite" if sec == "URL Rewrite" else sec))
        lines.extend(mod.raw_section(sec))
        lines.append("")
        # 校验计数
        data = mod.data_lines(sec)
        if sec == "Rule":
            bad = sum(1 for ln in data if not parse_rule_line(ln))
            unknown = sum(1 for ln in data
                          if parse_rule_line(ln) and parse_rule_line(ln)["type"] not in KNOWN_RULE_TYPES)
            note = []
            if bad:
                note.append("无法解析 %d 行（原样保留）" % bad)
            if unknown:
                note.append("未知规则类型 %d 行（原样保留）" % unknown)
            stats.add(os.path.basename(mod.path), "Surge 规则", len(data), len(data),
                      "；".join(note) if note else "-")
        elif sec == "Script":
            weird = sum(1 for ln in data if "script-path=" not in ln)
            stats.add(os.path.basename(mod.path), "Surge 脚本", len(data), len(data),
                      "源行格式异常 %d 条（原样保留）" % weird if weird else "-")
    write_file(out_path, "\n".join(lines).rstrip() + "\n")


# ---------------------------------------------------------------- Loon

SCRIPT_PARAM_KEYS = {"script-path", "requires-body", "max-size", "argument",
                     "binary-body-mode", "enable", "timeout"}


def parse_script_line(line):
    """解析 Shadowrocket/Surge 脚本行 Name=type=T,pattern=P,k=v,...
    pattern 值可含逗号：按已知参数键切分。返回 dict 或 None。"""
    if "=" not in line:
        return None
    name, rest = line.split("=", 1)
    name = name.strip()
    rest = rest.strip()
    if not rest.startswith("type="):
        return None
    tokens = rest.split(",")
    fields = {}
    order = []
    cur_key = None
    for tok in tokens:
        m = re.match(r"^([a-zA-Z-]+)=(.*)$", tok)
        if m and (cur_key is None or m.group(1) in SCRIPT_PARAM_KEYS or m.group(1) == "type" or (cur_key == "type")):
            cur_key = m.group(1)
            fields[cur_key] = m.group(2)
            order.append(cur_key)
        elif cur_key is not None:
            fields[cur_key] += "," + tok
        else:
            return None
    if "type" not in fields or "script-path" not in fields:
        return None
    fields["name"] = name
    fields["_order"] = order
    return fields


def script_line_to_loon(f):
    """Loon [Script] 语法：type pattern script-path=..., requires-body=true, tag=名称"""
    parts = [f["type"]]
    if f.get("pattern"):
        parts.append(f["pattern"])
    kv = ["script-path=" + f["script-path"]]
    if "requires-body" in f:
        kv.append("requires-body=" + ("true" if f["requires-body"] in ("1", "true", "True") else "false"))
    for k in f["_order"]:
        if k in ("type", "pattern", "script-path", "requires-body"):
            continue
        kv.append("%s=%s" % (k, f[k]))
    kv.append("tag=" + f["name"])
    return " ".join(parts[:2]) + " " + ", ".join(kv) if len(parts) > 1 else parts[0] + " " + ", ".join(kv)


def emit_loon(mod, out_path, stats):
    base = os.path.basename(mod.path)
    lines = []
    name = (mod.name or base) + " (Loon)"
    lines.append("#!name=" + name)
    if mod.desc:
        lines.append("#!desc=" + mod.desc)
    lines.append("# 由 NetPilot 转换器自 Shadowrocket 模块自动生成，源更新后自动同步，请勿手动编辑。")
    lines.append("")

    # [Rule] 直通
    rules = mod.data_lines("Rule")
    if rules:
        lines.append("[Rule]")
        lines.extend(rules)
        lines.append("")
        stats.add(base, "Loon 规则", len(rules), len(rules))

    # [URL Rewrite] -> [Rewrite] 直通（Surge 风格行，待真机验证后如需再调整映射）
    rewrites = mod.data_lines("URL Rewrite")
    if rewrites:
        lines.append("[Rewrite]")
        lines.extend(rewrites)
        lines.append("")
        stats.add(base, "Loon 重写", len(rewrites), len(rewrites))

    # [Script] 结构转换
    scripts = mod.data_lines("Script")
    if scripts:
        out, dropped = [], 0
        for ln in scripts:
            f = parse_script_line(ln)
            if f is None:
                dropped += 1
                continue
            out.append(script_line_to_loon(f))
        lines.append("[Script]")
        lines.extend(out)
        lines.append("")
        stats.add(base, "Loon 脚本", len(scripts), len(out),
                  "源行格式异常丢弃 %d 条" % dropped if dropped else "-")

    # [MITM] 去掉 %APPEND% 与 enable 行
    mitm = mod.data_lines("MITM")
    if mitm:
        hosts = []
        for ln in mitm:
            if ln.strip().lower().startswith("hostname"):
                _, _, v = ln.partition("=")
                v = v.strip()
                if v.startswith("%APPEND%"):
                    v = v[len("%APPEND%"):].strip()
                hosts = [h.strip() for h in v.split(",") if h.strip()]
        lines.append("[MITM]")
        if hosts:
            lines.append("hostname = " + ", ".join(hosts))
        lines.append("")
        stats.add(base, "Loon MITM 域名", len(hosts), len(hosts))
    write_file(out_path, "\n".join(lines).rstrip() + "\n")


# ---------------------------------------------------------------- Clash / Mihomo

def yaml_quote(s):
    return "'" + s.replace("'", "''") + "'"


def collect_clash(modules, stats):
    """按策略分片收集规则。返回 {分片名: set(payload 条目)}。"""
    buckets = {"Ads": set(), "Proxy": set(), "Direct": set()}
    counters = {}
    for mod in modules:
        base = os.path.basename(mod.path)
        for ln in mod.data_lines("Rule"):
            r = parse_rule_line(ln)
            if r is None:
                counters["无法解析"] = counters.get("无法解析", 0) + 1
                continue
            pol = r["policy"]
            if pol in REJECT_FAMILY:
                bucket = "Ads"
                if pol not in ("REJECT", "REJECT-DROP"):
                    counters["REJECT 变体降级为 REJECT"] = counters.get("REJECT 变体降级为 REJECT", 0) + 1
            elif pol == "PROXY":
                bucket = "Proxy"
            elif pol == "DIRECT":
                bucket = "Direct"
            else:
                counters["未知策略丢弃"] = counters.get("未知策略丢弃", 0) + 1
                continue
            t, v = r["type"], r["value"]
            if t == "URL-REGEX":
                counters["URL-REGEX 丢弃（Clash 语义不等价）"] = counters.get("URL-REGEX 丢弃（Clash 语义不等价）", 0) + 1
                continue
            if t not in KNOWN_RULE_TYPES:
                counters["未知类型丢弃"] = counters.get("未知类型丢弃", 0) + 1
                continue
            entry = "%s,%s" % (t, v)
            for ex in r["extras"]:
                entry += "," + ex
            if entry in buckets[bucket]:
                counters["重复去重"] = counters.get("重复去重", 0) + 1
            buckets[bucket].add(entry)
        stats.add(base, "Clash 输入规则", len(mod.data_lines("Rule")), len(mod.data_lines("Rule")))
    return buckets, counters


def emit_clash_provider(path, title, entries):
    lines = []
    lines.append("# NetPilot %s（由 Shadowrocket 模块自动转换，源更新后自动同步，请勿手动编辑）" % title)
    lines.append("# 条目数：%d" % len(entries))
    lines.append("payload:")
    for e in sorted(entries):
        lines.append("  - " + yaml_quote(e))
    write_file(path, "\n".join(lines) + "\n")


# ---------------------------------------------------------------- Quantumult X

QX_TYPE_MAP = {
    "DOMAIN": "host",
    "DOMAIN-SUFFIX": "host-suffix",
    "DOMAIN-KEYWORD": "host-keyword",
    "IP-CIDR": "ip-cidr",
    "IP-CIDR6": "ip6-cidr",
    "GEOIP": "geoip",
    "USER-AGENT": "user-agent",
}


def collect_quanx(modules, stats):
    """按策略分片收集 QX filter 条目。返回 (buckets, counters)。"""
    buckets = {"Ads": set(), "Proxy": set(), "Direct": set()}
    counters = {}
    for mod in modules:
        for ln in mod.data_lines("Rule"):
            r = parse_rule_line(ln)
            if r is None:
                counters["无法解析"] = counters.get("无法解析", 0) + 1
                continue
            pol = r["policy"]
            if pol in REJECT_FAMILY:
                bucket, qpol = "Ads", "reject"
                if pol not in ("REJECT", "REJECT-DROP"):
                    counters["REJECT 变体降级为 reject"] = counters.get("REJECT 变体降级为 reject", 0) + 1
            elif pol == "PROXY":
                bucket, qpol = "Proxy", "proxy"
            elif pol == "DIRECT":
                bucket, qpol = "Direct", "direct"
            else:
                counters["未知策略丢弃"] = counters.get("未知策略丢弃", 0) + 1
                continue
            t = r["type"]
            if t == "URL-REGEX":
                counters["URL-REGEX 丢弃（QX filter 不支持）"] = counters.get("URL-REGEX 丢弃（QX filter 不支持）", 0) + 1
                continue
            if t not in QX_TYPE_MAP:
                counters["QX 不支持的类型丢弃"] = counters.get("QX 不支持的类型丢弃", 0) + 1
                continue
            v = r["value"].lower() if t == "GEOIP" else r["value"]
            entry = "%s, %s, %s" % (QX_TYPE_MAP[t], v, qpol)
            for ex in r["extras"]:
                entry += ", " + ex
            if entry in buckets[bucket]:
                counters["重复去重"] = counters.get("重复去重", 0) + 1
            buckets[bucket].add(entry)
    return buckets, counters


def emit_quanx_list(path, title, entries):
    lines = ["# NetPilot %s（由 Shadowrocket 模块自动转换，源更新后自动同步，请勿手动编辑）" % title,
             "# 条目数：%d" % len(entries)]
    lines.extend(sorted(entries))
    write_file(path, "\n".join(lines) + "\n")


def emit_quanx(modules, root, stats):
    shield = modules[0]
    buckets, counters = collect_quanx(modules, stats)

    # 全量分片
    titles = {"Ads": "去广告过滤器（reject）", "Proxy": "代理过滤器（proxy）", "Direct": "直连过滤器（direct）"}
    for name, entries in buckets.items():
        emit_quanx_list(os.path.join(root, "quanx", "filter", "NetPilot_%s.list" % name),
                        titles[name], entries)

    # 精简版广告过滤器：仅 2 段域名（注册域层级）的 host-suffix + 全部 host 精确规则，
    # 覆盖主要广告网络，条目约为全量广告的四成，供低内存设备选用。
    lite = set()
    for e in buckets["Ads"]:
        parts = [p.strip() for p in e.split(",")]
        if parts[0] == "host":
            lite.add(e)
        elif parts[0] == "host-suffix" and parts[1].count(".") == 1:
            lite.add(e)
    emit_quanx_list(os.path.join(root, "quanx", "filter", "NetPilot_Ads_Lite.list"),
                    "去广告过滤器·精简版（仅注册域层级，约全量四成）", lite)
    counters["精简版条目"] = len(lite)

    # 重写：[URL Rewrite] -> QX rewrite 语法。源里混有两种写法：
    # 两段式“正则 reject*”（Surge 原生写法，QX 恰好同格式）与三段式“正则 _ 动作”/“正则 目标 状态码”。
    rewrites = shield.data_lines("URL Rewrite")
    out, dropped = [], 0
    for ln in rewrites:
        fields = ln.strip().split()
        if len(fields) == 2 and fields[1].lower().startswith("reject"):
            out.append("%s %s" % (fields[0], fields[1].lower()))
        elif len(fields) == 3 and fields[1] == "_" and fields[2].lower().startswith("reject"):
            out.append("%s %s" % (fields[0], fields[2].lower()))
        elif len(fields) == 3 and fields[2] in ("302", "307"):
            out.append("%s %s %s" % (fields[0], fields[2], fields[1]))
        else:
            dropped += 1
    lines = ["# NetPilot 重写（由 Shadowrocket 模块 [URL Rewrite] 自动转换，请勿手动编辑）",
             "# 条目数：%d" % len(out)]
    lines.extend(out)
    write_file(os.path.join(root, "quanx", "rewrite", "NetPilot_Rewrite.conf"), "\n".join(lines) + "\n")
    stats.add("NetPilot_Shield.module", "QX 重写", len(rewrites), len(out),
              "QX 无对应写法丢弃 %d 条" % dropped if dropped else "-")

    # 脚本：[Script] -> QX rewrite 的 script-response-body 行
    scripts = shield.data_lines("Script")
    out, dropped = [], 0
    for ln in scripts:
        f = parse_script_line(ln)
        if f is None:
            dropped += 1
            continue
        kind = "script-response-body" if f.get("requires-body") in ("1", "true", "True") \
            else "script-response-header"
        out.append("%s url %s %s" % (f["pattern"], kind, f["script-path"]))
    lines = ["# NetPilot 脚本重写（由 Shadowrocket 模块 [Script] 自动转换，请勿手动编辑）",
             "# 条目数：%d（QX 的脚本 API 与 Shadowrocket 不完全一致，个别脚本可能需人工适配）" % len(out)]
    lines.extend(out)
    write_file(os.path.join(root, "quanx", "rewrite", "NetPilot_Scripts.conf"), "\n".join(lines) + "\n")
    stats.add("NetPilot_Shield.module", "QX 脚本", len(scripts), len(out),
              "源行格式异常丢弃 %d 条" % dropped if dropped else "-")

    # MITM 域名清单（粘贴到 QX 配置的 [mitm] hostname 后）
    hosts = []
    for ln in shield.data_lines("MITM"):
        if ln.strip().lower().startswith("hostname"):
            _, _, v = ln.partition("=")
            v = v.strip()
            if v.startswith("%APPEND%"):
                v = v[len("%APPEND%"):].strip()
            hosts = [h.strip() for h in v.split(",") if h.strip()]
    write_file(os.path.join(root, "quanx", "mitm_hostname.txt"),
               "# NetPilot MITM 域名清单：把下面一行粘贴到 Quantumult X 配置 [mitm] 段的 hostname = 之后\n"
               + ", ".join(hosts) + "\n")
    stats.add("NetPilot_Shield.module", "QX MITM 域名", len(hosts), len(hosts))

    gen_readme(os.path.join(root, "quanx", "README.md"), "NetPilot · Quantumult X 版",
               "由 Shadowrocket 模块自动转换。filter/ 为按策略分片的过滤器（Ads/Proxy/Direct），"
               "另有去广告精简版 Ads_Lite（仅注册域层级，约全量四成，适合低内存设备）；"
               "rewrite/ 为重写与脚本；mitm_hostname.txt 为解密域名清单。",
               [("Ads 过滤器", len(buckets["Ads"])), ("Proxy 过滤器", len(buckets["Proxy"])),
                ("Direct 过滤器", len(buckets["Direct"])), ("Ads 精简版", len(lite))],
                   "Quantumult X → 设置 → 引用：过滤器引用订阅 filter/*.list，"
                   "重写引用订阅 rewrite/*.conf。过滤器中的策略名 proxy 需要你在 QX 里有同名策略组，"
                   "或在订阅引用时用 QX 的策略映射改成你自己的组名。")
    return counters


# ---------------------------------------------------------------- 通用

def write_file(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(content)


def gen_readme(path, title, intro, counts, usage):
    lines = ["# " + title, "", intro, "", "## 内容", ""]
    for k, v in counts:
        lines.append("- %s：%d" % (k, v))
    lines += ["", "## 用法", "", usage, "",
              "> 本目录文件由转换器自动生成，源文件更新后自动同步，请勿手动编辑。"]
    write_file(path, "\n".join(lines) + "\n")


def generate(root):
    """执行全部转换，返回 (stats, failures[list], clash_counters)。"""
    stats = Stats()
    failures = []
    modules_dir = os.path.join(root, "modules")
    shield = Module(os.path.join(modules_dir, "NetPilot_Shield.module"))
    direct = Module(os.path.join(modules_dir, "NetPilot_Direct.module"))
    mods = [shield, direct]

    # ---- Surge
    try:
        for mod, fn in ((shield, "NetPilot_Shield.module"), (direct, "NetPilot_Direct.module")):
            emit_surge(mod, os.path.join(root, "surge", fn), stats)
        gen_readme(os.path.join(root, "surge", "README.md"), "NetPilot · Surge 版",
                   "与 Shadowrocket 源模块同语法、经合规校验的 Surge 模块，订阅链接即为本目录文件的 raw 地址。",
                   [("Shield 模块", len(shield.data_lines("Rule"))), ("Direct 模块", len(direct.data_lines("Rule")))],
                   "Surge → 配置 → 模块 → 从 URL 安装，填入 .module 文件的链接。")
    except Exception as e:  # noqa: BLE001
        failures.append("Surge: %s" % e)

    # ---- Loon
    try:
        for mod, fn in ((shield, "NetPilot_Shield.plugin"), (direct, "NetPilot_Direct.plugin")):
            emit_loon(mod, os.path.join(root, "loon", fn), stats)
        gen_readme(os.path.join(root, "loon", "README.md"), "NetPilot · Loon 版",
                   "由 Shadowrocket 模块自动转换的 Loon 插件：规则与重写直通映射，脚本段已转换为 Loon 语法，MITM 域名已合并。",
                   [("Shield 规则", len(shield.data_lines("Rule"))), ("Direct 规则", len(direct.data_lines("Rule")))],
                   "Loon → 设置 → 插件 → 添加，填入 .plugin 文件的链接。")
    except Exception as e:  # noqa: BLE001
        failures.append("Loon: %s" % e)

    # ---- Clash / Mihomo
    clash_counters = {}
    try:
        buckets, clash_counters = collect_clash(mods, stats)
        titles = {"Ads": "去广告规则集（REJECT）", "Proxy": "代理规则集（PROXY）", "Direct": "直连规则集（DIRECT）"}
        for name, entries in buckets.items():
            emit_clash_provider(os.path.join(root, "clash", "NetPilot_%s.yaml" % name),
                                titles[name], entries)
        gen_readme(os.path.join(root, "clash", "README.md"), "NetPilot · Clash / Mihomo 规则集",
                   "按策略分片的 Rule Provider（classical）：Ads=去广告、Proxy=需代理、Direct=直连。"
                   "这是规则集而非完整配置，需挂到你自己的配置上使用，示例见 config_example.yaml。",
                   [(k, len(v)) for k, v in buckets.items()],
                   "把 config_example.yaml 中的 rule-providers 与 rules 片段合并进你的 Clash/Mihomo 配置，"
                   "或用 Stash 的覆写引用（见仓库 stash/ 目录）。")
    except Exception as e:  # noqa: BLE001
        failures.append("Clash: %s" % e)

    # ---- Quantumult X
    quanx_counters = {}
    try:
        quanx_counters = emit_quanx(mods, root, stats)
    except Exception as e:  # noqa: BLE001
        failures.append("Quantumult X: %s" % e)

    return stats, failures, clash_counters, quanx_counters


def render_summary(stats, failures, clash_counters, quanx_counters=None):
    out = ["## NetPilot 格式转换汇总", "",
           "| 源文件 | 类别 | 输入 | 输出 | 说明 |",
           "|---|---|---:|---:|---|"]
    for m, c, i, o, n in stats.rows:
        out.append("| %s | %s | %d | %d | %s |" % (m, c, i, o, n))
    if clash_counters:
        out += ["", "Clash 转换明细："]
        for k, v in sorted(clash_counters.items()):
            out.append("- %s：%d" % (k, v))
    if quanx_counters:
        out += ["", "Quantumult X 转换明细："]
        for k, v in sorted(quanx_counters.items()):
            out.append("- %s：%d" % (k, v))
    if failures:
        out += ["", "### ⚠️ 失败的格式"]
        for f in failures:
            out.append("- " + f)
    else:
        out += ["", "全部格式转换成功。"]
    return "\n".join(out)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default=".")
    ap.add_argument("--verify-idempotent", action="store_true",
                    help="在两个临时目录各生成一遍并逐文件比对，验证幂等")
    args = ap.parse_args()

    if args.verify_idempotent:
        import filecmp
        import shutil
        dirs = []
        try:
            for _ in range(2):
                tmp = tempfile.mkdtemp(prefix="netpilot-convert-")
                # 临时目录需要源文件：以符号链接方式复用仓库 modules/
                os.symlink(os.path.abspath(os.path.join(args.root, "modules")),
                           os.path.join(tmp, "modules"))
                generate(tmp)
                dirs.append(tmp)
            ok = True
            for sub in ("surge", "loon", "clash", "quanx"):
                rels = []
                for base, _dd, files in os.walk(os.path.join(dirs[0], sub)):
                    for fn in files:
                        rels.append(os.path.relpath(os.path.join(base, fn), dirs[0]))
                for rel in sorted(rels):
                    p2 = os.path.join(dirs[1], rel)
                    if not os.path.exists(p2) or not filecmp.cmp(
                            os.path.join(dirs[0], rel), p2, shallow=False):
                        ok = False
                        print("幂等校验失败：%s 两次生成不一致" % rel)
            print("幂等校验通过：两次生成逐字节一致。" if ok else "幂等校验未通过。")
            return 0 if ok else 1
        finally:
            for d in dirs:
                shutil.rmtree(d, ignore_errors=True)

    stats, failures, clash_counters, quanx_counters = generate(args.root)
    print(render_summary(stats, failures, clash_counters, quanx_counters))
    # 全部失败才返回非零；单格式失败已在汇总中醒目标记，不阻断其他格式提交
    return 1 if len(failures) >= 4 else 0


if __name__ == "__main__":
    sys.exit(main())
