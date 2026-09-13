# 变更报告 2026-09-05

生成时间：2026-09-05 15:05:34

---

## 直连模块

- 原有规则数：110375
- 新增规则数：0
- 过滤海外规则：930
- 最终规则数：110375

## 代理模块

- 原有规则数：27339
- 新增规则数：0
- 最终规则数：27339

## 去广告模块

- 原有规则数：189463
- 新增规则数：0
- 最终规则数：189463

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

发现 1 条异常规则：

- ('DOMAIN-SUFFIX,OMAIN-SUFFIX,bing.net,PROXY', "策略 'BING.NET' 不合法")
## 规则源健康状态

- ✅ https://raw.githubusercontent.com/GMOogway/shadowrocket-rules/master/sr_direct_list.module (成功 8, 失败 0, 连续失败 0)
- ✅ https://raw.githubusercontent.com/GMOogway/shadowrocket-rules/master/sr_proxy_list.module (成功 8, 失败 0, 连续失败 0)
- ✅ https://raw.githubusercontent.com/LOWERTOP/Shadowrocket-First/main/Talkatone.sgmodule (成功 8, 失败 0, 连续失败 0)
- ✅ https://raw.githubusercontent.com/huijingfei/Shadowrocket-Rules/refs/heads/main/sr_app_ad.module (成功 8, 失败 0, 连续失败 0)
- ✅ https://raw.githubusercontent.com/deezertidal/shadowrocket-rules/refs/heads/main/modules/startingad.module (成功 8, 失败 0, 连续失败 0)
- ✅ https://raw.githubusercontent.com/GMOogway/shadowrocket-rules/master/sr_reject_list.module (成功 8, 失败 0, 连续失败 0)
- ✅ https://raw.githubusercontent.com/Unwhimsical/NetPilot/refs/heads/main/modules/%E6%B5%8B%E8%AF%95.module (成功 8, 失败 0, 连续失败 0)
- ✅ https://raw.githubusercontent.com/LOWERTOP/Shadowrocket-First/main/TalkatoneAntiAds.list (成功 8, 失败 0, 连续失败 0)
## DNS 泄漏风险

- **高风险 - 直连海外域名**
  直连规则包含海外域名: DOMAIN,adcdownload.apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **高风险 - 直连海外域名**
  直连规则包含海外域名: DOMAIN,adcdownload.apple.com.akadns.net,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **高风险 - 直连海外域名**
  直连规则包含海外域名: DOMAIN,amp-api-edge-lb-cn.itunes-apple.com.akadns.net,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **高风险 - 直连海外域名**
  直连规则包含海外域名: DOMAIN,amp-api-edge-lb.itunes-apple.com.akadns.net,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **高风险 - 直连海外域名**
  直连规则包含海外域名: DOMAIN,amp-api-edge.apps.apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **高风险 - 直连海外域名**
  直连规则包含海外域名: DOMAIN,amp-api-edge.music.apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **高风险 - 直连海外域名**
  直连规则包含海外域名: DOMAIN,amp-api-search-edge.apps.apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **高风险 - 直连海外域名**
  直连规则包含海外域名: DOMAIN,amp-api-updates.apps.apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **高风险 - 直连海外域名**
  直连规则包含海外域名: DOMAIN,amp-api.apps.apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **高风险 - 直连海外域名**
  直连规则包含海外域名: DOMAIN,amp-api.media.apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **高风险 - 直连海外域名**
  直连规则包含海外域名: DOMAIN,amp-api.music.apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **高风险 - 直连海外域名**
  直连规则包含海外域名: DOMAIN,amp-api.podcasts.apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **高风险 - 直连海外域名**
  直连规则包含海外域名: DOMAIN,aod-ssl.itunes.apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **高风险 - 直连海外域名**
  直连规则包含海外域名: DOMAIN,aod.itunes.apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **高风险 - 直连海外域名**
  直连规则包含海外域名: DOMAIN,api-edge.apps.apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **高风险 - 直连海外域名**
  直连规则包含海外域名: DOMAIN,app-site-association.cdn-apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **高风险 - 直连海外域名**
  直连规则包含海外域名: DOMAIN,appldnld.apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **高风险 - 直连海外域名**
  直连规则包含海外域名: DOMAIN,appleid.cdn-apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **高风险 - 直连海外域名**
  直连规则包含海外域名: DOMAIN,apptrailers.itunes.apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **高风险 - 直连海外域名**
  直连规则包含海外域名: DOMAIN,bag-cdn.itunes-apple.com.akadns.net,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **高风险 - 直连海外域名**
  直连规则包含海外域名: DOMAIN,bag.itunes.apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **高风险 - 直连海外域名**
  直连规则包含海外域名: DOMAIN,bookkeeper.itunes.apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **高风险 - 直连海外域名**
  直连规则包含海外域名: DOMAIN,cdn-cn.apple-mapkit.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **高风险 - 直连海外域名**
  直连规则包含海外域名: DOMAIN,cdn-cn1.apple-mapkit.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **高风险 - 直连海外域名**
  直连规则包含海外域名: DOMAIN,cdn-cn2.apple-mapkit.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **高风险 - 直连海外域名**
  直连规则包含海外域名: DOMAIN,cdn-cn3.apple-mapkit.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **高风险 - 直连海外域名**
  直连规则包含海外域名: DOMAIN,cdn-cn4.apple-mapkit.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **高风险 - 直连海外域名**
  直连规则包含海外域名: DOMAIN,cdn.apple-mapkit.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **高风险 - 直连海外域名**
  直连规则包含海外域名: DOMAIN,cdn1.apple-mapkit.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **高风险 - 直连海外域名**
  直连规则包含海外域名: DOMAIN,cdn2.apple-mapkit.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **高风险 - 直连海外域名**
  直连规则包含海外域名: DOMAIN,cdn3.apple-mapkit.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **高风险 - 直连海外域名**
  直连规则包含海外域名: DOMAIN,cdn4.apple-mapkit.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **高风险 - 直连海外域名**
  直连规则包含海外域名: DOMAIN,cds.apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **高风险 - 直连海外域名**
  直连规则包含海外域名: DOMAIN,cds.apple.com.akadns.net,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **高风险 - 直连海外域名**
  直连规则包含海外域名: DOMAIN,cdsassets.apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **高风险 - 直连海外域名**
  直连规则包含海外域名: DOMAIN,certs-lb.apple.com.akadns.net,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **高风险 - 直连海外域名**
  直连规则包含海外域名: DOMAIN,certs.apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **高风险 - 直连海外域名**
  直连规则包含海外域名: DOMAIN,cl1-cdn.origin-apple.com.akadns.net,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **高风险 - 直连海外域名**
  直连规则包含海外域名: DOMAIN,cl1.apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **高风险 - 直连海外域名**
  直连规则包含海外域名: DOMAIN,cl2-cdn.origin-apple.com.akadns.net,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **高风险 - 直连海外域名**
  直连规则包含海外域名: DOMAIN,cl2-cn.apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **高风险 - 直连海外域名**
  直连规则包含海外域名: DOMAIN,cl2.apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **高风险 - 直连海外域名**
  直连规则包含海外域名: DOMAIN,cl2.apple.com.edgekey.net.globalredir.akadns.net,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **高风险 - 直连海外域名**
  直连规则包含海外域名: DOMAIN,cl3-cdn.origin-apple.com.akadns.net,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **高风险 - 直连海外域名**
  直连规则包含海外域名: DOMAIN,cl3.apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **高风险 - 直连海外域名**
  直连规则包含海外域名: DOMAIN,cl4-cdn.origin-apple.com.akadns.net,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **高风险 - 直连海外域名**
  直连规则包含海外域名: DOMAIN,cl4-cn.apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **高风险 - 直连海外域名**
  直连规则包含海外域名: DOMAIN,cl4.apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **高风险 - 直连海外域名**
  直连规则包含海外域名: DOMAIN,cl5-cdn.origin-apple.com.akadns.net,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **高风险 - 直连海外域名**
  直连规则包含海外域名: DOMAIN,cl5.apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **高风险 - 直连海外域名**
  直连规则包含海外域名: DOMAIN,client-api.itunes.apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **高风险 - 直连海外域名**
  直连规则包含海外域名: DOMAIN,clientflow.apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **高风险 - 直连海外域名**
  直连规则包含海外域名: DOMAIN,clientflow.apple.com.akadns.net,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **高风险 - 直连海外域名**
  直连规则包含海外域名: DOMAIN,cma.itunes.apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **高风险 - 直连海外域名**
  直连规则包含海外域名: DOMAIN,cn-smp-paymentservices.apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **高风险 - 直连海外域名**
  直连规则包含海外域名: DOMAIN,communities.apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **高风险 - 直连海外域名**
  直连规则包含海外域名: DOMAIN,configuration.apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **高风险 - 直连海外域名**
  直连规则包含海外域名: DOMAIN,configuration.apple.com.akadns.net,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **高风险 - 直连海外域名**
  直连规则包含海外域名: DOMAIN,crl-lb.apple.com.akadns.net,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **高风险 - 直连海外域名**
  直连规则包含海外域名: DOMAIN,crl.apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **高风险 - 直连海外域名**
  直连规则包含海外域名: DOMAIN,cstat.apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **高风险 - 直连海外域名**
  直连规则包含海外域名: DOMAIN,cstat.cdn-apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **高风险 - 直连海外域名**
  直连规则包含海外域名: DOMAIN,dd-cdn.origin-apple.com.akadns.net,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **高风险 - 直连海外域名**
  直连规则包含海外域名: DOMAIN,dejavu.apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **高风险 - 直连海外域名**
  直连规则包含海外域名: DOMAIN,devimages-cdn.apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **高风险 - 直连海外域名**
  直连规则包含海外域名: DOMAIN,devstreaming-cdn.apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **高风险 - 直连海外域名**
  直连规则包含海外域名: DOMAIN,discussionschinese.apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **高风险 - 直连海外域名**
  直连规则包含海外域名: DOMAIN,download.developer.apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **高风险 - 直连海外域名**
  直连规则包含海外域名: DOMAIN,downloaddispatch.itunes.apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **高风险 - 直连海外域名**
  直连规则包含海外域名: DOMAIN,entitlements-edge.itunes.apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **高风险 - 直连海外域名**
  直连规则包含海外域名: DOMAIN,experiments.apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **高风险 - 直连海外域名**
  直连规则包含海外域名: DOMAIN,fides-pol.apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **高风险 - 直连海外域名**
  直连规则包含海外域名: DOMAIN,fpinit.itunes.apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **高风险 - 直连海外域名**
  直连规则包含海外域名: DOMAIN,gsp10-ssl-cn.ls.apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **高风险 - 直连海外域名**
  直连规则包含海外域名: DOMAIN,gsp11-cn.ls.apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **高风险 - 直连海外域名**
  直连规则包含海外域名: DOMAIN,gsp12-cn.ls.apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **高风险 - 直连海外域名**
  直连规则包含海外域名: DOMAIN,gsp13-cn.ls.apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **高风险 - 直连海外域名**
  直连规则包含海外域名: DOMAIN,gsp4-cn.ls.apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **高风险 - 直连海外域名**
  直连规则包含海外域名: DOMAIN,gsp4-cn.ls.apple.com.edgekey.net.globalredir.akadns.net,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **高风险 - 直连海外域名**
  直连规则包含海外域名: DOMAIN,gsp5-cn.ls.apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **高风险 - 直连海外域名**
  直连规则包含海外域名: DOMAIN,gsp85-cn-ssl.ls.apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **高风险 - 直连海外域名**
  直连规则包含海外域名: DOMAIN,gspe11-2-cn-ssl.ls.apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **高风险 - 直连海外域名**
  直连规则包含海外域名: DOMAIN,gspe12-cn-ssl.ls.apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **高风险 - 直连海外域名**
  直连规则包含海外域名: DOMAIN,gspe19-2-cn-ssl.ls-apple.com.akadns.net,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **高风险 - 直连海外域名**
  直连规则包含海外域名: DOMAIN,gspe19-2-cn-ssl.ls.apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **高风险 - 直连海外域名**
  直连规则包含海外域名: DOMAIN,gspe19-cn-ssl.ls.apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **高风险 - 直连海外域名**
  直连规则包含海外域名: DOMAIN,gspe19-cn.ls-apple.com.akadns.net,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **高风险 - 直连海外域名**
  直连规则包含海外域名: DOMAIN,gspe19-cn.ls.apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **高风险 - 直连海外域名**
  直连规则包含海外域名: DOMAIN,gspe21-ssl.ls.apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **高风险 - 直连海外域名**
  直连规则包含海外域名: DOMAIN,gspe35-ssl.ls.apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **高风险 - 直连海外域名**
  直连规则包含海外域名: DOMAIN,gspe79-cn-ssl.ls.apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **高风险 - 直连海外域名**
  直连规则包含海外域名: DOMAIN,gspe85-cn-ssl.ls.apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **高风险 - 直连海外域名**
  直连规则包含海外域名: DOMAIN,guzzoni-apple-com.v.aaplimg.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **高风险 - 直连海外域名**
  直连规则包含海外域名: DOMAIN,guzzoni.apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **高风险 - 直连海外域名**
  直连规则包含海外域名: DOMAIN,guzzoni.smoot.apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **高风险 - 直连海外域名**
  直连规则包含海外域名: DOMAIN,images.apple.com.edgekey.net.globalredir.akadns.net,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **高风险 - 直连海外域名**
  直连规则包含海外域名: DOMAIN,inappcheck-cn.itunes-apple.com.akadns.net,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **高风险 - 直连海外域名**
  直连规则包含海外域名: DOMAIN,inappcheck-lb.itunes-apple.com.akadns.net,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **高风险 - 直连海外域名**
  直连规则包含海外域名: DOMAIN,inappcheck.itunes.apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **高风险 - 直连海外域名**
  直连规则包含海外域名: DOMAIN,init-kt.apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **高风险 - 直连海外域名**
  直连规则包含海外域名: DOMAIN,init-p01md-lb.push-apple.com.akadns.net,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **高风险 - 直连海外域名**
  直连规则包含海外域名: DOMAIN,init-p01md.apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **高风险 - 直连海外域名**
  直连规则包含海外域名: DOMAIN,init-p01st-lb.push-apple.com.akadns.net,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **高风险 - 直连海外域名**
  直连规则包含海外域名: DOMAIN,init-p01st.push.apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **高风险 - 直连海外域名**
  直连规则包含海外域名: DOMAIN,init-s01st-lb.push-apple.com.akadns.net,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **高风险 - 直连海外域名**
  直连规则包含海外域名: DOMAIN,init-s01st.push.apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **高风险 - 直连海外域名**
  直连规则包含海外域名: DOMAIN,init.ess.apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **高风险 - 直连海外域名**
  直连规则包含海外域名: DOMAIN,init.gc-lb.apple.com.akadns.net,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **高风险 - 直连海外域名**
  直连规则包含海外域名: DOMAIN,init.gc.apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **高风险 - 直连海外域名**
  直连规则包含海外域名: DOMAIN,init.itunes.apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **高风险 - 直连海外域名**
  直连规则包含海外域名: DOMAIN,iosapps.itunes.apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **高风险 - 直连海外域名**
  直连规则包含海外域名: DOMAIN,ipcdn.apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **高风险 - 直连海外域名**
  直连规则包含海外域名: DOMAIN,iphone-ld.apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **高风险 - 直连海外域名**
  直连规则包含海外域名: DOMAIN,iphone-ld.origin-apple.com.akadns.net,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **高风险 - 直连海外域名**
  直连规则包含海外域名: DOMAIN,is-ssl.mzstatic.com-cn-lb.itunes-apple.com.akadns.net,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **高风险 - 直连海外域名**
  直连规则包含海外域名: DOMAIN,itunes-apple.com.akadns.net,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **高风险 - 直连海外域名**
  直连规则包含海外域名: DOMAIN,itunes.apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **高风险 - 直连海外域名**
  直连规则包含海外域名: DOMAIN,itunesconnect.apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **高风险 - 直连海外域名**
  直连规则包含海外域名: DOMAIN,js-cdn.music.apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **高风险 - 直连海外域名**
  直连规则包含海外域名: DOMAIN,km.support.apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **高风险 - 直连海外域名**
  直连规则包含海外域名: DOMAIN,maps.apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **高风险 - 直连海外域名**
  直连规则包含海外域名: DOMAIN,mensura.cdn-apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **高风险 - 直连海外域名**
  直连规则包含海外域名: DOMAIN,mesu-cdn.apple.com.akadns.net,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **高风险 - 直连海外域名**
  直连规则包含海外域名: DOMAIN,mesu-china.apple.com.akadns.net,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **高风险 - 直连海外域名**
  直连规则包含海外域名: DOMAIN,mesu.apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **高风险 - 直连海外域名**
  直连规则包含海外域名: DOMAIN,misc-assets.itunes.apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **高风险 - 直连海外域名**
  直连规则包含海外域名: DOMAIN,ml.cdn-apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **高风险 - 直连海外域名**
  直连规则包含海外域名: DOMAIN,music.apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **高风险 - 直连海外域名**
  直连规则包含海外域名: DOMAIN,musicstatus.music.apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **高风险 - 直连海外域名**
  直连规则包含海外域名: DOMAIN,mvod.itunes.apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **高风险 - 直连海外域名**
  直连规则包含海外域名: DOMAIN,myapp.itunes.apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **高风险 - 直连海外域名**
  直连规则包含海外域名: DOMAIN,np-edge.itunes.apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **高风险 - 直连海外域名**
  直连规则包含海外域名: DOMAIN,ocsp.apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **高风险 - 直连海外域名**
  直连规则包含海外域名: DOMAIN,ocsp2.apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **高风险 - 直连海外域名**
  直连规则包含海外域名: DOMAIN,oscdn.apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **高风险 - 直连海外域名**
  直连规则包含海外域名: DOMAIN,oscdn.origin-apple.com.akadns.net,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **高风险 - 直连海外域名**
  直连规则包含海外域名: DOMAIN,osxapps.itunes.apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **高风险 - 直连海外域名**
  直连规则包含海外域名: DOMAIN,pancake.apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **高风险 - 直连海外域名**
  直连规则包含海外域名: DOMAIN,pba0.apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **高风险 - 直连海外域名**
  直连规则包含海外域名: DOMAIN,pd-nk.itunes.apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **高风险 - 直连海外域名**
  直连规则包含海外域名: DOMAIN,pd.itunes.apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **高风险 - 直连海外域名**
  直连规则包含海外域名: DOMAIN,play-edge.itunes.apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **高风险 - 直连海外域名**
  直连规则包含海外域名: DOMAIN,play.itunes.apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **高风险 - 直连海外域名**
  直连规则包含海外域名: DOMAIN,play.music.apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **高风险 - 直连海外域名**
  直连规则包含海外域名: DOMAIN,podcasts.apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **高风险 - 直连海外域名**
  直连规则包含海外域名: DOMAIN,podcasts.itunes.apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **高风险 - 直连海外域名**
  直连规则包含海外域名: DOMAIN,probe.siri.apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **高风险 - 直连海外域名**
  直连规则包含海外域名: DOMAIN,prod-support.apple-support.akadns.net,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **高风险 - 直连海外域名**
  直连规则包含海外域名: DOMAIN,publicassets.cdn-apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **高风险 - 直连海外域名**
  直连规则包含海外域名: DOMAIN,se-edge.itunes.apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **高风险 - 直连海外域名**
  直连规则包含海外域名: DOMAIN,se2.itunes.apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **高风险 - 直连海外域名**
  直连规则包含海外域名: DOMAIN,search.itunes.apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **高风险 - 直连海外域名**
  直连规则包含海外域名: DOMAIN,seed-sequoia.siri.apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **高风险 - 直连海外域名**
  直连规则包含海外域名: DOMAIN,seed-swallow.siri.apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **高风险 - 直连海外域名**
  直连规则包含海外域名: DOMAIN,seed.siri.apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **高风险 - 直连海外域名**
  直连规则包含海外域名: DOMAIN,sequoia.apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **高风险 - 直连海外域名**
  直连规则包含海外域名: DOMAIN,sf-api-token-service.itunes.apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **高风险 - 直连海外域名**
  直连规则包含海外域名: DOMAIN,sh-pod2-smp-device.apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **高风险 - 直连海外域名**
  直连规则包含海外域名: DOMAIN,shazam-insights.cdn-apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **高风险 - 直连海外域名**
  直连规则包含海外域名: DOMAIN,smp-device-content.apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **高风险 - 直连海外域名**
  直连规则包含海外域名: DOMAIN,sp.itunes.apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **高风险 - 直连海外域名**
  直连规则包含海外域名: DOMAIN,speedysub.music.apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **高风险 - 直连海外域名**
  直连规则包含海外域名: DOMAIN,static.gc.apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **高风险 - 直连海外域名**
  直连规则包含海外域名: DOMAIN,stocks-sparkline-lb.apple.com.akadns.net,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **高风险 - 直连海外域名**
  直连规则包含海外域名: DOMAIN,stocks-sparkline.apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **高风险 - 直连海外域名**
  直连规则包含海外域名: DOMAIN,store.apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **高风险 - 直连海外域名**
  直连规则包含海外域名: DOMAIN,store.apple.com.edgekey.net,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **高风险 - 直连海外域名**
  直连规则包含海外域名: DOMAIN,store.apple.com.edgekey.net.globalredir.akadns.net,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **高风险 - 直连海外域名**
  直连规则包含海外域名: DOMAIN,store.storeimages.apple.com.akadns.net,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **高风险 - 直连海外域名**
  直连规则包含海外域名: DOMAIN,store.storeimages.cdn-apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **高风险 - 直连海外域名**
  直连规则包含海外域名: DOMAIN,streamingaudio.itunes.apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **高风险 - 直连海外域名**
  直连规则包含海外域名: DOMAIN,su.itunes.apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **高风险 - 直连海外域名**
  直连规则包含海外域名: DOMAIN,support-china.apple-support.akadns.net,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **高风险 - 直连海外域名**
  直连规则包含海外域名: DOMAIN,support.apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **高风险 - 直连海外域名**
  直连规则包含海外域名: DOMAIN,swallow-apple-com.v.aaplimg.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **高风险 - 直连海外域名**
  直连规则包含海外域名: DOMAIN,swallow.apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **高风险 - 直连海外域名**
  直连规则包含海外域名: DOMAIN,swcatalog-cdn.apple.com.akadns.net,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **高风险 - 直连海外域名**
  直连规则包含海外域名: DOMAIN,swcatalog.apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **高风险 - 直连海外域名**
  直连规则包含海外域名: DOMAIN,swcdn.apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **高风险 - 直连海外域名**
  直连规则包含海外域名: DOMAIN,swdist.apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **高风险 - 直连海外域名**
  直连规则包含海外域名: DOMAIN,swdist.apple.com.akadns.net,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **高风险 - 直连海外域名**
  直连规则包含海外域名: DOMAIN,swscan-cdn.apple.com.akadns.net,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **高风险 - 直连海外域名**
  直连规则包含海外域名: DOMAIN,swscan.apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **高风险 - 直连海外域名**
  直连规则包含海外域名: DOMAIN,sylvan.apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **高风险 - 直连海外域名**
  直连规则包含海外域名: DOMAIN,sync.itunes.apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **高风险 - 直连海外域名**
  直连规则包含海外域名: DOMAIN,tf-feedback.itunes.apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **高风险 - 直连海外域名**
  直连规则包含海外域名: DOMAIN,tj-pod1-smp-device.apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **高风险 - 直连海外域名**
  直连规则包含海外域名: DOMAIN,tj-pod2-smp-device.apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **高风险 - 直连海外域名**
  直连规则包含海外域名: DOMAIN,tj-pod3-smp-device.apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **高风险 - 直连海外域名**
  直连规则包含海外域名: DOMAIN,universal-activity-service.itunes.apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **高风险 - 直连海外域名**
  直连规则包含海外域名: DOMAIN,updates-http.cdn-apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **高风险 - 直连海外域名**
  直连规则包含海外域名: DOMAIN,updates-http.cdn-apple.com.akadns.net,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **高风险 - 直连海外域名**
  直连规则包含海外域名: DOMAIN,updates.cdn-apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **高风险 - 直连海外域名**
  直连规则包含海外域名: DOMAIN,upp.itunes.apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **高风险 - 直连海外域名**
  直连规则包含海外域名: DOMAIN,valid.apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **高风险 - 直连海外域名**
  直连规则包含海外域名: DOMAIN,valid.origin-apple.com.akadns.net,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **高风险 - 直连海外域名**
  直连规则包含海外域名: DOMAIN,weather-data.apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **高风险 - 直连海外域名**
  直连规则包含海外域名: DOMAIN,weather-data.apple.com.akadns.net,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **高风险 - 直连海外域名**
  直连规则包含海外域名: DOMAIN,weather-map.apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **高风险 - 直连海外域名**
  直连规则包含海外域名: DOMAIN,weather-map2.apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **高风险 - 直连海外域名**
  直连规则包含海外域名: DOMAIN,weatherkit.apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **高风险 - 直连海外域名**
  直连规则包含海外域名: DOMAIN,www.apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **高风险 - 直连海外域名**
  直连规则包含海外域名: DOMAIN,www.apple.com.edgekey.net.globalredir.akadns.net,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **高风险 - 直连海外域名**
  直连规则包含海外域名: DOMAIN,www.support.apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **高风险 - 直连海外域名**
  直连规则包含海外域名: DOMAIN,xp.apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **高风险 - 直连海外域名**
  直连规则包含海外域名: DOMAIN-SUFFIX,apple-corer.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **高风险 - 直连海外域名**
  直连规则包含海外域名: DOMAIN-SUFFIX,apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **高风险 - 直连海外域名**
  直连规则包含海外域名: DOMAIN-SUFFIX,apple110.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **高风险 - 直连海外域名**
  直连规则包含海外域名: DOMAIN-SUFFIX,apple114.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **高风险 - 直连海外域名**
  直连规则包含海外域名: DOMAIN-SUFFIX,apple17.club,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **高风险 - 直连海外域名**
  直连规则包含海外域名: DOMAIN-SUFFIX,apple4.us,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **高风险 - 直连海外域名**
  直连规则包含海外域名: DOMAIN-SUFFIX,apple523.club,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **高风险 - 直连海外域名**
  直连规则包含海外域名: DOMAIN-SUFFIX,apple886.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **高风险 - 直连海外域名**
  直连规则包含海外域名: DOMAIN-SUFFIX,applebl.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **高风险 - 直连海外域名**
  直连规则包含海外域名: DOMAIN-SUFFIX,applejp.cloud,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **高风险 - 直连海外域名**
  直连规则包含海外域名: DOMAIN-SUFFIX,applemei.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **高风险 - 直连海外域名**
  直连规则包含海外域名: DOMAIN-SUFFIX,applepopo.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **高风险 - 直连海外域名**
  直连规则包含海外域名: DOMAIN-SUFFIX,appletuan.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **高风险 - 直连海外域名**
  直连规则包含海外域名: DOMAIN-SUFFIX,applex.net,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **高风险 - 直连海外域名**
  直连规则包含海外域名: DOMAIN-SUFFIX,applezhang.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **高风险 - 直连海外域名**
  直连规则包含海外域名: DOMAIN-SUFFIX,badapple.pro,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **高风险 - 直连海外域名**
  直连规则包含海外域名: DOMAIN-SUFFIX,china-applefix.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **高风险 - 直连海外域名**
  直连规则包含海外域名: DOMAIN-SUFFIX,iappler.net,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **高风险 - 直连海外域名**
  直连规则包含海外域名: DOMAIN-SUFFIX,nnpurapple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **高风险 - 直连海外域名**
  直连规则包含海外域名: DOMAIN-SUFFIX,red-apple.net,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **高风险 - 直连海外域名**
  直连规则包含海外域名: DOMAIN-SUFFIX,redapplechina.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **高风险 - 直连海外域名**
  直连规则包含海外域名: DOMAIN-SUFFIX,simapple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **高风险 - 直连海外域名**
  直连规则包含海外域名: DOMAIN-SUFFIX,spotify.map.fastly.net,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **高风险 - 直连海外域名**
  直连规则包含海外域名: DOMAIN-SUFFIX,spotify.map.fastlylb.net,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **高风险 - 直连海外域名**
  直连规则包含海外域名: DOMAIN-SUFFIX,svip5-applefix.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **高风险 - 直连海外域名**
  直连规则包含海外域名: DOMAIN-SUFFIX,tuiapple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **中风险 - 代理规则使用 no-resolve**
  代理规则带 no-resolve: IP-CIDR,104.18.0.0/15,PROXY,no-resolve，该域名的 DNS 将在本地解析，可能泄漏。

- **中风险 - 代理规则使用 no-resolve**
  代理规则带 no-resolve: IP-CIDR,143.198.200.27/32,PROXY,no-resolve，该域名的 DNS 将在本地解析，可能泄漏。

- **中风险 - 代理规则使用 no-resolve**
  代理规则带 no-resolve: IP-CIDR,159.89.204.203/32,PROXY,no-resolve，该域名的 DNS 将在本地解析，可能泄漏。

- **中风险 - 代理规则使用 no-resolve**
  代理规则带 no-resolve: IP-CIDR,172.64.0.0/13,PROXY,no-resolve，该域名的 DNS 将在本地解析，可能泄漏。

- **中风险 - 代理规则使用 no-resolve**
  代理规则带 no-resolve: IP-CIDR,24.199.123.28/32,PROXY,no-resolve，该域名的 DNS 将在本地解析，可能泄漏。

- **中风险 - 代理规则使用 no-resolve**
  代理规则带 no-resolve: IP-CIDR,45.76.214.191/32,PROXY,no-resolve，该域名的 DNS 将在本地解析，可能泄漏。

- **中风险 - 代理规则使用 no-resolve**
  代理规则带 no-resolve: IP-CIDR,64.23.132.171/32,PROXY,no-resolve，该域名的 DNS 将在本地解析，可能泄漏。

- **中风险 - dns-direct-system 开启**
  主配置中 dns-direct-system = true，直连域名将使用系统 DNS，可能造成 DNS 泄漏。建议改为 false。

---

详细日志请查看同目录下的 update 日志文件。
