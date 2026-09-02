#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import re
import requests
import datetime

# ========== 用户配置区 ==========
GITHUB_USERNAME = "Unwhimsical"        # 请改成你的 GitHub 用户名
REPO_NAME = "NetPilot"
BRANCH = "main"

# 上游模块源：key 为模块类型（direct/proxy/shield），value 为 URL 列表
# - direct: 直连规则，生成/更新 NetPilot_Direct.module
# - proxy : 代理分流规则，会合并进 NetPilot_Shield.module 的“代理分流”部分
# - shield: 去广告拦截规则，会合并进 NetPilot_Shield.module 的“去广告拦截”部分
UPSTREAM_MODULE_SOURCES = {
    "direct": [
        "https://raw.githubusercontent.com/GMOogway/shadowrocket-rules/master/sr_direct_list.module",
    ],
    "proxy": [
        "https://raw.githubusercontent.com/GMOogway/shadowrocket-rules/master/sr_proxy_list.module",
    ],
    "shield": [
        "https://raw.githubusercontent.com/huijingfei/Shadowrocket-Rules/refs/heads/main/sr_app_ad.module",
        "https://raw.githubusercontent.com/deezertidal/shadowrocket-rules/refs/heads/main/modules/startingad.module",
        "https://yfamilys.com/module/adultraplus.module",
        "https://yfamilys.com/module/adultra.module",
        "https://yfamilys.com/module/startingad.module",
        "https://yfamilys.com/module/ZhihuBlock.sgmodule",
        "https://raw.githubusercontent.com/GMOogway/shadowrocket-rules/master/sr_reject_list.module",
    ],
}

# 需要本地化的独立 JS 脚本源（键为文件名，值为 URL）
UPSTREAM_JS_SOURCES = {
    "weibo_main.js": "https://raw.githubusercontent.com/zmqcherish/proxy-script/main/weibo_main.js",
    "weibo_launch.js": "https://raw.githubusercontent.com/zmqcherish/proxy-script/main/weibo_launch.js",
    "wechat_ad.js": "https://raw.githubusercontent.com/NobyDa/Script/master/QuantumultX/File/Wechat.js",
}

# 模块文件路径（请根据你仓库中的实际文件名修改）
DIRECT_MODULE_PATH = "modules/NetPilot_Direct.module"
SHIELD_MODULE_PATH = "modules/NetPilot_Shield.module"
LOCAL_JS_DIR = "modules/local_js"

# 日志目录
LOG_DIR = "logs"

# 是否强制所有 MITM hostname 使用 %APPEND%
FORCE_APPEND = True

# ========== 工具函数 ==========
def fetch(url):
    """
    下载文本内容，使用浏览器请求头和 Session 尝试绕过简单反爬。
    如果仍然失败，抛出异常。
    """
    print(f"Fetching: {url}")
    headers = {
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1",
        "Accept": "text/plain, */*; q=0.01",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive",
        "Referer": "https://yfamilys.com/",
    }
    # 创建 Session，尝试获取 Cookie
    session = requests.Session()
    try:
        # 先访问主页，模拟浏览器行为，可能会获得必要的 Cookie
        if "yfamilys.com" in url:
            session.get("https://yfamilys.com/", headers=headers, timeout=20)
    except Exception:
        pass  # 忽略主页访问错误
    # 真正请求模块
    r = session.get(url, timeout=30, headers=headers)
    r.raise_for_status()
    return r.text

def clean_mitm(module_content):
    """
    清洗模块中的 [MITM] 段：
    - 删除 ca-p12 和 ca-passphrase
    - 确保 hostname 以 %APPEND% 开头（如果 FORCE_APPEND 为 True）
    """
    mitm_match = re.search(r'\[MITM\](.*?)(?=\[|$)', module_content, re.DOTALL)
    if not mitm_match:
        return module_content
    mitm_block = mitm_match.group(1)
    # 删除证书相关行
    mitm_block = re.sub(r'(?im)^\s*ca-p12\s*=.*$', '', mitm_block)
    mitm_block = re.sub(r'(?im)^\s*ca-passphrase\s*=.*$', '', mitm_block)
    # 提取 hostname 行
    hostname_match = re.search(r'(?im)^\s*hostname\s*=\s*(.*)$', mitm_block)
    if hostname_match:
        hostnames = hostname_match.group(1).strip()
        if FORCE_APPEND and not hostnames.startswith('%APPEND%'):
            hostnames = '%APPEND% ' + hostnames
        mitm_block = re.sub(r'(?im)^\s*hostname\s*=.*$', f'hostname = {hostnames}', mitm_block)
    else:
        # 没有 hostname，添加默认
        mitm_block += '\nhostname = %APPEND%\n'
    # 重新组合
    new_mitm = '[MITM]' + mitm_block.rstrip() + '\n'
    module_content = module_content[:mitm_match.start()] + new_mitm + module_content[mitm_match.end():]
    return module_content

def extract_rules(module_content, policy=None):
    """
    从模块内容中提取规则行。
    如果指定 policy，则只提取该策略的规则；否则提取所有规则行。
    """
    rules = []
    for line in module_content.splitlines():
        line = line.strip()
        if line.startswith(('DOMAIN,', 'DOMAIN-SUFFIX,', 'DOMAIN-KEYWORD,', 'IP-CIDR,', 'IP-CIDR6,', 'USER-AGENT,', 'PROCESS-NAME,', 'URL-REGEX,')):
            if policy is None:
                rules.append(line)
            else:
                if line.endswith(',' + policy) or (policy + ',') in line:
                    rules.append(line)
    return rules

def extract_url_rewrite(module_content):
    """提取 [URL Rewrite] 段中的规则（非注释行）"""
    rewrite_lines = []
    in_rewrite = False
    for line in module_content.splitlines():
        if line.strip().startswith('[URL Rewrite]'):
            in_rewrite = True
            continue
        if in_rewrite and line.strip().startswith('['):
            break
        if in_rewrite and line.strip() and not line.strip().startswith('#'):
            rewrite_lines.append(line.strip())
    return rewrite_lines

def extract_scripts(module_content):
    """提取 [Script] 段中的所有条目"""
    scripts = []
    in_script = False
    for line in module_content.splitlines():
        if line.strip().startswith('[Script]'):
            in_script = True
            continue
        if in_script and line.strip().startswith('['):
            break
        if in_script and line.strip() and not line.strip().startswith('#'):
            scripts.append(line.strip())
    return scripts

def extract_mitm_hostnames(module_content):
    """提取 [MITM] 段中的 hostname 列表（返回字符串，可能包含 %APPEND% 前缀）"""
    mitm_match = re.search(r'\[MITM\](.*?)(?=\[|$)', module_content, re.DOTALL)
    if not mitm_match:
        return ""
    mitm_block = mitm_match.group(1)
    hostname_match = re.search(r'(?im)^\s*hostname\s*=\s*(.*)$', mitm_block)
    if hostname_match:
        return hostname_match.group(1).strip()
    return ""

def localize_scripts(scripts, local_js_dir, download_log):
    """
    下载脚本中引用的 JS 文件到 local_js_dir，并替换 script-path 为本地仓库 URL。
    同时将每个脚本的下载状态记录到 download_log 列表中。
    """
    os.makedirs(local_js_dir, exist_ok=True)
    updated_scripts = []
    for script_line in scripts:
        m = re.search(r'script-path=([^,\s]+)', script_line)
        if not m:
            updated_scripts.append(script_line)
            continue
        original_url = m.group(1)
        filename = original_url.split('/')[-1]
        local_path = os.path.join(local_js_dir, filename)
        try:
            content = fetch(original_url)
            with open(local_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Downloaded JS: {filename}")
            download_log.append(f"✅ {filename} 下载成功")
        except Exception as e:
            print(f"Failed to download {original_url}: {e}")
            download_log.append(f"❌ {filename} 下载失败: {e}")
            # 下载失败则保留原始脚本行（不替换路径）
            updated_scripts.append(script_line)
            continue
        local_url = f"https://raw.githubusercontent.com/{GITHUB_USERNAME}/{REPO_NAME}/{BRANCH}/{LOCAL_JS_DIR}/{filename}"
        new_line = script_line.replace(original_url, local_url)
        updated_scripts.append(new_line)
    return updated_scripts

def merge_unique(original_list, new_list):
    """合并两个列表，去重并保持原始列表在前，新列表追加不重复项"""
    seen = set(original_list)
    result = original_list.copy()
    for item in new_list:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

def is_reject_rule(rule):
    """判断规则是否为 REJECT 系列"""
    return bool(re.search(r',REJECT(-[A-Z]+)?', rule))

def get_added_items(original_list, new_list):
    """返回新列表中不在原列表中的项（即新增项）"""
    original_set = set(original_list)
    added = []
    for item in new_list:
        if item not in original_set:
            added.append(item)
    return added

def main():
    # 获取当前 UTC 时间字符串和日期
    current_time = datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S UTC')
    current_date = datetime.datetime.utcnow().strftime('%Y-%m-%d')

    # 初始化日志相关
    log_lines = []
    log_lines.append(f"# 更新日志 {current_date}\n")
    log_lines.append(f"**运行时间**: {current_time}\n")
    log_lines.append("---\n")

    # ========== 处理直连模块 ==========
    print("=== Processing Direct Module ===")
    log_lines.append("## 直连模块\n")
    direct_source_status = []
    if UPSTREAM_MODULE_SOURCES["direct"]:
        original_direct_rules = []
        if os.path.exists(DIRECT_MODULE_PATH):
            with open(DIRECT_MODULE_PATH, 'r', encoding='utf-8') as f:
                original_direct_content = f.read()
            original_direct_rules = extract_rules(original_direct_content)
        new_direct_rules = []
        for url in UPSTREAM_MODULE_SOURCES["direct"]:
            try:
                content = fetch(url)
                content = clean_mitm(content)
                new_direct_rules.extend(extract_rules(content, 'DIRECT'))
                direct_source_status.append(f"✅ {url}")
            except Exception as e:
                print(f"Failed to process {url}: {e}")
                direct_source_status.append(f"❌ {url} - {e}")
        merged_direct_rules = merge_unique(original_direct_rules, new_direct_rules)
        added_direct_rules = get_added_items(original_direct_rules, new_direct_rules)

        log_lines.append("### 上游源状态\n")
        log_lines.extend([f"- {status}" for status in direct_source_status])
        log_lines.append(f"\n**原有规则数**: {len(original_direct_rules)}")
        log_lines.append(f"**新增规则数**: {len(added_direct_rules)}")
        log_lines.append(f"**更新后总数**: {len(merged_direct_rules)}\n")
        if added_direct_rules:
            log_lines.append("#### 新增规则明细\n")
            log_lines.extend([f"- {rule}" for rule in added_direct_rules])
        log_lines.append("\n")

        direct_parts = [
            "#!name=NetPilot Direct",
            f"#!desc=直连规则总数: {len(merged_direct_rules)}",
            "# 描述：国内直连规则，自动更新",
            f"# 更新时间: {current_time}",
            f"# 直连规则总数: {len(merged_direct_rules)}",
            "[Rule]"
        ]
        direct_parts.append("\n".join(original_direct_rules))
        if added_direct_rules:
            direct_parts.append(f"# === 新增规则 {current_time} ===")
            direct_parts.append("\n".join(added_direct_rules))
        direct_parts.append("GEOIP,CN,DIRECT")
        direct_module = "\n\n".join(direct_parts) + "\n"
        os.makedirs(os.path.dirname(DIRECT_MODULE_PATH), exist_ok=True)
        with open(DIRECT_MODULE_PATH, 'w', encoding='utf-8') as f:
            f.write(direct_module)
        print("Direct module written.")
    else:
        log_lines.append("无直连上游源，跳过直连模块更新。\n")
        print("No direct upstream sources, skipping Direct module generation.")

    # ========== 处理去广告+代理模块 (Shield) ==========
    print("=== Processing Shield Module ===")
    log_lines.append("## 代理分流模块\n")
    original_proxy_rules = []
    original_reject_rules = []
    original_rewrites = []
    original_scripts = []
    original_hostnames = ""
    if os.path.exists(SHIELD_MODULE_PATH):
        with open(SHIELD_MODULE_PATH, 'r', encoding='utf-8') as f:
            original_shield_content = f.read()
        all_original_rules = extract_rules(original_shield_content)
        for rule in all_original_rules:
            if is_reject_rule(rule):
                original_reject_rules.append(rule)
            else:
                original_proxy_rules.append(rule)
        original_rewrites = extract_url_rewrite(original_shield_content)
        original_scripts = extract_scripts(original_shield_content)
        original_hostnames = extract_mitm_hostnames(original_shield_content)
        print("Loaded existing shield module content for merging.")
    else:
        print("No existing shield module found; creating new one.")

    # 代理源
    proxy_source_status = []
    new_proxy_rules = []
    for url in UPSTREAM_MODULE_SOURCES.get("proxy", []):
        try:
            content = fetch(url)
            content = clean_mitm(content)
            new_proxy_rules.extend(extract_rules(content, 'PROXY'))
            proxy_source_status.append(f"✅ {url}")
        except Exception as e:
            print(f"Failed to process proxy source {url}: {e}")
            proxy_source_status.append(f"❌ {url} - {e}")

    # shield源
    shield_source_status = []
    new_reject_rules = []
    new_rewrites = []
    new_scripts = []
    new_hostnames_set = set()
    for url in UPSTREAM_MODULE_SOURCES.get("shield", []):
        try:
            content = fetch(url)
            content = clean_mitm(content)
            new_reject_rules.extend(extract_rules(content, 'REJECT'))
            new_reject_rules.extend(extract_rules(content, 'REJECT-200'))
            new_reject_rules.extend(extract_rules(content, 'REJECT-DICT'))
            new_reject_rules.extend(extract_rules(content, 'REJECT-IMG'))
            new_reject_rules.extend(extract_rules(content, 'REJECT-NO-DROP'))
            new_rewrites.extend(extract_url_rewrite(content))
            new_scripts.extend(extract_scripts(content))
            upstream_hostnames = extract_mitm_hostnames(content)
            if upstream_hostnames:
                clean_hostnames = upstream_hostnames.replace('%APPEND%', '').strip()
                if clean_hostnames:
                    for h in clean_hostnames.split(','):
                        h = h.strip()
                        if h:
                            new_hostnames_set.add(h)
            shield_source_status.append(f"✅ {url}")
        except Exception as e:
            print(f"Failed to process shield source {url}: {e}")
            shield_source_status.append(f"❌ {url} - {e}")

    merged_proxy_rules = merge_unique(original_proxy_rules, new_proxy_rules)
    added_proxy_rules = get_added_items(original_proxy_rules, new_proxy_rules)
    merged_reject_rules = merge_unique(original_reject_rules, new_reject_rules)
    added_reject_rules = get_added_items(original_reject_rules, new_reject_rules)
    merged_rewrites = merge_unique(original_rewrites, new_rewrites)
    merged_scripts = merge_unique(original_scripts, new_scripts)

    # 日志代理
    log_lines.append("### 上游源状态\n")
    log_lines.extend([f"- {status}" for status in proxy_source_status])
    log_lines.append(f"\n**原有代理规则数**: {len(original_proxy_rules)}")
    log_lines.append(f"**新增代理规则数**: {len(added_proxy_rules)}")
    log_lines.append(f"**更新后代理规则总数**: {len(merged_proxy_rules)}\n")
    if added_proxy_rules:
        log_lines.append("#### 新增代理规则明细\n")
        log_lines.extend([f"- {rule}" for rule in added_proxy_rules])
    log_lines.append("\n")

    # 日志去广告
    log_lines.append("## 去广告模块\n")
    log_lines.append("### 上游源状态\n")
    log_lines.extend([f"- {status}" for status in shield_source_status])
    log_lines.append(f"\n**原有去广告规则数**: {len(original_reject_rules)}")
    log_lines.append(f"**新增去广告规则数**: {len(added_reject_rules)}")
    log_lines.append(f"**更新后去广告规则总数**: {len(merged_reject_rules)}\n")
    if added_reject_rules:
        log_lines.append("#### 新增去广告规则明细\n")
        log_lines.extend([f"- {rule}" for rule in added_reject_rules])
    log_lines.append("\n")

    # 合并 hostname
    original_hostname_list = []
    if original_hostnames:
        clean_original = original_hostnames.replace('%APPEND%', '').strip()
        if clean_original:
            original_hostname_list = [h.strip() for h in clean_original.split(',') if h.strip()]
    all_hostnames = original_hostname_list + [h for h in new_hostnames_set if h not in original_hostname_list]
    merged_hostnames = ', '.join(all_hostnames)
    if FORCE_APPEND:
        if not merged_hostnames.startswith('%APPEND%'):
            merged_hostnames = '%APPEND% ' + merged_hostnames

    # 本地化脚本
    download_log = []
    updated_scripts = localize_scripts(merged_scripts, LOCAL_JS_DIR, download_log)
    log_lines.append("## JS 脚本本地化\n")
    log_lines.extend([f"- {status}" for status in download_log])
    log_lines.append("\n")

    # 生成 Shield 模块
    shield_parts = [
        "#!name=NetPilot Shield",
        f"#!desc=代理规则: {len(merged_proxy_rules)} ｜ 去广告规则: {len(merged_reject_rules)}",
        "# 描述：代理分流 + 去广告模块，自动更新",
        f"# 更新时间: {current_time}",
        f"# 代理规则总数: {len(merged_proxy_rules)}",
        f"# 去广告规则总数: {len(merged_reject_rules)}",
        "[Rule]"
    ]
    shield_parts.append("# --- 代理分流规则 ---")
    shield_parts.append("\n".join(original_proxy_rules))
    if added_proxy_rules:
        shield_parts.append(f"# === 新增代理规则 {current_time} ===")
        shield_parts.append("\n".join(added_proxy_rules))
    shield_parts.append("# --- 去广告拦截规则 ---")
    shield_parts.append("\n".join(original_reject_rules))
    if added_reject_rules:
        shield_parts.append(f"# === 新增去广告规则 {current_time} ===")
        shield_parts.append("\n".join(added_reject_rules))
    shield_parts.append("[URL Rewrite]")
    shield_parts.append("\n".join(merged_rewrites))
    shield_parts.append("[Script]")
    shield_parts.append("\n".join(updated_scripts))
    shield_parts.append("[MITM]")
    shield_parts.append(f"enable = true\nhostname = {merged_hostnames}")
    shield_content = "\n\n".join(shield_parts) + "\n"
    os.makedirs(os.path.dirname(SHIELD_MODULE_PATH), exist_ok=True)
    with open(SHIELD_MODULE_PATH, 'w', encoding='utf-8') as f:
        f.write(shield_content)
    print("Shield module written with merged content (proxy + adblock separated).")

    # 独立 JS 源
    log_lines.append("## 独立 JS 源\n")
    for filename, url in UPSTREAM_JS_SOURCES.items():
        local_path = os.path.join(LOCAL_JS_DIR, filename)
        os.makedirs(LOCAL_JS_DIR, exist_ok=True)
        try:
            content = fetch(url)
            with open(local_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Downloaded independent JS: {filename}")
            log_lines.append(f"- ✅ {filename} 下载成功")
        except Exception as e:
            print(f"Failed to download {url}: {e}")
            log_lines.append(f"- ❌ {filename} 下载失败: {e}")

    # 写日志
    log_lines.append("---\n")
    log_content = "\n".join(log_lines)
    log_file_path = os.path.join(LOG_DIR, f"update_{current_date}.md")
    os.makedirs(LOG_DIR, exist_ok=True)
    with open(log_file_path, 'w', encoding='utf-8') as f:
        f.write(log_content)
    print(f"Log written to {log_file_path}")

if __name__ == "__main__":
    main()
