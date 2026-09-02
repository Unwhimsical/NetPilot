#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import re
import glob
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
    ],
    "shield": [
        "https://raw.githubusercontent.com/huijingfei/Shadowrocket-Rules/refs/heads/main/sr_app_ad.module",
        "https://raw.githubusercontent.com/deezertidal/shadowrocket-rules/refs/heads/main/modules/startingad.module",
        "https://raw.githubusercontent.com/GMOogway/shadowrocket-rules/master/sr_reject_list.module",
        "https://raw.githubusercontent.com/Unwhimsical/NetPilot/refs/heads/main/modules/%E6%B5%8B%E8%AF%95.module",
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
FLAGGED_DOMAINS_FILE = "config/flagged_domains.txt"   # 拉黑域名标记文件，放在 config 目录
MAX_LOG_FILES = 5
MAX_LOG_ITEMS = 5

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

def load_blacklisted_hostnames():
    """读取 config/flagged_domains.txt 中标记了 #black 的域名"""
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
    """读取 config/flagged_domains.txt 中所有域名（不论是否有标记）"""
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
    """更新 config/flagged_domains.txt，保留已有标记，追加新发现的域名"""
    # 确保 config 目录存在
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
    base = os.path.join(log_subdir, "update")
    return log_subdir, base

def get_log_file_path(current_date):
    log_subdir, base = get_log_dir_and_base(current_date)
    existing_logs = sorted(glob.glob(os.path.join(log_subdir, "update*.md")))
    count = len(existing_logs)

    if count >= MAX_LOG_FILES:
        oldest = existing_logs[0]
        os.remove(oldest)
        print(f"Removed oldest log to keep limit: {oldest}")
        existing_logs = sorted(glob.glob(os.path.join(log_subdir, "update*.md")))
        if not existing_logs:
            max_num = 0
        else:
            max_num = 0
            for f in existing_logs:
                name = os.path.basename(f)
                if name == "update.md":
                    num = 1
                else:
                    match = re.search(r'update_(\d+)\.md', name)
                    if match:
                        num = int(match.group(1))
                    else:
                        num = 0
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
                match = re.search(r'update_(\d+)\.md', name)
                if match:
                    existing_nums.add(int(match.group(1)))
        next_num = 1
        while next_num in existing_nums:
            next_num += 1

    if next_num == 1:
        return os.path.join(log_subdir, "update.md")
    else:
        return os.path.join(log_subdir, f"update_{next_num}.md")

def cleanup_legacy_log_files(log_dir):
    if not os.path.isdir(log_dir):
        return
    for filename in os.listdir(log_dir):
        if filename.startswith("update_") and filename.endswith(".md"):
            filepath = os.path.join(log_dir, filename)
            if os.path.isfile(filepath):
                print(f"Deleting legacy log file: {filepath}")
                os.remove(filepath)

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
            print(f"⛔ Script blacklisted, skipping: {filename}")
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
                print(f"Downloaded JS: {filename}")
                download_log.append(f"✅ {filename} 下载成功")
                risks = scan_js_content(content)
                if risks:
                    download_log.append(f"⚠️ {filename} 可疑模式: {', '.join(risks[:3])}")
            except Exception as e:
                print(f"Failed to download {original_url}: {e}")
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

def main():
    tz = datetime.timezone(datetime.timedelta(hours=8))
    now = datetime.datetime.now(tz)
    current_time = now.strftime('%Y-%m-%d %H:%M:%S 北京时间')
    current_date = now.strftime('%Y-%m-%d')

    # 清理旧格式日志文件
    cleanup_legacy_log_files(LOG_DIR)

    # 读取用户标记的拉黑域名
    blacklisted_hostnames = load_blacklisted_hostnames()
    existing_flagged = load_existing_flagged_domains()

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
            show_items = added_direct_rules[:MAX_LOG_ITEMS]
            log_lines.extend([f"- {rule}" for rule in show_items])
            if len(added_direct_rules) > MAX_LOG_ITEMS:
                log_lines.append(f"仅显示前 {MAX_LOG_ITEMS} 条，共 {len(added_direct_rules)} 条")
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
        show_items = added_proxy_rules[:MAX_LOG_ITEMS]
        log_lines.extend([f"- {rule}" for rule in show_items])
        if len(added_proxy_rules) > MAX_LOG_ITEMS:
            log_lines.append(f"仅显示前 {MAX_LOG_ITEMS} 条，共 {len(added_proxy_rules)} 条")
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
        show_items = added_reject_rules[:MAX_LOG_ITEMS]
        log_lines.extend([f"- {rule}" for rule in show_items])
        if len(added_reject_rules) > MAX_LOG_ITEMS:
            log_lines.append(f"仅显示前 {MAX_LOG_ITEMS} 条，共 {len(added_reject_rules)} 条")
    log_lines.append("\n")

    # ====== 合并 hostname（应用安全过滤） ======
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

    # 更新 config/flagged_domains.txt
    update_flagged_domains_file(dangerous_domains)

    # 在当天日志子目录中保存危险域名快照
    log_subdir, _ = get_log_dir_and_base(current_date)
    snapshot_path = os.path.join(log_subdir, "dangerous_domains.txt")
    with open(snapshot_path, 'w', encoding='utf-8') as f:
        f.write(f"# 危险域名快照 {current_date}\n")
        f.write(f"# 共 {len(dangerous_domains)} 个\n\n")
        for d in sorted(dangerous_domains):
            f.write(d + "\n")
    print(f"Dangerous domains snapshot saved to {snapshot_path}")

    merged_hostnames = ', '.join(filtered_hostnames)
    if FORCE_APPEND:
        if not merged_hostnames.startswith('%APPEND%'):
            merged_hostnames = '%APPEND% ' + merged_hostnames

    # 日志记录敏感域名（全部显示）
    if sensitive_removed:
        log_lines.append("## ⚠️ 敏感域名已自动过滤（银行/支付）\n")
        log_lines.extend([f"- {h}" for h in sensitive_removed])
        log_lines.append("\n")

    # 日志记录危险域名（全部显示）
    new_dangerous = [d for d in dangerous_domains if d not in existing_flagged]
    if new_dangerous:
        log_lines.append(f"## ⚠️ 新发现危险域名（共 {len(new_dangerous)} 个，默认保留）\n")
        log_lines.append("如需拉黑，编辑 `config/flagged_domains.txt`，在对应域名后加 `#black`，然后手动运行脚本即可。\n")
        log_lines.extend([f"- {h}" for h in new_dangerous])
        log_lines.append("\n")

    # 本地化脚本
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
            print(f"Downloaded independent JS: {filename}")
            independent_log.append(f"✅ {filename} 下载成功")
            risks = scan_js_content(content)
            if risks:
                independent_log.append(f"⚠️ {filename} 可疑模式: {', '.join(risks[:3])}")
        except Exception as e:
            print(f"Failed to download {url}: {e}")
            independent_log.append(f"❌ {filename} 下载失败: {e}")

    if independent_log:
        log_lines.append("## 独立 JS 源\n")
        log_lines.extend([f"- {status}" for status in independent_log])
        log_lines.append("\n")

    # 写入日志文件（同一天自动编号，最多5个）
    log_lines.append("---\n")
    log_content = "\n".join(log_lines)
    log_file_path = get_log_file_path(current_date)
    with open(log_file_path, 'w', encoding='utf-8') as f:
        f.write(log_content)
    print(f"Log written to {log_file_path}")

if __name__ == "__main__":
    main()