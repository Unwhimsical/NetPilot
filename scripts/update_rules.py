#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import re
import sys
import glob
import json
import shutil
import argparse
import requests
import datetime

# ========== 用户配置区 ==========
GITHUB_USERNAME = "Unwhimsical"
REPO_NAME = "NetPilot"
BRANCH = "main"

UPSTREAM_MODULE_SOURCES = {
    "direct": [
        "https://raw.githubusercontent.com/GMOogway/shadowrocket-rules/master/sr_direct_list.module",
    ],
    "proxy": [
        "https://raw.githubusercontent.com/GMOogway/shadowrocket-rules/master/sr_proxy_list.module",
        "https://raw.githubusercontent.com/LOWERTOP/Shadowrocket-First/main/Talkatone.sgmodule",
    ],
    "shield": [
        "https://raw.githubusercontent.com/huijingfei/Shadowrocket-Rules/refs/heads/main/sr_app_ad.module",
        "https://raw.githubusercontent.com/deezertidal/shadowrocket-rules/refs/heads/main/modules/startingad.module",
        "https://raw.githubusercontent.com/GMOogway/shadowrocket-rules/master/sr_reject_list.module",
        "https://raw.githubusercontent.com/Unwhimsical/NetPilot/refs/heads/main/modules/%E6%B5%8B%E8%AF%95.module",
        "https://raw.githubusercontent.com/LOWERTOP/Shadowrocket-First/main/TalkatoneAntiAds.list",
    ],
}

UPSTREAM_JS_SOURCES = {
    "weibo_main.js": "https://raw.githubusercontent.com/zmqcherish/proxy-script/main/weibo_main.js",
    "weibo_launch.js": "https://raw.githubusercontent.com/zmqcherish/proxy-script/main/weibo_launch.js",
    "wechat_ad.js": "https://raw.githubusercontent.com/NobyDa/Script/master/QuantumultX/File/Wechat.js",
}

DIRECT_MODULE_PATH = "modules/NetPilot_Direct.module"
SHIELD_MODULE_PATH = "modules/NetPilot_Shield.module"
LOCAL_JS_DIR = "modules/local_js"
LOG_DIR = "logs"
BACKUP_DIR = "backups"
FLAGGED_DOMAINS_FILE = "config/flagged_domains.txt"
DIRECT_BLACKLIST_FILE = "config/direct_blacklist.txt"
DIRECT_WHITELIST_FILE = "config/direct_whitelist.txt"
SOURCE_HEALTH_FILE = "config/source_health.json"
MAX_LOG_FILES = 5
MAX_LOG_ITEMS = 5
MAX_BACKUP_DAYS = 7

FORCE_APPEND = True
SKIP_EXISTING_JS = True

SENSITIVE_KEYWORDS = [
    'bank', 'pay', 'unionpay', 'alipay', 'wechatpay',
    'icbc', 'ccb', 'boc', 'cmb', 'spdb', 'citic', 'cebbank',
    'cmbc', 'pingan', 'bocomm', 'psbc', 'cib', 'hxb', 'czbank',
    'cbhb', 'bosc', 'jsbchina', 'nbcb', 'njcb', 'hzbank'
]

DANGEROUS_HOSTNAME_KEYWORDS = [
    'ad', 'ads', 'track', 'log', 'sdk', 'push', 'stat', 'monitor',
    'analytics', 'crash', 'bugly', 'umeng', 'appsflyer', 'adjust'
]

DANGEROUS_JS_PATTERNS = [
    r'\$httpClient\.(get|post|put|delete)',
    r'\$task\.fetch',
    r'eval\(',
    r'new Function\(',
    r'device\.id',
    r'location\.',
    r'pasteboard',
    r'\$persistentStore\.write',
    r'\$prefs\.setValueForKey',
]

# ========== 工具函数 ==========
def fetch(url):
    print(f"Fetching: {url}")
    headers = {
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1",
        "Accept": "text/plain, */*; q=0.01",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive",
        "Referer": "https://yfamilys.com/",
    }
    session = requests.Session()
    try:
        if "yfamilys.com" in url:
            session.get("https://yfamilys.com/", headers=headers, timeout=20)
    except Exception:
        pass
    r = session.get(url, timeout=30, headers=headers)
    r.raise_for_status()
    return r.text

def clean_mitm(module_content):
    mitm_match = re.search(r'\[MITM\](.*?)(?=\[|$)', module_content, re.DOTALL)
    if not mitm_match:
        return module_content
    mitm_block = mitm_match.group(1)
    mitm_block = re.sub(r'(?im)^\s*ca-p12\s*=.*$', '', mitm_block)
    mitm_block = re.sub(r'(?im)^\s*ca-passphrase\s*=.*$', '', mitm_block)
    hostname_match = re.search(r'(?im)^\s*hostname\s*=\s*(.*)$', mitm_block)
    if hostname_match:
        hostnames = hostname_match.group(1).strip()
        if FORCE_APPEND and not hostnames.startswith('%APPEND%'):
            hostnames = '%APPEND% ' + hostnames
        mitm_block = re.sub(r'(?im)^\s*hostname\s*=.*$', f'hostname = {hostnames}', mitm_block)
    else:
        mitm_block += '\nhostname = %APPEND%\n'
    new_mitm = '[MITM]' + mitm_block.rstrip() + '\n'
    module_content = module_content[:mitm_match.start()] + new_mitm + module_content[mitm_match.end():]
    return module_content

def extract_rules(module_content, policy=None):
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
    mitm_match = re.search(r'\[MITM\](.*?)(?=\[|$)', module_content, re.DOTALL)
    if not mitm_match:
        return ""
    mitm_block = mitm_match.group(1)
    hostname_match = re.search(r'(?im)^\s*hostname\s*=\s*(.*)$', mitm_block)
    if hostname_match:
        return hostname_match.group(1).strip()
    return ""

def is_sensitive_hostname(hostname):
    low = hostname.lower()
    return any(k in low for k in SENSITIVE_KEYWORDS)

def is_dangerous_hostname(hostname):
    low = hostname.lower()
    return any(k in low for k in DANGEROUS_HOSTNAME_KEYWORDS)

def scan_js_content(js_content):
    risks = []
    for pattern in DANGEROUS_JS_PATTERNS:
        if re.search(pattern, js_content):
            risks.append(pattern)
    return risks

def load_keyword_list(file_path):
    keywords = []
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith('#'):
                    keywords.append(line)
    return keywords

def extract_domain_from_rule(rule):
    parts = rule.split(',')
    if len(parts) >= 2:
        return parts[1].strip().lower()
    return ""

def domain_match(domain, keyword):
    if not domain:
        return False
    domain = domain.lstrip('.')
    keyword = keyword.lower().lstrip('.')
    return domain == keyword or domain.endswith('.' + keyword)

def should_keep_direct(rule, blacklist, whitelist):
    domain = extract_domain_from_rule(rule)
    low = rule.lower()
    if any(domain_match(domain, kw) or kw in low for kw in whitelist):
        return True
    if any(domain_match(domain, kw) or kw in low for kw in blacklist):
        return False
    return True

def sort_rules(rules):
    order = ['DOMAIN', 'DOMAIN-SUFFIX', 'DOMAIN-KEYWORD', 'IP-CIDR6', 'IP-CIDR', 'USER-AGENT', 'PROCESS-NAME', 'URL-REGEX']
    type_map = {t: i for i, t in enumerate(order)}
    def get_rule_type(rule):
        return rule.split(',')[0] if ',' in rule else ''
    def key_func(rule):
        prefix = get_rule_type(rule)
        type_index = type_map.get(prefix, 99)
        return (type_index, rule)
    return sorted(rules, key=key_func)

def detect_rule_conflicts(rules):
    domain_map = {}
    conflicts = []
    for rule in rules:
        parts = rule.split(',')
        if len(parts) < 3:
            continue
        rule_type = parts[0].strip().upper()
        target = parts[1].strip().lower()
        policy = parts[2].strip().upper()
        if rule_type not in ('DOMAIN', 'DOMAIN-SUFFIX', 'DOMAIN-KEYWORD'):
            continue
        key = f"{rule_type}:{target}"
        if key not in domain_map:
            domain_map[key] = []
        domain_map[key].append(rule)
    for key, rule_list in domain_map.items():
        policies = set()
        for r in rule_list:
            policy = r.split(',')[2].strip().upper()
            policies.add(policy)
        if len(policies) > 1:
            conflicts.append({"key": key, "rules": rule_list})
    return conflicts

def detect_parent_child_conflicts(rules):
    domain_rules = []
    suffix_rules = []
    conflicts = []
    for rule in rules:
        parts = rule.split(',')
        if len(parts) < 3:
            continue
        rule_type = parts[0].strip().upper()
        target = parts[1].strip().lower()
        policy = parts[2].strip().upper()
        if rule_type == 'DOMAIN':
            domain_rules.append((target, rule, policy))
        elif rule_type == 'DOMAIN-SUFFIX':
            suffix_rules.append((target, rule, policy))
    for exact_domain, exact_rule, exact_policy in domain_rules:
        for suffix_domain, suffix_rule, suffix_policy in suffix_rules:
            if exact_domain == suffix_domain or exact_domain.endswith('.' + suffix_domain):
                if exact_policy != suffix_policy:
                    conflicts.append({
                        'exact_rule': exact_rule,
                        'suffix_rule': suffix_rule,
                        'exact_domain': exact_domain,
                        'suffix_domain': suffix_domain,
                        'description': f'DOMAIN {exact_domain} ({exact_policy}) 被 DOMAIN-SUFFIX {suffix_domain} ({suffix_policy}) 覆盖'
                    })
    return conflicts

def quality_check_rules(rules, label="rules"):
    valid = []
    invalid = []
    valid_prefixes = (
        'DOMAIN,', 'DOMAIN-SUFFIX,', 'DOMAIN-KEYWORD,',
        'IP-CIDR,', 'IP-CIDR6,', 'USER-AGENT,',
        'PROCESS-NAME,', 'URL-REGEX,', 'GEOIP,',
    )
    valid_policies = ('DIRECT', 'PROXY', 'REJECT', 'REJECT-200', 'REJECT-DICT', 'REJECT-IMG', 'REJECT-NO-DROP')
    seen = set()
    for rule in rules:
        if not rule.strip():
            continue
        if not rule.startswith(valid_prefixes):
            invalid.append(rule)
            continue
        parts = rule.split(',')
        if len(parts) < 3:
            invalid.append(rule)
            continue
        policy = parts[2].strip().upper()
        if policy not in valid_policies and not policy.startswith('REJECT'):
            invalid.append(rule)
            continue
        if rule in seen:
            invalid.append(rule)
            continue
        seen.add(rule)
        valid.append(rule)
    return valid, invalid

def test_rule_hit(domain, rules):
    domain = domain.lower()
    for rule in rules:
        parts = rule.split(',')
        if len(parts) < 3:
            continue
        rule_type = parts[0].strip().upper()
        target = parts[1].strip().lower()
        policy = parts[2].strip().upper()
        if rule_type == 'DOMAIN':
            if domain == target:
                return rule
        elif rule_type == 'DOMAIN-SUFFIX':
            if domain == target or domain.endswith('.' + target):
                return rule
        elif rule_type == 'DOMAIN-KEYWORD':
            if target in domain:
                return rule
    return None

# ========== 源健康监控 ==========
def load_source_health():
    if os.path.exists(SOURCE_HEALTH_FILE):
        with open(SOURCE_HEALTH_FILE, 'r', encoding='utf-8') as f:
            try:
                return json.load(f)
            except Exception:
                pass
    return {}

def save_source_health(health_data):
    os.makedirs(os.path.dirname(SOURCE_HEALTH_FILE), exist_ok=True)
    with open(SOURCE_HEALTH_FILE, 'w', encoding='utf-8') as f:
        json.dump(health_data, f, ensure_ascii=False, indent=2)

def get_health_status(consecutive_fail, last_success, last_fail):
    now = datetime.datetime.now()
    if consecutive_fail >= 3:
        return "unhealthy"
    if consecutive_fail >= 1:
        return "warning"
    if last_success:
        try:
            last_success_dt = datetime.datetime.strptime(last_success, "%Y-%m-%d %H:%M:%S")
            if (now - last_success_dt).days > 7:
                return "unhealthy"
        except Exception:
            pass
    return "healthy"

def update_source_health(url, success, error=None, health_data=None):
    if health_data is None:
        health_data = {}
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    entry = health_data.get(url, {
        "total_success": 0,
        "total_fail": 0,
        "consecutive_fail": 0,
        "last_success": None,
        "last_fail": None,
        "last_error": None,
        "status": "healthy"
    })
    if success:
        entry["total_success"] += 1
        entry["consecutive_fail"] = 0
        entry["last_success"] = now
        entry["last_error"] = None
    else:
        entry["total_fail"] += 1
        entry["consecutive_fail"] += 1
        entry["last_fail"] = now
        entry["last_error"] = str(error) if error else "Unknown error"
    entry["status"] = get_health_status(entry["consecutive_fail"], entry["last_success"], entry["last_fail"])
    health_data[url] = entry
    return health_data

def render_health_summary(health_data, log_lines):
    log_lines.append("## 🩺 规则源健康状态\n")
    if not health_data:
        log_lines.append("暂无记录\n")
        return
    for url, entry in health_data.items():
        status_icon = {
            "healthy": "✅",
            "warning": "⚠️",
            "unhealthy": "❌"
        }.get(entry.get("status"), "❓")
        log_lines.append(
            f"- {status_icon} {url}\n"
            f"  - 成功 {entry.get('total_success', 0)} 次，失败 {entry.get('total_fail', 0)} 次，"
            f"连续失败 {entry.get('consecutive_fail', 0)} 次\n"
            f"  - 最近成功: {entry.get('last_success') or '无'}\n"
            f"  - 最近失败: {entry.get('last_fail') or '无'} {('- ' + entry.get('last_error')) if entry.get('last_error') else ''}\n"
        )
    log_lines.append("\n")

# ========== 版本化备份 ==========
def backup_module_file(src_path, backup_subdir):
    if not os.path.exists(src_path):
        return None
    os.makedirs(backup_subdir, exist_ok=True)
    timestamp = datetime.datetime.now().strftime('%H%M%S')
    filename = os.path.basename(src_path)
    stem, ext = os.path.splitext(filename)
    backup_path = os.path.join(backup_subdir, f"{stem}_{timestamp}{ext}")
    shutil.copy2(src_path, backup_path)
    print(f"Backed up {filename} to {backup_path}")
    return backup_path

def cleanup_old_backups(backup_dir, keep_days=MAX_BACKUP_DAYS):
    if not os.path.isdir(backup_dir):
        return
    cutoff = datetime.datetime.now() - datetime.timedelta(days=keep_days)
    for date_dir in os.listdir(backup_dir):
        dir_path = os.path.join(backup_dir, date_dir)
        if not os.path.isdir(dir_path):
            continue
        try:
            dir_date = datetime.datetime.strptime(date_dir, '%Y-%m-%d')
            if dir_date < cutoff:
                shutil.rmtree(dir_path)
                print(f"Removed old backup directory: {dir_path}")
        except ValueError:
            continue

# ========== 健康检查模块 ==========
def health_check_module(module_content, label, min_rules=50, max_rules=100000):
    if not module_content or not module_content.strip():
        return False, f"{label}: 模块内容为空"
    if '[Rule]' not in module_content:
        return False, f"{label}: 缺少 [Rule] 段"
    rules = extract_rules(module_content)
    rule_count = len(rules)
    if rule_count < min_rules:
        return False, f"{label}: 规则数量过少 ({rule_count} < {min_rules})"
    if rule_count > max_rules:
        return False, f"{label}: 规则数量过多 ({rule_count} > {max_rules})"
    file_size = len(module_content.encode('utf-8'))
    if file_size > 5 * 1024 * 1024:
        return False, f"{label}: 模块文件过大 ({file_size / 1024 / 1024:.1f} MB)"
    return True, f"{label}: 健康检查通过（{rule_count} 条规则）"

# ========== 规则命中查询 CLI ==========
def query_rule_hit(domain, direct_module_path, shield_module_path):
    print(f"\n=== 规则命中查询: {domain} ===")
    result = {"domain": domain, "matches": []}
    if os.path.exists(direct_module_path):
        with open(direct_module_path, 'r', encoding='utf-8') as f:
            direct_content = f.read()
        direct_rules = extract_rules(direct_content)
        direct_rules = sort_rules(direct_rules)
        hit = test_rule_hit(domain, direct_rules)
        if hit:
            policy = hit.split(',')[2].strip().upper()
            result["matches"].append({"module": "Direct", "rule": hit, "policy": policy})
            result["final_policy"] = policy
            result["final_module"] = "Direct"
            print(f"✅ 直连模块命中: {hit}")
            print(f"   最终策略: {policy}")
            return result
    if os.path.exists(shield_module_path):
        with open(shield_module_path, 'r', encoding='utf-8') as f:
            shield_content = f.read()
        shield_rules = extract_rules(shield_content)
        proxy_rules = [r for r in shield_rules if not is_reject_rule(r)]
        reject_rules = [r for r in shield_rules if is_reject_rule(r)]
        proxy_rules = sort_rules(proxy_rules)
        hit = test_rule_hit(domain, proxy_rules)
        if hit:
            policy = hit.split(',')[2].strip().upper()
            result["matches"].append({"module": "Shield-Proxy", "rule": hit, "policy": policy})
            result["final_policy"] = policy
            result["final_module"] = "Shield-Proxy"
            print(f"✅ Shield 代理规则命中: {hit}")
            print(f"   最终策略: {policy}")
            return result
        reject_rules = sort_rules(reject_rules)
        hit = test_rule_hit(domain, reject_rules)
        if hit:
            policy = hit.split(',')[2].strip().upper()
            result["matches"].append({"module": "Shield-Adblock", "rule": hit, "policy": policy})
            result["final_policy"] = policy
            result["final_module"] = "Shield-Adblock"
            print(f"✅ Shield 去广告规则命中: {hit}")
            print(f"   最终策略: {policy}")
            return result
    result["final_policy"] = "FINAL（默认策略，通常为 PROXY）"
    result["final_module"] = "Final"
    print(f"⚠️ 未命中任何明确规则，走 FINAL 兜底策略（通常为 PROXY）")
    return result

# ========== 变更报告 ==========
def generate_change_report(current_date, log_lines, direct_stats, proxy_stats, reject_stats, conflicts, parent_child_conflicts, quality_issues, health_data):
    report = []
    report.append(f"# 变更报告 {current_date}\n")
    report.append(f"生成时间：{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    report.append("---\n")
    report.append("## 直连模块\n")
    report.append(f"- 原有规则数：{direct_stats.get('original', 0)}")
    report.append(f"- 新增规则数：{direct_stats.get('added', 0)}")
    report.append(f"- 过滤海外规则：{direct_stats.get('filtered', 0)}")
    report.append(f"- 最终规则数：{direct_stats.get('final', 0)}\n")
    report.append("## 代理模块\n")
    report.append(f"- 原有规则数：{proxy_stats.get('original', 0)}")
    report.append(f"- 新增规则数：{proxy_stats.get('added', 0)}")
    report.append(f"- 最终规则数：{proxy_stats.get('final', 0)}\n")
    report.append("## 去广告模块\n")
    report.append(f"- 原有规则数：{reject_stats.get('original', 0)}")
    report.append(f"- 新增规则数：{reject_stats.get('added', 0)}")
    report.append(f"- 最终规则数：{reject_stats.get('final', 0)}\n")
    report.append("## 规则冲突检测\n")
    if conflicts:
        report.append(f"检测到 {len(conflicts)} 组同域名策略冲突：\n")
        for c in conflicts[:10]:
            report.append(f"- {c['key']}")
            for r in c['rules']:
                report.append(f"  - {r}")
    else:
        report.append("未检测到同域名策略冲突。\n")
    report.append("## 父子域冲突检测\n")
    if parent_child_conflicts:
        report.append(f"检测到 {len(parent_child_conflicts)} 组父子域冲突：\n")
        for c in parent_child_conflicts[:10]:
            report.append(f"- {c['description']}")
    else:
        report.append("未检测到父子域冲突。\n")
    report.append("## 质量检查\n")
    if quality_issues:
        report.append(f"发现 {len(quality_issues)} 条异常规则：\n")
        for q in quality_issues[:20]:
            report.append(f"- {q}")
    else:
        report.append("所有规则格式正常。\n")
    report.append("## 规则源健康状态\n")
    if health_data:
        for url, entry in health_data.items():
            status_icon = {"healthy": "✅", "warning": "⚠️", "unhealthy": "❌"}.get(entry.get("status"), "❓")
            report.append(f"- {status_icon} {url} (成功 {entry.get('total_success', 0)}, 失败 {entry.get('total_fail', 0)}, 连续失败 {entry.get('consecutive_fail', 0)})")
    else:
        report.append("暂无记录\n")
    report.append("---\n")
    report.append("详细日志请查看同目录下的 update 日志文件。\n")
    report_path = os.path.join(LOG_DIR, current_date, "change_report.md")
    os.makedirs(os.path.dirname(report_path), exist_ok=True)
    with open(report_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(report))
    print(f"Change report saved to {report_path}")

# ========== 其他辅助函数 ==========
def load_blacklisted_hostnames():
    blacklisted = set()
    if os.path.exists(FLAGGED_DOMAINS_FILE):
        with open(FLAGGED_DOMAINS_FILE, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith('#'):
                    continue
                if '#black' in line:
                    domain = line.split('#')[0].strip()
                    if domain:
                        blacklisted.add(domain)
    return blacklisted

def load_existing_flagged_domains():
    domains = set()
    if os.path.exists(FLAGGED_DOMAINS_FILE):
        with open(FLAGGED_DOMAINS_FILE, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith('#'):
                    continue
                domain = line.split('#')[0].strip()
                if domain:
                    domains.add(domain)
    return domains

def update_flagged_domains_file(new_dangerous_domains):
    os.makedirs(os.path.dirname(FLAGGED_DOMAINS_FILE), exist_ok=True)
    existing_blacklisted = load_blacklisted_hostnames()
    existing_domains = load_existing_flagged_domains()
    all_domains = existing_domains | set(new_dangerous_domains)
    header = "# 危险域名标记文件\n"
    header += "# 在要拉黑的域名后面添加 #black 标记，然后手动运行脚本即可生效\n"
    header += "# 示例：ad.12306.cn #black\n"
    header += "# 未标记的域名默认保留，且不会在日志中重复提示\n\n"
    body_lines = []
    for domain in sorted(all_domains):
        if domain in existing_blacklisted:
            body_lines.append(f"{domain} #black")
        else:
            body_lines.append(domain)
    with open(FLAGGED_DOMAINS_FILE, 'w', encoding='utf-8') as f:
        f.write(header)
        f.write('\n'.join(body_lines))
        f.write('\n')

def get_log_dir_and_base(current_date):
    log_subdir = os.path.join(LOG_DIR, current_date)
    os.makedirs(log_subdir, exist_ok=True)
    return log_subdir, os.path.join(log_subdir, "update")

def get_log_file_path(current_date):
    log_subdir, _ = get_log_dir_and_base(current_date)
    existing_logs = sorted(glob.glob(os.path.join(log_subdir, "update*.md")))
    count = len(existing_logs)
    if count >= MAX_LOG_FILES:
        oldest = existing_logs[0]
        os.remove(oldest)
        existing_logs = sorted(glob.glob(os.path.join(log_subdir, "update*.md")))
        max_num = 0
        for f in existing_logs:
            name = os.path.basename(f)
            if name == "update.md":
                num = 1
            else:
                m = re.search(r'update_(\d+)\.md', name)
                num = int(m.group(1)) if m else 0
            if num > max_num:
                max_num = num
        next_num = max_num + 1
    else:
        existing_nums = set()
        for f in existing_logs:
            name = os.path.basename(f)
            if name == "update.md":
                existing_nums.add(1)
            else:
                m = re.search(r'update_(\d+)\.md', name)
                if m:
                    existing_nums.add(int(m.group(1)))
        next_num = 1
        while next_num in existing_nums:
            next_num += 1
    if next_num == 1:
        return os.path.join(log_subdir, "update.md")
    return os.path.join(log_subdir, f"update_{next_num}.md")

def cleanup_legacy_log_files(log_dir):
    if not os.path.isdir(log_dir):
        return
    for filename in os.listdir(log_dir):
        if filename.startswith("update_") and filename.endswith(".md"):
            filepath = os.path.join(log_dir, filename)
            if os.path.isfile(filepath):
                os.remove(filepath)

def get_today_stats_path(current_date):
    return os.path.join(LOG_DIR, current_date, "today_stats.json")

def load_today_stats(current_date):
    stats_path = get_today_stats_path(current_date)
    if os.path.exists(stats_path):
        with open(stats_path, 'r', encoding='utf-8') as f:
            try:
                return json.load(f)
            except Exception:
                pass
    return {"added_direct": 0, "added_proxy": 0, "added_reject": 0}

def save_today_stats(current_date, stats):
    stats_path = get_today_stats_path(current_date)
    os.makedirs(os.path.dirname(stats_path), exist_ok=True)
    with open(stats_path, 'w', encoding='utf-8') as f:
        json.dump(stats, f, ensure_ascii=False, indent=2)

def update_readme(direct_total, proxy_total, reject_total, added_direct, added_proxy, added_reject, current_date):
    readme_path = "README.md"
    if not os.path.exists(readme_path):
        return
    with open(readme_path, "r", encoding="utf-8") as f:
        content = f.read()
    stats_text = (
        f"## 📊 更新统计\n"
        f"- 更新时间：{current_date}\n"
        f"- 直连规则总数：**{direct_total}**（今日新增 {added_direct} 条）\n"
        f"- 代理规则总数：**{proxy_total}**（今日新增 {added_proxy} 条）\n"
        f"- 去广告规则总数：**{reject_total}**（今日新增 {added_reject} 条）\n"
    )
    pattern = re.compile(r"<!-- STATS_START -->.*?<!-- STATS_END -->", re.DOTALL)
    replacement = f"<!-- STATS_START -->\n{stats_text}\n<!-- STATS_END -->"
    new_content = pattern.sub(replacement, content)
    if new_content == content:
        new_content += f"\n\n<!-- STATS_START -->\n{stats_text}\n<!-- STATS_END -->\n"
    with open(readme_path, "w", encoding="utf-8") as f:
        f.write(new_content)
    print("README updated.")

def localize_scripts(scripts, local_js_dir, download_log, script_blacklist):
    os.makedirs(local_js_dir, exist_ok=True)
    updated_scripts = []
    seen_urls = set()
    seen_filenames = set()
    for script_line in scripts:
        m = re.search(r'script-path=([^,\s]+)', script_line)
        if not m:
            updated_scripts.append(script_line)
            continue
        original_url = m.group(1)
        filename = original_url.split('/')[-1]
        if original_url in seen_urls or filename in seen_filenames:
            local_url = f"https://raw.githubusercontent.com/{GITHUB_USERNAME}/{REPO_NAME}/{BRANCH}/{LOCAL_JS_DIR}/{filename}"
            new_line = script_line.replace(original_url, local_url)
            updated_scripts.append(new_line)
            continue
        seen_urls.add(original_url)
        seen_filenames.add(filename)
        if filename in script_blacklist:
            download_log.append(f"⛔ {filename} 已被拉黑，跳过")
            continue
        local_path = os.path.join(local_js_dir, filename)
        if SKIP_EXISTING_JS and os.path.exists(local_path):
            pass
        else:
            try:
                content = fetch(original_url)
                with open(local_path, 'w', encoding='utf-8') as f:
                    f.write(content)
                download_log.append(f"✅ {filename} 下载成功")
                risks = scan_js_content(content)
                if risks:
                    download_log.append(f"⚠️ {filename} 可疑模式: {', '.join(risks[:3])}")
            except Exception as e:
                download_log.append(f"❌ {filename} 下载失败: {e}")
                updated_scripts.append(script_line)
                continue
        local_url = f"https://raw.githubusercontent.com/{GITHUB_USERNAME}/{REPO_NAME}/{BRANCH}/{LOCAL_JS_DIR}/{filename}"
        new_line = script_line.replace(original_url, local_url)
        updated_scripts.append(new_line)
    return updated_scripts

def merge_unique(original_list, new_list):
    seen = set(original_list)
    result = original_list.copy()
    for item in new_list:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

def is_reject_rule(rule):
    return bool(re.search(r',REJECT(-[A-Z]+)?', rule))

def get_added_items(original_list, new_list):
    original_set = set(original_list)
    added = []
    for item in new_list:
        if item not in original_set:
            added.append(item)
    return added

def parse_args():
    parser = argparse.ArgumentParser(description="NetPilot 规则自动更新与查询工具")
    parser.add_argument("--query-domain", type=str, default=None, help="查询指定域名的最终命中策略")
    return parser.parse_args()

def main():
    args = parse_args()
    if args.query_domain:
        query_rule_hit(args.query_domain, DIRECT_MODULE_PATH, SHIELD_MODULE_PATH)
        return 0

    tz = datetime.timezone(datetime.timedelta(hours=8))
    now = datetime.datetime.now(tz)
    current_time = now.strftime('%Y-%m-%d %H:%M:%S 北京时间')
    current_date = now.strftime('%Y-%m-%d')

    cleanup_legacy_log_files(LOG_DIR)
    today_stats = load_today_stats(current_date)
    blacklisted_hostnames = load_blacklisted_hostnames()
    existing_flagged = load_existing_flagged_domains()
    direct_blacklist = load_keyword_list(DIRECT_BLACKLIST_FILE)
    direct_whitelist = load_keyword_list(DIRECT_WHITELIST_FILE)

    # 加载源健康数据
    health_data = load_source_health()

    added_direct_rules = []
    added_proxy_rules = []
    added_reject_rules = []
    sorted_direct_rules = []
    sorted_proxy_rules = []
    sorted_reject_rules = []

    direct_stats = {}
    proxy_stats = {}
    reject_stats = {}
    all_conflicts = []
    all_parent_child_conflicts = []
    all_quality_issues = []
    health_checks = []

    log_lines = []
    log_lines.append(f"# 更新日志 {current_date}\n")
    log_lines.append(f"**运行时间**: {current_time}\n")
    log_lines.append("---\n")

    # ========== 版本化备份 ==========
    backup_subdir = os.path.join(BACKUP_DIR, current_date)
    backup_module_file(DIRECT_MODULE_PATH, backup_subdir)
    backup_module_file(SHIELD_MODULE_PATH, backup_subdir)
    cleanup_old_backups(BACKUP_DIR)

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
                health_data = update_source_health(url, success=True, health_data=health_data)
            except Exception as e:
                direct_source_status.append(f"❌ {url} - {e}")
                health_data = update_source_health(url, success=False, error=e, health_data=health_data)

        merged_direct_rules = merge_unique(original_direct_rules, new_direct_rules)
        before_filter = len(merged_direct_rules)
        filtered_direct_rules = [rule for rule in merged_direct_rules if should_keep_direct(rule, direct_blacklist, direct_whitelist)]
        filtered_out = before_filter - len(filtered_direct_rules)

        valid_direct, invalid_direct = quality_check_rules(filtered_direct_rules, "直连规则")
        all_quality_issues.extend(invalid_direct)

        direct_conflicts = detect_rule_conflicts(valid_direct)
        direct_parent_child = detect_parent_child_conflicts(valid_direct)
        all_conflicts.extend(direct_conflicts)
        all_parent_child_conflicts.extend(direct_parent_child)

        added_direct_rules = get_added_items(original_direct_rules, valid_direct)
        sorted_direct_rules = sort_rules(valid_direct)

        direct_stats = {
            'original': len(original_direct_rules),
            'added': len(added_direct_rules),
            'filtered': filtered_out,
            'final': len(sorted_direct_rules)
        }

        if filtered_out:
            log_lines.append(f"⚠️ 已过滤海外直连规则：{filtered_out} 条\n")
        if direct_conflicts:
            log_lines.append(f"⚠️ 同域名策略冲突 {len(direct_conflicts)} 组\n")
        if direct_parent_child:
            log_lines.append(f"⚠️ 父子域冲突 {len(direct_parent_child)} 组\n")
        if invalid_direct:
            log_lines.append(f"⚠️ 异常规则 {len(invalid_direct)} 条已过滤\n")

        log_lines.append("### 上游源状态\n")
        log_lines.extend([f"- {status}" for status in direct_source_status])
        log_lines.append(f"\n**原有规则数**: {len(original_direct_rules)}")
        log_lines.append(f"**新增规则数**: {len(added_direct_rules)}")
        log_lines.append(f"**更新后总数**: {len(sorted_direct_rules)}\n")
        if added_direct_rules:
            log_lines.append("#### 新增规则明细\n")
            show_items = added_direct_rules[:MAX_LOG_ITEMS]
            log_lines.extend([f"- {rule}" for rule in show_items])
            if len(added_direct_rules) > MAX_LOG_ITEMS:
                log_lines.append(f"仅显示前 {MAX_LOG_ITEMS} 条，共 {len(added_direct_rules)} 条")
        log_lines.append("\n")

        # 生成直连模块内容
        direct_parts = [
            "#!name=NetPilot Direct",
            f"#!desc=直连规则总数: {len(sorted_direct_rules)}",
            "# 描述：国内直连规则，自动更新",
            f"# 更新时间: {current_time}",
            f"# 直连规则总数: {len(sorted_direct_rules)}",
            "[Rule]"
        ]
        direct_parts.append("\n".join(sorted_direct_rules))
        direct_parts.append("GEOIP,CN,DIRECT")
        direct_module = "\n\n".join(direct_parts) + "\n"

        direct_health_ok, direct_health_msg = health_check_module(direct_module, "直连模块", min_rules=50)
        health_checks.append(direct_health_msg)
        log_lines.append(f"🩺 {direct_health_msg}\n")

        if direct_health_ok:
            os.makedirs(os.path.dirname(DIRECT_MODULE_PATH), exist_ok=True)
            with open(DIRECT_MODULE_PATH, 'w', encoding='utf-8') as f:
                f.write(direct_module)
            print("Direct module written.")
        else:
            log_lines.append("⚠️ 直连模块健康检查未通过，已保留原文件\n")
    else:
        log_lines.append("无直连上游源，跳过直连模块更新。\n")

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

    proxy_source_status = []
    new_proxy_rules = []
    for url in UPSTREAM_MODULE_SOURCES.get("proxy", []):
        try:
            content = fetch(url)
            content = clean_mitm(content)
            new_proxy_rules.extend(extract_rules(content, 'PROXY'))
            proxy_source_status.append(f"✅ {url}")
            health_data = update_source_health(url, success=True, health_data=health_data)
        except Exception as e:
            proxy_source_status.append(f"❌ {url} - {e}")
            health_data = update_source_health(url, success=False, error=e, health_data=health_data)

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
            health_data = update_source_health(url, success=True, health_data=health_data)
        except Exception as e:
            shield_source_status.append(f"❌ {url} - {e}")
            health_data = update_source_health(url, success=False, error=e, health_data=health_data)

    merged_proxy_rules = merge_unique(original_proxy_rules, new_proxy_rules)
    merged_reject_rules = merge_unique(original_reject_rules, new_reject_rules)
    merged_rewrites = merge_unique(original_rewrites, new_rewrites)
    merged_scripts = merge_unique(original_scripts, new_scripts)

    valid_proxy, invalid_proxy = quality_check_rules(merged_proxy_rules, "代理规则")
    valid_reject, invalid_reject = quality_check_rules(merged_reject_rules, "去广告规则")
    all_quality_issues.extend(invalid_proxy)
    all_quality_issues.extend(invalid_reject)

    proxy_conflicts = detect_rule_conflicts(valid_proxy)
    reject_conflicts = detect_rule_conflicts(valid_reject)
    proxy_parent_child = detect_parent_child_conflicts(valid_proxy)
    reject_parent_child = detect_parent_child_conflicts(valid_reject)
    all_conflicts.extend(proxy_conflicts)
    all_conflicts.extend(reject_conflicts)
    all_parent_child_conflicts.extend(proxy_parent_child)
    all_parent_child_conflicts.extend(reject_parent_child)

    added_proxy_rules = get_added_items(original_proxy_rules, valid_proxy)
    added_reject_rules = get_added_items(original_reject_rules, valid_reject)

    sorted_proxy_rules = sort_rules(valid_proxy)
    sorted_reject_rules = sort_rules(valid_reject)

    proxy_stats = {
        'original': len(original_proxy_rules),
        'added': len(added_proxy_rules),
        'final': len(sorted_proxy_rules)
    }
    reject_stats = {
        'original': len(original_reject_rules),
        'added': len(added_reject_rules),
        'final': len(sorted_reject_rules)
    }

    log_lines.append("### 上游源状态\n")
    log_lines.extend([f"- {status}" for status in proxy_source_status])
    log_lines.append(f"\n**原有代理规则数**: {len(original_proxy_rules)}")
    log_lines.append(f"**新增代理规则数**: {len(added_proxy_rules)}")
    log_lines.append(f"**更新后代理规则总数**: {len(sorted_proxy_rules)}\n")
    if added_proxy_rules:
        log_lines.append("#### 新增代理规则明细\n")
        show_items = added_proxy_rules[:MAX_LOG_ITEMS]
        log_lines.extend([f"- {rule}" for rule in show_items])
        if len(added_proxy_rules) > MAX_LOG_ITEMS:
            log_lines.append(f"仅显示前 {MAX_LOG_ITEMS} 条，共 {len(added_proxy_rules)} 条")
    log_lines.append("\n")

    log_lines.append("## 去广告模块\n")
    log_lines.append("### 上游源状态\n")
    log_lines.extend([f"- {status}" for status in shield_source_status])
    log_lines.append(f"\n**原有去广告规则数**: {len(original_reject_rules)}")
    log_lines.append(f"**新增去广告规则数**: {len(added_reject_rules)}")
    log_lines.append(f"**更新后去广告规则总数**: {len(sorted_reject_rules)}\n")
    if added_reject_rules:
        log_lines.append("#### 新增去广告规则明细\n")
        show_items = added_reject_rules[:MAX_LOG_ITEMS]
        log_lines.extend([f"- {rule}" for rule in show_items])
        if len(added_reject_rules) > MAX_LOG_ITEMS:
            log_lines.append(f"仅显示前 {MAX_LOG_ITEMS} 条，共 {len(added_reject_rules)} 条")
    log_lines.append("\n")

    # ====== 合并 hostname ======
    original_hostname_list = []
    if original_hostnames:
        clean_original = original_hostnames.replace('%APPEND%', '').strip()
        if clean_original:
            original_hostname_list = [h.strip() for h in clean_original.split(',') if h.strip()]

    candidate_hostnames = original_hostname_list + [h for h in new_hostnames_set if h not in original_hostname_list]

    filtered_hostnames = []
    sensitive_removed = []
    dangerous_domains = []

    for h in candidate_hostnames:
        if h in blacklisted_hostnames:
            continue
        if is_sensitive_hostname(h):
            sensitive_removed.append(h)
            continue
        if is_dangerous_hostname(h):
            dangerous_domains.append(h)
        filtered_hostnames.append(h)

    update_flagged_domains_file(dangerous_domains)

    log_subdir, _ = get_log_dir_and_base(current_date)
    snapshot_path = os.path.join(log_subdir, "dangerous_domains.txt")
    with open(snapshot_path, 'w', encoding='utf-8') as f:
        f.write(f"# 危险域名快照 {current_date}\n")
        f.write(f"# 共 {len(dangerous_domains)} 个\n\n")
        for d in sorted(dangerous_domains):
            f.write(d + "\n")

    merged_hostnames = ', '.join(filtered_hostnames)
    if FORCE_APPEND:
        if not merged_hostnames.startswith('%APPEND%'):
            merged_hostnames = '%APPEND% ' + merged_hostnames

    if sensitive_removed:
        log_lines.append("## ⚠️ 敏感域名已自动过滤（银行/支付）\n")
        log_lines.extend([f"- {h}" for h in sensitive_removed])
        log_lines.append("\n")

    new_dangerous = [d for d in dangerous_domains if d not in existing_flagged]
    if new_dangerous:
        log_lines.append(f"## ⚠️ 新发现危险域名（共 {len(new_dangerous)} 个，默认保留）\n")
        log_lines.append("如需拉黑，编辑 `config/flagged_domains.txt`，在对应域名后加 `#black`，然后手动运行脚本即可。\n")
        log_lines.extend([f"- {h}" for h in new_dangerous])
        log_lines.append("\n")

    download_log = []
    script_blacklist = set()
    updated_scripts = localize_scripts(merged_scripts, LOCAL_JS_DIR, download_log, script_blacklist)
    if download_log:
        log_lines.append("## JS 脚本本地化\n")
        log_lines.extend([f"- {status}" for status in download_log])
        log_lines.append("\n")

    # 生成 shield 模块
    shield_parts = [
        "#!name=NetPilot Shield",
        f"#!desc=代理规则: {len(sorted_proxy_rules)} ｜ 去广告规则: {len(sorted_reject_rules)}",
        "# 描述：代理分流 + 去广告模块，自动更新",
        f"# 更新时间: {current_time}",
        f"# 代理规则总数: {len(sorted_proxy_rules)}",
        f"# 去广告规则总数: {len(sorted_reject_rules)}",
        "[Rule]"
    ]
    shield_parts.append("# --- 代理分流规则 ---")
    shield_parts.append("\n".join(sorted_proxy_rules))
    shield_parts.append("# --- 去广告拦截规则 ---")
    shield_parts.append("\n".join(sorted_reject_rules))
    shield_parts.append("[URL Rewrite]")
    shield_parts.append("\n".join(merged_rewrites))
    shield_parts.append("[Script]")
    shield_parts.append("\n".join(updated_scripts))
    shield_parts.append("[MITM]")
    shield_parts.append(f"enable = true\nhostname = {merged_hostnames}")
    shield_content = "\n\n".join(shield_parts) + "\n"

    shield_health_ok, shield_health_msg = health_check_module(shield_content, "Shield模块", min_rules=50)
    health_checks.append(shield_health_msg)
    log_lines.append(f"🩺 {shield_health_msg}\n")

    if shield_health_ok:
        os.makedirs(os.path.dirname(SHIELD_MODULE_PATH), exist_ok=True)
        with open(SHIELD_MODULE_PATH, 'w', encoding='utf-8') as f:
            f.write(shield_content)
        print("Shield module written with merged content (proxy + adblock separated).")
    else:
        log_lines.append("⚠️ Shield 模块健康检查未通过，已保留原文件\n")

    # 独立 JS 源
    independent_log = []
    for filename, url in UPSTREAM_JS_SOURCES.items():
        local_path = os.path.join(LOCAL_JS_DIR, filename)
        os.makedirs(LOCAL_JS_DIR, exist_ok=True)
        if SKIP_EXISTING_JS and os.path.exists(local_path):
            continue
        try:
            content = fetch(url)
            with open(local_path, 'w', encoding='utf-8') as f:
                f.write(content)
            independent_log.append(f"✅ {filename} 下载成功")
            risks = scan_js_content(content)
            if risks:
                independent_log.append(f"⚠️ {filename} 可疑模式: {', '.join(risks[:3])}")
            health_data = update_source_health(url, success=True, health_data=health_data)
        except Exception as e:
            independent_log.append(f"❌ {filename} 下载失败: {e}")
            health_data = update_source_health(url, success=False, error=e, health_data=health_data)

    if independent_log:
        log_lines.append("## 独立 JS 源\n")
        log_lines.extend([f"- {status}" for status in independent_log])
        log_lines.append("\n")

    # 在日志末尾添加源健康摘要
    render_health_summary(health_data, log_lines)

    # 写入日志
    log_lines.append("---\n")
    log_content = "\n".join(log_lines)
    log_file_path = get_log_file_path(current_date)
    with open(log_file_path, 'w', encoding='utf-8') as f:
        f.write(log_content)
    print(f"Log written to {log_file_path}")

    # 保存源健康数据
    save_source_health(health_data)

    # 更新今日累计统计
    today_stats["added_direct"] += len(added_direct_rules)
    today_stats["added_proxy"] += len(added_proxy_rules)
    today_stats["added_reject"] += len(added_reject_rules)
    save_today_stats(current_date, today_stats)

    # 更新 README
    update_readme(
        direct_total=len(sorted_direct_rules),
        proxy_total=len(sorted_proxy_rules),
        reject_total=len(sorted_reject_rules),
        added_direct=today_stats["added_direct"],
        added_proxy=today_stats["added_proxy"],
        added_reject=today_stats["added_reject"],
        current_date=current_date,
    )

    # 生成变更报告（包含健康数据）
    generate_change_report(
        current_date=current_date,
        log_lines=log_lines,
        direct_stats=direct_stats,
        proxy_stats=proxy_stats,
        reject_stats=reject_stats,
        conflicts=all_conflicts,
        parent_child_conflicts=all_parent_child_conflicts,
        quality_issues=all_quality_issues,
        health_data=health_data,
    )

    return 0

if __name__ == "__main__":
    sys.exit(main())
