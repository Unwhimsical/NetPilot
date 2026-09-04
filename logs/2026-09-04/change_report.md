# 变更报告 2026-09-04

生成时间：2026-09-04 17:00:40

---

## 直连模块

- 原有规则数：110117
- 新增规则数：0
- 过滤海外规则：1159
- 最终规则数：110117

## 代理模块

- 原有规则数：27327
- 新增规则数：0
- 最终规则数：27327

## 去广告模块

- 原有规则数：189157
- 新增规则数：0
- 最终规则数：189157

## 规则冲突检测

检测到 17 组同域名策略冲突：

- DOMAIN-SUFFIX:adashx.m.taobao.com
  - DOMAIN-SUFFIX,adashx.m.taobao.com,REJECT
  - DOMAIN-SUFFIX,adashx.m.taobao.com,REJECT-200
- DOMAIN-SUFFIX:amdc.m.taobao.com
  - DOMAIN-SUFFIX,amdc.m.taobao.com,REJECT
  - DOMAIN-SUFFIX,amdc.m.taobao.com,REJECT-200
- DOMAIN-SUFFIX:applog.uc.cn
  - DOMAIN-SUFFIX,applog.uc.cn,REJECT
  - DOMAIN-SUFFIX,applog.uc.cn,REJECT-200
- DOMAIN-SUFFIX:cnlogs.umengcloud.com
  - DOMAIN-SUFFIX,cnlogs.umengcloud.com,REJECT
  - DOMAIN-SUFFIX,cnlogs.umengcloud.com,REJECT-DICT
- DOMAIN-SUFFIX:df.tanx.com
  - DOMAIN-SUFFIX,df.tanx.com,REJECT
  - DOMAIN-SUFFIX,df.tanx.com,REJECT-200
- DOMAIN-SUFFIX:dualstack-logs.amap.com
  - DOMAIN-SUFFIX,dualstack-logs.amap.com,REJECT
  - DOMAIN-SUFFIX,dualstack-logs.amap.com,REJECT-200
- DOMAIN-SUFFIX:e.qq.com
  - DOMAIN-SUFFIX,e.qq.com,REJECT
  - DOMAIN-SUFFIX,e.qq.com,REJECT-DICT
- DOMAIN-SUFFIX:h-adashx.ut.taobao.com
  - DOMAIN-SUFFIX,h-adashx.ut.taobao.com,REJECT
  - DOMAIN-SUFFIX,h-adashx.ut.taobao.com,REJECT-200
- DOMAIN-SUFFIX:imasdk.googleapis.com
  - DOMAIN-SUFFIX,imasdk.googleapis.com,REJECT
  - DOMAIN-SUFFIX,imasdk.googleapis.com,REJECT-DICT
- DOMAIN-SUFFIX:iyes.youku.com
  - DOMAIN-SUFFIX,iyes.youku.com,REJECT
  - DOMAIN-SUFFIX,iyes.youku.com,REJECT-200
## 父子域冲突检测

未检测到父子域冲突。

## 质量检查

发现 7 条异常规则：

- ('URL-REGEX,"^https?:\\/\\/(.*\\.)?gossipfuli[0-9]{3,4}\\.xyz.*$",PROXY', '策略 \'4}\\.XYZ.*$"\' 不合法')
- ('URL-REGEX,"^https?:\\/\\/(.*\\.)?zayy([0-9]{0,3})?\\.xyz.*$",PROXY', '策略 \'3})?\\.XYZ.*$"\' 不合法')
- ('URL-REGEX,"^https?:\\/\\/(.*\\.)?supxxx[0-9]{0,2}\\.com.*$",PROXY', '策略 \'2}\\.COM.*$"\' 不合法')
- ('URL-REGEX,"^https?:\\/\\/(.*\\.)?jiuse[0-9]{1,3}\\.com.*$",PROXY', '策略 \'3}\\.COM.*$"\' 不合法')
- ('URL-REGEX,"^https?:\\/\\/(.*\\.)?luchuxue([0-9]{0,5})\\.buzz.*$",PROXY', '策略 \'5})\\.BUZZ.*$"\' 不合法')
- ('URL-REGEX,"^https?:\\/\\/(.*\\.)?chuzs[1-9]{0,2}\\.buzz.*$",PROXY', '策略 \'2}\\.BUZZ.*$"\' 不合法')
- ('DOMAIN-SUFFIX,OMAIN-SUFFIX,bing.net,PROXY', "策略 'BING.NET' 不合法")
## 规则源健康状态

- ✅ https://raw.githubusercontent.com/GMOogway/shadowrocket-rules/master/sr_direct_list.module (成功 3, 失败 0, 连续失败 0)
- ✅ https://raw.githubusercontent.com/GMOogway/shadowrocket-rules/master/sr_proxy_list.module (成功 3, 失败 0, 连续失败 0)
- ✅ https://raw.githubusercontent.com/LOWERTOP/Shadowrocket-First/main/Talkatone.sgmodule (成功 3, 失败 0, 连续失败 0)
- ✅ https://raw.githubusercontent.com/huijingfei/Shadowrocket-Rules/refs/heads/main/sr_app_ad.module (成功 3, 失败 0, 连续失败 0)
- ✅ https://raw.githubusercontent.com/deezertidal/shadowrocket-rules/refs/heads/main/modules/startingad.module (成功 3, 失败 0, 连续失败 0)
- ✅ https://raw.githubusercontent.com/GMOogway/shadowrocket-rules/master/sr_reject_list.module (成功 3, 失败 0, 连续失败 0)
- ✅ https://raw.githubusercontent.com/Unwhimsical/NetPilot/refs/heads/main/modules/%E6%B5%8B%E8%AF%95.module (成功 3, 失败 0, 连续失败 0)
- ✅ https://raw.githubusercontent.com/LOWERTOP/Shadowrocket-First/main/TalkatoneAntiAds.list (成功 3, 失败 0, 连续失败 0)
---

详细日志请查看同目录下的 update 日志文件。
