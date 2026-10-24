# NetPilot · Quantumult X 版

由 Shadowrocket 模块自动转换。filter/ 为按策略分片的过滤器（Ads/Proxy/Direct），另有去广告精简版 Ads_Lite（仅注册域层级，约全量四成，适合低内存设备）；rewrite/ 为重写与脚本；mitm_hostname.txt 为解密域名清单。

## 内容

- Ads 过滤器：218598
- Proxy 过滤器：27466
- Direct 过滤器：111192
- Ads 精简版：88039

## 用法

Quantumult X → 设置 → 引用：过滤器引用订阅 filter/*.list，重写引用订阅 rewrite/*.conf。过滤器中的策略名 proxy 需要你在 QX 里有同名策略组，或在订阅引用时用 QX 的策略映射改成你自己的组名。

> 本目录文件由转换器自动生成，源文件更新后自动同步，请勿手动编辑。
