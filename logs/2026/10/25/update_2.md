# 更新日志 2026-10-25

**运行时间**: 2026-10-25 16:55:59 北京时间

---

## 直连模块

### 🔍 过滤海外/强制代理直连规则（共 942 条）

**原因**：规则域名匹配海外黑名单关键词，或属于强制代理域名（如定位模块）。

<details>
<summary>展开查看被过滤规则及命中关键词</summary>

```
- DOMAIN-SUFFIX,magentochina.org,DIRECT  (命中: magento)
- DOMAIN-SUFFIX,awsdns-cn-24.net,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,awsdns-cn-11.biz,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,applysquare.net,DIRECT  (命中: square)
- DOMAIN-SUFFIX,hf-iflysse.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,hminvestment.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,shmhtv.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,hmplay.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,chinacreator.com,DIRECT  (命中: acr)
- DOMAIN-SUFFIX,lhmp.cc,DIRECT  (命中: hm)
- DOMAIN,fonts.gstatic.com,DIRECT  (命中: gstatic.com)
- DOMAIN-SUFFIX,thmovie.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,oemsoc.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,shmljm.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,myvs.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,awsdns-cn-27.biz,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,aflytec.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,awsdns-cn-46.net,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,awsdns-cn-48.com,DIRECT  (命中: aws)
- URL-REGEX,"^https?:\/\/.+\.awsdns-cn-[0-9][a-e0-9]\.cn.*$",DIRECT  (命中: aws)
- DOMAIN-SUFFIX,download.visualstudio.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,hmmachine.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,iflysec.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,hmj666.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,oemsocuat.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,wish-hightech.com,DIRECT  (命中: wish)
- DOMAIN,www-googletagmanager.l.google.com,DIRECT  (命中: google)
- DOMAIN-SUFFIX,iflytek.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,msdprod-ad.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,citichmc.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,3richman.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,bixuecrm.com,DIRECT  (命中: ecr)
- DOMAIN-SUFFIX,hmus.net,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,njhmmr.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,cloudfront-cn.net,DIRECT  (命中: cloudfront)
- DOMAIN-SUFFIX,awsdns-cn-27.com,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,youtube-dubbing.com,DIRECT  (命中: youtube)
- DOMAIN-SUFFIX,awsdns-cn-24.biz,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,xawscu.com,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,secrui.com,DIRECT  (命中: ecr)
- DOMAIN-SUFFIX,happypingpang.com,DIRECT  (命中: pypi)
- DOMAIN-SUFFIX,lubanpm.com,DIRECT  (命中: npm)
- DOMAIN-SUFFIX,vultrcn.com,DIRECT  (命中: vultr)
- DOMAIN-SUFFIX,flymeos.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,dockerinfo.net,DIRECT  (命中: docker)
- DOMAIN-SUFFIX,mpnbenefits.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,chmgames.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,iflyaiedu.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,toprender.com,DIRECT  (命中: render)
- DOMAIN,gs-loc-cn.apple.com,DIRECT  (命中: 强制代理域名)
- DOMAIN-SUFFIX,yindo-ohm.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,awsdns-cn-62.net,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,azureflame.cloud,DIRECT  (命中: azure)
- DOMAIN-SUFFIX,awsdns-cn-16.biz,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,ttfly.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,hnpm.cc,DIRECT  (命中: npm)
- DOMAIN-SUFFIX,azuremigratetest.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,hmwzjs.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,wishtec.com,DIRECT  (命中: wish)
- DOMAIN-SUFFIX,ahmif.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,tecreal.com,DIRECT  (命中: ecr)
- DOMAIN,download.visualstudio.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,3hmedicalgroup.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,npmtrend.com,DIRECT  (命中: npm)
- DOMAIN-SUFFIX,awsdns-cn-44.net,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,ahmky.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,digcredit.com,DIRECT  (命中: gcr)
- DOMAIN,officemktuat.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,xn--vhqqbz2p62hm92e04p.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,airtofly.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,cdnhwcohm19.com,DIRECT  (命中: hm)
- DOMAIN,mpnbenefitsrtluat.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN,googleanalytics.com,DIRECT  (命中: google)
- DOMAIN-SUFFIX,mcohmygod.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,englishmasterclub.com,DIRECT  (命中: hm)
- DOMAIN,mpnbenefitsrtl.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,hearfly.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,officebay.net,DIRECT  (命中: ebay)
- DOMAIN-SUFFIX,awsdns-cn-63.com,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,macrolake.com,DIRECT  (命中: acr)
- DOMAIN-SUFFIX,yytiflytek.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,flashmemoryworld.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,hmltec.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,smogfly.com,DIRECT  (命中: fly)
- DOMAIN,googleoptimize.com,DIRECT  (命中: google)
- DOMAIN-SUFFIX,bwfhmall.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,hmzixin.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,oacrm.com,DIRECT  (命中: acr)
- DOMAIN-SUFFIX,jinshmgw.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,meiji-icecream.com,DIRECT  (命中: ecr)
- DOMAIN-SUFFIX,aliexpress.com,DIRECT  (命中: aliexpress)
- DOMAIN-SUFFIX,akamai.com,DIRECT  (命中: akamai)
- DOMAIN-SUFFIX,glhmmr.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,iflyhealth.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,macrozheng.com,DIRECT  (命中: acr)
- DOMAIN-SUFFIX,724pridecryogenics.com,DIRECT  (命中: ecr)
- DOMAIN,redirector.c.mail.google.com,DIRECT  (命中: google)
- DOMAIN-SUFFIX,awsdns-cn-45.net,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,macrounion.com,DIRECT  (命中: acr)
- DOMAIN-SUFFIX,hm-3223.net,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,awsdns-cn-02.biz,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,smogflycloud.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,zhmedcenter.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,awsdns-cn-45.com,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,chinaflashmarket.com,DIRECT  (命中: hm)
- DOMAIN,download.tensorflow.google.com,DIRECT  (命中: google)
- DOMAIN-SUFFIX,awsdns-cn-56.biz,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,secretflow.com,DIRECT  (命中: ecr)
- DOMAIN-SUFFIX,awsdns-cn-52.net,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,wecrm.net,DIRECT  (命中: ecr)
- DOMAIN,qpx.googleflights.net,DIRECT  (命中: google)
- DOMAIN-SUFFIX,oneflys.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,njnaws.com,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,hmgbtv.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,sphmc.org,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,aftersale-amazon.com,DIRECT  (命中: amazon)
- DOMAIN-SUFFIX,neihanfly.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,ctrender.com,DIRECT  (命中: render)
- DOMAIN,ssl.gstatic.com,DIRECT  (命中: gstatic.com)
- DOMAIN-SUFFIX,megaemoji.com,DIRECT  (命中: mega)
- DOMAIN-SUFFIX,secrss.com,DIRECT  (命中: ecr)
- DOMAIN-SUFFIX,storeedge.microsoft.com,DIRECT  (命中: microsoft)
- URL-REGEX,"^https?:\/\/.+\.awsdns-cn-[0-9][0-9]\.(biz|com|net|top).*$",DIRECT  (命中: aws)
- DOMAIN-SUFFIX,itfly.net,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,hm16888.net,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,flyadx.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,awsdns-cn-37.com,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,azureyun.com,DIRECT  (命中: azure)
- DOMAIN-SUFFIX,googlevoice.org,DIRECT  (命中: google)
- DOMAIN-SUFFIX,chinahvacr.com,DIRECT  (命中: acr)
- DOMAIN-SUFFIX,ghsmpwalmart.com,DIRECT  (命中: walmart)
- DOMAIN-SUFFIX,chnrailway.com,DIRECT  (命中: railway)
- DOMAIN-SUFFIX,flylinking.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,awsdns-cn-19.biz,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,bfhmj.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,flyingpigeon1936.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,hkgcr.com,DIRECT  (命中: gcr)
- DOMAIN-SUFFIX,iflyadx.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,cthhmu.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,victoriassecretclearance.online,DIRECT  (命中: ecr)
- DOMAIN-SUFFIX,eflycloud.com,DIRECT  (命中: fly)
- DOMAIN,redirector.c.play.google.com,DIRECT  (命中: google)
- DOMAIN-SUFFIX,lzhmmr.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,awsdns-cn-12.biz,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,sunnyfly.com,DIRECT  (命中: fly)
- DOMAIN,collaborate.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN,googleadservices-cn.com,DIRECT  (命中: google)
- DOMAIN-SUFFIX,awsdns-cn-47.biz,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,hellogitlab.com,DIRECT  (命中: gitlab)
- DOMAIN-SUFFIX,googleyixia.com,DIRECT  (命中: google)
- DOMAIN-SUFFIX,chiconysquare.com,DIRECT  (命中: square)
- DOMAIN-SUFFIX,qiantangcredit.com,DIRECT  (命中: gcr)
- DOMAIN-SUFFIX,aliexpress-media.com,DIRECT  (命中: aliexpress)
- DOMAIN-SUFFIX,zxhmjj.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,lzarays.com,DIRECT  (命中: zara)
- DOMAIN-SUFFIX,awsdns-cn-46.biz,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,awsdns-cn-12.net,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,shlawserve.com,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,yz-proton.com,DIRECT  (命中: proton)
- DOMAIN-SUFFIX,whmxrj.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,awsdns-cn-41.com,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,awsdns-cn-61.biz,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,htyhm.com,DIRECT  (命中: hm)
- DOMAIN,wear.googleapis.com,DIRECT  (命中: google)
- DOMAIN-SUFFIX,czhmjx.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,squarecn.com,DIRECT  (命中: square)
- DOMAIN,googlevads-cn.com,DIRECT  (命中: google)
- DOMAIN-SUFFIX,flyneutron.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,awsdns-cn-62.biz,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,jhmnew.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,ifireflygame.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,azurestackhub.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,seersecret.com,DIRECT  (命中: ecr)
- DOMAIN-SUFFIX,awsdns-cn-14.com,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,iflynote.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,lgstatic.com,DIRECT  (命中: gstatic.com)
- DOMAIN-SUFFIX,gacrnd.com,DIRECT  (命中: acr)
- DOMAIN-SUFFIX,bjhdhm.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,macrr.com,DIRECT  (命中: acr)
- DOMAIN-SUFFIX,yunqifly.com,DIRECT  (命中: fly)
- DOMAIN,windbg.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,fingerflyapp.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,ncjrailway.com,DIRECT  (命中: railway)
- DOMAIN-SUFFIX,bbgstatic.com,DIRECT  (命中: gstatic.com)
- DOMAIN-SUFFIX,awsdns-cn-17.com,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,chinacraa.org,DIRECT  (命中: acr)
- DOMAIN-SUFFIX,bmp.ovh,DIRECT  (命中: ovh)
- DOMAIN-SUFFIX,awsdns-cn-60.com,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,hmxixie.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,mightsquare.com,DIRECT  (命中: square)
- DOMAIN-SUFFIX,weighment.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,smogflycloud.net,DIRECT  (命中: fly)
- DOMAIN,redirector.c.chat.google.com,DIRECT  (命中: google)
- DOMAIN-SUFFIX,dockerone.com,DIRECT  (命中: docker)
- DOMAIN-SUFFIX,chinawssdxh.com,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,lex.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,lenovo.com.cdn.cloudflare.net,DIRECT  (命中: cloudflare)
- DOMAIN-SUFFIX,awsdns-cn-16.net,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,dhmeri.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,iflygse.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,qjhm.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,vultrvps.com,DIRECT  (命中: vultr)
- DOMAIN-SUFFIX,ghmcchina.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,awsdns-cn-35.biz,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,hm120.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,flytexpress.com,DIRECT  (命中: fly)
- URL-REGEX,"^https?:\/\/.+-mihayo\.akamaized\.net.*$",DIRECT  (命中: akamai)
- DOMAIN-SUFFIX,gzrecruit.com,DIRECT  (命中: ecr)
- DOMAIN-SUFFIX,rohm-chip.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,vlportal.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN,google-analytics.com,DIRECT  (命中: google)
- DOMAIN,crashlyticsreports-pa.googleapis.com,DIRECT  (命中: google)
- DOMAIN,adservice.google.com,DIRECT  (命中: google)
- DOMAIN-SUFFIX,targetportion.com,DIRECT  (命中: target)
- DOMAIN-SUFFIX,awsdns-cn-01.net,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,chmia.org,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,flymeauto.com,DIRECT  (命中: fly)
- DOMAIN,google-analytics-cn.com,DIRECT  (命中: google)
- DOMAIN-SUFFIX,chihm.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,awsdns-cn-36.biz,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,vdfly.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,zztfly.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,bghmj.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,whmj.org,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,awsdns-cn-48.net,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,smogfly.cloud,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,fly3949.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,appsflyer-cn.com,DIRECT  (命中: fly)
- DOMAIN,googleapis-cn.com,DIRECT  (命中: google)
- DOMAIN,mbs.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,windbg.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,natywish.com,DIRECT  (命中: wish)
- DOMAIN-SUFFIX,zhmf.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,renderbus.com,DIRECT  (命中: render)
- DOMAIN,osrelease.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN,surface.downloads.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,cloudflarestaging.com,DIRECT  (命中: cloudflare)
- DOMAIN-SUFFIX,lnwish.com,DIRECT  (命中: wish)
- DOMAIN-SUFFIX,githubshare.com,DIRECT  (命中: github)
- DOMAIN-SUFFIX,acloudrender.com,DIRECT  (命中: render)
- DOMAIN-SUFFIX,whmdedu.com,DIRECT  (命中: hm)
- DOMAIN,dreamsparkuat.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,awsdns-cn-58.com,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,southmoney.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,awsdns-cn-00.net,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,yjdatasos.com,DIRECT  (命中: asos)
- DOMAIN-SUFFIX,hmxw.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,phmacn.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,awsdns-cn-15.net,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,cloudhvacr.com,DIRECT  (命中: acr)
- DOMAIN,cdn.globalsigncdn.com.cdn.cloudflare.net,DIRECT  (命中: cloudflare)
- DOMAIN-SUFFIX,shmama.net,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,hmgj.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,c-thme.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,bjwhmedia.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,flygon.net,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,dreamspark.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,collaborate.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,edgeone-browser-rendering.com,DIRECT  (命中: render)
- DOMAIN-SUFFIX,thmzedu.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,google-hub.com,DIRECT  (命中: google)
- DOMAIN-SUFFIX,awsdns-cn-06.com,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,cheetahmobile.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,zgxhm.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,officemkt.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,ahmwgroup.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,osrelease.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,arefly.com,DIRECT  (命中: fly)
- DOMAIN,googleoptimize-cn.com,DIRECT  (命中: google)
- DOMAIN-SUFFIX,awsdns-cn-63.net,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,xn--y8jhmm6gn.moe,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,thmz.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,hmoe.link,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,megagamelog.com,DIRECT  (命中: mega)
- DOMAIN-SUFFIX,hmchina.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,whhmmbl.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,fly-exp.com,DIRECT  (命中: fly)
- DOMAIN,msdprod-ad.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,whminwei.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,hmszkj.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,nhmuni.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,zhmu.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,bjhmdkj.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,protontechcn.com,DIRECT  (命中: proton)
- DOMAIN-SUFFIX,machenike.com,DIRECT  (命中: nike)
- DOMAIN-SUFFIX,awsdns-cn-14.biz,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,forcecreat.com,DIRECT  (命中: ecr)
- DOMAIN-SUFFIX,wishdown.com,DIRECT  (命中: wish)
- DOMAIN-SUFFIX,drugoogle.com,DIRECT  (命中: google)
- DOMAIN-SUFFIX,kindechem.com,DIRECT  (命中: kinde)
- DOMAIN,sdx.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN,dreamspark.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,protong.com,DIRECT  (命中: proton)
- DOMAIN-SUFFIX,zjecredit.org,DIRECT  (命中: ecr)
- DOMAIN-SUFFIX,likeaboat2023.com,DIRECT  (命中: ikea)
- DOMAIN-SUFFIX,awsdns-cn-56.net,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,d5render.com,DIRECT  (命中: render)
- DOMAIN-SUFFIX,azuretouch.net,DIRECT  (命中: azure)
- DOMAIN-SUFFIX,lhmj.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,awsdns-cn-07.net,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,awsdns-cn-00.com,DIRECT  (命中: aws)
- DOMAIN,checkin.gstatic.com,DIRECT  (命中: gstatic.com)
- DOMAIN-SUFFIX,unpmcc.com,DIRECT  (命中: npm)
- DOMAIN-SUFFIX,awsdns-cn-35.net,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,whmoocs.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,daiwofly.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,lexuat.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,awsdns-cn-20.net,DIRECT  (命中: aws)
- DOMAIN,googlesyndication-cn.com,DIRECT  (命中: google)
- DOMAIN-SUFFIX,jshmrcb.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,volic.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,imgs.ovh,DIRECT  (命中: ovh)
- DOMAIN-SUFFIX,awsdns-cn-37.net,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,fireflyacg.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,iflydatahub.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,itacademy.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,bzmhm.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,awsdns-cn-42.com,DIRECT  (命中: aws)
- DOMAIN,images-cn-8.ssl-images-amazon.com,DIRECT  (命中: amazon)
- DOMAIN-SUFFIX,fly998.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,hmzhtc.cc,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,awsdns-cn-23.net,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,megarobo.com,DIRECT  (命中: mega)
- DOMAIN-SUFFIX,chmc.cc,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,flymobi.biz,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,seaflysoft.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,gxhhmed.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,awsdns-cn-39.biz,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,awsdns-vip.com,DIRECT  (命中: aws)
- DOMAIN,pki-goog.l.google.com,DIRECT  (命中: google)
- DOMAIN,googletagservices-cn.com,DIRECT  (命中: google)
- DOMAIN-SUFFIX,hifly.mobi,DIRECT  (命中: fly)
- DOMAIN,cache.pack.google.com,DIRECT  (命中: google)
- DOMAIN-SUFFIX,awsdns-cn-25.com,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,openai.wf,DIRECT  (命中: openai)
- DOMAIN-SUFFIX,flymeyun.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,hmjc.org,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,officecdn.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,t-firefly.com,DIRECT  (命中: fly)
- DOMAIN,software.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,awsdns-cn-28.biz,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,bulbsquare.com,DIRECT  (命中: square)
- DOMAIN-SUFFIX,macrosan.com,DIRECT  (命中: acr)
- DOMAIN-SUFFIX,shmarathon.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,yzhmyy.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,awsdns-cn-59.net,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,hbhm.net,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,ylxhmy.com,DIRECT  (命中: hm)
- DOMAIN,vscode.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,azure.cc,DIRECT  (命中: azure)
- DOMAIN-SUFFIX,gdlinefly.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,hifly.tv,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,ddwhm.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,flypy.cc,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,wecrm.com,DIRECT  (命中: ecr)
- DOMAIN-SUFFIX,awsdns-cn-54.biz,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,e-flyinc.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,awsdns-cn-41.biz,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,facri.com,DIRECT  (命中: acr)
- DOMAIN-SUFFIX,gyhm.cc,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,mpnbenefitsrtluat.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,nike666.com,DIRECT  (命中: nike)
- DOMAIN-SUFFIX,chinacrops.org,DIRECT  (命中: acr)
- DOMAIN-SUFFIX,bjhmyq.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,51render.com,DIRECT  (命中: render)
- DOMAIN-SUFFIX,awsdns-cn-44.biz,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,hm163.net,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,hzhm888.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,gemini530.net,DIRECT  (命中: gemini)
- DOMAIN-SUFFIX,flyml.net,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,zhmodaoli.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,itgemini.net,DIRECT  (命中: gemini)
- DOMAIN-SUFFIX,awsdns-cn-11.com,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,minecraftzw.com,DIRECT  (命中: ecr)
- DOMAIN-SUFFIX,acrossmetals.com,DIRECT  (命中: acr)
- DOMAIN-SUFFIX,thmins.com,DIRECT  (命中: hm)
- DOMAIN,safebrowsing-cache.google.com,DIRECT  (命中: google)
- DOMAIN-SUFFIX,wish3d.com,DIRECT  (命中: wish)
- DOMAIN-SUFFIX,chmecc.org,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,zchmh.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,cloudflarestoragegw.com,DIRECT  (命中: cloudflare)
- DOMAIN-SUFFIX,nnpml.com,DIRECT  (命中: npm)
- DOMAIN-SUFFIX,hyahm.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,hyundai-chhm.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,sdx.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,iqhmh.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,hmtrhf.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,awsdns-cn-40.biz,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,awsdns-cn-33.biz,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,acroview.com,DIRECT  (命中: acr)
- DOMAIN-SUFFIX,iflyink.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,gxlzhm.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,techmoris.com,DIRECT  (命中: hm)
- DOMAIN,tac.googleapis.com,DIRECT  (命中: google)
- DOMAIN-SUFFIX,znhhmedical.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,awspaas.com,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,macroprocess.com,DIRECT  (命中: acr)
- DOMAIN-SUFFIX,msdn.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,renderincloud.com,DIRECT  (命中: render)
- DOMAIN-SUFFIX,squarefong.com,DIRECT  (命中: square)
- DOMAIN-SUFFIX,dcg.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,awsdns-cn-60.biz,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,t-npm.com,DIRECT  (命中: npm)
- DOMAIN-SUFFIX,qzynhhmm.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,abcdocker.com,DIRECT  (命中: docker)
- DOMAIN-SUFFIX,flycua.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,awsamazonlab.com,DIRECT  (命中: amazon)
- DOMAIN,csi.gstatic.com,DIRECT  (命中: gstatic.com)
- DOMAIN-SUFFIX,awsdns-cn-38.net,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,awsdns-cn-24.com,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,hmgreat.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,hbysfhm.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,chmod0777kk.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,xn--nmqp78hmufjwu.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,shmds.vip,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,cproton.com,DIRECT  (命中: proton)
- DOMAIN-SUFFIX,thmnet.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,shmondial.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,jxhmjx.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,gx-hm.com,DIRECT  (命中: hm)
- DOMAIN,cbdstest.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,eflybird.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,lawsdata.com,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,gxhmba.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,awsdns-cn-33.net,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,shmylike.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,smogfly.net,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,acrel-znyf.com,DIRECT  (命中: acr)
- DOMAIN-SUFFIX,pmphmooc.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,iflyrec.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,haiqianghm.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,algorithmart.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,jxhmxxjs.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,cloudflareprod.com,DIRECT  (命中: cloudflare)
- DOMAIN-SUFFIX,railwaybill.com,DIRECT  (命中: railway)
- DOMAIN,g2.gstatic.com,DIRECT  (命中: gstatic.com)
- DOMAIN,lexuat.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,hicnhm.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,sdhmjt.net,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,chinacrankshaft.com,DIRECT  (命中: acr)
- DOMAIN-SUFFIX,awsdns-cn-43.biz,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,oktamall.com,DIRECT  (命中: okta)
- DOMAIN-SUFFIX,openai-hub.com,DIRECT  (命中: openai)
- DOMAIN-SUFFIX,mikecrm.com,DIRECT  (命中: ecr)
- DOMAIN,cache-management-prod.google.com,DIRECT  (命中: google)
- DOMAIN-SUFFIX,cloudflareanycast.net,DIRECT  (命中: cloudflare)
- DOMAIN-SUFFIX,czxthmls.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,awsdns-cn-04.net,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,tlhmhd.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,shmds.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,flyfishx.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,shmaas.net,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,awsdns-cn-50.net,DIRECT  (命中: aws)
- DOMAIN,vz.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,rcolab.com,DIRECT  (命中: colab)
- DOMAIN,rsm.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN,tools.google.com,DIRECT  (命中: google)
- DOMAIN-SUFFIX,awsdns-cn-07.biz,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,mysecretrainbow.com,DIRECT  (命中: ecr)
- DOMAIN-SUFFIX,telegramtoke.com,DIRECT  (命中: telegram)
- DOMAIN,clickserver.googleads.com,DIRECT  (命中: google)
- DOMAIN,collaborateppe.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,ideacreated.com,DIRECT  (命中: acr)
- DOMAIN-SUFFIX,awsdns-cn-60.net,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,chinacrt.com,DIRECT  (命中: acr)
- DOMAIN-SUFFIX,hbhmxx.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,cloudflare.fun,DIRECT  (命中: cloudflare)
- DOMAIN-SUFFIX,shmbjy.org,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,hmz8.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,ggshmy.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,gxhmdjt.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,likeacg.com,DIRECT  (命中: ikea)
- DOMAIN-SUFFIX,51google.com,DIRECT  (命中: google)
- DOMAIN-SUFFIX,thmall.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,awsdns-cn-18.net,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,cloudflareglobal.net,DIRECT  (命中: cloudflare)
- DOMAIN-SUFFIX,shmusic.org,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,shmockup.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,shmzgroup.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,awsdns-cn-42.biz,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,aliexpress.ru,DIRECT  (命中: aliexpress)
- DOMAIN-SUFFIX,ucfly.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,mysecrettop.com,DIRECT  (命中: ecr)
- DOMAIN-SUFFIX,megawords.cc,DIRECT  (命中: mega)
- DOMAIN-SUFFIX,azurestackhubuat.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,szpowerfly.com,DIRECT  (命中: fly)
- DOMAIN,images-cn.ssl-images-amazon.com,DIRECT  (命中: amazon)
- DOMAIN-SUFFIX,hm-optics.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,shtimessquare.com,DIRECT  (命中: square)
- DOMAIN-SUFFIX,xn--vhq4ut2dsxd5xqnicjxxo55a756aovhik0aunm.com,DIRECT  (命中: ovh)
- DOMAIN-SUFFIX,azuremigrate.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,jdhmediajd.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,bshmzx.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,hefeilaws.com,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,shmengzhong.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,hmyzs.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,storecorefulfillment.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,gshmhotels.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,awsdns-cn-40.com,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,awsdns-cn-55.net,DIRECT  (命中: aws)
- DOMAIN,developer.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,collaborateppe.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,fhmooc.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,iva-schmetz.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,hmx-led.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,megagenchina.com,DIRECT  (命中: mega)
- DOMAIN-SUFFIX,qixingcr.com,DIRECT  (命中: gcr)
- DOMAIN-SUFFIX,awsonamazon.com,DIRECT  (命中: amazon)
- DOMAIN-SUFFIX,qhmsg.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,grender.com,DIRECT  (命中: render)
- DOMAIN-SUFFIX,awsdns-cn-37.biz,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,awsdns-cn-09.net,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,megajoy.com,DIRECT  (命中: mega)
- DOMAIN-SUFFIX,ntrailway.com,DIRECT  (命中: railway)
- DOMAIN-SUFFIX,flyme.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,oemssl.cn.cdn.cloudflare.net,DIRECT  (命中: cloudflare)
- DOMAIN,officemkt.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,sheinet.com,DIRECT  (命中: shein)
- DOMAIN-SUFFIX,techmiao.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,awsdns-cn-50.biz,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,asosde.com,DIRECT  (命中: asos)
- DOMAIN-SUFFIX,gdsunfly.com,DIRECT  (命中: fly)
- DOMAIN,oemsocuat.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN,connectivitycheck.gstatic.com,DIRECT  (命中: gstatic.com)
- DOMAIN-SUFFIX,megahugo.net,DIRECT  (命中: mega)
- DOMAIN-SUFFIX,withmedia.net,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,macrowing.com,DIRECT  (命中: acr)
- DOMAIN-SUFFIX,awsdns-cn-48.biz,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,sun-wish.com,DIRECT  (命中: wish)
- DOMAIN-SUFFIX,macrosilicon.com,DIRECT  (命中: acr)
- DOMAIN-SUFFIX,fly160.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,awsdns-cn-17.biz,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,hm5988.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,awsdns-cn-09.biz,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,asosoaiid.com,DIRECT  (命中: asos)
- DOMAIN-SUFFIX,xhmwxy.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,awsdns-cn-44.com,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,tb-whatsapp.com,DIRECT  (命中: whatsapp)
- DOMAIN-SUFFIX,hmadgz.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,awsdns-cn-22.net,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,aquayee.com,DIRECT  (命中: quay)
- DOMAIN-SUFFIX,megasig.com,DIRECT  (命中: mega)
- DOMAIN-SUFFIX,gemini-galaxy.com,DIRECT  (命中: gemini)
- DOMAIN-SUFFIX,xhmedia.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,shmengyang.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,nike.host,DIRECT  (命中: nike)
- DOMAIN-SUFFIX,zhinikefu.com,DIRECT  (命中: nike)
- DOMAIN-SUFFIX,hmrsrc.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,square16.org,DIRECT  (命中: square)
- DOMAIN-SUFFIX,91hmi.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,originalkindergarten.com,DIRECT  (命中: kinde)
- DOMAIN-SUFFIX,szhmjp.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,qflyinc.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,surface.downloads.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,awsdns-cn-26.com,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,qdhmsoft.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,shmet.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,tshmkj.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,awsdns-cn-36.net,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,52kfly.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,cqrailway.com,DIRECT  (命中: railway)
- DOMAIN-SUFFIX,qeoagphm.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,hmzs.net,DIRECT  (命中: hm)
- DOMAIN,azurestackhub.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,yingyecraft.com,DIRECT  (命中: ecr)
- DOMAIN,avail.googleflights.net,DIRECT  (命中: google)
- DOMAIN-SUFFIX,hmtgo.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,cmacredit.org,DIRECT  (命中: acr)
- DOMAIN-SUFFIX,dylyghm.com,DIRECT  (命中: hm)
- DOMAIN,lex.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,xahmqy.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,xhma.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,awsdns-cn-31.net,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,tinsecret.com,DIRECT  (命中: ecr)
- DOMAIN-SUFFIX,qualcomm.cn.cdn.cloudflare.net,DIRECT  (命中: cloudflare)
- DOMAIN-SUFFIX,hmqjsb.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,hmqg.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,flyco.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,aliexpress.us,DIRECT  (命中: aliexpress)
- DOMAIN-SUFFIX,hmting.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,awsdns-cn-05.net,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,shmog.org,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,hmeili.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,flyai.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,awsdns-cn-36.com,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,smogfly.club,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,fhmv.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,ztrhmall.com,DIRECT  (命中: hm)
- DOMAIN,azurestackhubuat.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,ecrrc.com,DIRECT  (命中: ecr)
- DOMAIN,googletraveladservices.com,DIRECT  (命中: google)
- DOMAIN-SUFFIX,pkulaws.com,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,zgzhmz.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,ghmba.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,elecrystal.com,DIRECT  (命中: ecr)
- DOMAIN-SUFFIX,awsdns-cn-17.net,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,whmnx.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,gdhmgc.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,jiansujihm.com,DIRECT  (命中: hm)
- DOMAIN,www.gstatic.com,DIRECT  (命中: gstatic.com)
- DOMAIN-SUFFIX,awsdns-cn-63.biz,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,applysquare.com,DIRECT  (命中: square)
- DOMAIN,c.android.clients.google.com,DIRECT  (命中: google)
- DOMAIN-SUFFIX,acrel-eem.com,DIRECT  (命中: acr)
- DOMAIN-SUFFIX,itacademyuat.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,hlnpm.com,DIRECT  (命中: npm)
- DOMAIN-SUFFIX,awsdns-cn-41.net,DIRECT  (命中: aws)
- DOMAIN,itacademyuat.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,iflytoy.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,whmylike.cc,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,awsdns-cn-53.com,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,flyingeffect.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,ecr-global.com,DIRECT  (命中: ecr)
- DOMAIN-SUFFIX,awsdns-cn-58.net,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,sectigochina.com.cdn.cloudflare.net,DIRECT  (命中: cloudflare)
- DOMAIN,storeedge.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,whhmgroup.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,awsdns-cn-58.biz,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,awsdns-cn-06.net,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,sxhm.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,iflydocs.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,awsdns-cn-19.net,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,syfly007.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,rainbutterfly.xyz,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,awsdns-cn-21.biz,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,cn-railway.net,DIRECT  (命中: railway)
- DOMAIN-SUFFIX,hmzhtc.com,DIRECT  (命中: hm)
- DOMAIN,performanceparameters.googleapis.com,DIRECT  (命中: google)
- DOMAIN,pagead-googlehosted.l.google.com,DIRECT  (命中: google)
- DOMAIN,azuremigratetest.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,sharjahmadrasa.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,awsdns-cn-22.com,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,mbs.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,cofly.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,beijing-hmo.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,mikeauth.com,DIRECT  (命中: ikea)
- DOMAIN-SUFFIX,googlebbs.net,DIRECT  (命中: google)
- DOMAIN,mpnbenefits.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,myhm.org,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,chmti.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,pihmh.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,i-firefly.com,DIRECT  (命中: fly)
- DOMAIN,volic.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,jcodecraeer.com,DIRECT  (命中: ecr)
- DOMAIN-SUFFIX,shmtu.net,DIRECT  (命中: hm)
- DOMAIN,g1.gstatic.com,DIRECT  (命中: gstatic.com)
- DOMAIN,msdn.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,hmtnew.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,flyhand.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,awsdns-cn-51.com,DIRECT  (命中: aws)
- DOMAIN,googleadservices.com,DIRECT  (命中: google)
- DOMAIN-SUFFIX,lzbhmy.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,awspony.com,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,hhmajiang.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,chinaacryl.com,DIRECT  (命中: acr)
- DOMAIN-SUFFIX,hmedu.com,DIRECT  (命中: hm)
- DOMAIN,safebrowsing.googleapis.com,DIRECT  (命中: google)
- DOMAIN-SUFFIX,hmnst.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,githubim.com,DIRECT  (命中: github)
- DOMAIN-SUFFIX,flydigi.com,DIRECT  (命中: fly)
- DOMAIN,clientservices.googleapis.com,DIRECT  (命中: google)
- DOMAIN-SUFFIX,alltechmed.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,vz.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,orasos.com,DIRECT  (命中: asos)
- DOMAIN-SUFFIX,whmnrc.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,whmama.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,honchmedia.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,thwgetsy.com,DIRECT  (命中: etsy)
- DOMAIN-SUFFIX,mecru.com,DIRECT  (命中: ecr)
- DOMAIN,googlesyndication.com,DIRECT  (命中: google)
- DOMAIN-SUFFIX,fly139.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,awsdns-cn-52.com,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,hmsemi.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,awsdns-cn-23.com,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,qmacro.com,DIRECT  (命中: acr)
- DOMAIN,myvs.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN,firebase-settings.crashlytics.com,DIRECT  (命中: firebase)
- DOMAIN-SUFFIX,elitecrm.com,DIRECT  (命中: ecr)
- DOMAIN-SUFFIX,testshm.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,googleppy.com,DIRECT  (命中: google)
- DOMAIN-SUFFIX,flyertea.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,flymopaper.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,hmwdj.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,awsdns-cn-18.biz,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,dagongcredit.com,DIRECT  (命中: gcr)
- DOMAIN-SUFFIX,volcecr.com,DIRECT  (命中: ecr)
- DOMAIN-SUFFIX,hmrczp.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,zjgcreative.com,DIRECT  (命中: gcr)
- DOMAIN-SUFFIX,fishflying.net,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,awsdns-cn-05.biz,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,flyenglish.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,netsyq.com,DIRECT  (命中: etsy)
- DOMAIN-SUFFIX,ylhmgz.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,athmapp.com,DIRECT  (命中: hm)
- DOMAIN,googletagmanager-cn.com,DIRECT  (命中: google)
- DOMAIN-SUFFIX,awsdns-cn-39.com,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,facebookol.com,DIRECT  (命中: facebook)
- DOMAIN-SUFFIX,gamegamept.com,DIRECT  (命中: mega)
- DOMAIN-SUFFIX,rushmail.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,googlenav.com,DIRECT  (命中: google)
- DOMAIN-SUFFIX,xczhmzb.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,cuahmap.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,hmfxw.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,whuznhmedj.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,awsdns-cn-29.biz,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,uuu.ovh,DIRECT  (命中: ovh)
- DOMAIN-SUFFIX,cloudflareinsights-cn.com,DIRECT  (命中: cloudflare)
- DOMAIN-SUFFIX,flygo.net,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,hm588.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,szhmkeji.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,hm025.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,secretgardenresorts.com,DIRECT  (命中: ecr)
- DOMAIN-SUFFIX,yfldocker.com,DIRECT  (命中: docker)
- DOMAIN-SUFFIX,qihangcrrc.com,DIRECT  (命中: gcr)
- DOMAIN-SUFFIX,dreamsparkuat.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,bjhmcm.com,DIRECT  (命中: hm)
- DOMAIN,ssl-google-analytics.l.google.com,DIRECT  (命中: google)
- DOMAIN-SUFFIX,dhmsnyy.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,haofly.net,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,shmetro.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,iflyread.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,whmvc.net,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,awsdns-cn-25.net,DIRECT  (命中: aws)
- DOMAIN,g3.gstatic.com,DIRECT  (命中: gstatic.com)
- DOMAIN,googletraveladservices-cn.com,DIRECT  (命中: google)
- DOMAIN-SUFFIX,awsdns-cn-03.biz,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,awsdns-cn-49.biz,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,sfecr.com,DIRECT  (命中: ecr)
- DOMAIN-SUFFIX,azureflying.com,DIRECT  (命中: azure)
- DOMAIN-SUFFIX,touchmark.art,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,hmhpay.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,3hmlg.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,cnflyinghorse.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,chinamaven.com,DIRECT  (命中: maven)
- DOMAIN-SUFFIX,awsdns-cn-51.biz,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,codeflying.net,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,awsdns-cn-59.biz,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,moonfly.net,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,hmlcar.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,02hm.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,dl.delivery.mp.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,hm152n.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,awsdns-cn-20.biz,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,awstar.net,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,dragonfly.fun,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,scratchmirror.net,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,ihmch.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,inflyway.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,awsdns-cn-34.com,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,hmf-china.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,officemktuat.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,edgeone-browser-rendering-dev.com,DIRECT  (命中: render)
- DOMAIN-SUFFIX,awsdns-cn-39.net,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,flyme.net,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,cloudflare-cn.com,DIRECT  (命中: cloudflare)
- DOMAIN-SUFFIX,jyhmz.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,edrawsoft.com,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,ceolaws.net,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,secretmine.net,DIRECT  (命中: ecr)
- DOMAIN-SUFFIX,armfly.com,DIRECT  (命中: fly)
- DOMAIN,vlportal.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,microsoftuwp.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,fawsoft.com,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,vecrp.com,DIRECT  (命中: ecr)
- DOMAIN-SUFFIX,awsdns-cn-52.biz,DIRECT  (命中: aws)
- DOMAIN,gs-loc.apple.com,DIRECT  (命中: 强制代理域名)
- DOMAIN-SUFFIX,azure-wave.com,DIRECT  (命中: azure)
- DOMAIN,googleflights-cn.net,DIRECT  (命中: google)
- DOMAIN-SUFFIX,24hmb.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,hmly666.cc,DIRECT  (命中: hm)
- DOMAIN,itacademy.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,machmall.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,shmhzp.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,ayhmjy.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,whmzkf.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,esdhm.net,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,shmedia.tech,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,whmeigao.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,msproduct.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,3zhm.com,DIRECT  (命中: hm)
- DOMAIN,g0.gstatic.com,DIRECT  (命中: gstatic.com)
- DOMAIN-SUFFIX,elongstatic.com,DIRECT  (命中: gstatic.com)
- DOMAIN-SUFFIX,ovhlb.net,DIRECT  (命中: ovh)
- DOMAIN-SUFFIX,welchmat.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,awsdns-cn-20.com,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,bebhmongb.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,kphm88.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,luxtarget.com,DIRECT  (命中: target)
- DOMAIN-SUFFIX,hmbzfjt.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,cyhm.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,haitianpm.com,DIRECT  (命中: npm)
- DOMAIN-SUFFIX,hmarathon.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,jinshasitemuseum.com,DIRECT  (命中: temu)
- DOMAIN-SUFFIX,googleplus.party,DIRECT  (命中: google)
- DOMAIN-SUFFIX,awsdns-cn-34.net,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,fhmion.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,yhm11.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,zzfly.net,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,wishcad.com,DIRECT  (命中: wish)
- DOMAIN,imasdk.googleapis.com,DIRECT  (命中: google)
- DOMAIN-SUFFIX,awsdns-cn-02.net,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,hnlshm.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,whmf8.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,zhmag.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,shmfmr.net,DIRECT  (命中: hm)
- DOMAIN,time.amazonaws.cn,DIRECT  (命中: amazon)
- DOMAIN-SUFFIX,hbhml.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,whoami.akamai.net,DIRECT  (命中: akamai)
- DOMAIN-SUFFIX,vscode.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,hmxx.net,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,jhqshfly.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,hhmage.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,awsdns-cn-21.net,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,ghmd448.com,DIRECT  (命中: hm)
- DOMAIN,dg-meta.video.google.com,DIRECT  (命中: google)
- DOMAIN-SUFFIX,cacre.org,DIRECT  (命中: acr)
- DOMAIN,redirector.c.youtubeeducation.com,DIRECT  (命中: youtube)
- DOMAIN-SUFFIX,cloudflarecn.net,DIRECT  (命中: cloudflare)
- DOMAIN-SUFFIX,software.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,nnhmcj.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,qhm123.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,wbecrisfro.com,DIRECT  (命中: ecr)
- DOMAIN,download.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN,surface.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,hfhm.com,DIRECT  (命中: hm)
- DOMAIN,storeedgefd.dsx.mp.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,9125flying.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,hyundai-hmtc.com,DIRECT  (命中: hm)
- DOMAIN,dl.google.com,DIRECT  (命中: google)
- DOMAIN-SUFFIX,zchmbx.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,openailab.com,DIRECT  (命中: openai)
- DOMAIN-SUFFIX,oecr.com,DIRECT  (命中: ecr)
- DOMAIN,gstaticadssl.l.google.com,DIRECT  (命中: google)
- DOMAIN-SUFFIX,chinaws.net,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,iflying.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,flyfunny.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,hmlan.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,rsm.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN,googleapps-cn.com,DIRECT  (命中: google)
- DOMAIN-SUFFIX,1fly.fun,DIRECT  (命中: fly)
- DOMAIN,azuremigrate.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,ugdocker.link,DIRECT  (命中: docker)
- DOMAIN,googletagservices.com,DIRECT  (命中: google)
- DOMAIN-SUFFIX,hwrecruit.com,DIRECT  (命中: ecr)
- DOMAIN,msproduct.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,awsdns-cn-01.biz,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,hfly.net,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,zhmold.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,lzghmy.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,awsdns-cn-09.com,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,ovhlb.com,DIRECT  (命中: ovh)
- DOMAIN-SUFFIX,simplecreator.net,DIRECT  (命中: ecr)
- DOMAIN-SUFFIX,cloudflareperf.com,DIRECT  (命中: cloudflare)
- DOMAIN-SUFFIX,awsdns-cn-47.net,DIRECT  (命中: aws)
- URL-REGEX,"^https?:\/\/r+[0-9]+(---|\.)sn-(2x3|ni5|j5o)\w{5}\.googlevideo\.com.*$",DIRECT  (命中: google)
- DOMAIN-SUFFIX,chmed.net,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,flysand.com,DIRECT  (命中: fly)
- DOMAIN,fontfiles.googleapis.com,DIRECT  (命中: google)
- DOMAIN-SUFFIX,awsdns-cn-45.biz,DIRECT  (命中: aws)
- DOMAIN,download.mlcc.google.com,DIRECT  (命中: google)
- DOMAIN-SUFFIX,weflywifi.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,hnsyhm.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,gogofly.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,fulinpm.com,DIRECT  (命中: npm)
- DOMAIN-SUFFIX,brighticecream.com,DIRECT  (命中: ecr)
- DOMAIN-SUFFIX,gzhm.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,cdnchatgpt.com,DIRECT  (命中: chatgpt)
- DOMAIN-SUFFIX,awsdns-cn-10.com,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,iflyiot.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,zhmzqi.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,cqs-hm.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,awsdns-cn-46.com,DIRECT  (命中: aws)
- DOMAIN,storecorefulfillment.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,flysheeep.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,chinacrane.net,DIRECT  (命中: acr)
- DOMAIN-SUFFIX,whmnls.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,whmc2005.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,shhmu.net,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,nikefans.com,DIRECT  (命中: nike)
- DOMAIN-SUFFIX,surface.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,awsdns-cn-07.com,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,iwishwed.com,DIRECT  (命中: wish)
- DOMAIN-SUFFIX,fly63.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,chatgptboke.com,DIRECT  (命中: chatgpt)
- DOMAIN-SUFFIX,zhmxchina.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,chinacrosspoint.com,DIRECT  (命中: acr)
- DOMAIN-SUFFIX,cnpmjs.org,DIRECT  (命中: npm)
- DOMAIN-SUFFIX,awsdns-cn-54.net,DIRECT  (命中: aws)
- DOMAIN,googletagmanager.com,DIRECT  (命中: google)
- DOMAIN-SUFFIX,wodecrowd.com,DIRECT  (命中: ecr)
- DOMAIN-SUFFIX,jhm2012.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,shms-expo.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,shhmbio.com,DIRECT  (命中: hm)
- DOMAIN,update.googleapis.com,DIRECT  (命中: google)
- DOMAIN,dl.l.google.com,DIRECT  (命中: google)
- DOMAIN-SUFFIX,sdhmkj.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,iflytektstd.com,DIRECT  (命中: fly)
- DOMAIN,www-google-analytics.l.google.com,DIRECT  (命中: google)
- DOMAIN-SUFFIX,surface-microsoftstore.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,awsdns-cn-47.com,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,awsdns-cn-57.com,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,omegatravel.net,DIRECT  (命中: mega)
- DOMAIN-SUFFIX,flytcloud.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,dmhmusic.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,wishisp.com,DIRECT  (命中: wish)
- DOMAIN-SUFFIX,npmmirror.com,DIRECT  (命中: npm)
- DOMAIN-SUFFIX,cbdstest.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,1818hm.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,shmaur.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,xrender.com,DIRECT  (命中: render)
- DOMAIN-SUFFIX,minecraftxz.com,DIRECT  (命中: ecr)
- DOMAIN-SUFFIX,yhchmo.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,whichmba.net,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,sdhmdp.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,2google.com,DIRECT  (命中: google)
- DOMAIN-SUFFIX,fly1999.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,cqhma.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,awsdns-cn-55.biz,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,mpnbenefitsrtl.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,shmusicschool.com,DIRECT  (命中: hm)
- DOMAIN,oemsoc.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,imags-google.com,DIRECT  (命中: google)
- DOMAIN-SUFFIX,4hmodel.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,mrwish.net,DIRECT  (命中: wish)
- DOMAIN-SUFFIX,hlhmf.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,hmkp.org,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,awsdns-cn-40.net,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,facebooksx.com,DIRECT  (命中: facebook)
- DOMAIN-SUFFIX,fishmobi.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,scratchmirror.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,fly84.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,cloudflareip.com,DIRECT  (命中: cloudflare)
- DOMAIN,officecdn.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,acrel-microgrid.com,DIRECT  (命中: acr)
- DOMAIN-SUFFIX,awsdns-cn-55.com,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,glflyy.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,whmlcy.net,DIRECT  (命中: hm)
- DOMAIN,redirector.c.pack.google.com,DIRECT  (命中: google)
- DOMAIN-SUFFIX,iflyresearch.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,feidacrusher.com,DIRECT  (命中: acr)
- DOMAIN-SUFFIX,awsdns-cn-28.net,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,awsdns-cn-62.com,DIRECT  (命中: aws)
```
</details>

### 上游源状态

- ✅ https://raw.githubusercontent.com/GMOogway/shadowrocket-rules/master/sr_direct_list.module

**原有规则数**: 111195
**新增规则数**: 7
**更新后总数**: 111202

#### 新增规则明细

<details>
<summary>展开查看新增规则（共 7 条）</summary>

```
DOMAIN-SUFFIX,ibangbank.com,DIRECT
DOMAIN-SUFFIX,nanocorechip.com,DIRECT
DOMAIN-SUFFIX,isigning.com,DIRECT
DOMAIN,storage.moegirl.org.cn,DIRECT
DOMAIN-SUFFIX,cqyyxc.com,DIRECT
DOMAIN,app.moegirl.org.cn,DIRECT
DOMAIN-SUFFIX,cdrcbank.com,DIRECT
```
</details>

🩺 直连模块: 健康检查通过（111202 条规则，3.6 MB）

✅ 直连模块已写入，共 111202 条规则

## 代理分流模块

### 🛡️ 白名单豁免（代理规则，共 23 条）

**原因**：这些域名在 `direct_whitelist.txt` 中，已从代理规则中移除，确保走直连。

<details>
<summary>展开查看被豁免的代理规则（23 条）</summary>


- `DOMAIN,xtls.github.io,PROXY`
  - 匹配白名单：`github.io`
  - 用途：GitHub Pages 站点
- `DOMAIN,nix-community.github.io,PROXY`
  - 匹配白名单：`github.io`
  - 用途：GitHub Pages 站点
- `DOMAIN,np-edge.itunes.apple.com,PROXY`
  - 匹配白名单：`itunes.apple.com`
  - 用途：iTunes/App Store 传统商店内容
- `DOMAIN-SUFFIX,bytegecko.com,PROXY`
  - 匹配白名单：`bytegecko.com`
  - 用途：字节跳动 CDN（网页资源）
- `DOMAIN,copilot-telemetry-service.githubusercontent.com,PROXY`
  - 匹配白名单：`githubusercontent.com`
  - 用途：GitHub 用户内容（raw 文件、图片、附件等）
- `DOMAIN-SUFFIX,snssdk.com,PROXY`
  - 匹配白名单：`snssdk.com`
  - 用途：字节跳动基础域名（短视频、直播等）
- `DOMAIN,hls.itunes.apple.com,PROXY`
  - 匹配白名单：`itunes.apple.com`
  - 用途：iTunes/App Store 传统商店内容
- `DOMAIN-SUFFIX,githubusercontent.com,PROXY`
  - 匹配白名单：`githubusercontent.com`
  - 用途：GitHub 用户内容（raw 文件、图片、附件等）
- `DOMAIN,metacubex.github.io,PROXY`
  - 匹配白名单：`github.io`
  - 用途：GitHub Pages 站点
- `DOMAIN,throneproj.github.io,PROXY`
  - 匹配白名单：`github.io`
  - 用途：GitHub Pages 站点
- `DOMAIN,bybit-exchange.github.io,PROXY`
  - 匹配白名单：`github.io`
  - 用途：GitHub Pages 站点
- `DOMAIN,matsuridayo.github.io,PROXY`
  - 匹配白名单：`github.io`
  - 用途：GitHub Pages 站点
- `DOMAIN-SUFFIX,github.io,PROXY`
  - 匹配白名单：`github.io`
  - 用途：GitHub Pages 站点
- `DOMAIN,uts-api.itunes.apple.com,PROXY`
  - 匹配白名单：`itunes.apple.com`
  - 用途：iTunes/App Store 传统商店内容
- `DOMAIN-SUFFIX,ru.ccb.com,PROXY`
  - 匹配白名单：`ccb.com`
  - 用途：中国建设银行
- `DOMAIN,play-edge.itunes.apple.com,PROXY`
  - 匹配白名单：`itunes.apple.com`
  - 用途：iTunes/App Store 传统商店内容
- `DOMAIN-SUFFIX,githubassets.com,PROXY`
  - 匹配白名单：`githubassets.com`
  - 用途：GitHub 静态资源（CSS、JS、头像等）
- `DOMAIN,trojan-gfw.github.io,PROXY`
  - 匹配白名单：`github.io`
  - 用途：GitHub Pages 站点
- `DOMAIN-SUFFIX,github.com,PROXY`
  - 匹配白名单：`github.com`
  - 用途：GitHub 主站
- `DOMAIN,copilot-telemetry.githubusercontent.com,PROXY`
  - 匹配白名单：`githubusercontent.com`
  - 用途：GitHub 用户内容（raw 文件、图片、附件等）
- `DOMAIN,hls-amt.itunes.apple.com,PROXY`
  - 匹配白名单：`itunes.apple.com`
  - 用途：iTunes/App Store 传统商店内容
- `DOMAIN,copilot-proxy.githubusercontent.com,PROXY`
  - 匹配白名单：`githubusercontent.com`
  - 用途：GitHub 用户内容（raw 文件、图片、附件等）
- `DOMAIN-SUFFIX,mzstatic.com,PROXY`
  - 匹配白名单：`mzstatic.com`
  - 用途：苹果商店静态资源 CDN（截图、图标等）

</details>

### 🛡️ 白名单豁免（去广告规则，共 30 条）

**原因**：这些域名在 `direct_whitelist.txt` 中，已从去广告规则中移除，避免误拦截。

<details>
<summary>展开查看被豁免的去广告规则（30 条）</summary>


- `DOMAIN,abtest-ch.snssdk.com,REJECT`
  - 匹配白名单：`snssdk.com`
  - 用途：字节跳动基础域名（短视频、直播等）
- `DOMAIN,ads.95516.com,REJECT`
  - 匹配白名单：`95516.com`
  - 用途：银联客服
- `DOMAIN,ads.cup.com.cn,REJECT`
  - 匹配白名单：`cup.com.cn`
  - 用途：银联
- `DOMAIN,log.amemv.com,REJECT`
  - 匹配白名单：`amemv.com`
  - 用途：字节跳动短视频（抖音、火山等）
- `DOMAIN,metrics.mzstatic.com,REJECT`
  - 匹配白名单：`mzstatic.com`
  - 用途：苹果商店静态资源 CDN（截图、图标等）
- `DOMAIN,open.snssdk.com,REJECT`
  - 匹配白名单：`snssdk.com`
  - 用途：字节跳动基础域名（短视频、直播等）
- `DOMAIN,p3-tt.byteimg.com,REJECT`
  - 匹配白名单：`byteimg.com`
  - 用途：字节跳动图片 CDN
- `DOMAIN,tnc3-aliec2.snssdk.com,REJECT`
  - 匹配白名单：`snssdk.com`
  - 用途：字节跳动基础域名（短视频、直播等）
- `DOMAIN,tnc3-alisc1.snssdk.com,REJECT`
  - 匹配白名单：`snssdk.com`
  - 用途：字节跳动基础域名（短视频、直播等）
- `DOMAIN,tnc3-bjlgy.snssdk.com,REJECT`
  - 匹配白名单：`snssdk.com`
  - 用途：字节跳动基础域名（短视频、直播等）
- `DOMAIN-SUFFIX,ads.cup.com.cn,REJECT`
  - 匹配白名单：`cup.com.cn`
  - 用途：银联
- `DOMAIN-SUFFIX,adv.ccb.com,REJECT`
  - 匹配白名单：`ccb.com`
  - 用途：中国建设银行
- `DOMAIN-SUFFIX,log.snssdk.com,REJECT-200`
  - 匹配白名单：`snssdk.com`
  - 用途：字节跳动基础域名（短视频、直播等）
- `DOMAIN-SUFFIX,metrics.mzstatic.com,REJECT`
  - 匹配白名单：`mzstatic.com`
  - 用途：苹果商店静态资源 CDN（截图、图标等）
- `DOMAIN-SUFFIX,log.snssdk.com,REJECT`
  - 匹配白名单：`snssdk.com`
  - 用途：字节跳动基础域名（短视频、直播等）
- `DOMAIN-SUFFIX,devgottia.github.io,REJECT`
  - 匹配白名单：`github.io`
  - 用途：GitHub Pages 站点
- `DOMAIN-SUFFIX,collector.github.com,REJECT`
  - 匹配白名单：`github.com`
  - 用途：GitHub 主站
- `DOMAIN-SUFFIX,dm.pstatp.com,REJECT`
  - 匹配白名单：`pstatp.com`
  - 用途：字节跳动基础域名（推荐、API 等）
- `DOMAIN-SUFFIX,log0-misc-hl.amemv.com,REJECT`
  - 匹配白名单：`amemv.com`
  - 用途：字节跳动短视频（抖音、火山等）
- `DOMAIN-SUFFIX,ib.snssdk.com,REJECT`
  - 匹配白名单：`snssdk.com`
  - 用途：字节跳动基础域名（短视频、直播等）
- `DOMAIN-SUFFIX,p3-ad-sign.byteimg.com,REJECT`
  - 匹配白名单：`byteimg.com`
  - 用途：字节跳动图片 CDN
- `DOMAIN-SUFFIX,log-hl.snssdk.com,REJECT`
  - 匹配白名单：`snssdk.com`
  - 用途：字节跳动基础域名（短视频、直播等）
- `DOMAIN-SUFFIX,mon.snssdk.com,REJECT`
  - 匹配白名单：`snssdk.com`
  - 用途：字节跳动基础域名（短视频、直播等）
- `DOMAIN-SUFFIX,googleads.github.io,REJECT`
  - 匹配白名单：`github.io`
  - 用途：GitHub Pages 站点
- `DOMAIN-SUFFIX,copilot-telemetry.githubusercontent.com,REJECT`
  - 匹配白名单：`githubusercontent.com`
  - 用途：GitHub 用户内容（raw 文件、图片、附件等）
- `DOMAIN-SUFFIX,analytics.githubassets.com,REJECT`
  - 匹配白名单：`githubassets.com`
  - 用途：GitHub 静态资源（CSS、JS、头像等）
- `DOMAIN-SUFFIX,mcs.snssdk.com,REJECT`
  - 匹配白名单：`snssdk.com`
  - 用途：字节跳动基础域名（短视频、直播等）
- `DOMAIN-SUFFIX,mihoutao1868.github.io,REJECT`
  - 匹配白名单：`github.io`
  - 用途：GitHub Pages 站点
- `DOMAIN-SUFFIX,collector-cdn.github.com,REJECT`
  - 匹配白名单：`github.com`
  - 用途：GitHub 主站
- `DOMAIN-SUFFIX,xlog.snssdk.com,REJECT`
  - 匹配白名单：`snssdk.com`
  - 用途：字节跳动基础域名（短视频、直播等）

</details>

### ❌ 代理规则质量检查异常（共 1 条）

**处理动作**：异常规则已从最终模块中移除。

<details>
<summary>展开查看异常规则及原因</summary>

```
- DOMAIN-SUFFIX,OMAIN-SUFFIX,bing.net,PROXY  (原因: 策略 'BING.NET' 不合法)
```
</details>

### ⚠️ Shield 模块同域名策略冲突（共 16 组）

**判断依据**：同一域名出现多个规则，且策略不同。

**处理动作**：排序后靠前的规则优先生效，后续冲突规则不会影响最终策略，但已记录。

<details>
<summary>展开查看冲突详情</summary>

**DOMAIN-SUFFIX:adashx.m.taobao.com**
```
- DOMAIN-SUFFIX,adashx.m.taobao.com,REJECT
- DOMAIN-SUFFIX,adashx.m.taobao.com,REJECT-200
```
**DOMAIN-SUFFIX:amdc.m.taobao.com**
```
- DOMAIN-SUFFIX,amdc.m.taobao.com,REJECT
- DOMAIN-SUFFIX,amdc.m.taobao.com,REJECT-200
```
**DOMAIN-SUFFIX:applog.uc.cn**
```
- DOMAIN-SUFFIX,applog.uc.cn,REJECT
- DOMAIN-SUFFIX,applog.uc.cn,REJECT-200
```
**DOMAIN-SUFFIX:cnlogs.umengcloud.com**
```
- DOMAIN-SUFFIX,cnlogs.umengcloud.com,REJECT
- DOMAIN-SUFFIX,cnlogs.umengcloud.com,REJECT-DICT
```
**DOMAIN-SUFFIX:df.tanx.com**
```
- DOMAIN-SUFFIX,df.tanx.com,REJECT
- DOMAIN-SUFFIX,df.tanx.com,REJECT-200
```
**DOMAIN-SUFFIX:dualstack-logs.amap.com**
```
- DOMAIN-SUFFIX,dualstack-logs.amap.com,REJECT
- DOMAIN-SUFFIX,dualstack-logs.amap.com,REJECT-200
```
**DOMAIN-SUFFIX:e.qq.com**
```
- DOMAIN-SUFFIX,e.qq.com,REJECT
- DOMAIN-SUFFIX,e.qq.com,REJECT-DICT
```
**DOMAIN-SUFFIX:h-adashx.ut.taobao.com**
```
- DOMAIN-SUFFIX,h-adashx.ut.taobao.com,REJECT
- DOMAIN-SUFFIX,h-adashx.ut.taobao.com,REJECT-200
```
**DOMAIN-SUFFIX:imasdk.googleapis.com**
```
- DOMAIN-SUFFIX,imasdk.googleapis.com,REJECT
- DOMAIN-SUFFIX,imasdk.googleapis.com,REJECT-DICT
```
**DOMAIN-SUFFIX:iyes.youku.com**
```
- DOMAIN-SUFFIX,iyes.youku.com,REJECT
- DOMAIN-SUFFIX,iyes.youku.com,REJECT-200
```
**DOMAIN-SUFFIX:lf-static.tiktokpangle-cdn-us.com**
```
- DOMAIN-SUFFIX,lf-static.tiktokpangle-cdn-us.com,REJECT
- DOMAIN-SUFFIX,lf-static.tiktokpangle-cdn-us.com,REJECT-200
```
**DOMAIN-SUFFIX:logs.amap.com**
```
- DOMAIN-SUFFIX,logs.amap.com,REJECT
- DOMAIN-SUFFIX,logs.amap.com,REJECT-200
```
**DOMAIN-SUFFIX:pangolin-sdk-toutiao-b.com**
```
- DOMAIN-SUFFIX,pangolin-sdk-toutiao-b.com,REJECT
- DOMAIN-SUFFIX,pangolin-sdk-toutiao-b.com,REJECT-DICT
```
**DOMAIN-SUFFIX:pangolin-sdk-toutiao.com**
```
- DOMAIN-SUFFIX,pangolin-sdk-toutiao.com,REJECT
- DOMAIN-SUFFIX,pangolin-sdk-toutiao.com,REJECT-DICT
```
**DOMAIN-SUFFIX:pglstatp-toutiao.com**
```
- DOMAIN-SUFFIX,pglstatp-toutiao.com,REJECT
- DOMAIN-SUFFIX,pglstatp-toutiao.com,REJECT-DICT
```
**DOMAIN-SUFFIX:ulogs.umengcloud.com**
```
- DOMAIN-SUFFIX,ulogs.umengcloud.com,REJECT
- DOMAIN-SUFFIX,ulogs.umengcloud.com,REJECT-DICT
```
</details>

### ⚠️ 父子域冲突（合计 45 组）

**判断依据**：DOMAIN 规则被 DOMAIN-SUFFIX 规则覆盖且策略不同。

**处理动作**：排序后 DOMAIN 规则在前，将优先生效。

<details>
<summary>展开查看冲突详情</summary>

- DOMAIN adashbc.ut.taobao.com (REJECT) 被 DOMAIN-SUFFIX adashbc.ut.taobao.com (REJECT-200) 覆盖
- DOMAIN adashx.m.taobao.com (REJECT) 被 DOMAIN-SUFFIX adashx.m.taobao.com (REJECT-200) 覆盖
- DOMAIN adashxgc.ut.taobao.com (REJECT) 被 DOMAIN-SUFFIX adashxgc.ut.taobao.com (REJECT-200) 覆盖
- DOMAIN api-access.pangolin-sdk-toutiao-b.com (REJECT) 被 DOMAIN-SUFFIX pangolin-sdk-toutiao-b.com (REJECT-DICT) 覆盖
- DOMAIN api-access.pangolin-sdk-toutiao.com (REJECT) 被 DOMAIN-SUFFIX pangolin-sdk-toutiao.com (REJECT-DICT) 覆盖
- DOMAIN api-access.pangolin-sdk-toutiao1.com (REJECT) 被 DOMAIN-SUFFIX pangolin-sdk-toutiao1.com (REJECT-DICT) 覆盖
- DOMAIN applog.uc.cn (REJECT) 被 DOMAIN-SUFFIX applog.uc.cn (REJECT-200) 覆盖
- DOMAIN bootpreload.uve.weibo.com (REJECT) 被 DOMAIN-SUFFIX bootpreload.uve.weibo.com (REJECT-200) 覆盖
- DOMAIN cnlogs.umeng.com (REJECT) 被 DOMAIN-SUFFIX cnlogs.umeng.com (REJECT-DICT) 覆盖
- DOMAIN cnlogs.umengcloud.com (REJECT) 被 DOMAIN-SUFFIX cnlogs.umengcloud.com (REJECT-DICT) 覆盖
- DOMAIN dualstack-logs.amap.com (REJECT) 被 DOMAIN-SUFFIX dualstack-logs.amap.com (REJECT-200) 覆盖
- DOMAIN ef-dongfeng.tanx.com (REJECT) 被 DOMAIN-SUFFIX ef-dongfeng.tanx.com (REJECT-200) 覆盖
- DOMAIN ef-dongfeng.tanx.com (REJECT) 被 DOMAIN-SUFFIX tanx.com (REJECT-200) 覆盖
- DOMAIN gromore.pangolin-sdk-toutiao.com (REJECT) 被 DOMAIN-SUFFIX pangolin-sdk-toutiao.com (REJECT-DICT) 覆盖
- DOMAIN h-adashx.ut.taobao.com (REJECT) 被 DOMAIN-SUFFIX h-adashx.ut.taobao.com (REJECT-200) 覆盖
- DOMAIN ifs.tanx.com (REJECT) 被 DOMAIN-SUFFIX tanx.com (REJECT-200) 覆盖
- DOMAIN lf3-ad-union-sdk.pglstatp-toutiao.com (REJECT) 被 DOMAIN-SUFFIX pglstatp-toutiao.com (REJECT-DICT) 覆盖
- DOMAIN lf6-ad-union-sdk.pglstatp-toutiao.com (REJECT) 被 DOMAIN-SUFFIX pglstatp-toutiao.com (REJECT-DICT) 覆盖
- DOMAIN log-api.pangolin-sdk-toutiao-b.com (REJECT) 被 DOMAIN-SUFFIX pangolin-sdk-toutiao-b.com (REJECT-DICT) 覆盖
- DOMAIN log-api.pangolin-sdk-toutiao.com (REJECT) 被 DOMAIN-SUFFIX pangolin-sdk-toutiao.com (REJECT-DICT) 覆盖
- DOMAIN logs.amap.com (REJECT) 被 DOMAIN-SUFFIX logs.amap.com (REJECT-200) 覆盖
- DOMAIN mssdk.volces.com (REJECT) 被 DOMAIN-SUFFIX mssdk.volces.com (REJECT-DICT) 覆盖
- DOMAIN p1-be-pack-sign.pglstatp-toutiao.com (REJECT) 被 DOMAIN-SUFFIX pglstatp-toutiao.com (REJECT-DICT) 覆盖
- DOMAIN p2-be-pack-sign.pglstatp-toutiao.com (REJECT) 被 DOMAIN-SUFFIX pglstatp-toutiao.com (REJECT-DICT) 覆盖
- DOMAIN p3-be-pack-sign.pglstatp-toutiao.com (REJECT) 被 DOMAIN-SUFFIX pglstatp-toutiao.com (REJECT-DICT) 覆盖
- DOMAIN p4-be-pack-sign.pglstatp-toutiao.com (REJECT) 被 DOMAIN-SUFFIX pglstatp-toutiao.com (REJECT-DICT) 覆盖
- DOMAIN p5-be-pack-sign.pglstatp-toutiao.com (REJECT) 被 DOMAIN-SUFFIX pglstatp-toutiao.com (REJECT-DICT) 覆盖
- DOMAIN p6-be-pack-sign.pglstatp-toutiao.com (REJECT) 被 DOMAIN-SUFFIX pglstatp-toutiao.com (REJECT-DICT) 覆盖
- DOMAIN pangolin-sdk-toutiao-b.com (REJECT) 被 DOMAIN-SUFFIX pangolin-sdk-toutiao-b.com (REJECT-DICT) 覆盖
- DOMAIN pglstatp-toutiao.com (REJECT) 被 DOMAIN-SUFFIX pglstatp-toutiao.com (REJECT-DICT) 覆盖
- DOMAIN resolve.umeng.com (REJECT) 被 DOMAIN-SUFFIX resolve.umeng.com (REJECT-DICT) 覆盖
- DOMAIN sdk-track.66mobi.com (REJECT) 被 DOMAIN-SUFFIX sdk-track.66mobi.com (REJECT-DICT) 覆盖
- DOMAIN sdk.1rtb.net (REJECT) 被 DOMAIN-SUFFIX sdk.1rtb.net (REJECT-DICT) 覆盖
- DOMAIN sdk.beizi.biz (REJECT) 被 DOMAIN-SUFFIX sdk.beizi.biz (REJECT-DICT) 覆盖
- DOMAIN sdk.e.qq.com (REJECT) 被 DOMAIN-SUFFIX e.qq.com (REJECT-DICT) 覆盖
- DOMAIN sdkapp.uve.weibo.com (REJECT) 被 DOMAIN-SUFFIX sdkapp.uve.weibo.com (REJECT-DICT) 覆盖
- DOMAIN sdkreport.e.qq.com (REJECT) 被 DOMAIN-SUFFIX e.qq.com (REJECT-DICT) 覆盖
- DOMAIN sf3-fe-tos.pglstatp-toutiao.com (REJECT) 被 DOMAIN-SUFFIX pglstatp-toutiao.com (REJECT-DICT) 覆盖
- DOMAIN smartad.10010.com (REJECT) 被 DOMAIN-SUFFIX smartad.10010.com (REJECT-200) 覆盖
- DOMAIN success.ctobsnssdk.com (REJECT) 被 DOMAIN-SUFFIX ctobsnssdk.com (REJECT-DICT) 覆盖
- DOMAIN tangram.e.qq.com (REJECT) 被 DOMAIN-SUFFIX e.qq.com (REJECT-DICT) 覆盖
- DOMAIN toblog.ctobsnssdk.com (REJECT) 被 DOMAIN-SUFFIX ctobsnssdk.com (REJECT-DICT) 覆盖
- DOMAIN ulogs.umeng.com (REJECT) 被 DOMAIN-SUFFIX ulogs.umeng.com (REJECT-DICT) 覆盖
- DOMAIN ulogs.umengcloud.com (REJECT) 被 DOMAIN-SUFFIX ulogs.umengcloud.com (REJECT-DICT) 覆盖
- DOMAIN utoken.umeng.com (REJECT) 被 DOMAIN-SUFFIX utoken.umeng.com (REJECT-DICT) 覆盖
</details>

### 上游源状态

- ✅ https://raw.githubusercontent.com/GMOogway/shadowrocket-rules/master/sr_proxy_list.module
- ✅ https://raw.githubusercontent.com/LOWERTOP/Shadowrocket-First/main/Talkatone.sgmodule

**原有代理规则数**: 27617
**新增代理规则数**: 22
**更新后代理规则总数**: 27639

#### 新增代理规则明细

<details>
<summary>展开查看新增代理规则（共 22 条）</summary>

```
DOMAIN-SUFFIX,1password.dev,PROXY
DOMAIN-SUFFIX,cyberpunk.net,PROXY
DOMAIN-SUFFIX,123av.org,PROXY
DOMAIN-SUFFIX,zozovideo.com,PROXY
DOMAIN-SUFFIX,thewitcher.com,PROXY
DOMAIN-SUFFIX,xn--pssu7ci3q5oge0ai91q.xn--j6w193g,PROXY
DOMAIN-SUFFIX,xn--fiq80y3xbiwrs0kiu9d.hk,PROXY
DOMAIN-SUFFIX,cdpred.services,PROXY
DOMAIN-SUFFIX,minkch.com,PROXY
DOMAIN-SUFFIX,xn--fiq80y.hk,PROXY
DOMAIN-SUFFIX,playgwent.com,PROXY
DOMAIN-SUFFIX,cdprojekt.red,PROXY
DOMAIN-SUFFIX,xn--fiq80y3xbiwrs0kiu9d.xn--j6w193g,PROXY
DOMAIN-SUFFIX,xn--pssu7cz8nr8ibkx1e8a.xn--j6w193g,PROXY
DOMAIN-SUFFIX,po-kaki-to.com,PROXY
DOMAIN-SUFFIX,cdprojektred.com,PROXY
DOMAIN-SUFFIX,njav.com,PROXY
DOMAIN-SUFFIX,xn--fiq80y3xbiwr.hk,PROXY
DOMAIN-SUFFIX,xn--fiq80y3xbiwr.xn--j6w193g,PROXY
DOMAIN-SUFFIX,kimootoko.net,PROXY
DOMAIN-SUFFIX,xn--fiq80y.xn--j6w193g,PROXY
DOMAIN-SUFFIX,cdprojekt.com,PROXY
```
</details>

## 去广告模块

### 上游源状态

- ✅ https://raw.githubusercontent.com/huijingfei/Shadowrocket-Rules/refs/heads/main/sr_app_ad.module
- ✅ https://raw.githubusercontent.com/deezertidal/shadowrocket-rules/refs/heads/main/modules/startingad.module
- ✅ https://raw.githubusercontent.com/GMOogway/shadowrocket-rules/master/sr_reject_list.module
- ✅ https://raw.githubusercontent.com/Unwhimsical/NetPilot/refs/heads/main/modules/%E6%B5%8B%E8%AF%95.module
- ✅ https://raw.githubusercontent.com/LOWERTOP/Shadowrocket-First/main/TalkatoneAntiAds.list

**原有去广告规则数**: 218619
**新增去广告规则数**: 362
**更新后去广告规则总数**: 218981

#### 新增去广告规则明细

<details>
<summary>展开查看新增去广告规则（共 362 条）</summary>

```
DOMAIN-SUFFIX,bellicuneal.qpon,REJECT
DOMAIN-SUFFIX,8u9j9clpjox1y327p2omhp.rest,REJECT
DOMAIN-SUFFIX,toaster22.com,REJECT
DOMAIN-SUFFIX,htaptaidjcase.online,REJECT
DOMAIN-SUFFIX,dystomeuterus.qpon,REJECT
DOMAIN-SUFFIX,aqslujcrohco.in,REJECT
DOMAIN-SUFFIX,yyhkprhqenoan.space,REJECT
DOMAIN-SUFFIX,geunbtsaktcgp.online,REJECT
DOMAIN-SUFFIX,nuraghecornage.cyou,REJECT
DOMAIN-SUFFIX,koryarmorer.qpon,REJECT
DOMAIN-SUFFIX,wyzoshttlyvrm.space,REJECT
DOMAIN-SUFFIX,treatssenegajiggit.cyou,REJECT
DOMAIN-SUFFIX,angekokdiscerp.qpon,REJECT
DOMAIN-SUFFIX,nmbdeqxdkvhvm.site,REJECT
DOMAIN-SUFFIX,palchthouse.qpon,REJECT
DOMAIN-SUFFIX,hippedsonnets.com,REJECT
DOMAIN-SUFFIX,mfgygyhpddlyo.online,REJECT
DOMAIN-SUFFIX,knjasgnwitdwf.space,REJECT
DOMAIN-SUFFIX,rpgghmnptqhhi.online,REJECT
DOMAIN-SUFFIX,7imiy33o9vkqvrggxo2xr8y3.rest,REJECT
DOMAIN-SUFFIX,pbztcgfpuwzem.website,REJECT
DOMAIN-SUFFIX,cexwqhxuxixew.site,REJECT
DOMAIN-SUFFIX,todditehexarch.com,REJECT
DOMAIN-SUFFIX,fzgafhllmzsjo.online,REJECT
DOMAIN-SUFFIX,cpufcccvnbyvo.website,REJECT
DOMAIN-SUFFIX,zinitelophich.com,REJECT
DOMAIN-SUFFIX,minyansbarble.cfd,REJECT
DOMAIN-SUFFIX,unrobebemottoirfan.cfd,REJECT
DOMAIN-SUFFIX,tartestblocksjimmer.cyou,REJECT
DOMAIN-SUFFIX,idatievineovering.qpon,REJECT
DOMAIN-SUFFIX,coiffesreal.qpon,REJECT
DOMAIN-SUFFIX,juliettcorylet.com,REJECT
DOMAIN-SUFFIX,kjdegeotelm.com,REJECT
DOMAIN-SUFFIX,88884zeebz6um74p3qn7eggep.cfd,REJECT
DOMAIN-SUFFIX,shovelimmov.cfd,REJECT
DOMAIN-SUFFIX,zmrdjhej.com,REJECT
DOMAIN-SUFFIX,awdddntkckatv.online,REJECT
DOMAIN-SUFFIX,byk4vjplgq1phgcn7y1re66n.cfd,REJECT
DOMAIN-SUFFIX,sabulumtarocco.com,REJECT
DOMAIN-SUFFIX,iexfibdglnsxh.online,REJECT
DOMAIN-SUFFIX,sqkbgwxsytvzs.online,REJECT
DOMAIN-SUFFIX,amusedradish.com,REJECT
DOMAIN-SUFFIX,temptedpitta.cfd,REJECT
DOMAIN-SUFFIX,vbjxaorqqwubz.space,REJECT
DOMAIN-SUFFIX,lhibnuyxomzqv.space,REJECT
DOMAIN-SUFFIX,iikkhsvwsiobw.space,REJECT
DOMAIN-SUFFIX,lowwoodtanner.cfd,REJECT
DOMAIN-SUFFIX,oktavvavg.in,REJECT
DOMAIN-SUFFIX,grizelromneyaisobase.cyou,REJECT
DOMAIN-SUFFIX,ceqcioycqoiqh.space,REJECT
DOMAIN-SUFFIX,2yv33e3yih6yetq65kb8p1txi25mbvn4xhpw.rest,REJECT
DOMAIN-SUFFIX,yezzzrhgrkwli.space,REJECT
DOMAIN-SUFFIX,ty1lqyw6muhtvpiu.rest,REJECT
DOMAIN-SUFFIX,aqifslbgumtev.online,REJECT
DOMAIN-SUFFIX,nxynjy2kej.com,REJECT
DOMAIN-SUFFIX,niduspraisesbatoon.cfd,REJECT
DOMAIN-SUFFIX,agelzcxqccfxo.space,REJECT
DOMAIN-SUFFIX,eschelesiphoid.com,REJECT
DOMAIN-SUFFIX,mandirpeoplet.com,REJECT
DOMAIN-SUFFIX,saltedfrieze.com,REJECT
DOMAIN-SUFFIX,bonnilyfurnish.qpon,REJECT
DOMAIN-SUFFIX,lwxsocpvczuiq.online,REJECT
DOMAIN-SUFFIX,pekrqyieeeeht.online,REJECT
DOMAIN-SUFFIX,mulchdenyhows.cyou,REJECT
DOMAIN-SUFFIX,dreuihdvyukvl.site,REJECT
DOMAIN-SUFFIX,rosaliediiodid.com,REJECT
DOMAIN-SUFFIX,ubogicetmixgdl.com,REJECT
DOMAIN-SUFFIX,hogubqiagoail.space,REJECT
DOMAIN-SUFFIX,agenddoomsnatchy.qpon,REJECT
DOMAIN-SUFFIX,bideryprotyl.cfd,REJECT
DOMAIN-SUFFIX,219veo9vnjle6mouez.cfd,REJECT
DOMAIN-SUFFIX,t1ufw6nz5f.com,REJECT
DOMAIN-SUFFIX,ocabcjkdjilai.space,REJECT
DOMAIN-SUFFIX,finfishamyelia.com,REJECT
DOMAIN-SUFFIX,wwczhowikfsyz.site,REJECT
DOMAIN-SUFFIX,ettlederethicgriskin.cyou,REJECT
DOMAIN-SUFFIX,4lu114x7k9ef6qr82.cfd,REJECT
DOMAIN-SUFFIX,nhfkuabmtisjt.online,REJECT
DOMAIN-SUFFIX,ptkvumzaajsob.website,REJECT
DOMAIN-SUFFIX,shoepacpoon.cyou,REJECT
DOMAIN-SUFFIX,dotalsamisentrompe.cfd,REJECT
DOMAIN-SUFFIX,asemquips.cfd,REJECT
DOMAIN-SUFFIX,snzamgaxaepeg.site,REJECT
DOMAIN-SUFFIX,yyxjwgyzltmkf.site,REJECT
DOMAIN-SUFFIX,kwyiknngshfhg.site,REJECT
DOMAIN-SUFFIX,packetspoisesbally.cfd,REJECT
DOMAIN-SUFFIX,ravktufmpgula.site,REJECT
DOMAIN-SUFFIX,niggotchesil.cyou,REJECT
DOMAIN-SUFFIX,kwmtfcylgivln.space,REJECT
DOMAIN-SUFFIX,djhanucviqf.com,REJECT
DOMAIN-SUFFIX,carotpoietictopes.qpon,REJECT
DOMAIN-SUFFIX,xlwfwvxwtozoa.space,REJECT
DOMAIN-SUFFIX,unlylpxmdcqcn.site,REJECT
DOMAIN-SUFFIX,blossomstorm.com,REJECT
DOMAIN-SUFFIX,njmwejmkxhtpi.site,REJECT
DOMAIN-SUFFIX,lfzerayskzafi.online,REJECT
DOMAIN-SUFFIX,ymhzywtdnrsta.site,REJECT
DOMAIN-SUFFIX,2ehvl111jccg2mg4824.cfd,REJECT
DOMAIN-SUFFIX,ylfnmfzbplwpg.online,REJECT
DOMAIN-SUFFIX,vvwoecwtugszl.online,REJECT
DOMAIN-SUFFIX,rjajotovkkkir.site,REJECT
DOMAIN-SUFFIX,botcheszest.com,REJECT
DOMAIN-SUFFIX,pilawscrewy.cfd,REJECT
DOMAIN-SUFFIX,lzswdckjqxbjr.site,REJECT
DOMAIN-SUFFIX,cetincipango.qpon,REJECT
DOMAIN-SUFFIX,goakfsoloeapw.online,REJECT
DOMAIN-SUFFIX,mvwzqtwvkhgei.site,REJECT
DOMAIN-SUFFIX,nikatgzcjrbbf.online,REJECT
DOMAIN-SUFFIX,tabaxirethnize.cyou,REJECT
DOMAIN-SUFFIX,pcjdovrvkaija.online,REJECT
DOMAIN-SUFFIX,bebleedchuffs.cfd,REJECT
DOMAIN-SUFFIX,ejfohieuzjdbm.site,REJECT
DOMAIN-SUFFIX,zestyalto.com,REJECT
DOMAIN-SUFFIX,fxhilzrijawtz.online,REJECT
DOMAIN-SUFFIX,misdeemacetary.cfd,REJECT
DOMAIN-SUFFIX,ofeiaibnwirml.online,REJECT
DOMAIN-SUFFIX,jvserdywzwvmh.website,REJECT
DOMAIN-SUFFIX,gweducsmotels.com,REJECT
DOMAIN-SUFFIX,zgphpybgswzie.online,REJECT
DOMAIN-SUFFIX,vwsuoczefptjr.website,REJECT
DOMAIN-SUFFIX,drkmkdnfarrey.site,REJECT
DOMAIN-SUFFIX,medicalenstamptictoc.qpon,REJECT
DOMAIN-SUFFIX,bandletscobs.qpon,REJECT
DOMAIN-SUFFIX,rgbaayfdyjzou.online,REJECT
DOMAIN-SUFFIX,cntsmkfxhorvt.site,REJECT
DOMAIN-SUFFIX,gooziucqysxjz.space,REJECT
DOMAIN-SUFFIX,ataqsinsgufxk.online,REJECT
DOMAIN-SUFFIX,gslozndcnlvvi.site,REJECT
DOMAIN-SUFFIX,ihihbckxoquli.online,REJECT
DOMAIN-SUFFIX,zadlclqnequke.site,REJECT
DOMAIN-SUFFIX,wicmdokqlpdso.space,REJECT
DOMAIN-SUFFIX,wodzxaloxquvz.space,REJECT
DOMAIN-SUFFIX,g2n3ewhou41oozqzf9iy8nv7m3.rest,REJECT
DOMAIN-SUFFIX,p1oo54kz6d.com,REJECT
DOMAIN-SUFFIX,croupyacouchysheers.cfd,REJECT
DOMAIN-SUFFIX,inswepttillaea.cyou,REJECT
DOMAIN-SUFFIX,qwtrmnaewnctq.space,REJECT
DOMAIN-SUFFIX,dyrwgnyjzaphq.space,REJECT
DOMAIN-SUFFIX,smoothcanoe.com,REJECT
DOMAIN-SUFFIX,hasselscloth.cyou,REJECT
DOMAIN-SUFFIX,mfwkhpoqjgwjz.space,REJECT
DOMAIN-SUFFIX,ylaizwqijnawh.site,REJECT
DOMAIN-SUFFIX,imefvemjrroxa.online,REJECT
DOMAIN-SUFFIX,sfumhmojnljka.online,REJECT
DOMAIN-SUFFIX,znjysufu.com,REJECT
DOMAIN-SUFFIX,wisjevyyjdjad.site,REJECT
DOMAIN-SUFFIX,nkjlbhfpxlfvx.space,REJECT
DOMAIN-SUFFIX,kmltaguttgpiq.space,REJECT
DOMAIN-SUFFIX,uywtigklrhywd.online,REJECT
DOMAIN-SUFFIX,dnvtyawatdnrr.site,REJECT
DOMAIN-SUFFIX,cdn.adelivery.se,REJECT
DOMAIN-SUFFIX,vnegfpasjdibx.site,REJECT
DOMAIN-SUFFIX,abkgsnvrgkikq.online,REJECT
DOMAIN-SUFFIX,oazfmcblopdje.online,REJECT
DOMAIN-SUFFIX,mlepzhgpdtyfb.site,REJECT
DOMAIN-SUFFIX,djoregzqjwthd.site,REJECT
DOMAIN-SUFFIX,robinggnathic.cfd,REJECT
DOMAIN-SUFFIX,grlrmortbxvee.space,REJECT
DOMAIN-SUFFIX,gnlmaqgvmwbkk.space,REJECT
DOMAIN-SUFFIX,uaeapcmjbmzad.space,REJECT
DOMAIN-SUFFIX,yawningparkas.com,REJECT
DOMAIN-SUFFIX,severerpreknow.com,REJECT
DOMAIN-SUFFIX,qtoonoecxthnl.space,REJECT
DOMAIN-SUFFIX,resizederinize.cfd,REJECT
DOMAIN-SUFFIX,zepzylmimnsxj.site,REJECT
DOMAIN-SUFFIX,calyclisuperb.cfd,REJECT
DOMAIN-SUFFIX,bdavjbhjpzjmt.space,REJECT
DOMAIN-SUFFIX,kyqkyumnlbjik.online,REJECT
DOMAIN-SUFFIX,lxntvjgjjmcdw.website,REJECT
DOMAIN-SUFFIX,epswiopwxylwi.site,REJECT
DOMAIN-SUFFIX,squgziaxhqj.com,REJECT
DOMAIN-SUFFIX,gytzzylfaokwt.online,REJECT
DOMAIN-SUFFIX,adewpxnzsnvib.site,REJECT
DOMAIN-SUFFIX,jucxhidpig.in,REJECT
DOMAIN-SUFFIX,crimumbowosith.qpon,REJECT
DOMAIN-SUFFIX,kxtsxpdqpksaw.online,REJECT
DOMAIN-SUFFIX,vsnctrfamkmai.online,REJECT
DOMAIN-SUFFIX,chcekcxekirtx.online,REJECT
DOMAIN-SUFFIX,athyridlidgate.cyou,REJECT
DOMAIN-SUFFIX,lbldkocndjvbw.site,REJECT
DOMAIN-SUFFIX,iqjgwbkeqkpix.online,REJECT
DOMAIN-SUFFIX,lavnkios.in,REJECT
DOMAIN-SUFFIX,hygeisthaida.cyou,REJECT
DOMAIN-SUFFIX,lineyalary.cyou,REJECT
DOMAIN-SUFFIX,photismdotherbiggah.cfd,REJECT
DOMAIN-SUFFIX,pdbemjjzwqcws.online,REJECT
DOMAIN-SUFFIX,aanvqmyqaojwu.website,REJECT
DOMAIN-SUFFIX,mqkosdxagptzh.online,REJECT
DOMAIN-SUFFIX,churromisos.com,REJECT
DOMAIN-SUFFIX,xkxxrdeuknhvz.site,REJECT
DOMAIN-SUFFIX,xyduvgcomskok.website,REJECT
DOMAIN-SUFFIX,napmfrdfkulkh.site,REJECT
DOMAIN-SUFFIX,wgtxtdheugybd.site,REJECT
DOMAIN-SUFFIX,jmbxsgugxfied.space,REJECT
DOMAIN-SUFFIX,lannerstaurinicarree.qpon,REJECT
DOMAIN-SUFFIX,nxyzabhy3.com,REJECT
DOMAIN-SUFFIX,xwdrmisubmm.com,REJECT
DOMAIN-SUFFIX,ikecwekdmbftc.space,REJECT
DOMAIN-SUFFIX,krdimzqznvbss.site,REJECT
DOMAIN-SUFFIX,uiiomzoajkypl.space,REJECT
DOMAIN-SUFFIX,sellingafaced.com,REJECT
DOMAIN-SUFFIX,qzcwqxjkuijaq.website,REJECT
DOMAIN-SUFFIX,wareggasehyo.cfd,REJECT
DOMAIN-SUFFIX,anaguasuitor.com,REJECT
DOMAIN-SUFFIX,yoksaffiant.cyou,REJECT
DOMAIN-SUFFIX,wwukvmgeutahv.website,REJECT
DOMAIN-SUFFIX,oxlqojvewyjni.site,REJECT
DOMAIN-SUFFIX,brenzcdjozwpw.website,REJECT
DOMAIN-SUFFIX,itxvswrxzslgt.online,REJECT
DOMAIN-SUFFIX,engsinseeovaria.cfd,REJECT
DOMAIN-SUFFIX,formingvaguish.com,REJECT
DOMAIN-SUFFIX,schutezest.qpon,REJECT
DOMAIN-SUFFIX,ijryyfexcfknw.online,REJECT
DOMAIN-SUFFIX,zmgzerfxzgkeq.online,REJECT
DOMAIN-SUFFIX,fakerstoterframing.qpon,REJECT
DOMAIN-SUFFIX,n5ku61z6km.com,REJECT
DOMAIN-SUFFIX,hoehodncrqnoc.website,REJECT
DOMAIN-SUFFIX,pingprove.com,REJECT
DOMAIN-SUFFIX,aqubzryzaqdxe.space,REJECT
DOMAIN-SUFFIX,qmepjwlgp.com,REJECT
DOMAIN-SUFFIX,1nrgur4y43.com,REJECT
DOMAIN-SUFFIX,xceehglvudviv.space,REJECT
DOMAIN-SUFFIX,torsescoltish.qpon,REJECT
DOMAIN-SUFFIX,mujteeuqrdvux.site,REJECT
DOMAIN-SUFFIX,yuwpcczbgmolj.com,REJECT
DOMAIN-SUFFIX,egycodcvtzehv.website,REJECT
DOMAIN-SUFFIX,ecvihexbkacpa.space,REJECT
DOMAIN-SUFFIX,mharavczumra.in,REJECT
DOMAIN-SUFFIX,carpoolgraff.cfd,REJECT
DOMAIN-SUFFIX,qxspkhpb.com,REJECT
DOMAIN-SUFFIX,icpjsggtmkdul.site,REJECT
DOMAIN-SUFFIX,pezcuiqgpqrhs.site,REJECT
DOMAIN-SUFFIX,vleqrwluxgslv.online,REJECT
DOMAIN-SUFFIX,cantabsteroid.cfd,REJECT
DOMAIN-SUFFIX,simconbutanefear.cfd,REJECT
DOMAIN-SUFFIX,zisdqzcpzgarq.space,REJECT
DOMAIN-SUFFIX,phustcugnffcn.space,REJECT
DOMAIN-SUFFIX,stbdktrfpkjsl.online,REJECT
DOMAIN-SUFFIX,cbxp9xqbnh.com,REJECT
DOMAIN-SUFFIX,eucztfyfooswmy.com,REJECT
DOMAIN-SUFFIX,hmiozovxgweym.site,REJECT
DOMAIN-SUFFIX,ynylicdrkzbtp.space,REJECT
DOMAIN-SUFFIX,urrfkabrkhxjat.com,REJECT
DOMAIN-SUFFIX,e448bf91d1.com,REJECT
DOMAIN-SUFFIX,mjhwpnzxkjocw.space,REJECT
DOMAIN-SUFFIX,knqspohyhyxwp.space,REJECT
DOMAIN-SUFFIX,keennight.com,REJECT
DOMAIN-SUFFIX,zowjwdmzntmyn.online,REJECT
DOMAIN-SUFFIX,dzwcpfwwkcexd.space,REJECT
DOMAIN-SUFFIX,misdoeraumaga.com,REJECT
DOMAIN-SUFFIX,rcwjxhashhfyg.online,REJECT
DOMAIN-SUFFIX,ruledkaimanthiolic.qpon,REJECT
DOMAIN-SUFFIX,tcerhxvlurvwf.site,REJECT
DOMAIN-SUFFIX,ipwqobevglbdk.online,REJECT
DOMAIN-SUFFIX,bdphtzfhmnfxo.space,REJECT
DOMAIN-SUFFIX,vvnnzpasmoafi.space,REJECT
DOMAIN-SUFFIX,whwfabebnnjfoi.com,REJECT
DOMAIN-SUFFIX,fluemansabine.qpon,REJECT
DOMAIN-SUFFIX,xdcxjbptkyzol.space,REJECT
DOMAIN-SUFFIX,ohedfrrwjemyg.website,REJECT
DOMAIN-SUFFIX,ismtpfncxnelg.online,REJECT
DOMAIN-SUFFIX,upbeatspring.com,REJECT
DOMAIN-SUFFIX,batemanlyopoma.cyou,REJECT
DOMAIN-SUFFIX,hieingintroit.cfd,REJECT
DOMAIN-SUFFIX,occluseduluth.cfd,REJECT
DOMAIN-SUFFIX,zgnxnixkxhcik.website,REJECT
DOMAIN-SUFFIX,abromalorarii.com,REJECT
DOMAIN-SUFFIX,vfcakwrxiaaws.site,REJECT
DOMAIN-SUFFIX,udeeakeymmowc.space,REJECT
DOMAIN-SUFFIX,gxjemsdjbgwse.site,REJECT
DOMAIN-SUFFIX,rodratton.qpon,REJECT
DOMAIN-SUFFIX,toniesglede.cfd,REJECT
DOMAIN-SUFFIX,ehwdvntpzjgtu.online,REJECT
DOMAIN-SUFFIX,ammankalians.qpon,REJECT
DOMAIN-SUFFIX,dutpzliwv.com,REJECT
DOMAIN-SUFFIX,zqycdzdckeyuf.space,REJECT
DOMAIN-SUFFIX,ylzblwispwrsi.online,REJECT
DOMAIN-SUFFIX,umtnpbqxhwuqr.online,REJECT
DOMAIN-SUFFIX,bgyfguewhfyjx.site,REJECT
DOMAIN-SUFFIX,ywdxitjjvljdj.site,REJECT
DOMAIN-SUFFIX,ukzkkfpeqhuue.site,REJECT
DOMAIN-SUFFIX,omeliepoetry.cfd,REJECT
DOMAIN-SUFFIX,t46z9wm1ogjhv7hhmhp.rest,REJECT
DOMAIN-SUFFIX,pbdxhfmuarvgv.space,REJECT
DOMAIN-SUFFIX,kfqmlaniiddgw.online,REJECT
DOMAIN-SUFFIX,mricm8uun4y359.rest,REJECT
DOMAIN-SUFFIX,ifvk56ft9o.com,REJECT
DOMAIN-SUFFIX,bglpxyquewvdp.site,REJECT
DOMAIN-SUFFIX,qjcjjbrocheou.online,REJECT
DOMAIN-SUFFIX,habrigzhfiddw.online,REJECT
DOMAIN-SUFFIX,qrnjezhqzokqz.website,REJECT
DOMAIN-SUFFIX,thyriswh.cyou,REJECT
DOMAIN-SUFFIX,yypmhepqhbnmc.site,REJECT
DOMAIN-SUFFIX,ainoibebedtrifler.cfd,REJECT
DOMAIN-SUFFIX,kskbpvqhwamtu.site,REJECT
DOMAIN-SUFFIX,umkchjusteppy.site,REJECT
DOMAIN-SUFFIX,badgertulip.com,REJECT
DOMAIN-SUFFIX,hubbingdjuka.qpon,REJECT
DOMAIN-SUFFIX,jqlrrfgqthdvn.online,REJECT
DOMAIN-SUFFIX,barkeepscegger.cyou,REJECT
DOMAIN-SUFFIX,brmsiboiewolm.space,REJECT
DOMAIN-SUFFIX,mkefhmdydhnck.site,REJECT
DOMAIN-SUFFIX,kmfqivcurfuku.site,REJECT
DOMAIN-SUFFIX,iddrxjthcvlng.space,REJECT
DOMAIN-SUFFIX,odpktokz.com,REJECT
DOMAIN-SUFFIX,jqosaebrqhihi.space,REJECT
DOMAIN-SUFFIX,fvvjspqqigorm.website,REJECT
DOMAIN-SUFFIX,dwzhvtvgknfjty.com,REJECT
DOMAIN-SUFFIX,ridgewaterfall.com,REJECT
DOMAIN-SUFFIX,efiktugboat.qpon,REJECT
DOMAIN-SUFFIX,canulatusker.qpon,REJECT
DOMAIN-SUFFIX,costeanpraises.qpon,REJECT
DOMAIN-SUFFIX,xoanonpacking.com,REJECT
DOMAIN-SUFFIX,vrzhovgxkeoag.space,REJECT
DOMAIN-SUFFIX,certainband.com,REJECT
DOMAIN-SUFFIX,elseshopescuir.qpon,REJECT
DOMAIN-SUFFIX,aleppobragslutayo.cyou,REJECT
DOMAIN-SUFFIX,zhppxjstwhjko.online,REJECT
DOMAIN-SUFFIX,tritonaneling.qpon,REJECT
DOMAIN-SUFFIX,bfdzzedkdfjts.site,REJECT
DOMAIN-SUFFIX,sihvwmknypeo.com,REJECT
DOMAIN-SUFFIX,xf9o6c6jnp.com,REJECT
DOMAIN-SUFFIX,fukmxaatfztwq.space,REJECT
DOMAIN-SUFFIX,unnoisyinvoked.com,REJECT
DOMAIN-SUFFIX,thqztbbekqsta.online,REJECT
DOMAIN-SUFFIX,8m96jlrph4z8xgxy1ie.cfd,REJECT
DOMAIN-SUFFIX,sissingforst.qpon,REJECT
DOMAIN-SUFFIX,kirkifyfoam.qpon,REJECT
DOMAIN-SUFFIX,irxtrbfehlpvu.online,REJECT
DOMAIN-SUFFIX,loomedhymn.qpon,REJECT
DOMAIN-SUFFIX,tupshits.com,REJECT
DOMAIN-SUFFIX,kpkxdikfmxknq.website,REJECT
DOMAIN-SUFFIX,slippykytoon.cyou,REJECT
DOMAIN-SUFFIX,g4xtww15iwrkwkkyj.rest,REJECT
DOMAIN-SUFFIX,dsxhnlgqoymrl.website,REJECT
DOMAIN-SUFFIX,gilgulberat.cfd,REJECT
DOMAIN-SUFFIX,b2rqwuqzea.com,REJECT
DOMAIN-SUFFIX,englifydecks.cfd,REJECT
DOMAIN-SUFFIX,eyvsrixrzszkl.online,REJECT
DOMAIN-SUFFIX,wangunszeguha.qpon,REJECT
DOMAIN-SUFFIX,bkqfyjvgaowoa.website,REJECT
DOMAIN-SUFFIX,upriahndtskmd.space,REJECT
DOMAIN-SUFFIX,saknmqlonwuok.site,REJECT
DOMAIN-SUFFIX,cnejpkmvsjvft.com,REJECT
DOMAIN-SUFFIX,qfqwgarymap.com,REJECT
DOMAIN-SUFFIX,wvvxvfxbbsvcp.space,REJECT
DOMAIN-SUFFIX,kwjffluyggjpn.website,REJECT
DOMAIN-SUFFIX,n25oieie5rxghc.cfd,REJECT
DOMAIN-SUFFIX,wrrsaegzdhqou.site,REJECT
DOMAIN-SUFFIX,tigroidtanger.com,REJECT
DOMAIN-SUFFIX,hvaukklmxktml.space,REJECT
DOMAIN-SUFFIX,priscanhutchie.com,REJECT
DOMAIN-SUFFIX,unedgedshank.com,REJECT
DOMAIN-SUFFIX,piannetrabat.cyou,REJECT
DOMAIN-SUFFIX,xvtqdotyggrjt.site,REJECT
DOMAIN-SUFFIX,mryntgkhlhtt.com,REJECT
DOMAIN-SUFFIX,zferbkcfprilb.space,REJECT
DOMAIN-SUFFIX,4v1wyy9r5z8xb9u.cfd,REJECT
DOMAIN-SUFFIX,rmcynkohoiugq.website,REJECT
DOMAIN-SUFFIX,rhzulyzpjvwmy.online,REJECT
DOMAIN-SUFFIX,garbcougars.cfd,REJECT
DOMAIN-SUFFIX,apzptquixoyr.com,REJECT
```
</details>

## ⚠️ 敏感域名已自动过滤（银行/支付）

**原因**：域名包含银行/支付关键词，为防止隐私泄露，不加入解密列表。

<details>
<summary>展开查看被过滤的敏感域名（共 7 个）</summary>

```
mpos-pic.helipay.com
lban.spdb.com.cn
creditcardapp.bankcomm.cn
creditcardapp.bankcomm.com
m.creditcard.ecitic.com
yunbusiness.ccb.com
webappcfg.paas.cmbchina.com
```
</details>

## JS 脚本本地化

<details>
<summary>展开查看 JS 本地化详情（共 128 条）</summary>

```
- ✅ Netpilot_adblock.js 下载成功
- ⚠️ Netpilot_adblock.js 可疑模式: \$httpClient\.(get|post|put|delete), \$task\.fetch, eval\(
- ⏭️ 12306.js 内容未变，跳过写入
- ⏭️ caixinads.js 内容未变，跳过写入
- ⏭️ fly.js 内容未变，跳过写入
- ⏭️ startup.js 内容未变，跳过写入
- ⏭️ jd_json.js 内容未变，跳过写入
- ⏭️ coolapk.js 内容未变，跳过写入
- ⏭️ shunfeng_json.js 内容未变，跳过写入
- ⏭️ stay.js 内容未变，跳过写入
- ⏭️ UnblockURLinWeChat.js 内容未变，跳过写入
- ⚠️ UnblockURLinWeChat.js 可疑模式: \$httpClient\.(get|post|put|delete), \$task\.fetch
- ⏭️ xiaohongshu.js 内容未变，跳过写入
- ⚠️ xiaohongshu.js 可疑模式: \$httpClient\.(get|post|put|delete), \$task\.fetch, pasteboard
- ⏭️ wyres.js 内容未变，跳过写入
- ⏭️ xmApp.js 内容未变，跳过写入
- ⏭️ rrtv_json.js 内容未变，跳过写入
- ⚠️ rrtv_json.js 可疑模式: \$httpClient\.(get|post|put|delete), \$task\.fetch, \$persistentStore\.write
- ⏭️ smzdm_json.js 内容未变，跳过写入
- ⏭️ picc_ads.js 内容未变，跳过写入
- ⏭️ ccblife.js 内容未变，跳过写入
- ⏭️ zhangshanggongjiao.js 内容未变，跳过写入
- ⏭️ zheye.min.js 内容未变，跳过写入
- ⚠️ zheye.min.js 可疑模式: \$task\.fetch, \$persistentStore\.write, \$prefs\.setValueForKey
- ⏭️ usmile.js 内容未变，跳过写入
- ⏭️ flyert.js 内容未变，跳过写入
- ⏭️ ltsst-ad.js 内容未变，跳过写入
- ⏭️ 123pan.js 内容未变，跳过写入
- ⚠️ 123pan.js 可疑模式: \$httpClient\.(get|post|put|delete), \$task\.fetch, \$persistentStore\.write
- ⏭️ caiyun_json.js 内容未变，跳过写入
- ⏭️ weibo_json.js 内容未变，跳过写入
- ⚠️ weibo_json.js 可疑模式: eval\(
- ⏭️ weibo_search_topic.json 内容未变，跳过写入
- ⏭️ weibo_search_info.json 内容未变，跳过写入
- ⏭️ kuwo.js 内容未变，跳过写入
- ⏭️ ddxq.js 内容未变，跳过写入
- ⏭️ smzdm_ads.js 内容未变，跳过写入
- ⏭️ Smzdm.js 内容未变，跳过写入
- ⏭️ cnftp.js 内容未变，跳过写入
- ⏭️ wechatApplet.js 内容未变，跳过写入
- ⏭️ fenbi.js 内容未变，跳过写入
- ⏭️ blued.js 内容未变，跳过写入
- ⏭️ bing.js 内容未变，跳过写入
- ⏭️ didiAds.js 内容未变，跳过写入
- ⏭️ soul_ads.js 内容未变，跳过写入
- ⚠️ soul_ads.js 可疑模式: \$httpClient\.(get|post|put|delete), \$task\.fetch, pasteboard
- ⏭️ myBlockAds.js 内容未变，跳过写入
- ⏭️ quark.js 内容未变，跳过写入
- ⏭️ pixivAds.js 内容未变，跳过写入
- ⏭️ baidumap.js 内容未变，跳过写入
- ⚠️ baidumap.js 可疑模式: eval\(
- ⏭️ ithome.js 内容未变，跳过写入
- ⏭️ xiaotucc.js 内容未变，跳过写入
- ⏭️ mafengwo.js 内容未变，跳过写入
- ⏭️ qidian.js 内容未变，跳过写入
- ⏭️ pupumarket.js 内容未变，跳过写入
- ⏭️ QuDa.js 内容未变，跳过写入
- ⏭️ netease.adblock.js 内容未变，跳过写入
- ⏭️ dianping.js 内容未变，跳过写入
- ⏭️ reddit.js 内容未变，跳过写入
- ⏭️ caixinAd.js 内容未变，跳过写入
- ⏭️ alicdn.js 内容未变，跳过写入
- ⏭️ miguvideo_ads.js 内容未变，跳过写入
- ⚠️ miguvideo_ads.js 可疑模式: \$httpClient\.(get|post|put|delete), \$task\.fetch, pasteboard
- ⏭️ dict-youdao-ad.js 内容未变，跳过写入
- ⏭️ 51job.js 内容未变，跳过写入
- ⏭️ mdb.js 内容未变，跳过写入
- ⏭️ cainiao.js 内容未变，跳过写入
- ⏭️ baishitv.js 内容未变，跳过写入
- ⏭️ zhuanzhuan.js 内容未变，跳过写入
- ⏭️ vgtime.js 内容未变，跳过写入
- ⏭️ foliday.js 内容未变，跳过写入
- ⏭️ dict.js 内容未变，跳过写入
- ⏭️ zhihu_openads.js 内容未变，跳过写入
- ⏭️ yx.js 内容未变，跳过写入
- ⏭️ 51card.js 内容未变，跳过写入
- ⏭️ soda.js 内容未变，跳过写入
- ⏭️ jingxiAd.js 内容未变，跳过写入
- ⏭️ keep.js 内容未变，跳过写入
- ⏭️ keepStyle.js 内容未变，跳过写入
- ⏭️ BahamutAnimeAds.js 内容未变，跳过写入
- ⚠️ BahamutAnimeAds.js 可疑模式: \$httpClient\.(get|post|put|delete), \$task\.fetch
- ⏭️ freshippo.js 内容未变，跳过写入
- ✅ redbook.ads.js 下载成功
- ⏭️ cainiao_json.js 内容未变，跳过写入
- ⏭️ 555Ad.js 内容未变，跳过写入
- ⏭️ xjsp.js 内容未变，跳过写入
- ⏭️ iqiyi_open_ads.js 内容未变，跳过写入
- ⏭️ ximalaya_json.js 内容未变，跳过写入
- ⏭️ amap.js 内容未变，跳过写入
- ⏭️ ahfs.js 内容未变，跳过写入
- ⏭️ tieba-proto.js 内容未变，跳过写入
- ⏭️ tieba-json.js 内容未变，跳过写入
- ⏭️ qq-news.js 内容未变，跳过写入
- ⏭️ tuhu.js 内容未变，跳过写入
- ⏭️ qmai.js 内容未变，跳过写入
- ⏭️ zhihu.js 内容未变，跳过写入
- ⏭️ wnbz.js 内容未变，跳过写入
- ⏭️ huifutianxia_ads.js 内容未变，跳过写入
- ⏭️ adrive.js 内容未变，跳过写入
- ⏭️ cmschina.js 内容未变，跳过写入
- ⏭️ lawson.js 内容未变，跳过写入
- ⏭️ PupuSplashAds.js 内容未变，跳过写入
- ⏭️ goofish.js 内容未变，跳过写入
- ⏭️ meiyou_ads.js 内容未变，跳过写入
- ⚠️ meiyou_ads.js 可疑模式: \$httpClient\.(get|post|put|delete), \$task\.fetch, pasteboard
- ⏭️ dianyinglieshou.js 内容未变，跳过写入
- ⏭️ jingdong.js 内容未变，跳过写入
- ⏭️ bohe_ads.js 内容未变，跳过写入
- ⏭️ mlxx.js 内容未变，跳过写入
- ⏭️ maimai_ads.js 内容未变，跳过写入
- ⏭️ adsense.js 内容未变，跳过写入
- ⏭️ umetrip_ads.js 内容未变，跳过写入
- ⏭️ amdc.js 内容未变，跳过写入
- ⏭️ applet.js 内容未变，跳过写入
- ⏭️ 12306.js 内容未变，跳过写入
- ⏭️ caixinads.js 内容未变，跳过写入
- ⏭️ fly.js 内容未变，跳过写入
- ⏭️ startup.js 内容未变，跳过写入
- ⏭️ jd_json.js 内容未变，跳过写入
- ⏭️ coolapk.js 内容未变，跳过写入
- ⏭️ shunfeng_json.js 内容未变，跳过写入
- ⏭️ stay.js 内容未变，跳过写入
- ⏭️ UnblockURLinWeChat.js 内容未变，跳过写入
- ⚠️ UnblockURLinWeChat.js 可疑模式: \$httpClient\.(get|post|put|delete), \$task\.fetch
- ❌ xiaohongshu.js 下载失败，已丢弃引用（下次会重试）: 404 Client Error: Not Found for url: https://github.com/ddgksf2013/Scripts/raw/master/xiaohongshu.js
- ❌ xiaohongshu.js 下载失败，已丢弃引用（下次会重试）: 404 Client Error: Not Found for url: https://github.com/ddgksf2013/Scripts/raw/master/xiaohongshu.js
- ❌ xiaohongshu.js 下载失败，已丢弃引用（下次会重试）: 404 Client Error: Not Found for url: https://github.com/ddgksf2013/Scripts/raw/master/xiaohongshu.js
```
</details>

🩺 Shield模块: 健康检查通过（246620 条规则，11.4 MB）

✅ Shield 模块已写入，代理 27639 条，去广告 218981 条

## 🩺 规则源健康状态

<details>
<summary>展开查看各上游源健康状态（共 8 个源）</summary>

- ✅ https://raw.githubusercontent.com/GMOogway/shadowrocket-rules/master/sr_direct_list.module
  - 成功 121 次，失败 0 次，连续失败 0 次
  - 最近成功: 2026-10-25 16:56:00
  - 最近失败: 无 

- ✅ https://raw.githubusercontent.com/GMOogway/shadowrocket-rules/master/sr_proxy_list.module
  - 成功 121 次，失败 0 次，连续失败 0 次
  - 最近成功: 2026-10-25 16:56:15
  - 最近失败: 无 

- ✅ https://raw.githubusercontent.com/LOWERTOP/Shadowrocket-First/main/Talkatone.sgmodule
  - 成功 121 次，失败 0 次，连续失败 0 次
  - 最近成功: 2026-10-25 16:56:15
  - 最近失败: 无 

- ✅ https://raw.githubusercontent.com/huijingfei/Shadowrocket-Rules/refs/heads/main/sr_app_ad.module
  - 成功 121 次，失败 0 次，连续失败 0 次
  - 最近成功: 2026-10-25 16:56:15
  - 最近失败: 无 

- ✅ https://raw.githubusercontent.com/deezertidal/shadowrocket-rules/refs/heads/main/modules/startingad.module
  - 成功 121 次，失败 0 次，连续失败 0 次
  - 最近成功: 2026-10-25 16:56:16
  - 最近失败: 无 

- ✅ https://raw.githubusercontent.com/GMOogway/shadowrocket-rules/master/sr_reject_list.module
  - 成功 121 次，失败 0 次，连续失败 0 次
  - 最近成功: 2026-10-25 16:56:17
  - 最近失败: 无 

- ✅ https://raw.githubusercontent.com/Unwhimsical/NetPilot/refs/heads/main/modules/%E6%B5%8B%E8%AF%95.module
  - 成功 121 次，失败 0 次，连续失败 0 次
  - 最近成功: 2026-10-25 16:56:17
  - 最近失败: 无 

- ✅ https://raw.githubusercontent.com/LOWERTOP/Shadowrocket-First/main/TalkatoneAntiAds.list
  - 成功 121 次，失败 0 次，连续失败 0 次
  - 最近成功: 2026-10-25 16:56:17
  - 最近失败: 无 

</details>

## 🔒 DNS 泄漏风险检测

### 🔴 高风险（229 条）

<details>
<summary>展开查看高风险详情</summary>

- **直连海外域名**
  直连规则包含海外域名: DOMAIN,adcdownload.apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **直连海外域名**
  直连规则包含海外域名: DOMAIN,adcdownload.apple.com.akadns.net,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **直连海外域名**
  直连规则包含海外域名: DOMAIN,amp-api-edge-lb-cn.itunes-apple.com.akadns.net,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **直连海外域名**
  直连规则包含海外域名: DOMAIN,amp-api-edge-lb.itunes-apple.com.akadns.net,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **直连海外域名**
  直连规则包含海外域名: DOMAIN,amp-api-edge.apps.apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **直连海外域名**
  直连规则包含海外域名: DOMAIN,amp-api-edge.music.apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **直连海外域名**
  直连规则包含海外域名: DOMAIN,amp-api-search-edge.apps.apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **直连海外域名**
  直连规则包含海外域名: DOMAIN,amp-api-updates.apps.apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **直连海外域名**
  直连规则包含海外域名: DOMAIN,amp-api.apps.apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **直连海外域名**
  直连规则包含海外域名: DOMAIN,amp-api.media.apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **直连海外域名**
  直连规则包含海外域名: DOMAIN,amp-api.music.apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **直连海外域名**
  直连规则包含海外域名: DOMAIN,amp-api.podcasts.apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **直连海外域名**
  直连规则包含海外域名: DOMAIN,aod-ssl.itunes.apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **直连海外域名**
  直连规则包含海外域名: DOMAIN,aod.itunes.apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **直连海外域名**
  直连规则包含海外域名: DOMAIN,api-edge.apps.apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **直连海外域名**
  直连规则包含海外域名: DOMAIN,app-site-association.cdn-apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **直连海外域名**
  直连规则包含海外域名: DOMAIN,appldnld.apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **直连海外域名**
  直连规则包含海外域名: DOMAIN,appleid.cdn-apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **直连海外域名**
  直连规则包含海外域名: DOMAIN,apptrailers.itunes.apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **直连海外域名**
  直连规则包含海外域名: DOMAIN,bag-cdn.itunes-apple.com.akadns.net,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **直连海外域名**
  直连规则包含海外域名: DOMAIN,bag.itunes.apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **直连海外域名**
  直连规则包含海外域名: DOMAIN,bookkeeper.itunes.apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **直连海外域名**
  直连规则包含海外域名: DOMAIN,cdn-cn.apple-mapkit.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **直连海外域名**
  直连规则包含海外域名: DOMAIN,cdn-cn1.apple-mapkit.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **直连海外域名**
  直连规则包含海外域名: DOMAIN,cdn-cn2.apple-mapkit.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **直连海外域名**
  直连规则包含海外域名: DOMAIN,cdn-cn3.apple-mapkit.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **直连海外域名**
  直连规则包含海外域名: DOMAIN,cdn-cn4.apple-mapkit.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **直连海外域名**
  直连规则包含海外域名: DOMAIN,cdn.apple-mapkit.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **直连海外域名**
  直连规则包含海外域名: DOMAIN,cdn1.apple-mapkit.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **直连海外域名**
  直连规则包含海外域名: DOMAIN,cdn2.apple-mapkit.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **直连海外域名**
  直连规则包含海外域名: DOMAIN,cdn3.apple-mapkit.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **直连海外域名**
  直连规则包含海外域名: DOMAIN,cdn4.apple-mapkit.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **直连海外域名**
  直连规则包含海外域名: DOMAIN,cds.apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **直连海外域名**
  直连规则包含海外域名: DOMAIN,cds.apple.com.akadns.net,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **直连海外域名**
  直连规则包含海外域名: DOMAIN,cdsassets.apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **直连海外域名**
  直连规则包含海外域名: DOMAIN,certs-lb.apple.com.akadns.net,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **直连海外域名**
  直连规则包含海外域名: DOMAIN,certs.apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **直连海外域名**
  直连规则包含海外域名: DOMAIN,cl1-cdn.origin-apple.com.akadns.net,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **直连海外域名**
  直连规则包含海外域名: DOMAIN,cl1.apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **直连海外域名**
  直连规则包含海外域名: DOMAIN,cl2-cdn.origin-apple.com.akadns.net,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **直连海外域名**
  直连规则包含海外域名: DOMAIN,cl2-cn.apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **直连海外域名**
  直连规则包含海外域名: DOMAIN,cl2.apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **直连海外域名**
  直连规则包含海外域名: DOMAIN,cl2.apple.com.edgekey.net.globalredir.akadns.net,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **直连海外域名**
  直连规则包含海外域名: DOMAIN,cl3-cdn.origin-apple.com.akadns.net,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **直连海外域名**
  直连规则包含海外域名: DOMAIN,cl3.apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **直连海外域名**
  直连规则包含海外域名: DOMAIN,cl4-cdn.origin-apple.com.akadns.net,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **直连海外域名**
  直连规则包含海外域名: DOMAIN,cl4-cn.apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **直连海外域名**
  直连规则包含海外域名: DOMAIN,cl4.apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **直连海外域名**
  直连规则包含海外域名: DOMAIN,cl5-cdn.origin-apple.com.akadns.net,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **直连海外域名**
  直连规则包含海外域名: DOMAIN,cl5.apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **直连海外域名**
  直连规则包含海外域名: DOMAIN,client-api.itunes.apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **直连海外域名**
  直连规则包含海外域名: DOMAIN,clientflow.apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **直连海外域名**
  直连规则包含海外域名: DOMAIN,clientflow.apple.com.akadns.net,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **直连海外域名**
  直连规则包含海外域名: DOMAIN,cma.itunes.apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **直连海外域名**
  直连规则包含海外域名: DOMAIN,cn-smp-paymentservices.apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **直连海外域名**
  直连规则包含海外域名: DOMAIN,communities.apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **直连海外域名**
  直连规则包含海外域名: DOMAIN,configuration.apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **直连海外域名**
  直连规则包含海外域名: DOMAIN,configuration.apple.com.akadns.net,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **直连海外域名**
  直连规则包含海外域名: DOMAIN,crl-lb.apple.com.akadns.net,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **直连海外域名**
  直连规则包含海外域名: DOMAIN,crl.apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **直连海外域名**
  直连规则包含海外域名: DOMAIN,cstat.apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **直连海外域名**
  直连规则包含海外域名: DOMAIN,cstat.cdn-apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **直连海外域名**
  直连规则包含海外域名: DOMAIN,dd-cdn.origin-apple.com.akadns.net,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **直连海外域名**
  直连规则包含海外域名: DOMAIN,dejavu.apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **直连海外域名**
  直连规则包含海外域名: DOMAIN,devimages-cdn.apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **直连海外域名**
  直连规则包含海外域名: DOMAIN,devstreaming-cdn.apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **直连海外域名**
  直连规则包含海外域名: DOMAIN,discussionschinese.apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **直连海外域名**
  直连规则包含海外域名: DOMAIN,download.developer.apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **直连海外域名**
  直连规则包含海外域名: DOMAIN,downloaddispatch.itunes.apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **直连海外域名**
  直连规则包含海外域名: DOMAIN,entitlements-edge.itunes.apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **直连海外域名**
  直连规则包含海外域名: DOMAIN,experiments.apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **直连海外域名**
  直连规则包含海外域名: DOMAIN,fides-pol.apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **直连海外域名**
  直连规则包含海外域名: DOMAIN,fpinit.itunes.apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **直连海外域名**
  直连规则包含海外域名: DOMAIN,gsp10-ssl-cn.ls.apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **直连海外域名**
  直连规则包含海外域名: DOMAIN,gsp11-cn.ls.apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **直连海外域名**
  直连规则包含海外域名: DOMAIN,gsp12-cn.ls.apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **直连海外域名**
  直连规则包含海外域名: DOMAIN,gsp13-cn.ls.apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **直连海外域名**
  直连规则包含海外域名: DOMAIN,gsp4-cn.ls.apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **直连海外域名**
  直连规则包含海外域名: DOMAIN,gsp4-cn.ls.apple.com.edgekey.net.globalredir.akadns.net,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **直连海外域名**
  直连规则包含海外域名: DOMAIN,gsp5-cn.ls.apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **直连海外域名**
  直连规则包含海外域名: DOMAIN,gsp85-cn-ssl.ls.apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **直连海外域名**
  直连规则包含海外域名: DOMAIN,gspe11-2-cn-ssl.ls.apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **直连海外域名**
  直连规则包含海外域名: DOMAIN,gspe12-cn-ssl.ls.apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **直连海外域名**
  直连规则包含海外域名: DOMAIN,gspe19-2-cn-ssl.ls-apple.com.akadns.net,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **直连海外域名**
  直连规则包含海外域名: DOMAIN,gspe19-2-cn-ssl.ls.apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **直连海外域名**
  直连规则包含海外域名: DOMAIN,gspe19-cn-ssl.ls.apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **直连海外域名**
  直连规则包含海外域名: DOMAIN,gspe19-cn.ls-apple.com.akadns.net,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **直连海外域名**
  直连规则包含海外域名: DOMAIN,gspe19-cn.ls.apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **直连海外域名**
  直连规则包含海外域名: DOMAIN,gspe21-ssl.ls.apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **直连海外域名**
  直连规则包含海外域名: DOMAIN,gspe35-ssl.ls.apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **直连海外域名**
  直连规则包含海外域名: DOMAIN,gspe79-cn-ssl.ls.apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **直连海外域名**
  直连规则包含海外域名: DOMAIN,gspe85-cn-ssl.ls.apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **直连海外域名**
  直连规则包含海外域名: DOMAIN,guzzoni-apple-com.v.aaplimg.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **直连海外域名**
  直连规则包含海外域名: DOMAIN,guzzoni.apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **直连海外域名**
  直连规则包含海外域名: DOMAIN,guzzoni.smoot.apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **直连海外域名**
  直连规则包含海外域名: DOMAIN,images.apple.com.edgekey.net.globalredir.akadns.net,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **直连海外域名**
  直连规则包含海外域名: DOMAIN,inappcheck-cn.itunes-apple.com.akadns.net,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **直连海外域名**
  直连规则包含海外域名: DOMAIN,inappcheck-lb.itunes-apple.com.akadns.net,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **直连海外域名**
  直连规则包含海外域名: DOMAIN,inappcheck.itunes.apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **直连海外域名**
  直连规则包含海外域名: DOMAIN,init-kt.apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **直连海外域名**
  直连规则包含海外域名: DOMAIN,init-p01md-lb.push-apple.com.akadns.net,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **直连海外域名**
  直连规则包含海外域名: DOMAIN,init-p01md.apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **直连海外域名**
  直连规则包含海外域名: DOMAIN,init-p01st-lb.push-apple.com.akadns.net,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **直连海外域名**
  直连规则包含海外域名: DOMAIN,init-p01st.push.apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **直连海外域名**
  直连规则包含海外域名: DOMAIN,init-s01st-lb.push-apple.com.akadns.net,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **直连海外域名**
  直连规则包含海外域名: DOMAIN,init-s01st.push.apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **直连海外域名**
  直连规则包含海外域名: DOMAIN,init.ess.apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **直连海外域名**
  直连规则包含海外域名: DOMAIN,init.gc-lb.apple.com.akadns.net,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **直连海外域名**
  直连规则包含海外域名: DOMAIN,init.gc.apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **直连海外域名**
  直连规则包含海外域名: DOMAIN,init.itunes.apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **直连海外域名**
  直连规则包含海外域名: DOMAIN,iosapps.itunes.apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **直连海外域名**
  直连规则包含海外域名: DOMAIN,ipcdn.apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **直连海外域名**
  直连规则包含海外域名: DOMAIN,iphone-ld.apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **直连海外域名**
  直连规则包含海外域名: DOMAIN,iphone-ld.origin-apple.com.akadns.net,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **直连海外域名**
  直连规则包含海外域名: DOMAIN,is-ssl.mzstatic.com-cn-lb.itunes-apple.com.akadns.net,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **直连海外域名**
  直连规则包含海外域名: DOMAIN,itunes-apple.com.akadns.net,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **直连海外域名**
  直连规则包含海外域名: DOMAIN,itunes.apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **直连海外域名**
  直连规则包含海外域名: DOMAIN,itunesconnect.apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **直连海外域名**
  直连规则包含海外域名: DOMAIN,js-cdn.music.apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **直连海外域名**
  直连规则包含海外域名: DOMAIN,km.support.apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **直连海外域名**
  直连规则包含海外域名: DOMAIN,maps.apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **直连海外域名**
  直连规则包含海外域名: DOMAIN,mensura.cdn-apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **直连海外域名**
  直连规则包含海外域名: DOMAIN,mesu-cdn.apple.com.akadns.net,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **直连海外域名**
  直连规则包含海外域名: DOMAIN,mesu-china.apple.com.akadns.net,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **直连海外域名**
  直连规则包含海外域名: DOMAIN,mesu.apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **直连海外域名**
  直连规则包含海外域名: DOMAIN,misc-assets.itunes.apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **直连海外域名**
  直连规则包含海外域名: DOMAIN,ml.cdn-apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **直连海外域名**
  直连规则包含海外域名: DOMAIN,music.apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **直连海外域名**
  直连规则包含海外域名: DOMAIN,musicstatus.music.apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **直连海外域名**
  直连规则包含海外域名: DOMAIN,mvod.itunes.apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **直连海外域名**
  直连规则包含海外域名: DOMAIN,myapp.itunes.apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **直连海外域名**
  直连规则包含海外域名: DOMAIN,np-edge.itunes.apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **直连海外域名**
  直连规则包含海外域名: DOMAIN,ocsp.apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **直连海外域名**
  直连规则包含海外域名: DOMAIN,ocsp2.apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **直连海外域名**
  直连规则包含海外域名: DOMAIN,oscdn.apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **直连海外域名**
  直连规则包含海外域名: DOMAIN,oscdn.origin-apple.com.akadns.net,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **直连海外域名**
  直连规则包含海外域名: DOMAIN,osxapps.itunes.apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **直连海外域名**
  直连规则包含海外域名: DOMAIN,pancake.apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **直连海外域名**
  直连规则包含海外域名: DOMAIN,pba0.apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **直连海外域名**
  直连规则包含海外域名: DOMAIN,pd-nk.itunes.apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **直连海外域名**
  直连规则包含海外域名: DOMAIN,pd.itunes.apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **直连海外域名**
  直连规则包含海外域名: DOMAIN,play-edge.itunes.apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **直连海外域名**
  直连规则包含海外域名: DOMAIN,play.itunes.apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **直连海外域名**
  直连规则包含海外域名: DOMAIN,play.music.apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **直连海外域名**
  直连规则包含海外域名: DOMAIN,podcasts.apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **直连海外域名**
  直连规则包含海外域名: DOMAIN,podcasts.itunes.apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **直连海外域名**
  直连规则包含海外域名: DOMAIN,probe.siri.apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **直连海外域名**
  直连规则包含海外域名: DOMAIN,prod-support.apple-support.akadns.net,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **直连海外域名**
  直连规则包含海外域名: DOMAIN,publicassets.cdn-apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **直连海外域名**
  直连规则包含海外域名: DOMAIN,se-edge.itunes.apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **直连海外域名**
  直连规则包含海外域名: DOMAIN,se2.itunes.apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **直连海外域名**
  直连规则包含海外域名: DOMAIN,search.itunes.apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **直连海外域名**
  直连规则包含海外域名: DOMAIN,seed-sequoia.siri.apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **直连海外域名**
  直连规则包含海外域名: DOMAIN,seed-swallow.siri.apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **直连海外域名**
  直连规则包含海外域名: DOMAIN,seed.siri.apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **直连海外域名**
  直连规则包含海外域名: DOMAIN,sequoia.apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **直连海外域名**
  直连规则包含海外域名: DOMAIN,sf-api-token-service.itunes.apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **直连海外域名**
  直连规则包含海外域名: DOMAIN,sh-pod2-smp-device.apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **直连海外域名**
  直连规则包含海外域名: DOMAIN,shazam-insights.cdn-apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **直连海外域名**
  直连规则包含海外域名: DOMAIN,smp-device-content.apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **直连海外域名**
  直连规则包含海外域名: DOMAIN,sp.itunes.apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **直连海外域名**
  直连规则包含海外域名: DOMAIN,speedysub.music.apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **直连海外域名**
  直连规则包含海外域名: DOMAIN,static.gc.apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **直连海外域名**
  直连规则包含海外域名: DOMAIN,stocks-sparkline-lb.apple.com.akadns.net,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **直连海外域名**
  直连规则包含海外域名: DOMAIN,stocks-sparkline.apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **直连海外域名**
  直连规则包含海外域名: DOMAIN,store.apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **直连海外域名**
  直连规则包含海外域名: DOMAIN,store.apple.com.edgekey.net,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **直连海外域名**
  直连规则包含海外域名: DOMAIN,store.apple.com.edgekey.net.globalredir.akadns.net,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **直连海外域名**
  直连规则包含海外域名: DOMAIN,store.storeimages.apple.com.akadns.net,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **直连海外域名**
  直连规则包含海外域名: DOMAIN,store.storeimages.cdn-apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **直连海外域名**
  直连规则包含海外域名: DOMAIN,streamingaudio.itunes.apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **直连海外域名**
  直连规则包含海外域名: DOMAIN,su.itunes.apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **直连海外域名**
  直连规则包含海外域名: DOMAIN,support-china.apple-support.akadns.net,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **直连海外域名**
  直连规则包含海外域名: DOMAIN,support.apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **直连海外域名**
  直连规则包含海外域名: DOMAIN,swallow-apple-com.v.aaplimg.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **直连海外域名**
  直连规则包含海外域名: DOMAIN,swallow.apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **直连海外域名**
  直连规则包含海外域名: DOMAIN,swcatalog-cdn.apple.com.akadns.net,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **直连海外域名**
  直连规则包含海外域名: DOMAIN,swcatalog.apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **直连海外域名**
  直连规则包含海外域名: DOMAIN,swcdn.apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **直连海外域名**
  直连规则包含海外域名: DOMAIN,swdist.apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **直连海外域名**
  直连规则包含海外域名: DOMAIN,swdist.apple.com.akadns.net,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **直连海外域名**
  直连规则包含海外域名: DOMAIN,swscan-cdn.apple.com.akadns.net,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **直连海外域名**
  直连规则包含海外域名: DOMAIN,swscan.apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **直连海外域名**
  直连规则包含海外域名: DOMAIN,sylvan.apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **直连海外域名**
  直连规则包含海外域名: DOMAIN,sync.itunes.apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **直连海外域名**
  直连规则包含海外域名: DOMAIN,tf-feedback.itunes.apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **直连海外域名**
  直连规则包含海外域名: DOMAIN,tj-pod1-smp-device.apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **直连海外域名**
  直连规则包含海外域名: DOMAIN,tj-pod2-smp-device.apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **直连海外域名**
  直连规则包含海外域名: DOMAIN,tj-pod3-smp-device.apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **直连海外域名**
  直连规则包含海外域名: DOMAIN,universal-activity-service.itunes.apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **直连海外域名**
  直连规则包含海外域名: DOMAIN,updates-http.cdn-apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **直连海外域名**
  直连规则包含海外域名: DOMAIN,updates-http.cdn-apple.com.akadns.net,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **直连海外域名**
  直连规则包含海外域名: DOMAIN,updates.cdn-apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **直连海外域名**
  直连规则包含海外域名: DOMAIN,upp.itunes.apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **直连海外域名**
  直连规则包含海外域名: DOMAIN,valid.apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **直连海外域名**
  直连规则包含海外域名: DOMAIN,valid.origin-apple.com.akadns.net,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **直连海外域名**
  直连规则包含海外域名: DOMAIN,weather-data.apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **直连海外域名**
  直连规则包含海外域名: DOMAIN,weather-data.apple.com.akadns.net,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **直连海外域名**
  直连规则包含海外域名: DOMAIN,weather-map.apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **直连海外域名**
  直连规则包含海外域名: DOMAIN,weather-map2.apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **直连海外域名**
  直连规则包含海外域名: DOMAIN,weatherkit.apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **直连海外域名**
  直连规则包含海外域名: DOMAIN,www.apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **直连海外域名**
  直连规则包含海外域名: DOMAIN,www.apple.com.edgekey.net.globalredir.akadns.net,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **直连海外域名**
  直连规则包含海外域名: DOMAIN,www.support.apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **直连海外域名**
  直连规则包含海外域名: DOMAIN,xp.apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **直连海外域名**
  直连规则包含海外域名: DOMAIN-SUFFIX,apple-corer.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **直连海外域名**
  直连规则包含海外域名: DOMAIN-SUFFIX,apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **直连海外域名**
  直连规则包含海外域名: DOMAIN-SUFFIX,apple110.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **直连海外域名**
  直连规则包含海外域名: DOMAIN-SUFFIX,apple114.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **直连海外域名**
  直连规则包含海外域名: DOMAIN-SUFFIX,apple17.club,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **直连海外域名**
  直连规则包含海外域名: DOMAIN-SUFFIX,apple4.us,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **直连海外域名**
  直连规则包含海外域名: DOMAIN-SUFFIX,apple523.club,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **直连海外域名**
  直连规则包含海外域名: DOMAIN-SUFFIX,apple886.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **直连海外域名**
  直连规则包含海外域名: DOMAIN-SUFFIX,applebl.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **直连海外域名**
  直连规则包含海外域名: DOMAIN-SUFFIX,applejp.cloud,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **直连海外域名**
  直连规则包含海外域名: DOMAIN-SUFFIX,applemei.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **直连海外域名**
  直连规则包含海外域名: DOMAIN-SUFFIX,applepopo.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **直连海外域名**
  直连规则包含海外域名: DOMAIN-SUFFIX,appletuan.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **直连海外域名**
  直连规则包含海外域名: DOMAIN-SUFFIX,applex.net,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **直连海外域名**
  直连规则包含海外域名: DOMAIN-SUFFIX,applezhang.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **直连海外域名**
  直连规则包含海外域名: DOMAIN-SUFFIX,badapple.pro,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **直连海外域名**
  直连规则包含海外域名: DOMAIN-SUFFIX,china-applefix.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **直连海外域名**
  直连规则包含海外域名: DOMAIN-SUFFIX,iappler.net,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **直连海外域名**
  直连规则包含海外域名: DOMAIN-SUFFIX,nnpurapple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **直连海外域名**
  直连规则包含海外域名: DOMAIN-SUFFIX,red-apple.net,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **直连海外域名**
  直连规则包含海外域名: DOMAIN-SUFFIX,redapplechina.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **直连海外域名**
  直连规则包含海外域名: DOMAIN-SUFFIX,simapple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **直连海外域名**
  直连规则包含海外域名: DOMAIN-SUFFIX,svip5-applefix.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **直连海外域名**
  直连规则包含海外域名: DOMAIN-SUFFIX,tuiapple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

</details>

### 🟡 中风险（8 条）

<details>
<summary>展开查看中风险详情</summary>

- **代理规则使用 no-resolve**
  代理规则带 no-resolve: IP-CIDR,104.18.0.0/15,PROXY,no-resolve，该域名的 DNS 将在本地解析，可能泄漏。

- **代理规则使用 no-resolve**
  代理规则带 no-resolve: IP-CIDR,143.198.200.27/32,PROXY,no-resolve，该域名的 DNS 将在本地解析，可能泄漏。

- **代理规则使用 no-resolve**
  代理规则带 no-resolve: IP-CIDR,159.89.204.203/32,PROXY,no-resolve，该域名的 DNS 将在本地解析，可能泄漏。

- **代理规则使用 no-resolve**
  代理规则带 no-resolve: IP-CIDR,172.64.0.0/13,PROXY,no-resolve，该域名的 DNS 将在本地解析，可能泄漏。

- **代理规则使用 no-resolve**
  代理规则带 no-resolve: IP-CIDR,24.199.123.28/32,PROXY,no-resolve，该域名的 DNS 将在本地解析，可能泄漏。

- **代理规则使用 no-resolve**
  代理规则带 no-resolve: IP-CIDR,45.76.214.191/32,PROXY,no-resolve，该域名的 DNS 将在本地解析，可能泄漏。

- **代理规则使用 no-resolve**
  代理规则带 no-resolve: IP-CIDR,64.23.132.171/32,PROXY,no-resolve，该域名的 DNS 将在本地解析，可能泄漏。

- **dns-direct-system 开启**
  主配置中 dns-direct-system = true，直连域名将使用系统 DNS，可能造成 DNS 泄漏。建议改为 false。

</details>



---
