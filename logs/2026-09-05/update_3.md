# 更新日志 2026-09-05

**运行时间**: 2026-09-05 15:05:15 北京时间

---

## 直连模块

### 🔍 过滤海外/强制代理直连规则（共 930 条）

**原因**：规则域名匹配海外黑名单关键词，或属于强制代理域名（如定位模块）。

<details>
<summary>展开查看被过滤规则及命中关键词</summary>

```
- DOMAIN-SUFFIX,fishmobi.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,hmchina.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,gogofly.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,iflygse.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,dockerone.com,DIRECT  (命中: docker)
- DOMAIN-SUFFIX,ddwhm.com,DIRECT  (命中: hm)
- DOMAIN,collaborate.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,megasig.com,DIRECT  (命中: mega)
- URL-REGEX,"^https?:\/\/.+\.awsdns-cn-[0-9][0-9]\.(biz|com|net|top).*$",DIRECT  (命中: aws)
- DOMAIN-SUFFIX,zhmold.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,3richman.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,qdhmsoft.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,awsdns-cn-11.com,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,jhm2012.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,sun-wish.com,DIRECT  (命中: wish)
- DOMAIN,myvs.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,googleppy.com,DIRECT  (命中: google)
- DOMAIN-SUFFIX,itacademyuat.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,hmly666.cc,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,chmed.net,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,seersecret.com,DIRECT  (命中: ecr)
- DOMAIN-SUFFIX,lex.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,googleplus.party,DIRECT  (命中: google)
- DOMAIN-SUFFIX,googleyixia.com,DIRECT  (命中: google)
- DOMAIN,storecorefulfillment.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,hmplay.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,acrossmetals.com,DIRECT  (命中: acr)
- DOMAIN-SUFFIX,awsdns-cn-27.com,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,hmzhtc.cc,DIRECT  (命中: hm)
- URL-REGEX,"^https?:\/\/.+-mihayo\.akamaized\.net.*$",DIRECT  (命中: akamai)
- DOMAIN-SUFFIX,zgxhm.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,bghmj.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,alltechmed.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,szpowerfly.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,shms-expo.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,t-firefly.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,mecru.com,DIRECT  (命中: ecr)
- DOMAIN-SUFFIX,cloudflare.fun,DIRECT  (命中: cloudflare)
- DOMAIN-SUFFIX,awsdns-cn-07.biz,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,eflycloud.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,whmylike.cc,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,htyhm.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,awsdns-cn-39.net,DIRECT  (命中: aws)
- DOMAIN,osrelease.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,awsdns-cn-40.com,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,chinacreator.com,DIRECT  (命中: acr)
- DOMAIN-SUFFIX,nnpml.com,DIRECT  (命中: npm)
- DOMAIN-SUFFIX,ahmif.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,googlevoice.org,DIRECT  (命中: google)
- DOMAIN-SUFFIX,vultrvps.com,DIRECT  (命中: vultr)
- DOMAIN-SUFFIX,edgeone-browser-rendering.com,DIRECT  (命中: render)
- DOMAIN-SUFFIX,awsdns-cn-11.biz,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,whmnx.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,chinaflashmarket.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,awsdns-cn-45.biz,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,aliexpress-media.com,DIRECT  (命中: aliexpress)
- DOMAIN-SUFFIX,oneflys.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,itfly.net,DIRECT  (命中: fly)
- DOMAIN,dg-meta.video.google.com,DIRECT  (命中: google)
- DOMAIN-SUFFIX,ceolaws.net,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,secretflow.com,DIRECT  (命中: ecr)
- DOMAIN,avail.googleflights.net,DIRECT  (命中: google)
- DOMAIN-SUFFIX,wishisp.com,DIRECT  (命中: wish)
- DOMAIN,crashlyticsreports-pa.googleapis.com,DIRECT  (命中: google)
- DOMAIN,googleoptimize-cn.com,DIRECT  (命中: google)
- DOMAIN-SUFFIX,awsdns-cn-06.net,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,npmmirror.com,DIRECT  (命中: npm)
- DOMAIN-SUFFIX,cloudfront-cn.net,DIRECT  (命中: cloudfront)
- DOMAIN-SUFFIX,iqhmh.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,azure.cc,DIRECT  (命中: azure)
- DOMAIN-SUFFIX,khmhvlw.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,shmengyang.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,i-firefly.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,ifireflygame.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,fly998.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,squarecn.com,DIRECT  (命中: square)
- DOMAIN-SUFFIX,ylxhmy.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,secrss.com,DIRECT  (命中: ecr)
- DOMAIN-SUFFIX,appsflyer-cn.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,smogfly.cloud,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,sphmc.org,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,awsdns-cn-46.biz,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,hmwdj.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,yindo-ohm.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,gamegamept.com,DIRECT  (命中: mega)
- DOMAIN-SUFFIX,24hmb.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,wishdown.com,DIRECT  (命中: wish)
- DOMAIN-SUFFIX,ucfly.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,shmedia.tech,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,whmzkf.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,chmod0777kk.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,shmfmr.net,DIRECT  (命中: hm)
- DOMAIN,c.android.clients.google.com,DIRECT  (命中: google)
- DOMAIN-SUFFIX,hf-iflysse.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,myhm.org,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,fly1999.com,DIRECT  (命中: fly)
- DOMAIN,googleadservices-cn.com,DIRECT  (命中: google)
- DOMAIN-SUFFIX,shmaas.net,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,sfecr.com,DIRECT  (命中: ecr)
- DOMAIN-SUFFIX,awsdns-cn-50.net,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,cqs-hm.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,cloudflareinsights-cn.com,DIRECT  (命中: cloudflare)
- DOMAIN,gs-loc.apple.com,DIRECT  (命中: 强制代理域名)
- DOMAIN-SUFFIX,withmedia.net,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,zhmxchina.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,flyml.net,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,windbg.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,chmti.com,DIRECT  (命中: hm)
- DOMAIN,google-analytics-cn.com,DIRECT  (命中: google)
- DOMAIN-SUFFIX,cmacredit.org,DIRECT  (命中: acr)
- DOMAIN-SUFFIX,awsdns-cn-45.com,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,dhmeri.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,vultrcn.com,DIRECT  (命中: vultr)
- DOMAIN-SUFFIX,ayhmjy.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,gdsunfly.com,DIRECT  (命中: fly)
- DOMAIN,gstaticadssl.l.google.com,DIRECT  (命中: google)
- DOMAIN-SUFFIX,weflywifi.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,jcodecraeer.com,DIRECT  (命中: ecr)
- DOMAIN-SUFFIX,awsdns-cn-37.net,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,shmhtv.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,awsdns-cn-44.biz,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,facri.com,DIRECT  (命中: acr)
- DOMAIN-SUFFIX,officebay.net,DIRECT  (命中: ebay)
- DOMAIN-SUFFIX,hmus.net,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,azureflying.com,DIRECT  (命中: azure)
- DOMAIN-SUFFIX,thmins.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,osrelease.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,hmoe.link,DIRECT  (命中: hm)
- DOMAIN,cbdstest.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,zjecredit.org,DIRECT  (命中: ecr)
- DOMAIN,storeedge.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,hbhmxx.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,hlhmf.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,mpnbenefits.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,hmmachine.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,zzfly.net,DIRECT  (命中: fly)
- DOMAIN,oemsoc.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,zhmodaoli.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,flymeos.com,DIRECT  (命中: fly)
- DOMAIN,googlesyndication-cn.com,DIRECT  (命中: google)
- DOMAIN-SUFFIX,chinawssdxh.com,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,pihmh.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,iflysec.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,awsdns-cn-24.biz,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,nike.host,DIRECT  (命中: nike)
- DOMAIN-SUFFIX,hmqjsb.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,awsdns-cn-09.com,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,whmnls.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,smogfly.club,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,lzbhmy.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,znhhmedical.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,bjhmcm.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,edrawsoft.com,DIRECT  (命中: aws)
- DOMAIN,vlportal.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,pmphmooc.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,secrui.com,DIRECT  (命中: ecr)
- DOMAIN-SUFFIX,npmtrend.com,DIRECT  (命中: npm)
- DOMAIN,googleapps-cn.com,DIRECT  (命中: google)
- DOMAIN-SUFFIX,awsdns-cn-45.net,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,cloudflarestoragegw.com,DIRECT  (命中: cloudflare)
- DOMAIN-SUFFIX,9125flying.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,yunqifly.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,hearfly.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,iwishwed.com,DIRECT  (命中: wish)
- DOMAIN,lexuat.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,aliexpress.us,DIRECT  (命中: aliexpress)
- DOMAIN,www-google-analytics.l.google.com,DIRECT  (命中: google)
- DOMAIN-SUFFIX,thmnet.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,awsdns-cn-63.biz,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,gemini-galaxy.com,DIRECT  (命中: gemini)
- DOMAIN-SUFFIX,3hmlg.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,macrozheng.com,DIRECT  (命中: acr)
- DOMAIN-SUFFIX,awsdns-cn-51.com,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,squarefong.com,DIRECT  (命中: square)
- DOMAIN-SUFFIX,elitecrm.com,DIRECT  (命中: ecr)
- DOMAIN-SUFFIX,collaborate.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,googlenav.com,DIRECT  (命中: google)
- DOMAIN-SUFFIX,awsdns-cn-40.net,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,lubanpm.com,DIRECT  (命中: npm)
- DOMAIN,pagead-googlehosted.l.google.com,DIRECT  (命中: google)
- DOMAIN-SUFFIX,minecraftxz.com,DIRECT  (命中: ecr)
- DOMAIN,google-analytics.com,DIRECT  (命中: google)
- DOMAIN,safebrowsing.googleapis.com,DIRECT  (命中: google)
- DOMAIN-SUFFIX,awsdns-cn-40.biz,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,awsonamazon.com,DIRECT  (命中: amazon)
- DOMAIN-SUFFIX,rushmail.com,DIRECT  (命中: hm)
- DOMAIN,sdx.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,awsdns-cn-46.net,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,surface.downloads.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,sheinet.com,DIRECT  (命中: shein)
- DOMAIN-SUFFIX,tshmkj.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,flymopaper.com,DIRECT  (命中: fly)
- DOMAIN,officecdn.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN,download.visualstudio.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,syfly007.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,awsdns-cn-57.com,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,ctrender.com,DIRECT  (命中: render)
- DOMAIN-SUFFIX,awsdns-cn-14.com,DIRECT  (命中: aws)
- DOMAIN,software.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,gzrecruit.com,DIRECT  (命中: ecr)
- DOMAIN-SUFFIX,ylhmgz.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,awsdns-cn-17.net,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,iflydatahub.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,megagamelog.com,DIRECT  (命中: mega)
- DOMAIN-SUFFIX,zgzhmz.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,chiconysquare.com,DIRECT  (命中: square)
- DOMAIN,fontfiles.googleapis.com,DIRECT  (命中: google)
- DOMAIN-SUFFIX,machmall.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,awsdns-cn-61.biz,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,google-hub.com,DIRECT  (命中: google)
- DOMAIN-SUFFIX,ugdocker.link,DIRECT  (命中: docker)
- DOMAIN-SUFFIX,dragonfly.fun,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,aquayee.com,DIRECT  (命中: quay)
- DOMAIN-SUFFIX,hmlcar.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,awsdns-cn-63.net,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,hmszkj.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,dmhmusic.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,telegramtoke.com,DIRECT  (命中: telegram)
- DOMAIN,pki-goog.l.google.com,DIRECT  (命中: google)
- DOMAIN-SUFFIX,shtimessquare.com,DIRECT  (命中: square)
- DOMAIN-SUFFIX,hmz8.com,DIRECT  (命中: hm)
- DOMAIN,windbg.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,mcohmygod.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,yingyecraft.com,DIRECT  (命中: ecr)
- DOMAIN,itacademyuat.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,citichmc.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,whmeigao.com,DIRECT  (命中: hm)
- DOMAIN,clickserver.googleads.com,DIRECT  (命中: google)
- DOMAIN-SUFFIX,grender.com,DIRECT  (命中: render)
- DOMAIN-SUFFIX,awsdns-cn-15.net,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,hm120.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,ttfly.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,mpnbenefitsrtluat.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,hyundai-chhm.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,awsdns-cn-22.net,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,awsdns-cn-56.biz,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,download.visualstudio.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,daiwofly.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,protontechcn.com,DIRECT  (命中: proton)
- DOMAIN-SUFFIX,gshmhotels.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,yhm11.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,msdn.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,smogfly.net,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,pkulaws.com,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,scratchmirror.net,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,hbysfhm.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,d5render.com,DIRECT  (命中: render)
- DOMAIN-SUFFIX,azureyun.com,DIRECT  (命中: azure)
- DOMAIN-SUFFIX,phmacn.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,qflyinc.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,bixuecrm.com,DIRECT  (命中: ecr)
- DOMAIN-SUFFIX,natywish.com,DIRECT  (命中: wish)
- DOMAIN-SUFFIX,njnaws.com,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,awsdns-cn-52.com,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,unpmcc.com,DIRECT  (命中: npm)
- DOMAIN-SUFFIX,flydigi.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,kphm88.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,awsdns-cn-55.net,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,mrwish.net,DIRECT  (命中: wish)
- DOMAIN-SUFFIX,chatgptboke.com,DIRECT  (命中: chatgpt)
- DOMAIN-SUFFIX,awsdns-cn-37.com,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,gzhm.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,awsdns-cn-42.biz,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,lawsdata.com,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,awsdns-cn-29.biz,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,hmfxw.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,52kfly.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,hifly.mobi,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,t-npm.com,DIRECT  (命中: npm)
- DOMAIN-SUFFIX,awsdns-cn-20.biz,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,jhmnew.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,youtube-dubbing.com,DIRECT  (命中: youtube)
- DOMAIN-SUFFIX,02hm.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,hm588.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,flytcloud.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,macrosan.com,DIRECT  (命中: acr)
- DOMAIN-SUFFIX,flashmemoryworld.com,DIRECT  (命中: hm)
- DOMAIN,redirector.c.chat.google.com,DIRECT  (命中: google)
- DOMAIN-SUFFIX,flylinking.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,xn--nmqp78hmufjwu.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,hm152n.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,hyundai-hmtc.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,omegatravel.net,DIRECT  (命中: mega)
- DOMAIN-SUFFIX,gdlinefly.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,flymeauto.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,awsdns-cn-18.biz,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,awsdns-cn-55.biz,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,awsdns-cn-54.biz,DIRECT  (命中: aws)
- DOMAIN,volic.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,zxhmjj.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,iflytoy.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,qhmsg.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,awsdns-cn-12.biz,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,qeoagphm.com,DIRECT  (命中: hm)
- DOMAIN,azurestackhubuat.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,iflytek.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,megajoy.com,DIRECT  (命中: mega)
- DOMAIN-SUFFIX,sqshmzx.net,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,awsdns-cn-54.net,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,renderincloud.com,DIRECT  (命中: render)
- DOMAIN-SUFFIX,hm16888.net,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,bulbsquare.com,DIRECT  (命中: square)
- DOMAIN-SUFFIX,storeedge.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,likeacg.com,DIRECT  (命中: ikea)
- DOMAIN-SUFFIX,edgeone-browser-rendering-dev.com,DIRECT  (命中: render)
- DOMAIN-SUFFIX,xhmedia.com,DIRECT  (命中: hm)
- DOMAIN,surface.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,shmetro.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,flytexpress.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,vz.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,techmiao.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,shmljm.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,hm-3223.net,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,simplecreator.net,DIRECT  (命中: ecr)
- DOMAIN-SUFFIX,hmtrhf.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,ncjrailway.com,DIRECT  (命中: railway)
- DOMAIN-SUFFIX,hmrczp.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,whmlcy.net,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,storecorefulfillment.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,sunnyfly.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,qmacro.com,DIRECT  (命中: acr)
- DOMAIN-SUFFIX,shmama.net,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,seaflysoft.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,southmoney.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,awsdns-cn-20.net,DIRECT  (命中: aws)
- DOMAIN,tools.google.com,DIRECT  (命中: google)
- DOMAIN-SUFFIX,testshm.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,whmdedu.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,hfhm.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,yjdatasos.com,DIRECT  (命中: asos)
- DOMAIN-SUFFIX,awsdns-cn-21.biz,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,shmusic.org,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,fly139.com,DIRECT  (命中: fly)
- DOMAIN,googlesyndication.com,DIRECT  (命中: google)
- DOMAIN-SUFFIX,oemssl.cn.cdn.cloudflare.net,DIRECT  (命中: cloudflare)
- DOMAIN-SUFFIX,uuu.ovh,DIRECT  (命中: ovh)
- DOMAIN-SUFFIX,englishmasterclub.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,hwrecruit.com,DIRECT  (命中: ecr)
- DOMAIN-SUFFIX,724pridecryogenics.com,DIRECT  (命中: ecr)
- DOMAIN-SUFFIX,awsdns-cn-34.net,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,officemkt.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,shmet.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,awsdns-cn-59.net,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,awsdns-cn-50.biz,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,gx-hm.com,DIRECT  (命中: hm)
- DOMAIN,itacademy.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,rohm-chip.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,awsdns-cn-60.biz,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,awsdns-cn-36.com,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,openai-hub.com,DIRECT  (命中: openai)
- DOMAIN,googletraveladservices.com,DIRECT  (命中: google)
- DOMAIN-SUFFIX,weighment.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,awsdns-cn-00.net,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,megahugo.net,DIRECT  (命中: mega)
- DOMAIN-SUFFIX,cqhma.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,awsdns-cn-46.com,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,whichmba.net,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,wishcad.com,DIRECT  (命中: wish)
- DOMAIN-SUFFIX,azurestackhub.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,toprender.com,DIRECT  (命中: render)
- DOMAIN-SUFFIX,2google.com,DIRECT  (命中: google)
- DOMAIN-SUFFIX,hnlshm.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,awsdns-cn-21.net,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,awsdns-cn-43.biz,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,wecrm.com,DIRECT  (命中: ecr)
- DOMAIN-SUFFIX,techmoris.com,DIRECT  (命中: hm)
- DOMAIN,redirector.c.pack.google.com,DIRECT  (命中: google)
- DOMAIN-SUFFIX,iflydocs.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,iflyhealth.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,zchmh.com,DIRECT  (命中: hm)
- DOMAIN,mbs.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,iflytektstd.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,1818hm.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,awsdns-cn-42.com,DIRECT  (命中: aws)
- DOMAIN,googletagservices-cn.com,DIRECT  (命中: google)
- DOMAIN-SUFFIX,whhmmbl.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,haofly.net,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,chmc.cc,DIRECT  (命中: hm)
- DOMAIN,qpx.googleflights.net,DIRECT  (命中: google)
- DOMAIN-SUFFIX,hmlan.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,secretgardenresorts.com,DIRECT  (命中: ecr)
- DOMAIN-SUFFIX,awsdns-cn-17.com,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,flyme.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,asosoaiid.com,DIRECT  (命中: asos)
- DOMAIN-SUFFIX,awsdns-cn-12.net,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,lzghmy.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,tlhmhd.com,DIRECT  (命中: hm)
- DOMAIN,redirector.c.youtubeeducation.com,DIRECT  (命中: youtube)
- DOMAIN-SUFFIX,thmzedu.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,xczhmzb.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,awspony.com,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,chinacrosspoint.com,DIRECT  (命中: acr)
- DOMAIN-SUFFIX,awsdns-cn-14.biz,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,fwfly.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,fly84.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,asosde.com,DIRECT  (命中: asos)
- DOMAIN-SUFFIX,cqrailway.com,DIRECT  (命中: railway)
- DOMAIN-SUFFIX,rsm.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,awsdns-cn-22.com,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,awsdns-cn-63.com,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,sharjahmadrasa.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,azureflame.cloud,DIRECT  (命中: azure)
- DOMAIN-SUFFIX,ggshmy.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,awsdns-cn-35.biz,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,flyertea.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,flygon.net,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,wbecrisfro.com,DIRECT  (命中: ecr)
- DOMAIN-SUFFIX,awsdns-cn-59.biz,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,qzynhhmm.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,awsdns-cn-58.net,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,jinshmgw.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,flymeyun.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,awsdns-cn-52.net,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,zchmbx.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,flyenglish.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,hmgbtv.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,awsdns-cn-33.biz,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,awsdns-cn-19.net,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,hmjc.org,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,awsdns-cn-28.biz,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,oktamall.com,DIRECT  (命中: okta)
- DOMAIN-SUFFIX,oemsocuat.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,iflying.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,jinshasitemuseum.com,DIRECT  (命中: temu)
- DOMAIN,safebrowsing-cache.google.com,DIRECT  (命中: google)
- DOMAIN,adservice.google.com,DIRECT  (命中: google)
- DOMAIN-SUFFIX,ahmky.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,awsdns-cn-49.biz,DIRECT  (命中: aws)
- DOMAIN,storeedgefd.dsx.mp.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,whmama.com,DIRECT  (命中: hm)
- DOMAIN,googletagmanager-cn.com,DIRECT  (命中: google)
- DOMAIN-SUFFIX,likeaboat2023.com,DIRECT  (命中: ikea)
- DOMAIN-SUFFIX,awsdns-cn-47.net,DIRECT  (命中: aws)
- DOMAIN,imasdk.googleapis.com,DIRECT  (命中: google)
- DOMAIN-SUFFIX,4hmodel.com,DIRECT  (命中: hm)
- DOMAIN,collaborateppe.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,chnrailway.com,DIRECT  (命中: railway)
- DOMAIN-SUFFIX,gemini530.net,DIRECT  (命中: gemini)
- DOMAIN-SUFFIX,athmapp.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,cloudflareperf.com,DIRECT  (命中: cloudflare)
- DOMAIN-SUFFIX,hellogitlab.com,DIRECT  (命中: gitlab)
- DOMAIN-SUFFIX,oemsoc.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,glhmmr.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,shmylike.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,awsdns-cn-24.com,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,neihanfly.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,ghsmpwalmart.com,DIRECT  (命中: walmart)
- DOMAIN-SUFFIX,zhmedcenter.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,whminwei.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,awsdns-cn-41.biz,DIRECT  (命中: aws)
- DOMAIN,ssl-google-analytics.l.google.com,DIRECT  (命中: google)
- DOMAIN-SUFFIX,luxtarget.com,DIRECT  (命中: target)
- DOMAIN-SUFFIX,facebookol.com,DIRECT  (命中: facebook)
- DOMAIN-SUFFIX,flyingeffect.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,awsdns-cn-62.com,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,njhmmr.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,acrel-eem.com,DIRECT  (命中: acr)
- DOMAIN-SUFFIX,awsamazonlab.com,DIRECT  (命中: amazon)
- DOMAIN-SUFFIX,awsdns-cn-23.net,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,secretmine.net,DIRECT  (命中: ecr)
- DOMAIN-SUFFIX,flyneutron.com,DIRECT  (命中: fly)
- DOMAIN,download.mlcc.google.com,DIRECT  (命中: google)
- DOMAIN-SUFFIX,yhchmo.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,szhmkeji.com,DIRECT  (命中: hm)
- DOMAIN,cdn.globalsigncdn.com.cdn.cloudflare.net,DIRECT  (命中: cloudflare)
- DOMAIN-SUFFIX,haitianpm.com,DIRECT  (命中: npm)
- DOMAIN-SUFFIX,lhmp.cc,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,bebhmongb.com,DIRECT  (命中: hm)
- DOMAIN,wear.googleapis.com,DIRECT  (命中: google)
- DOMAIN-SUFFIX,hlnpm.com,DIRECT  (命中: npm)
- DOMAIN,googleoptimize.com,DIRECT  (命中: google)
- DOMAIN-SUFFIX,aliexpress.com,DIRECT  (命中: aliexpress)
- DOMAIN-SUFFIX,whmj.org,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,fingerflyapp.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,openai.wf,DIRECT  (命中: openai)
- DOMAIN,update.googleapis.com,DIRECT  (命中: google)
- DOMAIN-SUFFIX,awsdns-cn-38.net,DIRECT  (命中: aws)
- DOMAIN,msdn.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,cloudflareanycast.net,DIRECT  (命中: cloudflare)
- DOMAIN-SUFFIX,qjhm.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,abcdocker.com,DIRECT  (命中: docker)
- DOMAIN,www-googletagmanager.l.google.com,DIRECT  (命中: google)
- DOMAIN-SUFFIX,hminvestment.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,hmsemi.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,touchmark.art,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,ghmcchina.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,shmockup.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,whmxrj.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,flyco.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,awsdns-cn-05.biz,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,cacre.org,DIRECT  (命中: acr)
- DOMAIN-SUFFIX,dylyghm.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,googlebbs.net,DIRECT  (命中: google)
- DOMAIN-SUFFIX,victoriassecretclearance.online,DIRECT  (命中: ecr)
- DOMAIN-SUFFIX,originalkindergarten.com,DIRECT  (命中: kinde)
- DOMAIN-SUFFIX,nhmuni.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,aliexpress.ru,DIRECT  (命中: aliexpress)
- DOMAIN,cache.pack.google.com,DIRECT  (命中: google)
- DOMAIN-SUFFIX,hmzixin.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,vdfly.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,zhmu.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,awsdns-cn-02.net,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,shmbjy.org,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,hifly.tv,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,shmondial.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,flyfishx.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,dl.delivery.mp.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,awsdns-cn-18.net,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,flyfunny.com,DIRECT  (命中: fly)
- DOMAIN,msdprod-ad.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,awsdns-cn-00.com,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,hmgreat.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,51render.com,DIRECT  (命中: render)
- DOMAIN-SUFFIX,xn--vhqqbz2p62hm92e04p.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,gdhmgc.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,hmxixie.com,DIRECT  (命中: hm)
- DOMAIN,mpnbenefits.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,officecdn.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,awsdns-cn-03.biz,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,nike666.com,DIRECT  (命中: nike)
- DOMAIN-SUFFIX,hmgj.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,iflyiot.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,awsdns-cn-07.com,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,hmnst.com,DIRECT  (命中: hm)
- DOMAIN,tac.googleapis.com,DIRECT  (命中: google)
- DOMAIN-SUFFIX,awsdns-cn-04.net,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,thwgetsy.com,DIRECT  (命中: etsy)
- DOMAIN,cache-management-prod.google.com,DIRECT  (命中: google)
- DOMAIN,googleapis-cn.com,DIRECT  (命中: google)
- DOMAIN-SUFFIX,awsdns-cn-60.net,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,awsdns-cn-53.com,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,zhmag.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,tecreal.com,DIRECT  (命中: ecr)
- DOMAIN-SUFFIX,awsdns-cn-23.com,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,dagongcredit.com,DIRECT  (命中: gcr)
- DOMAIN-SUFFIX,iflyaiedu.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,tinsecret.com,DIRECT  (命中: ecr)
- DOMAIN-SUFFIX,happypingpang.com,DIRECT  (命中: pypi)
- DOMAIN-SUFFIX,awsdns-cn-19.biz,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,jhqshfly.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,sectigochina.com.cdn.cloudflare.net,DIRECT  (命中: cloudflare)
- DOMAIN-SUFFIX,macrosilicon.com,DIRECT  (命中: acr)
- DOMAIN-SUFFIX,protong.com,DIRECT  (命中: proton)
- DOMAIN-SUFFIX,iflyink.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,cloudflareip.com,DIRECT  (命中: cloudflare)
- DOMAIN-SUFFIX,bjhdhm.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,forcecreat.com,DIRECT  (命中: ecr)
- DOMAIN-SUFFIX,szhmjp.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,chinacrops.org,DIRECT  (命中: acr)
- DOMAIN-SUFFIX,targetportion.com,DIRECT  (命中: target)
- DOMAIN-SUFFIX,chinacrane.net,DIRECT  (命中: acr)
- DOMAIN-SUFFIX,sdx.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,thmovie.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,qixingcr.com,DIRECT  (命中: gcr)
- DOMAIN,mpnbenefitsrtluat.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,hmtgo.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,hmrsrc.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,awsdns-cn-10.com,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,whhmgroup.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,whmf8.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,3hmedicalgroup.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,xrender.com,DIRECT  (命中: render)
- DOMAIN-SUFFIX,awsdns-cn-01.biz,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,hbhml.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,chihm.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,gxhhmed.com,DIRECT  (命中: hm)
- DOMAIN,redirector.c.play.google.com,DIRECT  (命中: google)
- DOMAIN-SUFFIX,awsdns-cn-25.com,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,megaemoji.com,DIRECT  (命中: mega)
- DOMAIN-SUFFIX,xawscu.com,DIRECT  (命中: aws)
- DOMAIN,gs-loc-cn.apple.com,DIRECT  (命中: 强制代理域名)
- DOMAIN-SUFFIX,awsdns-cn-48.net,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,flyme.net,DIRECT  (命中: fly)
- DOMAIN,images-cn.ssl-images-amazon.com,DIRECT  (命中: amazon)
- DOMAIN-SUFFIX,hmyzs.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,hmltec.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,fulinpm.com,DIRECT  (命中: npm)
- DOMAIN-SUFFIX,hmtnew.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,minecraftzw.com,DIRECT  (命中: ecr)
- DOMAIN-SUFFIX,gxhmdjt.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,hmedu.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,hmting.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,azuretouch.net,DIRECT  (命中: azure)
- DOMAIN-SUFFIX,hm163.net,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,yhmob.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,awsdns-cn-09.net,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,chinacrankshaft.com,DIRECT  (命中: acr)
- DOMAIN-SUFFIX,awsdns-cn-36.net,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,czxthmls.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,hhmajiang.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,c-thme.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,awsdns-cn-60.com,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,mightsquare.com,DIRECT  (命中: square)
- DOMAIN-SUFFIX,googley8rb.com,DIRECT  (命中: google)
- DOMAIN-SUFFIX,shmzgroup.com,DIRECT  (命中: hm)
- DOMAIN,vscode.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,ntrailway.com,DIRECT  (命中: railway)
- DOMAIN,developer.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,thmall.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,scratchmirror.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,hmj666.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,openailab.com,DIRECT  (命中: openai)
- DOMAIN-SUFFIX,mikecrm.com,DIRECT  (命中: ecr)
- DOMAIN-SUFFIX,hmbzfjt.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,wecrm.net,DIRECT  (命中: ecr)
- DOMAIN-SUFFIX,wish-hightech.com,DIRECT  (命中: wish)
- DOMAIN-SUFFIX,mysecrettop.com,DIRECT  (命中: ecr)
- DOMAIN-SUFFIX,azuremigrate.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,brighticecream.com,DIRECT  (命中: ecr)
- DOMAIN-SUFFIX,nnhmcj.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,fireflyacg.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,hm-optics.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,cheetahmobile.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,oecr.com,DIRECT  (命中: ecr)
- DOMAIN-SUFFIX,microsoftuwp.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,chinaacryl.com,DIRECT  (命中: acr)
- DOMAIN-SUFFIX,awsdns-cn-44.net,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,imags-google.com,DIRECT  (命中: google)
- DOMAIN-SUFFIX,ecr-global.com,DIRECT  (命中: ecr)
- DOMAIN-SUFFIX,chinacraa.org,DIRECT  (命中: acr)
- DOMAIN-SUFFIX,software.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,hmadgz.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,hefeilaws.com,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,zjgcreative.com,DIRECT  (命中: gcr)
- DOMAIN-SUFFIX,macroprocess.com,DIRECT  (命中: acr)
- DOMAIN-SUFFIX,ecrrc.com,DIRECT  (命中: ecr)
- DOMAIN-SUFFIX,ovhlb.com,DIRECT  (命中: ovh)
- DOMAIN-SUFFIX,ghmd448.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,cproton.com,DIRECT  (命中: proton)
- DOMAIN-SUFFIX,lexuat.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,awsdns-cn-27.biz,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,jdhmediajd.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,shmtu.net,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,yfldocker.com,DIRECT  (命中: docker)
- DOMAIN-SUFFIX,shhmbio.com,DIRECT  (命中: hm)
- DOMAIN,googleflights-cn.net,DIRECT  (命中: google)
- DOMAIN-SUFFIX,dreamspark.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,yzhmyy.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,awsdns-cn-55.com,DIRECT  (命中: aws)
- DOMAIN,oemsocuat.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,akamai.com,DIRECT  (命中: akamai)
- DOMAIN-SUFFIX,msdprod-ad.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- URL-REGEX,"^https?:\/\/.+\.awsdns-cn-[0-9][a-e0-9]\.cn.*$",DIRECT  (命中: aws)
- DOMAIN-SUFFIX,smogfly.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,myvs.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,yz-proton.com,DIRECT  (命中: proton)
- DOMAIN-SUFFIX,awsdns-cn-52.biz,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,hmqg.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,cofly.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,awsdns-cn-31.net,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,iflyadx.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,lzarays.com,DIRECT  (命中: zara)
- DOMAIN-SUFFIX,hmx-led.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,awsdns-cn-24.net,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,cloudflareglobal.net,DIRECT  (命中: cloudflare)
- DOMAIN,azurestackhub.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,nikefans.com,DIRECT  (命中: nike)
- DOMAIN-SUFFIX,gxhmba.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,square16.org,DIRECT  (命中: square)
- DOMAIN-SUFFIX,cn-railway.net,DIRECT  (命中: railway)
- DOMAIN,azuremigrate.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,cloudflarestaging.com,DIRECT  (命中: cloudflare)
- DOMAIN-SUFFIX,cloudflare-cn.com,DIRECT  (命中: cloudflare)
- DOMAIN-SUFFIX,imgs.ovh,DIRECT  (命中: ovh)
- DOMAIN-SUFFIX,awsdns-cn-25.net,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,azurestackhubuat.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,hnsyhm.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,awsdns-cn-41.com,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,feidacrusher.com,DIRECT  (命中: acr)
- DOMAIN-SUFFIX,awsdns-cn-36.biz,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,dreamsparkuat.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN,time.amazonaws.cn,DIRECT  (命中: amazon)
- DOMAIN,googletraveladservices-cn.com,DIRECT  (命中: google)
- DOMAIN-SUFFIX,awsdns-cn-39.biz,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,awsdns-cn-34.com,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,cuahmap.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,zhmf.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,wodecrowd.com,DIRECT  (命中: ecr)
- DOMAIN,mpnbenefitsrtl.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN,download.tensorflow.google.com,DIRECT  (命中: google)
- DOMAIN,googleadservices.com,DIRECT  (命中: google)
- DOMAIN-SUFFIX,hmzs.net,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,glflyy.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,e-flyinc.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,flymobi.biz,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,fishflying.net,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,oacrm.com,DIRECT  (命中: acr)
- DOMAIN-SUFFIX,welchmat.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,volcecr.com,DIRECT  (命中: ecr)
- DOMAIN,rsm.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,awsdns-cn-47.com,DIRECT  (命中: aws)
- DOMAIN,surface.downloads.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN,firebase-settings.crashlytics.com,DIRECT  (命中: firebase)
- DOMAIN-SUFFIX,volic.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,gyhm.cc,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,surface.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,cbdstest.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,meiji-icecream.com,DIRECT  (命中: ecr)
- DOMAIN-SUFFIX,azuremigratetest.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,chmecc.org,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,shmarathon.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,czhmjx.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,sdhmdp.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,dcg.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,beijing-hmo.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,algorithmart.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,flycua.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,qualcomm.cn.cdn.cloudflare.net,DIRECT  (命中: cloudflare)
- DOMAIN-SUFFIX,mbs.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,hzhm888.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,magentochina.org,DIRECT  (命中: magento)
- DOMAIN-SUFFIX,gacrnd.com,DIRECT  (命中: acr)
- DOMAIN-SUFFIX,whmoocs.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,ovhlb.net,DIRECT  (命中: ovh)
- DOMAIN-SUFFIX,acrel-microgrid.com,DIRECT  (命中: acr)
- DOMAIN,msproduct.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,iva-schmetz.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,chmia.org,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,fly3949.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,netsyq.com,DIRECT  (命中: etsy)
- DOMAIN-SUFFIX,bfhmj.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,hmzhtc.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,awsdns-cn-16.biz,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,sdhmkj.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,railwaybill.com,DIRECT  (命中: railway)
- DOMAIN-SUFFIX,shlawserve.com,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,tb-whatsapp.com,DIRECT  (命中: whatsapp)
- DOMAIN-SUFFIX,iflyread.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,chinamaven.com,DIRECT  (命中: maven)
- DOMAIN-SUFFIX,awsdns-cn-17.biz,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,bmp.ovh,DIRECT  (命中: ovh)
- DOMAIN-SUFFIX,download.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,hmxx.net,DIRECT  (命中: hm)
- DOMAIN,download.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,awsdns-cn-28.net,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,awsdns-cn-05.net,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,xn--vhq4ut2dsxd5xqnicjxxo55a756aovhik0aunm.com,DIRECT  (命中: ovh)
- DOMAIN-SUFFIX,md-hmjt.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,airtofly.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,hbhm.net,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,aflytec.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,3zhm.com,DIRECT  (命中: hm)
- DOMAIN,redirector.c.mail.google.com,DIRECT  (命中: google)
- DOMAIN-SUFFIX,cloudflarecn.net,DIRECT  (命中: cloudflare)
- DOMAIN-SUFFIX,cnflyinghorse.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,shmusicschool.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,acloudrender.com,DIRECT  (命中: render)
- DOMAIN-SUFFIX,cnpmjs.org,DIRECT  (命中: npm)
- DOMAIN-SUFFIX,whuznhmedj.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,fly63.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,xhmwxy.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,arefly.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,shmds.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,flyhand.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,whmc2005.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,collaborateppe.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,hfly.net,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,ztrhmall.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,awsdns-vip.com,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,elecrystal.com,DIRECT  (命中: ecr)
- DOMAIN-SUFFIX,chmgames.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,zhmzqi.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,haiqianghm.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,flyingpigeon1936.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,hmarathon.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,jxhmxxjs.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,awsdns-cn-37.biz,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,awsdns-cn-56.net,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,officemktuat.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,cthhmu.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,awsdns-cn-33.net,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,chinaws.net,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,ihmch.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,shmog.org,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,itgemini.net,DIRECT  (命中: gemini)
- DOMAIN-SUFFIX,jiansujihm.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,azure-wave.com,DIRECT  (命中: azure)
- DOMAIN,googlevads-cn.com,DIRECT  (命中: google)
- DOMAIN-SUFFIX,awsdns-cn-16.net,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,thmz.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,awsdns-cn-02.biz,DIRECT  (命中: aws)
- DOMAIN,lex.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,hmkp.org,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,awsdns-cn-35.net,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,applysquare.com,DIRECT  (命中: square)
- DOMAIN-SUFFIX,awsdns-cn-07.net,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,acroview.com,DIRECT  (命中: acr)
- DOMAIN-SUFFIX,hyahm.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,qihangcrrc.com,DIRECT  (命中: gcr)
- DOMAIN-SUFFIX,google444.com,DIRECT  (命中: google)
- DOMAIN-SUFFIX,chinacrt.com,DIRECT  (命中: acr)
- DOMAIN-SUFFIX,vscode.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,awsdns-cn-06.com,DIRECT  (命中: aws)
- DOMAIN,officemktuat.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,shmds.vip,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,hicnhm.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,zhinikefu.com,DIRECT  (命中: nike)
- DOMAIN-SUFFIX,macrolake.com,DIRECT  (命中: acr)
- DOMAIN,googleanalytics.com,DIRECT  (命中: google)
- DOMAIN-SUFFIX,honchmedia.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,shmaur.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,eflybird.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,awsdns-cn-09.biz,DIRECT  (命中: aws)
- DOMAIN,dreamspark.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,hmxw.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,itacademy.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,hm5988.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,bjwhmedia.com,DIRECT  (命中: hm)
- DOMAIN,images-cn-8.ssl-images-amazon.com,DIRECT  (命中: amazon)
- DOMAIN-SUFFIX,jxhmjx.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,wishtec.com,DIRECT  (命中: wish)
- DOMAIN-SUFFIX,iflyresearch.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,awspaas.com,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,lhmj.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,hmeili.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,mysecretrainbow.com,DIRECT  (命中: ecr)
- DOMAIN-SUFFIX,whmvc.net,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,digcredit.com,DIRECT  (命中: gcr)
- DOMAIN,dl.google.com,DIRECT  (命中: google)
- DOMAIN-SUFFIX,hmf-china.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,awsdns-cn-44.com,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,fly-exp.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,hnpm.cc,DIRECT  (命中: npm)
- DOMAIN-SUFFIX,ghmba.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,rcolab.com,DIRECT  (命中: colab)
- DOMAIN-SUFFIX,awsdns-cn-58.com,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,awsdns-cn-48.com,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,xn--y8jhmm6gn.moe,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,sxhm.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,dhmsnyy.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,awsdns-cn-62.net,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,jyhmz.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,vecrp.com,DIRECT  (命中: ecr)
- DOMAIN,dl.l.google.com,DIRECT  (命中: google)
- DOMAIN-SUFFIX,facebooksx.com,DIRECT  (命中: facebook)
- DOMAIN,performanceparameters.googleapis.com,DIRECT  (命中: google)
- DOMAIN-SUFFIX,91hmi.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,whmnrc.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,megagenchina.com,DIRECT  (命中: mega)
- DOMAIN-SUFFIX,cloudflareprod.com,DIRECT  (命中: cloudflare)
- DOMAIN,officemkt.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,ideacreated.com,DIRECT  (命中: acr)
- DOMAIN-SUFFIX,ahmwgroup.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,1fly.fun,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,mikeauth.com,DIRECT  (命中: ikea)
- DOMAIN-SUFFIX,esdhm.net,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,bjhmyq.com,DIRECT  (命中: hm)
- DOMAIN,dreamsparkuat.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,shmhzp.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,machenike.com,DIRECT  (命中: nike)
- DOMAIN-SUFFIX,moonfly.net,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,zenithmining.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,kindechem.com,DIRECT  (命中: kinde)
- DOMAIN-SUFFIX,lnwish.com,DIRECT  (命中: wish)
- DOMAIN,googletagservices.com,DIRECT  (命中: google)
- DOMAIN,googletagmanager.com,DIRECT  (命中: google)
- DOMAIN-SUFFIX,armfly.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,awsdns-cn-48.biz,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,macrowing.com,DIRECT  (命中: acr)
- DOMAIN-SUFFIX,codeflying.net,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,rainbutterfly.xyz,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,vlportal.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN,azuremigratetest.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,fhmooc.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,smogflycloud.net,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,dockerinfo.net,DIRECT  (命中: docker)
- DOMAIN-SUFFIX,gxlzhm.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,iflynote.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,awsdns-cn-01.net,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,awsdns-cn-26.com,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,cdnhwcohm19.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,drugoogle.com,DIRECT  (命中: google)
- DOMAIN-SUFFIX,lenovo.com.cdn.cloudflare.net,DIRECT  (命中: cloudflare)
- DOMAIN-SUFFIX,fhmion.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,awsdns-cn-20.com,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,awsdns-cn-41.net,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,jshmrcb.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,megarobo.com,DIRECT  (命中: mega)
- DOMAIN-SUFFIX,51google.com,DIRECT  (命中: google)
- DOMAIN-SUFFIX,zztfly.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,sdhmjt.net,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,hhmage.com,DIRECT  (命中: hm)
- DOMAIN,clientservices.googleapis.com,DIRECT  (命中: google)
- DOMAIN-SUFFIX,flysheeep.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,whoami.akamai.net,DIRECT  (命中: akamai)
- DOMAIN-SUFFIX,awsdns-cn-62.biz,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,aftersale-amazon.com,DIRECT  (命中: amazon)
- DOMAIN-SUFFIX,fawsoft.com,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,cyhm.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,cloudhvacr.com,DIRECT  (命中: acr)
- DOMAIN-SUFFIX,renderbus.com,DIRECT  (命中: render)
- DOMAIN-SUFFIX,flygo.net,DIRECT  (命中: fly)
- URL-REGEX,"^https?:\/\/r+[0-9]+(---|\.)sn-(2x3|ni5|j5o)\w{5}\.googlevideo\.com.*$",DIRECT  (命中: google)
- DOMAIN-SUFFIX,flyai.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,awstar.net,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,macrounion.com,DIRECT  (命中: acr)
- DOMAIN-SUFFIX,orasos.com,DIRECT  (命中: asos)
- DOMAIN-SUFFIX,hmwzjs.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,flysand.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,yytiflytek.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,mpnbenefitsrtl.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,bshmzx.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,xhma.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,awsdns-cn-58.biz,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,fly160.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,flyadx.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,shhmu.net,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,chinahvacr.com,DIRECT  (命中: acr)
- DOMAIN-SUFFIX,megawords.cc,DIRECT  (命中: mega)
- DOMAIN-SUFFIX,lzhmmr.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,hm025.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,wish3d.com,DIRECT  (命中: wish)
- DOMAIN-SUFFIX,fhmv.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,awsdns-cn-39.com,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,bwfhmall.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,qhm123.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,awsdns-cn-51.biz,DIRECT  (命中: aws)
- DOMAIN,vz.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,iflyrec.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,smogflycloud.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,hkgcr.com,DIRECT  (命中: gcr)
- DOMAIN-SUFFIX,xahmqy.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,cdnchatgpt.com,DIRECT  (命中: chatgpt)
- DOMAIN-SUFFIX,applysquare.net,DIRECT  (命中: square)
- DOMAIN-SUFFIX,bzmhm.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,awsdns-cn-47.biz,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,macrr.com,DIRECT  (命中: acr)
- DOMAIN-SUFFIX,inflyway.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,acrel-znyf.com,DIRECT  (命中: acr)
- DOMAIN-SUFFIX,msproduct.download.prss.microsoft.com,DIRECT  (命中: microsoft)
```
</details>

### 上游源状态

- ✅ https://raw.githubusercontent.com/GMOogway/shadowrocket-rules/master/sr_direct_list.module

**原有规则数**: 110375
**新增规则数**: 0
**更新后总数**: 110375

🩺 直连模块: 健康检查通过（110375 条规则）

## 代理分流模块

### ❌ 代理规则质量检查异常（共 1 条）

**处理动作**：异常规则已从最终模块中移除。

<details>
<summary>展开查看异常规则及原因</summary>

```
- DOMAIN-SUFFIX,OMAIN-SUFFIX,bing.net,PROXY  (原因: 策略 'BING.NET' 不合法)
```
</details>

### ⚠️ Shield 模块同域名策略冲突（共 17 组）

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
**DOMAIN-SUFFIX:log.snssdk.com**
```
- DOMAIN-SUFFIX,log.snssdk.com,REJECT
- DOMAIN-SUFFIX,log.snssdk.com,REJECT-DICT-200
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

### 上游源状态

- ✅ https://raw.githubusercontent.com/GMOogway/shadowrocket-rules/master/sr_proxy_list.module
- ✅ https://raw.githubusercontent.com/LOWERTOP/Shadowrocket-First/main/Talkatone.sgmodule

**原有代理规则数**: 27339
**新增代理规则数**: 0
**更新后代理规则总数**: 27339

## 去广告模块

### 上游源状态

- ✅ https://raw.githubusercontent.com/huijingfei/Shadowrocket-Rules/refs/heads/main/sr_app_ad.module
- ✅ https://raw.githubusercontent.com/deezertidal/shadowrocket-rules/refs/heads/main/modules/startingad.module
- ✅ https://raw.githubusercontent.com/GMOogway/shadowrocket-rules/master/sr_reject_list.module
- ✅ https://raw.githubusercontent.com/Unwhimsical/NetPilot/refs/heads/main/modules/%E6%B5%8B%E8%AF%95.module
- ✅ https://raw.githubusercontent.com/LOWERTOP/Shadowrocket-First/main/TalkatoneAntiAds.list

**原有去广告规则数**: 189463
**新增去广告规则数**: 0
**更新后去广告规则总数**: 189463

## ⚠️ 敏感域名已自动过滤（银行/支付）

**原因**：域名包含银行/支付关键词，为防止隐私泄露，不加入解密列表。

<details>
<summary>展开查看被过滤的敏感域名（共 13 个）</summary>

```
api.waitwaitpay.com
webappcfg.paas.cmbchina.com
creditcardapp.bankcomm.cn
creditcardapp.bankcomm.com
ump.sz.creditcard.ecitic.com
mbasecc.bas.cmbchina.com
m.stock.pingan.com
mpos-pic.helipay.com
zjmbank.js96008.com
m.creditcard.ecitic.com
yunbusiness.ccb.com
adv.ccb.com
lban.spdb.com.cn
```
</details>

🩺 Shield模块: 健康检查通过（216802 条规则）

## 🩺 规则源健康状态

- ✅ https://raw.githubusercontent.com/GMOogway/shadowrocket-rules/master/sr_direct_list.module
  - 成功 8 次，失败 0 次，连续失败 0 次
  - 最近成功: 2026-09-05 15:05:15
  - 最近失败: 无 

- ✅ https://raw.githubusercontent.com/GMOogway/shadowrocket-rules/master/sr_proxy_list.module
  - 成功 8 次，失败 0 次，连续失败 0 次
  - 最近成功: 2026-09-05 15:05:25
  - 最近失败: 无 

- ✅ https://raw.githubusercontent.com/LOWERTOP/Shadowrocket-First/main/Talkatone.sgmodule
  - 成功 8 次，失败 0 次，连续失败 0 次
  - 最近成功: 2026-09-05 15:05:25
  - 最近失败: 无 

- ✅ https://raw.githubusercontent.com/huijingfei/Shadowrocket-Rules/refs/heads/main/sr_app_ad.module
  - 成功 8 次，失败 0 次，连续失败 0 次
  - 最近成功: 2026-09-05 15:05:25
  - 最近失败: 无 

- ✅ https://raw.githubusercontent.com/deezertidal/shadowrocket-rules/refs/heads/main/modules/startingad.module
  - 成功 8 次，失败 0 次，连续失败 0 次
  - 最近成功: 2026-09-05 15:05:25
  - 最近失败: 无 

- ✅ https://raw.githubusercontent.com/GMOogway/shadowrocket-rules/master/sr_reject_list.module
  - 成功 8 次，失败 0 次，连续失败 0 次
  - 最近成功: 2026-09-05 15:05:26
  - 最近失败: 无 

- ✅ https://raw.githubusercontent.com/Unwhimsical/NetPilot/refs/heads/main/modules/%E6%B5%8B%E8%AF%95.module
  - 成功 8 次，失败 0 次，连续失败 0 次
  - 最近成功: 2026-09-05 15:05:27
  - 最近失败: 无 

- ✅ https://raw.githubusercontent.com/LOWERTOP/Shadowrocket-First/main/TalkatoneAntiAds.list
  - 成功 8 次，失败 0 次，连续失败 0 次
  - 最近成功: 2026-09-05 15:05:27
  - 最近失败: 无 



## 🔒 DNS 泄漏风险检测

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
