#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import re
import requests

# ========== 用户配置区 ==========
GITHUB_USERNAME = "Unwhimsical"        # 请改成你的 GitHub 用户名
REPO_NAME = "NetPilot"
BRANCH = "main"

# 上游模块源：key 为模块类型（direct/shield），value 为 URL 列表
# 注意：direct 源可以留空，留空则不会重新生成直连模块，只保留你手动维护的 NetPilot Direct.module
UPSTREAM_MODULE_SOURCES = {
    "direct": [
        # "https://raw.githubusercontent.com/Unwhimsical/Default/refs/heads/main/sr_direct_list.module",  # 已失效，暂时注释
        # "https://raw.githubusercontent.com/deezertidal/shadowrocket-rules/refs/heads/main/modules/startingad.module",  # 如果可用请取消注释
    ],
    "shield": [
        "https://raw.githubusercontent.com/huijingfei/Shadowrocket-Rules/refs/heads/main/sr_app_ad.module",
        "https://raw.githubusercontent.com/deezertidal/shadowrocket-rules/refs/heads/main/modules/startingad.module",
    ],
}

# 需要本地化的独立 JS 脚本源（键为文件名，值为 URL）
UPSTREAM_JS_SOURCES = {
    "weibo_main.js": "https://raw.githubusercontent.com/zmqcherish/proxy-script/main/weibo_main.js",
    "weibo_launch.js": "https://raw.githubusercontent.com/zmqcherish/proxy-script/main/weibo_launch.js",
    "wechat_ad.js": "https://raw.githubusercontent.com/NobyDa/Script/master/QuantumultX/File/Wechat.js",
}

# 模块文件路径（请根据你仓库中的实际文件名修改，如果文件名包含空格请保留空格）
DIRECT_MODULE_PATH = "modules/NetPilot_Direct.module"   # 或者改为 "modules/NetPilot_Direct.module"
SHIELD_MODULE_PATH = "modules/NetPilot_Shield.module"   # 或者改为 "modules/NetPilot_Shield.module"
LOCAL_JS_DIR = "modules/local_js"

# 是否强制所有 MITM hostname 使用 %APPEND%
FORCE_APPEND = True

# ========== 工具函数 ==========
def fetch(url):
    """下载文本内容，失败时抛出异常"""
    print(f"Fetching: {url}")
    r = requests.get(url, timeout=30)
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

def extract_rules(module_content, policy):
    """
    从模块内容中提取指定策略的规则行
    policy: 例如 'DIRECT', 'REJECT', 'PROXY'
    """
    rules = []
    for line in module_content.splitlines():
        line = line.strip()
        # 匹配类似 DOMAIN-SUFFIX,example.com,DIRECT 的规则，忽略注释和空行
        if line.startswith(('DOMAIN,', 'DOMAIN-SUFFIX,', 'DOMAIN-KEYWORD,', 'IP-CIDR,', 'IP-CIDR6,', 'USER-AGENT,', 'PROCESS-NAME,', 'URL-REGEX,')):
            # 检查策略是否匹配（考虑策略后可能带 no-resolve 等附加参数）
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

def localize_scripts(scripts, local_js_dir):
    """
    下载脚本中引用的 JS 文件到 local_js_dir，并替换 script-path 为本地仓库 URL
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
        except Exception as e:
            print(f"Failed to download {original_url}: {e}")
            # 下载失败则保留原始脚本行（不替换路径）
            updated_scripts.append(script_line)
            continue
        # 生成本地 raw URL
        local_url = f"https://raw.githubusercontent.com/{GITHUB_USERNAME}/{REPO_NAME}/{BRANCH}/{LOCAL_JS_DIR}/{filename}"
        new_line = script_line.replace(original_url, local_url)
        updated_scripts.append(new_line)
    return updated_scripts

def main():
    # ========== 处理直连模块 ==========
    print("=== Processing Direct Module ===")
    if UPSTREAM_MODULE_SOURCES["direct"]:
        direct_rules = []
        for url in UPSTREAM_MODULE_SOURCES["direct"]:
            try:
                content = fetch(url)
                content = clean_mitm(content)
                direct_rules.extend(extract_rules(content, 'DIRECT'))
            except Exception as e:
                print(f"Failed to process {url}: {e}")
        # 去重
        seen = set()
        unique_direct = []
        for rule in direct_rules:
            if rule not in seen:
                seen.add(rule)
                unique_direct.append(rule)
        # 生成直连模块
        direct_module = "#!name=NetPilot Direct\n#!desc=国内直连规则，自动更新\n[Rule]\n" + "\n".join(unique_direct) + "\n"
        direct_module += "GEOIP,CN,DIRECT\n"
        os.makedirs(os.path.dirname(DIRECT_MODULE_PATH), exist_ok=True)
        with open(DIRECT_MODULE_PATH, 'w', encoding='utf-8') as f:
            f.write(direct_module)
        print("Direct module written.")
    else:
        print("No direct upstream sources, skipping Direct module generation (manual file preserved).")

    # ========== 处理去广告模块 ==========
    print("=== Processing Shield Module ===")
    reject_rules = []
    rewrite_rules = []
    all_scripts = []
    for url in UPSTREAM_MODULE_SOURCES["shield"]:
        try:
            content = fetch(url)
            content = clean_mitm(content)
            reject_rules.extend(extract_rules(content, 'REJECT'))
            reject_rules.extend(extract_rules(content, 'REJECT-200'))
            reject_rules.extend(extract_rules(content, 'REJECT-DICT'))
            reject_rules.extend(extract_rules(content, 'REJECT-IMG'))
            reject_rules.extend(extract_rules(content, 'REJECT-NO-DROP'))
            rewrite_rules.extend(extract_url_rewrite(content))
            all_scripts.extend(extract_scripts(content))
        except Exception as e:
            print(f"Failed to process {url}: {e}")

    # 去重 reject
    seen_reject = set()
    unique_reject = []
    for rule in reject_rules:
        if rule not in seen_reject:
            seen_reject.add(rule)
            unique_reject.append(rule)

    # 去重 rewrite
    seen_rewrite = set()
    unique_rewrite = []
    for rule in rewrite_rules:
        if rule not in seen_rewrite:
            seen_rewrite.add(rule)
            unique_rewrite.append(rule)

    # 本地化 JS 脚本
    updated_scripts = localize_scripts(all_scripts, LOCAL_JS_DIR)

    # 组装 shield 模块
    shield_parts = ["#!name=NetPilot Shield", "#!desc=去广告模块，自动更新", "[Rule]"]
    shield_parts.append("\n".join(unique_reject))
    shield_parts.append("[URL Rewrite]")
    shield_parts.append("\n".join(unique_rewrite))
    shield_parts.append("[Script]")
    shield_parts.append("\n".join(updated_scripts))
    shield_parts.append("[MITM]")

    # 获取已有 shield 模块中的 hostname（如果有），否则用默认
    existing_shield_hostnames = ""
    if os.path.exists(SHIELD_MODULE_PATH):
        with open(SHIELD_MODULE_PATH, 'r', encoding='utf-8') as f:
            old_content = f.read()
        old_mitm_match = re.search(r'\[MITM\](.*?)(?=\[|$)', old_content, re.DOTALL)
        if old_mitm_match:
            old_hostname_match = re.search(r'(?im)^\s*hostname\s*=\s*(.*)$', old_mitm_match.group(1))
            if old_hostname_match:
                existing_shield_hostnames = old_hostname_match.group(1).strip()
    if not existing_shield_hostnames:
        existing_shield_hostnames = "%APPEND%"
    shield_parts.append(f"enable = true\nhostname = {existing_shield_hostnames}")
    shield_content = "\n\n".join(shield_parts) + "\n"
    os.makedirs(os.path.dirname(SHIELD_MODULE_PATH), exist_ok=True)
    with open(SHIELD_MODULE_PATH, 'w', encoding='utf-8') as f:
        f.write(shield_content)
    print("Shield module written.")

    # ========== 处理独立 JS 源 ==========
    for filename, url in UPSTREAM_JS_SOURCES.items():
        local_path = os.path.join(LOCAL_JS_DIR, filename)
        os.makedirs(LOCAL_JS_DIR, exist_ok=True)
        try:
            content = fetch(url)
            with open(local_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Downloaded independent JS: {filename}")
        except Exception as e:
            print(f"Failed to download {url}: {e}")

if __name__ == "__main__":
    main()
