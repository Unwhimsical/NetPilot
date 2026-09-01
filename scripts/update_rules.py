#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import re
import requests
import hashlib
import json

# ========== 用户配置区 ==========
# 你的 GitHub 用户名（用于生成 raw URL）
GITHUB_USERNAME = "Unwhimsical"
REPO_NAME = "NetPilot"
BRANCH = "main"

# 上游模块源：key 为模块类型（direct/shield），value 为 URL 列表
UPSTREAM_MODULE_SOURCES = {
    "direct": [
        "https://raw.githubusercontent.com/Unwhimsical/Default/refs/heads/main/sr_direct_list.module",
        "https://raw.githubusercontent.com/deezertidal/shadowrocket-rules/refs/heads/main/modules/startingad.module",
        
        # 可添加更多直连源
    ],
    "shield": [
        "https://raw.githubusercontent.com/huijingfei/Shadowrocket-Rules/refs/heads/main/sr_app_ad.module",
        # 如果有微博模块的 URL 也可以添加，这里假设你已将微博规则合并进 shield，无需额外源
    ],
}

# 需要本地化的 JS 脚本源（键为文件名，值为 URL）
UPSTREAM_JS_SOURCES = {
    "weibo_main.js": "https://raw.githubusercontent.com/zmqcherish/proxy-script/main/weibo_main.js",
    "weibo_launch.js": "https://raw.githubusercontent.com/zmqcherish/proxy-script/main/weibo_launch.js",
    "wechat_ad.js": "https://raw.githubusercontent.com/NobyDa/Script/master/QuantumultX/File/Wechat.js",
    # 以后新增脚本在此添加
}

# 模块文件路径
DIRECT_MODULE_PATH = "modules/NetPilot_Direct.module"
SHIELD_MODULE_PATH = "modules/NetPilot_Shield.module"
LOCAL_JS_DIR = "modules/local_js"

# 是否强制所有 MITM hostname 使用 %APPEND%
FORCE_APPEND = True

# ========== 工具函数 ==========
def fetch(url):
    """下载文本内容"""
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
    # 提取 [MITM] 段
    mitm_match = re.search(r'\[MITM\](.*?)(?=\[|$)', module_content, re.DOTALL)
    if not mitm_match:
        return module_content
    mitm_block = mitm_match.group(1)
    # 删除 ca-p12 和 ca-passphrase 行
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
        # 没有 hostname，添加空 hostname
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
        # 匹配形如 TYPE,value,policy 或 TYPE,value,policy,no-resolve
        if line.startswith(('DOMAIN,', 'DOMAIN-SUFFIX,', 'DOMAIN-KEYWORD,', 'IP-CIDR,', 'IP-CIDR6,', 'USER-AGENT,', 'PROCESS-NAME,', 'URL-REGEX,')):
            if line.endswith(',' + policy) or (policy + ',') in line:
                rules.append(line)
    return rules

def extract_url_rewrite(module_content):
    """提取 URL Rewrite 规则（非注释行）"""
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
    """提取所有 Script 条目"""
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
    下载脚本中的 JS 文件到 local_js_dir，并替换 script-path 为本地 URL
    返回更新后的脚本列表
    """
    os.makedirs(local_js_dir, exist_ok=True)
    updated_scripts = []
    for script_line in scripts:
        # 提取 script-path 中的 URL
        m = re.search(r'script-path=([^,\s]+)', script_line)
        if not m:
            updated_scripts.append(script_line)
            continue
        original_url = m.group(1)
        filename = original_url.split('/')[-1]
        local_path = os.path.join(local_js_dir, filename)
        # 下载文件
        try:
            content = fetch(original_url)
            with open(local_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Downloaded JS: {filename}")
        except Exception as e:
            print(f"Failed to download {original_url}: {e}")
            # 保留原样
            updated_scripts.append(script_line)
            continue
        # 生成本地 raw URL
        local_url = f"https://raw.githubusercontent.com/{GITHUB_USERNAME}/{REPO_NAME}/{BRANCH}/{LOCAL_JS_DIR}/{filename}"
        new_line = script_line.replace(original_url, local_url)
        updated_scripts.append(new_line)
    return updated_scripts

def build_module(content_parts):
    """将各部分组装成完整模块文本"""
    return "\n".join(content_parts)

def main():
    # 处理直连模块
    print("=== Processing Direct Module ===")
    direct_rules = []
    for url in UPSTREAM_MODULE_SOURCES["direct"]:
        content = fetch(url)
        # 清洗 MITM（直连模块一般不需要 MITM，但以防万一）
        content = clean_mitm(content)
        direct_rules.extend(extract_rules(content, 'DIRECT'))
    # 去重并保持顺序
    seen = set()
    unique_direct = []
    for rule in direct_rules:
        if rule not in seen:
            seen.add(rule)
            unique_direct.append(rule)
    # 组装直连模块
    direct_module = "#!name=NetPilot Direct\n#!desc=国内直连规则，自动更新\n[Rule]\n" + "\n".join(unique_direct) + "\n"
    # 添加常见兜底规则（可选）
    direct_module += "GEOIP,CN,DIRECT\n"
    # 写入文件
    os.makedirs(os.path.dirname(DIRECT_MODULE_PATH), exist_ok=True)
    with open(DIRECT_MODULE_PATH, 'w', encoding='utf-8') as f:
        f.write(direct_module)
    print("Direct module written.")

    # 处理去广告模块
    print("=== Processing Shield Module ===")
    reject_rules = []
    rewrite_rules = []
    all_scripts = []
    for url in UPSTREAM_MODULE_SOURCES["shield"]:
        content = fetch(url)
        content = clean_mitm(content)
        reject_rules.extend(extract_rules(content, 'REJECT'))
        reject_rules.extend(extract_rules(content, 'REJECT-200'))
        reject_rules.extend(extract_rules(content, 'REJECT-DICT'))
        reject_rules.extend(extract_rules(content, 'REJECT-IMG'))
        reject_rules.extend(extract_rules(content, 'REJECT-NO-DROP'))
        rewrite_rules.extend(extract_url_rewrite(content))
        all_scripts.extend(extract_scripts(content))
    # 去重
    seen_reject = set()
    unique_reject = []
    for rule in reject_rules:
        if rule not in seen_reject:
            seen_reject.add(rule)
            unique_reject.append(rule)
    seen_rewrite = set()
    unique_rewrite = []
    for rule in rewrite_rules:
        if rule not in seen_rewrite:
            seen_rewrite.add(rule)
            unique_rewrite.append(rule)
    # 本地化脚本
    updated_scripts = localize_scripts(all_scripts, LOCAL_JS_DIR)
    # 组装 shield 模块
    shield_parts = ["#!name=NetPilot Shield", "#!desc=去广告模块，自动更新", "[Rule]"]
    shield_parts.append("\n".join(unique_reject))
    shield_parts.append("[URL Rewrite]")
    shield_parts.append("\n".join(unique_rewrite))
    shield_parts.append("[Script]")
    shield_parts.append("\n".join(updated_scripts))
    shield_parts.append("[MITM]")
    # 合并 hostname：这里简单把 common 解密域名加上，实际应从上游提取，但我们已经删除了 ca-p12，需要从原始内容提取 hostname 合并。
    # 此处为简化，从本地 shield 文件可能已有 hostname，我们保留原有模块中的 hostname（如果存在）
    # 获取现有 shield 文件的 hostname 并追加
    existing_shield_hostnames = ""
    if os.path.exists(SHIELD_MODULE_PATH):
        with open(SHIELD_MODULE_PATH, 'r', encoding='utf-8') as f:
            old_content = f.read()
        old_mitm_match = re.search(r'\[MITM\](.*?)(?=\[|$)', old_content, re.DOTALL)
        if old_mitm_match:
            old_hostname_match = re.search(r'(?im)^\s*hostname\s*=\s*(.*)$', old_mitm_match.group(1))
            if old_hostname_match:
                existing_shield_hostnames = old_hostname_match.group(1).strip()
    # 如果现有 hostname 为空，设置默认
    if not existing_shield_hostnames:
        existing_shield_hostnames = "%APPEND%"
    shield_parts.append(f"enable = true\nhostname = {existing_shield_hostnames}")
    shield_content = "\n\n".join(shield_parts) + "\n"
    with open(SHIELD_MODULE_PATH, 'w', encoding='utf-8') as f:
        f.write(shield_content)
    print("Shield module written.")

    # 处理独立 JS 源（即使模块中没有引用，也确保下载）
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
