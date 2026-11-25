# 更新日志 2026-11-25

**运行时间**: 2026-11-25 08:31:55 北京时间

---

## 直连模块

### 🔍 过滤海外/强制代理直连规则（共 944 条）

**原因**：规则域名匹配海外黑名单关键词，或属于强制代理域名（如定位模块）。

<details>
<summary>展开查看被过滤规则及命中关键词</summary>

```
- DOMAIN-SUFFIX,whhmgroup.com,DIRECT  (命中: hm)
- DOMAIN,connectivitycheck.gstatic.com,DIRECT  (命中: gstatic.com)
- DOMAIN-SUFFIX,awsdns-cn-11.biz,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,meiji-icecream.com,DIRECT  (命中: ecr)
- DOMAIN-SUFFIX,storeedge.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,vecrp.com,DIRECT  (命中: ecr)
- DOMAIN,developer.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,machmall.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,jhm2012.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,hyundai-chhm.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,awsdns-cn-37.biz,DIRECT  (命中: aws)
- DOMAIN,surface.downloads.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,wishtec.com,DIRECT  (命中: wish)
- DOMAIN-SUFFIX,flytexpress.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,fly3949.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,yindo-ohm.com,DIRECT  (命中: hm)
- DOMAIN,fonts.gstatic.com,DIRECT  (命中: gstatic.com)
- DOMAIN-SUFFIX,scratchmirror.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,acroview.com,DIRECT  (命中: acr)
- DOMAIN-SUFFIX,chinacrankshaft.com,DIRECT  (命中: acr)
- DOMAIN-SUFFIX,awsdns-cn-01.net,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,flymeos.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,zztfly.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,awsdns-cn-06.com,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,shmylike.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,jinshasitemuseum.com,DIRECT  (命中: temu)
- DOMAIN-SUFFIX,zhmag.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,sdx.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,hm163.net,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,ylhmgz.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,yunqifly.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,azureyun.com,DIRECT  (命中: azure)
- DOMAIN-SUFFIX,cthhmu.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,ggshmy.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,sdhmkj.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,awsdns-cn-52.biz,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,awsdns-cn-01.biz,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,whmdedu.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,applysquare.com,DIRECT  (命中: square)
- DOMAIN-SUFFIX,awsdns-cn-29.biz,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,cqs-hm.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,cyhm.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,scratchmirror.net,DIRECT  (命中: hm)
- URL-REGEX,"^https?:\/\/r+[0-9]+(---|\.)sn-(2x3|ni5|j5o)\w{5}\.googlevideo\.com.*$",DIRECT  (命中: google)
- DOMAIN-SUFFIX,awsdns-cn-03.biz,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,xn--y8jhmm6gn.moe,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,iflying.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,flydigi.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,hnpm.cc,DIRECT  (命中: npm)
- DOMAIN-SUFFIX,awstar.net,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,eflycloud.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,awsdns-cn-18.biz,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,gacrnd.com,DIRECT  (命中: acr)
- DOMAIN-SUFFIX,ghsmpwalmart.com,DIRECT  (命中: walmart)
- DOMAIN-SUFFIX,shmockup.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,bjwhmedia.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,hmtgo.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,mysecretrainbow.com,DIRECT  (命中: ecr)
- DOMAIN-SUFFIX,hm588.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,xn--nmqp78hmufjwu.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,gamegamept.com,DIRECT  (命中: mega)
- DOMAIN-SUFFIX,tlhmhd.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,natywish.com,DIRECT  (命中: wish)
- DOMAIN-SUFFIX,yytiflytek.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,awsdns-cn-10.com,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,thmnet.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,hhmage.com,DIRECT  (命中: hm)
- DOMAIN,googleoptimize.com,DIRECT  (命中: google)
- DOMAIN,officemktuat.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,awsdns-cn-23.net,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,cmacredit.org,DIRECT  (命中: acr)
- DOMAIN-SUFFIX,brighticecream.com,DIRECT  (命中: ecr)
- DOMAIN-SUFFIX,azuremigratetest.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,ttfly.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,shhmu.net,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,ncjrailway.com,DIRECT  (命中: railway)
- DOMAIN-SUFFIX,awsdns-cn-44.net,DIRECT  (命中: aws)
- DOMAIN,googletagmanager.com,DIRECT  (命中: google)
- DOMAIN-SUFFIX,shms-expo.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,awsdns-cn-24.biz,DIRECT  (命中: aws)
- DOMAIN,cache-management-prod.google.com,DIRECT  (命中: google)
- DOMAIN-SUFFIX,zgzhmz.com,DIRECT  (命中: hm)
- DOMAIN,clickserver.googleads.com,DIRECT  (命中: google)
- DOMAIN,dg-meta.video.google.com,DIRECT  (命中: google)
- DOMAIN-SUFFIX,zhmxchina.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,googlevoice.org,DIRECT  (命中: google)
- DOMAIN-SUFFIX,cnflyinghorse.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,youtube-dubbing.com,DIRECT  (命中: youtube)
- DOMAIN-SUFFIX,iflygse.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,qixingcr.com,DIRECT  (命中: gcr)
- DOMAIN-SUFFIX,kphm88.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,awsdns-cn-37.com,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,fly160.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,3hmlg.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,rainbutterfly.xyz,DIRECT  (命中: fly)
- DOMAIN,ssl-google-analytics.l.google.com,DIRECT  (命中: google)
- DOMAIN-SUFFIX,awsdns-cn-55.com,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,szpowerfly.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,whminwei.com,DIRECT  (命中: hm)
- DOMAIN,download.visualstudio.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,whmama.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,hefeilaws.com,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,chmed.net,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,flymobi.biz,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,hzhm888.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,cqrailway.com,DIRECT  (命中: railway)
- DOMAIN-SUFFIX,wishetin.com,DIRECT  (命中: wish)
- DOMAIN-SUFFIX,whmc2005.com,DIRECT  (命中: hm)
- DOMAIN,googleapis-cn.com,DIRECT  (命中: google)
- DOMAIN-SUFFIX,inflyway.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,myvs.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,awsdns-cn-59.net,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,t-npm.com,DIRECT  (命中: npm)
- DOMAIN-SUFFIX,hmting.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,flyfunny.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,touchmark.art,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,bulbsquare.com,DIRECT  (命中: square)
- DOMAIN-SUFFIX,hmltec.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,flygo.net,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,cloudflareglobal.net,DIRECT  (命中: cloudflare)
- DOMAIN-SUFFIX,xczhmzb.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,hkgcr.com,DIRECT  (命中: gcr)
- DOMAIN-SUFFIX,ecrrc.com,DIRECT  (命中: ecr)
- DOMAIN-SUFFIX,awsdns-cn-61.biz,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,secretmine.net,DIRECT  (命中: ecr)
- DOMAIN-SUFFIX,sfecr.com,DIRECT  (命中: ecr)
- DOMAIN-SUFFIX,awsdns-cn-16.net,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,seaflysoft.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,hmqjsb.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,awsdns-cn-41.com,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,szhmjp.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,lzhmmr.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,hmfxw.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,hmarathon.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,shmet.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,openailab.com,DIRECT  (命中: openai)
- DOMAIN-SUFFIX,cloudflareperf.com,DIRECT  (命中: cloudflare)
- DOMAIN-SUFFIX,nike.host,DIRECT  (命中: nike)
- DOMAIN-SUFFIX,awsdns-cn-22.com,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,fly1999.com,DIRECT  (命中: fly)
- DOMAIN,lexuat.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,secrui.com,DIRECT  (命中: ecr)
- DOMAIN-SUFFIX,ctrender.com,DIRECT  (命中: render)
- DOMAIN-SUFFIX,3richman.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,dcg.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,honchmedia.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,czxthmls.com,DIRECT  (命中: hm)
- DOMAIN,collaborateppe.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,aliexpress.com,DIRECT  (命中: aliexpress)
- DOMAIN-SUFFIX,fhmion.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,surface.downloads.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,iflytek.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,chinamaven.com,DIRECT  (命中: maven)
- DOMAIN-SUFFIX,bjhmyq.com,DIRECT  (命中: hm)
- DOMAIN,windbg.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- URL-REGEX,"^https?:\/\/.+-mihayo\.akamaized\.net.*$",DIRECT  (命中: akamai)
- DOMAIN-SUFFIX,zhmold.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,azure.cc,DIRECT  (命中: azure)
- DOMAIN-SUFFIX,googleyixia.com,DIRECT  (命中: google)
- DOMAIN-SUFFIX,toprender.com,DIRECT  (命中: render)
- DOMAIN-SUFFIX,wodecrowd.com,DIRECT  (命中: ecr)
- DOMAIN,lex.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,acloudrender.com,DIRECT  (命中: render)
- DOMAIN-SUFFIX,qiantangcredit.com,DIRECT  (命中: gcr)
- DOMAIN,volic.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,npmtrend.com,DIRECT  (命中: npm)
- DOMAIN-SUFFIX,awsdns-cn-55.biz,DIRECT  (命中: aws)
- DOMAIN,crashlyticsreports-pa.googleapis.com,DIRECT  (命中: google)
- DOMAIN-SUFFIX,shmama.net,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,hmsemi.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,fishflying.net,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,hmwzjs.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,shmengyang.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,fly139.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,flyai.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,awsdns-cn-51.com,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,iflyink.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,lexuat.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN,avail.googleflights.net,DIRECT  (命中: google)
- DOMAIN,storecorefulfillment.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,elecrystal.com,DIRECT  (命中: ecr)
- DOMAIN-SUFFIX,awsdns-cn-06.net,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,dockerone.com,DIRECT  (命中: docker)
- DOMAIN-SUFFIX,awsdns-cn-02.biz,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,likeaboat2023.com,DIRECT  (命中: ikea)
- DOMAIN-SUFFIX,itfly.net,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,alltechmed.com,DIRECT  (命中: hm)
- DOMAIN,checkin.gstatic.com,DIRECT  (命中: gstatic.com)
- DOMAIN-SUFFIX,02hm.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,jxhmjx.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,awsdns-cn-44.com,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,oemssl.cn.cdn.cloudflare.net,DIRECT  (命中: cloudflare)
- DOMAIN-SUFFIX,fhmv.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,awsdns-cn-36.com,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,hmbzfjt.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,ntrailway.com,DIRECT  (命中: railway)
- DOMAIN-SUFFIX,awsdns-cn-07.net,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,hicnhm.com,DIRECT  (命中: hm)
- DOMAIN,osrelease.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,square16.org,DIRECT  (命中: square)
- DOMAIN-SUFFIX,acrel-eem.com,DIRECT  (命中: acr)
- DOMAIN,qpx.googleflights.net,DIRECT  (命中: google)
- DOMAIN-SUFFIX,hbysfhm.com,DIRECT  (命中: hm)
- DOMAIN,googleoptimize-cn.com,DIRECT  (命中: google)
- DOMAIN-SUFFIX,cloudflare-cn.com,DIRECT  (命中: cloudflare)
- DOMAIN-SUFFIX,ugdocker.link,DIRECT  (命中: docker)
- DOMAIN-SUFFIX,hmlcar.com,DIRECT  (命中: hm)
- DOMAIN,redirector.c.play.google.com,DIRECT  (命中: google)
- DOMAIN-SUFFIX,chihm.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,dhmsnyy.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,edgeone-browser-rendering.com,DIRECT  (命中: render)
- DOMAIN-SUFFIX,cloudflareinsights-cn.com,DIRECT  (命中: cloudflare)
- DOMAIN-SUFFIX,awspony.com,DIRECT  (命中: aws)
- DOMAIN,googleadservices.com,DIRECT  (命中: google)
- DOMAIN-SUFFIX,githubshare.com,DIRECT  (命中: github)
- DOMAIN-SUFFIX,shmljm.com,DIRECT  (命中: hm)
- DOMAIN,surface.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,hmyzs.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,iflyaiedu.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,ghmba.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,awsdns-cn-39.com,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,nnpml.com,DIRECT  (命中: npm)
- DOMAIN-SUFFIX,awsdns-cn-26.com,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,whmeigao.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,megaemoji.com,DIRECT  (命中: mega)
- DOMAIN-SUFFIX,awsonamazon.com,DIRECT  (命中: amazon)
- DOMAIN,msproduct.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,unpmcc.com,DIRECT  (命中: npm)
- DOMAIN-SUFFIX,sxhm.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,gxhmdjt.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,netsyq.com,DIRECT  (命中: etsy)
- DOMAIN-SUFFIX,xhma.com,DIRECT  (命中: hm)
- DOMAIN,officecdn.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,jhmnew.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,aflytec.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,vultrcn.com,DIRECT  (命中: vultr)
- DOMAIN-SUFFIX,wish3d.com,DIRECT  (命中: wish)
- DOMAIN-SUFFIX,smogfly.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,awsdns-cn-45.biz,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,mcohmygod.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,megagamelog.com,DIRECT  (命中: mega)
- DOMAIN-SUFFIX,ovhlb.com,DIRECT  (命中: ovh)
- DOMAIN-SUFFIX,secretflow.com,DIRECT  (命中: ecr)
- DOMAIN-SUFFIX,zbwhmedia.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,smogflycloud.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,mpnbenefits.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,hmxixie.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,gdlinefly.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,macrowing.com,DIRECT  (命中: acr)
- DOMAIN-SUFFIX,awsdns-cn-49.biz,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,machenike.com,DIRECT  (命中: nike)
- DOMAIN-SUFFIX,appsflyer-cn.com,DIRECT  (命中: fly)
- DOMAIN,azuremigrate.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,bjhdhm.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,awsdns-cn-12.biz,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,awsdns-cn-20.biz,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,ghmcchina.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,qjhm.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,awsdns-cn-20.net,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,iflynote.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,abcdocker.com,DIRECT  (命中: docker)
- DOMAIN,pki-goog.l.google.com,DIRECT  (命中: google)
- DOMAIN-SUFFIX,awsdns-cn-14.com,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,hmnst.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,beijing-hmo.com,DIRECT  (命中: hm)
- URL-REGEX,"^https?:\/\/.+\.awsdns-cn-[0-9][0-9]\.(biz|com|net|top).*$",DIRECT  (命中: aws)
- DOMAIN-SUFFIX,tinsecret.com,DIRECT  (命中: ecr)
- DOMAIN-SUFFIX,bmp.ovh,DIRECT  (命中: ovh)
- DOMAIN-SUFFIX,lex.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,chinacrt.com,DIRECT  (命中: acr)
- DOMAIN,oemsoc.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,lawsdata.com,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,whmnx.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,megagenchina.com,DIRECT  (命中: mega)
- DOMAIN-SUFFIX,awsdns-cn-21.net,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,azurestackhubuat.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,flymeauto.com,DIRECT  (命中: fly)
- DOMAIN,cdn.globalsigncdn.com.cdn.cloudflare.net,DIRECT  (命中: cloudflare)
- DOMAIN-SUFFIX,awsdns-cn-31.net,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,vz.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,ghmd448.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,kindechem.com,DIRECT  (命中: kinde)
- DOMAIN-SUFFIX,awsdns-cn-38.net,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,zchmbx.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,tecreal.com,DIRECT  (命中: ecr)
- DOMAIN-SUFFIX,jxhmxxjs.com,DIRECT  (命中: hm)
- DOMAIN,firebase-settings.crashlytics.com,DIRECT  (命中: firebase)
- DOMAIN-SUFFIX,whmoocs.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,awsdns-cn-40.net,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,awsdns-cn-47.net,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,secretgardenresorts.com,DIRECT  (命中: ecr)
- DOMAIN-SUFFIX,flysand.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,mecru.com,DIRECT  (命中: ecr)
- DOMAIN-SUFFIX,whmvc.net,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,thmz.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,awsdns-cn-48.com,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,googlenav.com,DIRECT  (命中: google)
- DOMAIN-SUFFIX,awsdns-cn-17.biz,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,hmgbtv.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,smogflycloud.net,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,azureflame.cloud,DIRECT  (命中: azure)
- DOMAIN-SUFFIX,htyhm.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,asosoaiid.com,DIRECT  (命中: asos)
- DOMAIN-SUFFIX,ideacreated.com,DIRECT  (命中: acr)
- DOMAIN-SUFFIX,awspaas.com,DIRECT  (命中: aws)
- DOMAIN,googletagservices-cn.com,DIRECT  (命中: google)
- DOMAIN-SUFFIX,lnwish.com,DIRECT  (命中: wish)
- DOMAIN,redirector.c.chat.google.com,DIRECT  (命中: google)
- DOMAIN-SUFFIX,qeoagphm.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,gemini530.net,DIRECT  (命中: gemini)
- DOMAIN-SUFFIX,lhmp.cc,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,elongstatic.com,DIRECT  (命中: gstatic.com)
- DOMAIN-SUFFIX,oemsoc.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,yingyecraft.com,DIRECT  (命中: ecr)
- DOMAIN-SUFFIX,whmf8.com,DIRECT  (命中: hm)
- DOMAIN,oemsocuat.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,ylxhmy.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,ceolaws.net,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,cloudflare.fun,DIRECT  (命中: cloudflare)
- DOMAIN,safebrowsing.googleapis.com,DIRECT  (命中: google)
- DOMAIN-SUFFIX,awsdns-cn-27.biz,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,imags-google.com,DIRECT  (命中: google)
- DOMAIN-SUFFIX,sectigochina.com.cdn.cloudflare.net,DIRECT  (命中: cloudflare)
- DOMAIN-SUFFIX,azure-wave.com,DIRECT  (命中: azure)
- DOMAIN,azurestackhubuat.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,qdhmsoft.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,hmus.net,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,shmog.org,DIRECT  (命中: hm)
- DOMAIN,download.mlcc.google.com,DIRECT  (命中: google)
- DOMAIN-SUFFIX,vultrvps.com,DIRECT  (命中: vultr)
- DOMAIN-SUFFIX,51google.com,DIRECT  (命中: google)
- DOMAIN-SUFFIX,mpnbenefitsrtluat.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,awsdns-cn-28.biz,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,awsdns-cn-18.net,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,volcecr.com,DIRECT  (命中: ecr)
- DOMAIN-SUFFIX,24hmb.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,bjhmdkj.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,awsdns-cn-40.biz,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,ahmwgroup.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,protong.com,DIRECT  (命中: proton)
- DOMAIN-SUFFIX,wishcad.com,DIRECT  (命中: wish)
- DOMAIN-SUFFIX,wecrm.com,DIRECT  (命中: ecr)
- DOMAIN-SUFFIX,awsdns-cn-17.net,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,whmnrc.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,bebhmongb.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,vscode.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,railwaybill.com,DIRECT  (命中: railway)
- DOMAIN-SUFFIX,oneflys.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,flygon.net,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,hmedu.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,eflybird.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,techmiao.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,awsdns-cn-07.biz,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,chinacrane.net,DIRECT  (命中: acr)
- DOMAIN-SUFFIX,zxhmjj.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,iflyrec.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,englishmasterclub.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,i-firefly.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,lzarays.com,DIRECT  (命中: zara)
- DOMAIN-SUFFIX,smogfly.cloud,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,shmds.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,awsdns-cn-45.net,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,awsdns-cn-41.net,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,gogofly.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,hmf-china.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,macrosan.com,DIRECT  (命中: acr)
- DOMAIN,itacademy.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,awsdns-cn-47.com,DIRECT  (命中: aws)
- DOMAIN,storeedge.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,dagongcredit.com,DIRECT  (命中: gcr)
- DOMAIN,googletagservices.com,DIRECT  (命中: google)
- DOMAIN-SUFFIX,njnaws.com,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,thwgetsy.com,DIRECT  (命中: etsy)
- DOMAIN-SUFFIX,weflywifi.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,9125flying.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,hmrsrc.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,sdhmjt.net,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,drugoogle.com,DIRECT  (命中: google)
- DOMAIN-SUFFIX,acrel-znyf.com,DIRECT  (命中: acr)
- DOMAIN-SUFFIX,ovhlb.net,DIRECT  (命中: ovh)
- DOMAIN-SUFFIX,shmhtv.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,fawsoft.com,DIRECT  (命中: aws)
- DOMAIN,g3.gstatic.com,DIRECT  (命中: gstatic.com)
- DOMAIN-SUFFIX,sunnyfly.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,lzbhmy.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,hmchina.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,cdnhwcohm19.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,shhmbio.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,flytcloud.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,awsdns-cn-59.biz,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,gdsunfly.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,rushmail.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,omegatravel.net,DIRECT  (命中: mega)
- DOMAIN,mpnbenefitsrtl.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,51render.com,DIRECT  (命中: render)
- DOMAIN-SUFFIX,sheinet.com,DIRECT  (命中: shein)
- DOMAIN-SUFFIX,awsdns-cn-23.com,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,chinaacryl.com,DIRECT  (命中: acr)
- DOMAIN,googlesyndication.com,DIRECT  (命中: google)
- DOMAIN,fontfiles.googleapis.com,DIRECT  (命中: google)
- DOMAIN-SUFFIX,awsamazonlab.com,DIRECT  (命中: amazon)
- DOMAIN,wear.googleapis.com,DIRECT  (命中: google)
- DOMAIN-SUFFIX,awsdns-cn-63.net,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,shmzgroup.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,algorithmart.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,awsdns-cn-05.net,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,xrender.com,DIRECT  (命中: render)
- DOMAIN-SUFFIX,awsdns-cn-54.net,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,czhmjx.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,chmecc.org,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,gyhm.cc,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,3hmedicalgroup.com,DIRECT  (命中: hm)
- DOMAIN,time.amazonaws.cn,DIRECT  (命中: amazon)
- DOMAIN-SUFFIX,chmod0777kk.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,zjecredit.org,DIRECT  (命中: ecr)
- DOMAIN-SUFFIX,flyme.com,DIRECT  (命中: fly)
- DOMAIN,update.googleapis.com,DIRECT  (命中: google)
- DOMAIN-SUFFIX,hearfly.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,officemktuat.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN,gs-loc-cn.apple.com,DIRECT  (命中: 强制代理域名)
- DOMAIN-SUFFIX,ahmky.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,cnpmjs.org,DIRECT  (命中: npm)
- DOMAIN-SUFFIX,hnlshm.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,ayhmjy.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,flyingeffect.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,lubanpm.com,DIRECT  (命中: npm)
- DOMAIN-SUFFIX,awsdns-cn-58.net,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,oacrm.com,DIRECT  (命中: acr)
- DOMAIN-SUFFIX,mpnbenefitsrtl.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,flyneutron.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,flymeyun.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,hbhmxx.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,asosde.com,DIRECT  (命中: asos)
- DOMAIN,www-google-analytics.l.google.com,DIRECT  (命中: google)
- DOMAIN-SUFFIX,iflyresearch.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,whmzkf.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,d5render.com,DIRECT  (命中: render)
- DOMAIN-SUFFIX,msdn.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,megarobo.com,DIRECT  (命中: mega)
- DOMAIN-SUFFIX,awsdns-cn-16.biz,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,microsoftuwp.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,windbg.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,awsdns-cn-53.com,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,aquayee.com,DIRECT  (命中: quay)
- DOMAIN,myvs.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,4hmodel.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,southmoney.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,edrawsoft.com,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,whmxrj.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,bghmj.com,DIRECT  (命中: hm)
- DOMAIN,googleadservices-cn.com,DIRECT  (命中: google)
- DOMAIN-SUFFIX,hmgreat.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,shtimessquare.com,DIRECT  (命中: square)
- DOMAIN-SUFFIX,zhmodaoli.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,oemsocuat.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,hmeili.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,hmz8.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,nikefans.com,DIRECT  (命中: nike)
- DOMAIN-SUFFIX,chinacrosspoint.com,DIRECT  (命中: acr)
- DOMAIN-SUFFIX,hhmajiang.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,acrossmetals.com,DIRECT  (命中: acr)
- DOMAIN-SUFFIX,awsdns-cn-62.net,DIRECT  (命中: aws)
- DOMAIN,cache.pack.google.com,DIRECT  (命中: google)
- DOMAIN-SUFFIX,digcredit.com,DIRECT  (命中: gcr)
- DOMAIN-SUFFIX,megasig.com,DIRECT  (命中: mega)
- DOMAIN-SUFFIX,hmtnew.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,iqhmh.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,aliexpress-media.com,DIRECT  (命中: aliexpress)
- DOMAIN-SUFFIX,hmxx.net,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,flyingpigeon1936.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,zgxhm.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,fishmobi.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,qmacro.com,DIRECT  (命中: acr)
- DOMAIN-SUFFIX,syfly007.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,aftersale-amazon.com,DIRECT  (命中: amazon)
- DOMAIN,csi.gstatic.com,DIRECT  (命中: gstatic.com)
- DOMAIN-SUFFIX,pihmh.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,dmhmusic.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,chmia.org,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,awsdns-cn-52.net,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,mysecrettop.com,DIRECT  (命中: ecr)
- DOMAIN-SUFFIX,renderbus.com,DIRECT  (命中: render)
- DOMAIN-SUFFIX,collaborateppe.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,hmhpay.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,awsdns-cn-41.biz,DIRECT  (命中: aws)
- DOMAIN,vlportal.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,shmaur.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,3zhm.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,awsdns-cn-60.com,DIRECT  (命中: aws)
- DOMAIN,download.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,pmphmooc.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,myhm.org,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,bixuecrm.com,DIRECT  (命中: ecr)
- DOMAIN,g2.gstatic.com,DIRECT  (命中: gstatic.com)
- DOMAIN-SUFFIX,withmedia.net,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,awsdns-cn-50.biz,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,hellogitlab.com,DIRECT  (命中: gitlab)
- DOMAIN-SUFFIX,awsdns-cn-24.com,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,macrounion.com,DIRECT  (命中: acr)
- DOMAIN-SUFFIX,qhmsg.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,glflyy.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,awsdns-cn-40.com,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,awsdns-cn-05.biz,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,ztrhmall.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,acrel-microgrid.com,DIRECT  (命中: acr)
- DOMAIN-SUFFIX,wecrm.net,DIRECT  (命中: ecr)
- DOMAIN-SUFFIX,awsdns-vip.com,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,aliexpress.us,DIRECT  (命中: aliexpress)
- DOMAIN-SUFFIX,jyhmz.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,codeflying.net,DIRECT  (命中: fly)
- DOMAIN,azuremigratetest.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,awsdns-cn-33.biz,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,flypy.cc,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,awsdns-cn-58.biz,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,shmhzp.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,smogfly.club,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,1fly.fun,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,fulinpm.com,DIRECT  (命中: npm)
- DOMAIN-SUFFIX,aliexpress.ru,DIRECT  (命中: aliexpress)
- DOMAIN-SUFFIX,qhm123.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,msproduct.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,iflytektstd.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,hm025.com,DIRECT  (命中: hm)
- DOMAIN,imasdk.googleapis.com,DIRECT  (命中: google)
- DOMAIN,clientservices.googleapis.com,DIRECT  (命中: google)
- DOMAIN-SUFFIX,bjhmcm.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,fireflyacg.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,e-flyinc.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,citichmc.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,macrolake.com,DIRECT  (命中: acr)
- DOMAIN-SUFFIX,fhmooc.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,shmedia.tech,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,vdfly.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,esdhm.net,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,gxlzhm.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,hmj666.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,thmovie.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,msdprod-ad.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,whmnls.com,DIRECT  (命中: hm)
- DOMAIN,googlevads-cn.com,DIRECT  (命中: google)
- DOMAIN-SUFFIX,awsdns-cn-52.com,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,haitianpm.com,DIRECT  (命中: npm)
- DOMAIN-SUFFIX,jcodecraeer.com,DIRECT  (命中: ecr)
- DOMAIN,download.tensorflow.google.com,DIRECT  (命中: google)
- DOMAIN-SUFFIX,hmszkj.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,xahmqy.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,awsdns-cn-28.net,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,iflyread.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,hwrecruit.com,DIRECT  (命中: ecr)
- DOMAIN-SUFFIX,minecraftxz.com,DIRECT  (命中: ecr)
- DOMAIN,azurestackhub.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,ihmch.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,webclose-whatsapp.com,DIRECT  (命中: whatsapp)
- DOMAIN-SUFFIX,awsdns-cn-57.com,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,testshm.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,squarecn.com,DIRECT  (命中: square)
- DOMAIN-SUFFIX,zchmh.com,DIRECT  (命中: hm)
- DOMAIN,ssl.gstatic.com,DIRECT  (命中: gstatic.com)
- DOMAIN-SUFFIX,chmgames.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,hmrczp.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,oecr.com,DIRECT  (命中: ecr)
- DOMAIN-SUFFIX,airtofly.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,iva-schmetz.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,secrss.com,DIRECT  (命中: ecr)
- DOMAIN-SUFFIX,surface.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,awsdns-cn-36.net,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,luxtarget.com,DIRECT  (命中: target)
- DOMAIN-SUFFIX,victoriassecretclearance.online,DIRECT  (命中: ecr)
- DOMAIN-SUFFIX,awsdns-cn-56.biz,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,targetportion.com,DIRECT  (命中: target)
- DOMAIN-SUFFIX,hmplay.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,chinaflashmarket.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,t-firefly.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,hfhm.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,chinacrops.org,DIRECT  (命中: acr)
- DOMAIN-SUFFIX,macrosilicon.com,DIRECT  (命中: acr)
- DOMAIN-SUFFIX,megajoy.com,DIRECT  (命中: mega)
- DOMAIN-SUFFIX,bshmzx.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,flysheeep.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,zhmu.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,mbs.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN,redirector.c.youtubeeducation.com,DIRECT  (命中: youtube)
- DOMAIN-SUFFIX,shmetro.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,flylinking.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,hm120.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,cuahmap.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,hminvestment.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,chinacreator.com,DIRECT  (命中: acr)
- DOMAIN-SUFFIX,yhchmo.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,awsdns-cn-02.net,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,awsdns-cn-47.biz,DIRECT  (命中: aws)
- DOMAIN,software.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,gzrecruit.com,DIRECT  (命中: ecr)
- DOMAIN-SUFFIX,lzghmy.com,DIRECT  (命中: hm)
- DOMAIN,cbdstest.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,hmly666.cc,DIRECT  (命中: hm)
- DOMAIN,vz.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,rsm.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,smogfly.net,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,shmaas.net,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,gzhm.com,DIRECT  (命中: hm)
- DOMAIN,redirector.c.pack.google.com,DIRECT  (命中: google)
- DOMAIN-SUFFIX,wishisp.com,DIRECT  (命中: wish)
- DOMAIN-SUFFIX,hm-optics.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,itgemini.net,DIRECT  (命中: gemini)
- DOMAIN-SUFFIX,awsdns-cn-00.com,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,awsdns-cn-56.net,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,awsdns-cn-25.net,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,npmmirror.com,DIRECT  (命中: npm)
- DOMAIN-SUFFIX,awsdns-cn-25.com,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,cloudhvacr.com,DIRECT  (命中: acr)
- DOMAIN-SUFFIX,flyertea.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,dreamsparkuat.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,dhmeri.com,DIRECT  (命中: hm)
- DOMAIN,googleflights-cn.net,DIRECT  (命中: google)
- DOMAIN-SUFFIX,awsdns-cn-50.net,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,qflyinc.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,athmapp.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,applysquare.net,DIRECT  (命中: square)
- DOMAIN-SUFFIX,bzmhm.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,hifly.mobi,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,hmmachine.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,xn--vhq4ut2dsxd5xqnicjxxo55a756aovhik0aunm.com,DIRECT  (命中: ovh)
- DOMAIN-SUFFIX,protontechcn.com,DIRECT  (命中: proton)
- DOMAIN-SUFFIX,awsdns-cn-58.com,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,cproton.com,DIRECT  (命中: proton)
- DOMAIN-SUFFIX,gx-hm.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,cloudflarestaging.com,DIRECT  (命中: cloudflare)
- DOMAIN-SUFFIX,dreamspark.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,flyml.net,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,glhmmr.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,awsdns-cn-27.com,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,qihangcrrc.com,DIRECT  (命中: gcr)
- DOMAIN-SUFFIX,techmoris.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,macrr.com,DIRECT  (命中: acr)
- DOMAIN-SUFFIX,cacre.org,DIRECT  (命中: acr)
- DOMAIN-SUFFIX,fly63.com,DIRECT  (命中: fly)
- DOMAIN,googleapps-cn.com,DIRECT  (命中: google)
- DOMAIN-SUFFIX,macrozheng.com,DIRECT  (命中: acr)
- DOMAIN-SUFFIX,oktamall.com,DIRECT  (命中: okta)
- DOMAIN-SUFFIX,hbhml.com,DIRECT  (命中: hm)
- DOMAIN,tac.googleapis.com,DIRECT  (命中: google)
- DOMAIN-SUFFIX,collaborate.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,cloudflarestoragegw.com,DIRECT  (命中: cloudflare)
- DOMAIN-SUFFIX,googleppy.com,DIRECT  (命中: google)
- DOMAIN-SUFFIX,awsdns-cn-55.net,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,awsdns-cn-63.biz,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,awsdns-cn-44.biz,DIRECT  (命中: aws)
- DOMAIN,g0.gstatic.com,DIRECT  (命中: gstatic.com)
- DOMAIN-SUFFIX,mikecrm.com,DIRECT  (命中: ecr)
- DOMAIN-SUFFIX,sphmc.org,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,hmadgz.com,DIRECT  (命中: hm)
- DOMAIN,google-analytics.com,DIRECT  (命中: google)
- DOMAIN-SUFFIX,uuu.ovh,DIRECT  (命中: ovh)
- DOMAIN-SUFFIX,yfldocker.com,DIRECT  (命中: docker)
- DOMAIN-SUFFIX,mrwish.net,DIRECT  (命中: wish)
- DOMAIN,vscode.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,dylyghm.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,akamai.com,DIRECT  (命中: akamai)
- DOMAIN-SUFFIX,lhmj.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,fly84.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,yzhmyy.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,moonfly.net,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,awsdns-cn-54.biz,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,cloudflareip.com,DIRECT  (命中: cloudflare)
- DOMAIN-SUFFIX,cloudfront-cn.net,DIRECT  (命中: cloudfront)
- DOMAIN,googletagmanager-cn.com,DIRECT  (命中: google)
- DOMAIN-SUFFIX,1818hm.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,orasos.com,DIRECT  (命中: asos)
- DOMAIN,gs-loc.apple.com,DIRECT  (命中: 强制代理域名)
- DOMAIN-SUFFIX,googlebbs.net,DIRECT  (命中: google)
- DOMAIN-SUFFIX,volic.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN,msdprod-ad.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,officemkt.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,zhinikefu.com,DIRECT  (命中: nike)
- DOMAIN-SUFFIX,awsdns-cn-21.biz,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,hmzs.net,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,hm152n.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,facri.com,DIRECT  (命中: acr)
- DOMAIN-SUFFIX,cn-railway.net,DIRECT  (命中: railway)
- DOMAIN,mpnbenefits.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,renderincloud.com,DIRECT  (命中: render)
- DOMAIN-SUFFIX,iflydatahub.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,whichmba.net,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,hf-iflysse.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,bwfhmall.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,whmj.org,DIRECT  (命中: hm)
- DOMAIN,safebrowsing-cache.google.com,DIRECT  (命中: google)
- DOMAIN-SUFFIX,hm16888.net,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,zhmzqi.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,awsdns-cn-12.net,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,znhhmedical.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,cqhma.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,daiwofly.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,osrelease.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,awsdns-cn-11.com,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,google-hub.com,DIRECT  (命中: google)
- DOMAIN-SUFFIX,awsdns-cn-22.net,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,download.visualstudio.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN,dreamsparkuat.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,magentochina.org,DIRECT  (命中: magento)
- DOMAIN-SUFFIX,squarefong.com,DIRECT  (命中: square)
- DOMAIN-SUFFIX,rohm-chip.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,hifly.tv,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,shmbjy.org,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,awsdns-cn-42.com,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,awsdns-cn-09.net,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,hmoe.link,DIRECT  (命中: hm)
- DOMAIN,mpnbenefitsrtluat.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,hmx-led.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,originalkindergarten.com,DIRECT  (命中: kinde)
- DOMAIN-SUFFIX,flymopaper.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,awsdns-cn-48.net,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,awsdns-cn-62.com,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,chinawssdxh.com,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,shmfmr.net,DIRECT  (命中: hm)
- DOMAIN,www.gstatic.com,DIRECT  (命中: gstatic.com)
- DOMAIN-SUFFIX,zzfly.net,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,awsdns-cn-09.biz,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,awsdns-cn-42.biz,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,hm-3223.net,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,qzynhhmm.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,megahugo.net,DIRECT  (命中: mega)
- DOMAIN-SUFFIX,awsdns-cn-63.com,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,hm5988.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,bfhmj.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,chinacraa.org,DIRECT  (命中: acr)
- DOMAIN-SUFFIX,hmzixin.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,sdhmdp.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,openai.wf,DIRECT  (命中: openai)
- DOMAIN-SUFFIX,whuznhmedj.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,awsdns-cn-35.net,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,thmall.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,hmzhtc.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,cloudflareprod.com,DIRECT  (命中: cloudflare)
- DOMAIN-SUFFIX,officecdn.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,thmzedu.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,hfly.net,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,gxhhmed.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,simplecreator.net,DIRECT  (命中: ecr)
- DOMAIN-SUFFIX,hmgj.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,telegramtoke.com,DIRECT  (命中: telegram)
- DOMAIN-SUFFIX,xn--vhqqbz2p62hm92e04p.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,iflyiot.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,2google.com,DIRECT  (命中: google)
- DOMAIN-SUFFIX,hlnpm.com,DIRECT  (命中: npm)
- DOMAIN-SUFFIX,hyahm.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,likeacg.com,DIRECT  (命中: ikea)
- DOMAIN-SUFFIX,haofly.net,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,xawscu.com,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,52kfly.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,mikeauth.com,DIRECT  (命中: ikea)
- DOMAIN-SUFFIX,sun-wish.com,DIRECT  (命中: wish)
- DOMAIN-SUFFIX,armfly.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,iflyhealth.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,hmtrhf.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,surface-microsoftstore.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,chatgptboke.com,DIRECT  (命中: chatgpt)
- DOMAIN-SUFFIX,724pridecryogenics.com,DIRECT  (命中: ecr)
- DOMAIN-SUFFIX,minecraftzw.com,DIRECT  (命中: ecr)
- DOMAIN-SUFFIX,dockerinfo.net,DIRECT  (命中: docker)
- DOMAIN,googleanalytics.com,DIRECT  (命中: google)
- DOMAIN,rsm.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN,googletraveladservices-cn.com,DIRECT  (命中: google)
- DOMAIN-SUFFIX,edgeone-browser-rendering-dev.com,DIRECT  (命中: render)
- DOMAIN-SUFFIX,neihanfly.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,chiconysquare.com,DIRECT  (命中: square)
- DOMAIN-SUFFIX,iflydocs.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,gemini-galaxy.com,DIRECT  (命中: gemini)
- DOMAIN,redirector.c.mail.google.com,DIRECT  (命中: google)
- DOMAIN-SUFFIX,91hmi.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,chinahvacr.com,DIRECT  (命中: acr)
- DOMAIN-SUFFIX,whhmmbl.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,jhqshfly.com,DIRECT  (命中: fly)
- DOMAIN,googlesyndication-cn.com,DIRECT  (命中: google)
- DOMAIN-SUFFIX,hmqg.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,fly998.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,dl.delivery.mp.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,awsdns-cn-60.net,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,awsdns-cn-34.com,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,awsdns-cn-36.biz,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,hmlan.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,hmkp.org,DIRECT  (命中: hm)
- DOMAIN,collaborate.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,thmins.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,azuremigrate.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,zhmedcenter.com,DIRECT  (命中: hm)
- DOMAIN,dl.l.google.com,DIRECT  (命中: google)
- DOMAIN-SUFFIX,awsdns-cn-48.biz,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,jiansujihm.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,awsdns-cn-33.net,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,zhmf.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,whmylike.cc,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,yhm11.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,awsdns-cn-04.net,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,fly-exp.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,facebooksx.com,DIRECT  (命中: facebook)
- DOMAIN-SUFFIX,seersecret.com,DIRECT  (命中: ecr)
- DOMAIN-SUFFIX,awsdns-cn-62.biz,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,azuretouch.net,DIRECT  (命中: azure)
- DOMAIN-SUFFIX,yjdatasos.com,DIRECT  (命中: asos)
- DOMAIN-SUFFIX,pkulaws.com,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,chnrailway.com,DIRECT  (命中: railway)
- DOMAIN-SUFFIX,jshmrcb.com,DIRECT  (命中: hm)
- DOMAIN,dl.google.com,DIRECT  (命中: google)
- DOMAIN-SUFFIX,macroprocess.com,DIRECT  (命中: acr)
- DOMAIN-SUFFIX,awsdns-cn-14.biz,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,happypingpang.com,DIRECT  (命中: pypi)
- DOMAIN-SUFFIX,ahmif.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,hyundai-hmtc.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,lgstatic.com,DIRECT  (命中: gstatic.com)
- DOMAIN-SUFFIX,wishdown.com,DIRECT  (命中: wish)
- DOMAIN-SUFFIX,tokenrhythm.studio,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,awsdns-cn-09.com,DIRECT  (命中: aws)
- DOMAIN,google-analytics-cn.com,DIRECT  (命中: google)
- DOMAIN-SUFFIX,shmarathon.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,awsdns-cn-51.biz,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,chmti.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,weighment.com,DIRECT  (命中: hm)
- DOMAIN,officemkt.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,cheetahmobile.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,rcolab.com,DIRECT  (命中: colab)
- DOMAIN,images-cn.ssl-images-amazon.com,DIRECT  (命中: amazon)
- DOMAIN-SUFFIX,nhmuni.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,awsdns-cn-34.net,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,wish-hightech.com,DIRECT  (命中: wish)
- DOMAIN-SUFFIX,tshmkj.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,awsdns-cn-45.com,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,awsdns-cn-19.biz,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,tb-whatsapp.com,DIRECT  (命中: whatsapp)
- DOMAIN-SUFFIX,njhmmr.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,elitecrm.com,DIRECT  (命中: ecr)
- DOMAIN-SUFFIX,phmacn.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,ifireflygame.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,wbecrisfro.com,DIRECT  (命中: ecr)
- DOMAIN-SUFFIX,awsdns-cn-17.com,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,shlawserve.com,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,ecr-global.com,DIRECT  (命中: ecr)
- DOMAIN-SUFFIX,cbdstest.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,hmwdj.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,feidacrusher.com,DIRECT  (命中: acr)
- DOMAIN-SUFFIX,shmtu.net,DIRECT  (命中: hm)
- DOMAIN,pagead-googlehosted.l.google.com,DIRECT  (命中: google)
- URL-REGEX,"^https?:\/\/.+\.awsdns-cn-[0-9][a-e0-9]\.cn.*$",DIRECT  (命中: aws)
- DOMAIN-SUFFIX,awsdns-cn-07.com,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,awsdns-cn-39.net,DIRECT  (命中: aws)
- DOMAIN,mbs.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,shmusic.org,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,itacademyuat.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,officebay.net,DIRECT  (命中: ebay)
- DOMAIN,tools.google.com,DIRECT  (命中: google)
- DOMAIN-SUFFIX,itacademy.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,yz-proton.com,DIRECT  (命中: proton)
- DOMAIN-SUFFIX,flycua.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,storecorefulfillment.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,iflysec.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,flyco.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,nnhmcj.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,flyenglish.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,gdhmgc.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,shmondial.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,whmlcy.net,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,hlhmf.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,awsdns-cn-20.com,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,hbhm.net,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,arefly.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,gxhmba.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,hmjc.org,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,flyme.net,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,xhmedia.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,chmc.cc,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,software.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,awsdns-cn-43.biz,DIRECT  (命中: aws)
- DOMAIN,adservice.google.com,DIRECT  (命中: google)
- DOMAIN-SUFFIX,awsdns-cn-24.net,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,xhmwxy.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,hnsyhm.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,dragonfly.fun,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,awsdns-cn-46.com,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,cloudflarecn.net,DIRECT  (命中: cloudflare)
- DOMAIN-SUFFIX,sharjahmadrasa.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,grender.com,DIRECT  (命中: render)
- DOMAIN-SUFFIX,lenovo.com.cdn.cloudflare.net,DIRECT  (命中: cloudflare)
- DOMAIN,g1.gstatic.com,DIRECT  (命中: gstatic.com)
- DOMAIN-SUFFIX,cofly.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,awsdns-cn-35.biz,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,nike666.com,DIRECT  (命中: nike)
- DOMAIN-SUFFIX,flashmemoryworld.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,gshmhotels.com,DIRECT  (命中: hm)
- DOMAIN,gstaticadssl.l.google.com,DIRECT  (命中: google)
- DOMAIN-SUFFIX,iflyadx.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,ucfly.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,chinaws.net,DIRECT  (命中: aws)
- DOMAIN,sdx.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,azureflying.com,DIRECT  (命中: azure)
- DOMAIN-SUFFIX,iwishwed.com,DIRECT  (命中: wish)
- DOMAIN,googletraveladservices.com,DIRECT  (命中: google)
- DOMAIN-SUFFIX,flyfishx.com,DIRECT  (命中: fly)
- DOMAIN,storeedgefd.dsx.mp.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,szhmkeji.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,cdnchatgpt.com,DIRECT  (命中: chatgpt)
- DOMAIN,msdn.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN,dreamspark.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,megawords.cc,DIRECT  (命中: mega)
- DOMAIN-SUFFIX,bbgstatic.com,DIRECT  (命中: gstatic.com)
- DOMAIN-SUFFIX,cloudflareanycast.net,DIRECT  (命中: cloudflare)
- DOMAIN-SUFFIX,iflytoy.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,jinshmgw.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,ddwhm.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,mightsquare.com,DIRECT  (命中: square)
- DOMAIN-SUFFIX,awsdns-cn-39.biz,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,awsdns-cn-19.net,DIRECT  (命中: aws)
- DOMAIN,c.android.clients.google.com,DIRECT  (命中: google)
- DOMAIN-SUFFIX,c-thme.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,jdhmediajd.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,whoami.akamai.net,DIRECT  (命中: akamai)
- DOMAIN-SUFFIX,flyadx.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,haiqianghm.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,awsdns-cn-60.biz,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,azurestackhub.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,awsdns-cn-00.net,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,forcecreat.com,DIRECT  (命中: ecr)
- DOMAIN-SUFFIX,openai-hub.com,DIRECT  (命中: openai)
- DOMAIN-SUFFIX,vlportal.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN,images-cn-8.ssl-images-amazon.com,DIRECT  (命中: amazon)
- DOMAIN-SUFFIX,zjgcreative.com,DIRECT  (命中: gcr)
- DOMAIN-SUFFIX,hmxw.com,DIRECT  (命中: hm)
- DOMAIN,www-googletagmanager.l.google.com,DIRECT  (命中: google)
- DOMAIN-SUFFIX,welchmat.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,qualcomm.cn.cdn.cloudflare.net,DIRECT  (命中: cloudflare)
- DOMAIN,itacademyuat.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,flyhand.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,awsdns-cn-46.net,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,awsdns-cn-46.biz,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,shmengzhong.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,awsdns-cn-15.net,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,fingerflyapp.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,shmds.vip,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,shmusicschool.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,awsdns-cn-37.net,DIRECT  (命中: aws)
- DOMAIN,performanceparameters.googleapis.com,DIRECT  (命中: google)
- DOMAIN-SUFFIX,hmzhtc.cc,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,githubim.com,DIRECT  (命中: github)
- DOMAIN-SUFFIX,imgs.ovh,DIRECT  (命中: ovh)
```
</details>

### 🧹 直连规则去重删除（共 262 条）

**处理动作**：同一域名、同一策略的重复规则已删除，只保留一条；跨策略的不删。

<details>
<summary>展开查看去重样例（前 20 条）</summary>

```
- DOMAIN,p9-juejin.byteimg.com,DIRECT  （被同策略父级 DOMAIN-SUFFIX,byteimg.com 覆盖）
- DOMAIN,opencourse.pku.edu.cn,DIRECT  （被同策略父级 DOMAIN-SUFFIX,cn 覆盖）
- DOMAIN,www.entrust.cn,DIRECT  （被同策略父级 DOMAIN-SUFFIX,cn 覆盖）
- DOMAIN,ss.bjmu.edu.cn,DIRECT  （被同策略父级 DOMAIN-SUFFIX,cn 覆盖）
- DOMAIN,swscan.apple.com,DIRECT  （被同策略父级 DOMAIN-SUFFIX,apple.com 覆盖）
- DOMAIN,ipcdn.apple.com,DIRECT  （被同策略父级 DOMAIN-SUFFIX,apple.com 覆盖）
- DOMAIN,itunesconnect.apple.com,DIRECT  （被同策略父级 DOMAIN-SUFFIX,apple.com 覆盖）
- DOMAIN,p06.upd.kaspersky.com,DIRECT  （被同策略父级 DOMAIN-SUFFIX,upd.kaspersky.com 覆盖）
- DOMAIN,api-edge.apps.apple.com,DIRECT  （被同策略父级 DOMAIN-SUFFIX,apple.com 覆盖）
- DOMAIN,osxapps.itunes.apple.com,DIRECT  （被同策略父级 DOMAIN-SUFFIX,apple.com 覆盖）
- DOMAIN,s16.upd.kaspersky.com,DIRECT  （被同策略父级 DOMAIN-SUFFIX,upd.kaspersky.com 覆盖）
- DOMAIN,devimages-cdn.apple.com,DIRECT  （被同策略父级 DOMAIN-SUFFIX,apple.com 覆盖）
- DOMAIN,amp-api.podcasts.apple.com,DIRECT  （被同策略父级 DOMAIN-SUFFIX,apple.com 覆盖）
- DOMAIN,p14.upd.kaspersky.com,DIRECT  （被同策略父级 DOMAIN-SUFFIX,upd.kaspersky.com 覆盖）
- DOMAIN,account-cn.alibabacloud.com,DIRECT  （被同策略父级 DOMAIN-SUFFIX,alibabacloud.com 覆盖）
- DOMAIN,maps.apple.com,DIRECT  （被同策略父级 DOMAIN-SUFFIX,apple.com 覆盖）
- DOMAIN,xz.pphimalayanrt.com,DIRECT  （被同策略父级 DOMAIN-SUFFIX,pphimalayanrt.com 覆盖）
- DOMAIN,sp.itunes.apple.com,DIRECT  （被同策略父级 DOMAIN-SUFFIX,apple.com 覆盖）
- DOMAIN,podcasts.apple.com,DIRECT  （被同策略父级 DOMAIN-SUFFIX,apple.com 覆盖）
- DOMAIN,dnl-03.geo.kaspersky.com,DIRECT  （被同策略父级 DOMAIN-SUFFIX,geo.kaspersky.com 覆盖）
... 另有 242 条未列出
```
</details>

### 上游源状态

- ✅ https://raw.githubusercontent.com/GMOogway/shadowrocket-rules/master/sr_direct_list.module

**原有规则数**: 111369
**新增规则数**: 0
**更新后总数**: 111369

🩺 直连模块: 健康检查通过（111369 条规则，3.6 MB）

✅ 直连模块已写入，共 111369 条规则

## 代理分流模块

### 🛡️ 白名单豁免（代理规则，共 30 条）

**原因**：这些域名在 `direct_whitelist.txt` 中，已从代理规则中移除，确保走直连。

<details>
<summary>展开查看被豁免的代理规则（30 条）</summary>


- `DOMAIN-SUFFIX,mzstatic.com,PROXY`
  - 匹配白名单：`mzstatic.com`
  - 用途：苹果商店静态资源 CDN（截图、图标等）
- `DOMAIN,matsuridayo.github.io,PROXY`
  - 匹配白名单：`github.io`
  - 用途：GitHub Pages 站点
- `DOMAIN-SUFFIX,ru.ccb.com,PROXY`
  - 匹配白名单：`ccb.com`
  - 用途：中国建设银行
- `DOMAIN,trojan-gfw.github.io,PROXY`
  - 匹配白名单：`github.io`
  - 用途：GitHub Pages 站点
- `DOMAIN,hls-amt.itunes.apple.com,PROXY`
  - 匹配白名单：`itunes.apple.com`
  - 用途：iTunes/App Store 传统商店内容
- `DOMAIN,nix-community.github.io,PROXY`
  - 匹配白名单：`github.io`
  - 用途：GitHub Pages 站点
- `DOMAIN,bybit-exchange.github.io,PROXY`
  - 匹配白名单：`github.io`
  - 用途：GitHub Pages 站点
- `DOMAIN,xtls.github.io,PROXY`
  - 匹配白名单：`github.io`
  - 用途：GitHub Pages 站点
- `DOMAIN,uts-api.itunes.apple.com,PROXY`
  - 匹配白名单：`itunes.apple.com`
  - 用途：iTunes/App Store 传统商店内容
- `DOMAIN,copilot-telemetry-service.githubusercontent.com,PROXY`
  - 匹配白名单：`githubusercontent.com`
  - 用途：GitHub 用户内容（raw 文件、图片、附件等）
- `DOMAIN-SUFFIX,githubassets.com,PROXY`
  - 匹配白名单：`githubassets.com`
  - 用途：GitHub 静态资源（CSS、JS、头像等）
- `DOMAIN,play-edge.itunes.apple.com,PROXY`
  - 匹配白名单：`itunes.apple.com`
  - 用途：iTunes/App Store 传统商店内容
- `DOMAIN-SUFFIX,githubusercontent.com,PROXY`
  - 匹配白名单：`githubusercontent.com`
  - 用途：GitHub 用户内容（raw 文件、图片、附件等）
- `DOMAIN-SUFFIX,github.com,PROXY`
  - 匹配白名单：`github.com`
  - 用途：GitHub 主站
- `DOMAIN,hls.itunes.apple.com,PROXY`
  - 匹配白名单：`itunes.apple.com`
  - 用途：iTunes/App Store 传统商店内容
- `DOMAIN,copilot-proxy.githubusercontent.com,PROXY`
  - 匹配白名单：`githubusercontent.com`
  - 用途：GitHub 用户内容（raw 文件、图片、附件等）
- `DOMAIN,metacubex.github.io,PROXY`
  - 匹配白名单：`github.io`
  - 用途：GitHub Pages 站点
- `DOMAIN,np-edge.itunes.apple.com,PROXY`
  - 匹配白名单：`itunes.apple.com`
  - 用途：iTunes/App Store 传统商店内容
- `DOMAIN-SUFFIX,snssdk.com,PROXY`
  - 匹配白名单：`snssdk.com`
  - 用途：字节跳动基础域名（短视频、直播等）
- `DOMAIN-SUFFIX,github.io,PROXY`
  - 匹配白名单：`github.io`
  - 用途：GitHub Pages 站点
- `DOMAIN-SUFFIX,bytegecko.com,PROXY`
  - 匹配白名单：`bytegecko.com`
  - 用途：字节跳动 CDN（网页资源）
- `DOMAIN,copilot-telemetry.githubusercontent.com,PROXY`
  - 匹配白名单：`githubusercontent.com`
  - 用途：GitHub 用户内容（raw 文件、图片、附件等）
- `DOMAIN,throneproj.github.io,PROXY`
  - 匹配白名单：`github.io`
  - 用途：GitHub Pages 站点
- `DOMAIN-SUFFIX,play.itunes.apple.com,PROXY`
  - 匹配白名单：`itunes.apple.com`
  - 用途：iTunes/App Store 传统商店内容
- `DOMAIN-SUFFIX,bag.itunes.apple.com,PROXY`
  - 匹配白名单：`itunes.apple.com`
  - 用途：iTunes/App Store 传统商店内容
- `DOMAIN-SUFFIX,raw.githubusercontent.com,PROXY`
  - 匹配白名单：`githubusercontent.com`
  - 用途：GitHub 用户内容（raw 文件、图片、附件等）
- `DOMAIN-SUFFIX,media.githubusercontent.com,PROXY`
  - 匹配白名单：`githubusercontent.com`
  - 用途：GitHub 用户内容（raw 文件、图片、附件等）
- `DOMAIN-SUFFIX,avatars2.githubusercontent.com,PROXY`
  - 匹配白名单：`githubusercontent.com`
  - 用途：GitHub 用户内容（raw 文件、图片、附件等）
- `DOMAIN-SUFFIX,gist.github.com,PROXY`
  - 匹配白名单：`github.com`
  - 用途：GitHub 主站
- `DOMAIN-SUFFIX,www.douyin.com,PROXY`
  - 匹配白名单：`douyin.com`
  - 用途：抖音主站

</details>

### 🛡️ 白名单豁免（去广告规则，共 31 条）

**原因**：这些域名在 `direct_whitelist.txt` 中，已从去广告规则中移除，避免误拦截。

<details>
<summary>展开查看被豁免的去广告规则（31 条）</summary>


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
- `DOMAIN-SUFFIX,p3-ad-sign.byteimg.com,REJECT`
  - 匹配白名单：`byteimg.com`
  - 用途：字节跳动图片 CDN
- `DOMAIN-SUFFIX,log.snssdk.com,REJECT`
  - 匹配白名单：`snssdk.com`
  - 用途：字节跳动基础域名（短视频、直播等）
- `DOMAIN-SUFFIX,log0-misc-hl.amemv.com,REJECT`
  - 匹配白名单：`amemv.com`
  - 用途：字节跳动短视频（抖音、火山等）
- `DOMAIN-SUFFIX,xlog.snssdk.com,REJECT`
  - 匹配白名单：`snssdk.com`
  - 用途：字节跳动基础域名（短视频、直播等）
- `DOMAIN-SUFFIX,mihoutao1868.github.io,REJECT`
  - 匹配白名单：`github.io`
  - 用途：GitHub Pages 站点
- `DOMAIN-SUFFIX,analytics.githubassets.com,REJECT`
  - 匹配白名单：`githubassets.com`
  - 用途：GitHub 静态资源（CSS、JS、头像等）
- `DOMAIN-SUFFIX,copilot-telemetry.githubusercontent.com,REJECT`
  - 匹配白名单：`githubusercontent.com`
  - 用途：GitHub 用户内容（raw 文件、图片、附件等）
- `DOMAIN-SUFFIX,metrics.mzstatic.com,REJECT`
  - 匹配白名单：`mzstatic.com`
  - 用途：苹果商店静态资源 CDN（截图、图标等）
- `DOMAIN-SUFFIX,mcs.snssdk.com,REJECT`
  - 匹配白名单：`snssdk.com`
  - 用途：字节跳动基础域名（短视频、直播等）
- `DOMAIN-SUFFIX,collector.github.com,REJECT`
  - 匹配白名单：`github.com`
  - 用途：GitHub 主站
- `DOMAIN-SUFFIX,ib.snssdk.com,REJECT`
  - 匹配白名单：`snssdk.com`
  - 用途：字节跳动基础域名（短视频、直播等）
- `DOMAIN-SUFFIX,log-hl.snssdk.com,REJECT`
  - 匹配白名单：`snssdk.com`
  - 用途：字节跳动基础域名（短视频、直播等）
- `DOMAIN-SUFFIX,dm.pstatp.com,REJECT`
  - 匹配白名单：`pstatp.com`
  - 用途：字节跳动基础域名（推荐、API 等）
- `DOMAIN-SUFFIX,googleads.github.io,REJECT`
  - 匹配白名单：`github.io`
  - 用途：GitHub Pages 站点
- `DOMAIN-SUFFIX,mon.snssdk.com,REJECT`
  - 匹配白名单：`snssdk.com`
  - 用途：字节跳动基础域名（短视频、直播等）
- `DOMAIN-SUFFIX,devgottia.github.io,REJECT`
  - 匹配白名单：`github.io`
  - 用途：GitHub Pages 站点
- `DOMAIN-SUFFIX,collector-cdn.github.com,REJECT`
  - 匹配白名单：`github.com`
  - 用途：GitHub 主站
- `DOMAIN-SUFFIX,log.cmbchina.com,REJECT`
  - 匹配白名单：`cmbchina.com`
  - 用途：招商银行

</details>

### ❌ 代理规则质量检查异常（共 6 条）

**处理动作**：异常规则已从最终模块中移除。

<details>
<summary>展开查看异常规则及原因</summary>

```
- DOMAIN-SUFFIX,IP-CIDR,143.198.200.27/32,no-resolve,PROXY  (原因: 策略 '143.198.200.27/32' 不合法)
- DOMAIN-SUFFIX,IP-CIDR,159.89.204.203/32,no-resolve,PROXY  (原因: 策略 '159.89.204.203/32' 不合法)
- DOMAIN-SUFFIX,IP-CIDR,24.199.123.28/32,no-resolve,PROXY  (原因: 策略 '24.199.123.28/32' 不合法)
- DOMAIN-SUFFIX,IP-CIDR,45.76.214.191/32,no-resolve,PROXY  (原因: 策略 '45.76.214.191/32' 不合法)
- DOMAIN-SUFFIX,IP-CIDR,64.23.132.171/32,no-resolve,PROXY  (原因: 策略 '64.23.132.171/32' 不合法)
- DOMAIN-SUFFIX,OMAIN-SUFFIX,BING.NET,PROXY  (原因: 策略 'BING.NET' 不合法)
```
</details>

### 🧹 代理规则去重删除（共 3077 条）

**处理动作**：同一域名、同一策略的重复规则已删除，只保留一条；跨策略的不删。

<details>
<summary>展开查看去重样例（前 20 条）</summary>

```
- DOMAIN,scholar.google.se,PROXY  （被同策略父级 DOMAIN-SUFFIX,google.se 覆盖）
- DOMAIN,ulrichsweb.serialssolutions.com,PROXY  （被同策略父级 DOMAIN-SUFFIX,serialssolutions.com 覆盖）
- DOMAIN,scholar.google.ru,PROXY  （被同策略父级 DOMAIN-SUFFIX,google.ru 覆盖）
- DOMAIN,csis-prod.s3.amazonaws.com,PROXY  （被同策略父级 DOMAIN-SUFFIX,amazonaws.com 覆盖）
- DOMAIN,wwis-dubc1-vip116.adobe.com,PROXY  （被同策略父级 DOMAIN-SUFFIX,adobe.com 覆盖）
- DOMAIN,vod-dash-uk-live.akamaized.net,PROXY  （被同策略父级 DOMAIN-SUFFIX,akamaized.net 覆盖）
- DOMAIN,time-c-wwv.nist.gov,PROXY  （被同策略父级 DOMAIN-SUFFIX,nist.gov 覆盖）
- DOMAIN,espn.api.edge.bamgrid.com,PROXY  （被同策略父级 DOMAIN-SUFFIX,bamgrid.com 覆盖）
- DOMAIN,api.statsig.com,PROXY  （被同策略 DOMAIN-SUFFIX,api.statsig.com 覆盖）
- DOMAIN,notary-submissions-prod.s3.us-west-2.amazonaws.com,PROXY  （被同策略父级 DOMAIN-SUFFIX,amazonaws.com 覆盖）
- DOMAIN,time2.google.com,PROXY  （被同策略父级 DOMAIN-SUFFIX,google.com 覆盖）
- DOMAIN,d3aqoihi2n8ty8.cloudfront.net,PROXY  （被同策略父级 DOMAIN-SUFFIX,cloudfront.net 覆盖）
- DOMAIN,3dns-2.adobe.com,PROXY  （被同策略父级 DOMAIN-SUFFIX,adobe.com 覆盖）
- DOMAIN,wip2.adobe.com,PROXY  （被同策略父级 DOMAIN-SUFFIX,adobe.com 覆盖）
- DOMAIN,d3ucl0eqgl80l5.cloudfront.net,PROXY  （被同策略父级 DOMAIN-SUFFIX,cloudfront.net 覆盖）
- DOMAIN,ubisoft-uplay-savegames.s3.amazonaws.com,PROXY  （被同策略父级 DOMAIN-SUFFIX,amazonaws.com 覆盖）
- DOMAIN,live.applicationinsights.azure.com,PROXY  （被同策略父级 DOMAIN-SUFFIX,azure.com 覆盖）
- DOMAIN,static-hamivideo.cdn.hinet.net,PROXY  （被同策略父级 DOMAIN-SUFFIX,hinet.net 覆盖）
- DOMAIN,dlgarenanow-a.akamaihd.net,PROXY  （被同策略父级 DOMAIN-SUFFIX,akamaihd.net 覆盖）
- DOMAIN,wwis-dubc1-vip104.adobe.com,PROXY  （被同策略父级 DOMAIN-SUFFIX,adobe.com 覆盖）
... 另有 3057 条未列出
```
</details>

### 🧹 去广告规则去重删除（共 868 条）

**处理动作**：同一域名、同一策略的重复规则已删除，只保留一条；跨策略的不删。

<details>
<summary>展开查看去重样例（前 20 条）</summary>

```
- DOMAIN-SUFFIX,57ro4evi31xq97w.yr1972kn5orxe4q.cfd,REJECT  （被同策略父级 DOMAIN-SUFFIX,yr1972kn5orxe4q.cfd 覆盖）
- DOMAIN-SUFFIX,6mwwun92mc6hwj2c.cmu8y2wm12ooip4nm.cfd,REJECT  （被同策略父级 DOMAIN-SUFFIX,cmu8y2wm12ooip4nm.cfd 覆盖）
- DOMAIN-SUFFIX,ad8fcd6370.029d52f978.com,REJECT  （被同策略父级 DOMAIN-SUFFIX,029d52f978.com 覆盖）
- DOMAIN-SUFFIX,mtt1uj.nq95ihw6l9bwzuy.cfd,REJECT  （被同策略父级 DOMAIN-SUFFIX,nq95ihw6l9bwzuy.cfd 覆盖）
- DOMAIN,ad-splash-tracking.hktvmall.com,REJECT  （被同策略 DOMAIN-SUFFIX,ad-splash-tracking.hktvmall.com 覆盖）
- DOMAIN,ad-splash.hktvmall.com,REJECT  （被同策略 DOMAIN-SUFFIX,ad-splash.hktvmall.com 覆盖）
- DOMAIN,ad.12306.cn,REJECT  （被同策略 DOMAIN-SUFFIX,ad.12306.cn 覆盖）
- DOMAIN,ad.api.3g.youku.com,REJECT  （被同策略 DOMAIN-SUFFIX,ad.api.3g.youku.com 覆盖）
- DOMAIN,ad.cctv.com,REJECT  （被同策略 DOMAIN-SUFFIX,ad.cctv.com 覆盖）
- DOMAIN,ad.doubleclick.net,REJECT  （被同策略父级 DOMAIN-SUFFIX,doubleclick.net 覆盖）
- DOMAIN,ad.gameley.com,REJECT  （被同策略 DOMAIN-SUFFIX,ad.gameley.com 覆盖）
- DOMAIN,ad.hpplay.cn,REJECT  （被同策略 DOMAIN-SUFFIX,ad.hpplay.cn 覆盖）
- DOMAIN,ad.qq.com,REJECT  （被同策略 DOMAIN-SUFFIX,ad.qq.com 覆盖）
- DOMAIN,ad.shunchangzhixing.com,REJECT  （被同策略 DOMAIN-SUFFIX,ad.shunchangzhixing.com 覆盖）
- DOMAIN,ad.tencentmusic.com,REJECT  （被同策略 DOMAIN-SUFFIX,ad.tencentmusic.com 覆盖）
- DOMAIN,ad.zijieapi.com,REJECT  （被同策略 DOMAIN-SUFFIX,ad.zijieapi.com 覆盖）
- DOMAIN,adash-emas.cn-hangzhou.aliyuncs.com,REJECT  （被同策略 DOMAIN-SUFFIX,adash-emas.cn-hangzhou.aliyuncs.com 覆盖）
- DOMAIN,adashx.m.taobao.com,REJECT  （被同策略 DOMAIN-SUFFIX,adashx.m.taobao.com 覆盖）
- DOMAIN,adbox.sina.com.cn,REJECT  （被同策略 DOMAIN-SUFFIX,adbox.sina.com.cn 覆盖）
- DOMAIN,adcdn.hpplay.cn,REJECT  （被同策略 DOMAIN-SUFFIX,adcdn.hpplay.cn 覆盖）
... 另有 848 条未列出
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
**DOMAIN-SUFFIX:tanx.com**
```
- DOMAIN-SUFFIX,tanx.com,REJECT
- DOMAIN-SUFFIX,tanx.com,REJECT-200
```
**DOMAIN-SUFFIX:ulogs.umengcloud.com**
```
- DOMAIN-SUFFIX,ulogs.umengcloud.com,REJECT
- DOMAIN-SUFFIX,ulogs.umengcloud.com,REJECT-DICT
```
</details>

### ⚠️ 父子域冲突（合计 13 组）

**判断依据**：DOMAIN 规则被 DOMAIN-SUFFIX 规则覆盖且策略不同。

**处理动作**：排序后 DOMAIN 规则在前，将优先生效。

<details>
<summary>展开查看冲突详情</summary>

- DOMAIN adashbc.ut.taobao.com (REJECT) 被 DOMAIN-SUFFIX adashbc.ut.taobao.com (REJECT-200) 覆盖
- DOMAIN adashxgc.ut.taobao.com (REJECT) 被 DOMAIN-SUFFIX adashxgc.ut.taobao.com (REJECT-200) 覆盖
- DOMAIN bootpreload.uve.weibo.com (REJECT) 被 DOMAIN-SUFFIX bootpreload.uve.weibo.com (REJECT-200) 覆盖
- DOMAIN cnlogs.umeng.com (REJECT) 被 DOMAIN-SUFFIX cnlogs.umeng.com (REJECT-DICT) 覆盖
- DOMAIN mssdk.volces.com (REJECT) 被 DOMAIN-SUFFIX mssdk.volces.com (REJECT-DICT) 覆盖
- DOMAIN resolve.umeng.com (REJECT) 被 DOMAIN-SUFFIX resolve.umeng.com (REJECT-DICT) 覆盖
- DOMAIN sdk-track.66mobi.com (REJECT) 被 DOMAIN-SUFFIX sdk-track.66mobi.com (REJECT-DICT) 覆盖
- DOMAIN sdk.1rtb.net (REJECT) 被 DOMAIN-SUFFIX sdk.1rtb.net (REJECT-DICT) 覆盖
- DOMAIN sdkapp.uve.weibo.com (REJECT) 被 DOMAIN-SUFFIX sdkapp.uve.weibo.com (REJECT-DICT) 覆盖
- DOMAIN smartad.10010.com (REJECT) 被 DOMAIN-SUFFIX smartad.10010.com (REJECT-200) 覆盖
- DOMAIN success.ctobsnssdk.com (REJECT) 被 DOMAIN-SUFFIX ctobsnssdk.com (REJECT-DICT) 覆盖
- DOMAIN ulogs.umeng.com (REJECT) 被 DOMAIN-SUFFIX ulogs.umeng.com (REJECT-DICT) 覆盖
- DOMAIN utoken.umeng.com (REJECT) 被 DOMAIN-SUFFIX utoken.umeng.com (REJECT-DICT) 覆盖
</details>

### 上游源状态

- ✅ https://raw.githubusercontent.com/GMOogway/shadowrocket-rules/master/sr_proxy_list.module
- ✅ https://raw.githubusercontent.com/LOWERTOP/Shadowrocket-First/main/Talkatone.sgmodule
- ✅ https://johnshall.github.io/Shadowrocket-ADBlock-Rules-Forever/sr_top500_banlist_ad.conf
- ✅ https://johnshall.github.io/Shadowrocket-ADBlock-Rules-Forever/sr_cnip_ad.conf

**原有代理规则数**: 48810
**新增代理规则数**: 0
**更新后代理规则总数**: 48810

## 去广告模块

### 上游源状态

- ✅ https://raw.githubusercontent.com/huijingfei/Shadowrocket-Rules/refs/heads/main/sr_app_ad.module
- ✅ https://raw.githubusercontent.com/deezertidal/shadowrocket-rules/refs/heads/main/modules/startingad.module
- ✅ https://raw.githubusercontent.com/GMOogway/shadowrocket-rules/master/sr_reject_list.module
- ✅ https://raw.githubusercontent.com/Unwhimsical/NetPilot/refs/heads/main/modules/%E6%B5%8B%E8%AF%95.module
- ✅ https://raw.githubusercontent.com/LOWERTOP/Shadowrocket-First/main/TalkatoneAntiAds.list
- ✅ https://johnshall.github.io/Shadowrocket-ADBlock-Rules-Forever/sr_ad_only.conf
- ✅ https://yfamilys.com/module/AdBlock.module
- ✅ https://yfamilys.com/module/adultraplus.module

**原有去广告规则数**: 241414
**新增去广告规则数**: 386
**更新后去广告规则总数**: 241796

#### 新增去广告规则明细

<details>
<summary>展开查看新增去广告规则（共 386 条）</summary>

```
DOMAIN-SUFFIX,029d52f978.com,REJECT
DOMAIN-SUFFIX,131vqvt1ni417ur85o1.cfd,REJECT
DOMAIN-SUFFIX,49ivw88hj9.com,REJECT
DOMAIN-SUFFIX,4b6n4r2ye1bzizl52.rest,REJECT
DOMAIN-SUFFIX,4hg1oddm34.com,REJECT
DOMAIN-SUFFIX,4xglxv36wklzgz81o19g1k5t5h65.cfd,REJECT
DOMAIN-SUFFIX,7on11fz9uiljn3v.rest,REJECT
DOMAIN-SUFFIX,9ip7few3b4jif4th2f936e1uy4.rest,REJECT
DOMAIN-SUFFIX,a6j9wqsyq6.com,REJECT
DOMAIN-SUFFIX,accededheerrend.cyou,REJECT
DOMAIN-SUFFIX,accjucvaz.in,REJECT
DOMAIN-SUFFIX,actiumfug.com,REJECT
DOMAIN-SUFFIX,afqxmyankob.in,REJECT
DOMAIN-SUFFIX,afreshpixiesepirote.cyou,REJECT
DOMAIN-SUFFIX,agibvcsxzxmjg.site,REJECT
DOMAIN-SUFFIX,ahgfywqmajfnn.website,REJECT
DOMAIN-SUFFIX,ajc1d0k4nr.com,REJECT
DOMAIN-SUFFIX,akalasestine.com,REJECT
DOMAIN-SUFFIX,albertosective.click,REJECT
DOMAIN-SUFFIX,aliptaegivers.com,REJECT
DOMAIN-SUFFIX,angwybrbsfrrb.site,REJECT
DOMAIN-SUFFIX,anoianeeders.rest,REJECT
DOMAIN-SUFFIX,armetsgonna.com,REJECT
DOMAIN-SUFFIX,asciticlargy.click,REJECT
DOMAIN-SUFFIX,asdseqcrshsoz.online,REJECT
DOMAIN-SUFFIX,asfaocttaado.com,REJECT
DOMAIN-SUFFIX,atmasfolksaymunda.cfd,REJECT
DOMAIN-SUFFIX,aubghm.com,REJECT
DOMAIN-SUFFIX,axcitqovidvoc.online,REJECT
DOMAIN-SUFFIX,b69bmb4lbkcmgn5wtjl.rest,REJECT
DOMAIN-SUFFIX,barbafvgixbsa.website,REJECT
DOMAIN-SUFFIX,bayokmisstayusques.cfd,REJECT
DOMAIN-SUFFIX,bdwlbrozfnlah.online,REJECT
DOMAIN-SUFFIX,beayrzcpfqwqr.website,REJECT
DOMAIN-SUFFIX,belkzeqkauwsl.website,REJECT
DOMAIN-SUFFIX,bemistssabringfodge.cyou,REJECT
DOMAIN-SUFFIX,bfiaccczaok.in,REJECT
DOMAIN-SUFFIX,bioxidebattle.click,REJECT
DOMAIN-SUFFIX,bjzvinxduxltg.website,REJECT
DOMAIN-SUFFIX,blightyvinic.click,REJECT
DOMAIN-SUFFIX,blushingexpert.pro,REJECT
DOMAIN-SUFFIX,bmxvcbvmigvrp.site,REJECT
DOMAIN-SUFFIX,bnexegykbnmjw.site,REJECT
DOMAIN-SUFFIX,bnqwba.com,REJECT
DOMAIN-SUFFIX,breakablepermission.pro,REJECT
DOMAIN-SUFFIX,brinktrayne.cyou,REJECT
DOMAIN-SUFFIX,bruciteawreak.rest,REJECT
DOMAIN-SUFFIX,bslndczooj.com,REJECT
DOMAIN-SUFFIX,burieschill.click,REJECT
DOMAIN-SUFFIX,calderaoutwell.com,REJECT
DOMAIN-SUFFIX,cambevasonnies.cyou,REJECT
DOMAIN-SUFFIX,carrizopresaw.rest,REJECT
DOMAIN-SUFFIX,cassavasnurl.cyou,REJECT
DOMAIN-SUFFIX,cexesmsbyvdwn.website,REJECT
DOMAIN-SUFFIX,charciaaccuse.click,REJECT
DOMAIN-SUFFIX,chekistirredcotman.cfd,REJECT
DOMAIN-SUFFIX,cissoiddownset.com,REJECT
DOMAIN-SUFFIX,cmsxigzqvurqm.space,REJECT
DOMAIN-SUFFIX,cmu8y2wm12ooip4nm.cfd,REJECT
DOMAIN-SUFFIX,coirsophy.cfd,REJECT
DOMAIN-SUFFIX,coldhighlight.com,REJECT
DOMAIN-SUFFIX,coolgarden.mobi,REJECT
DOMAIN-SUFFIX,coolgarden.pro,REJECT
DOMAIN-SUFFIX,corinnewhiffy.com,REJECT
DOMAIN-SUFFIX,crunkdemur.rest,REJECT
DOMAIN-SUFFIX,csnfevdbreypv.space,REJECT
DOMAIN-SUFFIX,csykvhl.com,REJECT
DOMAIN-SUFFIX,ctqgtnwberglg.space,REJECT
DOMAIN-SUFFIX,cwsxeyiooubjg.space,REJECT
DOMAIN-SUFFIX,cydmiagrgipxu.space,REJECT
DOMAIN-SUFFIX,cygnetskeyhole.cyou,REJECT
DOMAIN-SUFFIX,d9zkof.com,REJECT
DOMAIN-SUFFIX,dacronpelted.rest,REJECT
DOMAIN-SUFFIX,daffodilrock.mobi,REJECT
DOMAIN-SUFFIX,dbawlenwwblcx.online,REJECT
DOMAIN-SUFFIX,defrostborer.cfd,REJECT
DOMAIN-SUFFIX,dekesleaner.cyou,REJECT
DOMAIN-SUFFIX,diarchgullynephric.cyou,REJECT
DOMAIN-SUFFIX,digeneaoctrois.com,REJECT
DOMAIN-SUFFIX,dishfulpavetta.com,REJECT
DOMAIN-SUFFIX,djymrgceujiml.website,REJECT
DOMAIN-SUFFIX,dkuoxtdptdmupt.com,REJECT
DOMAIN-SUFFIX,dnhepqnyxrmnn.space,REJECT
DOMAIN-SUFFIX,dtucndqmxbitf.online,REJECT
DOMAIN-SUFFIX,dxdwfgqtuegmy.website,REJECT
DOMAIN-SUFFIX,dxmjdtwhytzxb.space,REJECT
DOMAIN-SUFFIX,dyv86qq19o.com,REJECT
DOMAIN-SUFFIX,dzvnirqek.com,REJECT
DOMAIN-SUFFIX,ecbgfnpmbgmni.website,REJECT
DOMAIN-SUFFIX,eelfxnnyjuatb.website,REJECT
DOMAIN-SUFFIX,eemehsezfbdjj.online,REJECT
DOMAIN-SUFFIX,ejdbpregfygg.com,REJECT
DOMAIN-SUFFIX,elvetfestino.cyou,REJECT
DOMAIN-SUFFIX,enkovpozogqax.online,REJECT
DOMAIN-SUFFIX,entombcarcass.com,REJECT
DOMAIN-SUFFIX,enwidenchaksi.rest,REJECT
DOMAIN-SUFFIX,enwytgaofkxlp.website,REJECT
DOMAIN-SUFFIX,erajtkihsjcws.website,REJECT
DOMAIN-SUFFIX,erlclick.com,REJECT
DOMAIN-SUFFIX,estdpfanrjjum.site,REJECT
DOMAIN-SUFFIX,evasiveloopers.cyou,REJECT
DOMAIN-SUFFIX,feebeduins.com,REJECT
DOMAIN-SUFFIX,ffcmdnnfmwsnv.website,REJECT
DOMAIN-SUFFIX,fgwlbyr.com,REJECT
DOMAIN-SUFFIX,fhqgblsehmaga.site,REJECT
DOMAIN-SUFFIX,filateaevialucanid.cyou,REJECT
DOMAIN-SUFFIX,fohbwgyxourjz.online,REJECT
DOMAIN-SUFFIX,foliousdesman.cfd,REJECT
DOMAIN-SUFFIX,fpjsfkktueiwt.online,REJECT
DOMAIN-SUFFIX,fps3xggxro.com,REJECT
DOMAIN-SUFFIX,fqfhznr3qn.com,REJECT
DOMAIN-SUFFIX,fqjykbut.com,REJECT
DOMAIN-SUFFIX,frpprbdipakwp.space,REJECT
DOMAIN-SUFFIX,fswvjpuppunku.space,REJECT
DOMAIN-SUFFIX,fumishfricace.com,REJECT
DOMAIN-SUFFIX,furtiverhetor.com,REJECT
DOMAIN-SUFFIX,fxmqrdjgbfqfl.space,REJECT
DOMAIN-SUFFIX,gausspinedabduct.cfd,REJECT
DOMAIN-SUFFIX,gejtnwwgrovnu.website,REJECT
DOMAIN-SUFFIX,ghautincant.cfd,REJECT
DOMAIN-SUFFIX,ghesscopsy.com,REJECT
DOMAIN-SUFFIX,ghoomdishful.cyou,REJECT
DOMAIN-SUFFIX,gibres.xyz,REJECT
DOMAIN-SUFFIX,giftedflax.info,REJECT
DOMAIN-SUFFIX,giftedflax.mobi,REJECT
DOMAIN-SUFFIX,gkretspkgsctm.online,REJECT
DOMAIN-SUFFIX,gldpkxwsmtfzv.online,REJECT
DOMAIN-SUFFIX,gnmogrbqfalhe.space,REJECT
DOMAIN-SUFFIX,gonimicinsigne.click,REJECT
DOMAIN-SUFFIX,gqdnvupzqvnmz.site,REJECT
DOMAIN-SUFFIX,grehhckjal.com,REJECT
DOMAIN-SUFFIX,groceryyusdrum.cyou,REJECT
DOMAIN-SUFFIX,gtboyumajcson.online,REJECT
DOMAIN-SUFFIX,gwpbffhjdemva.site,REJECT
DOMAIN-SUFFIX,gxrdxtfsuksug.website,REJECT
DOMAIN-SUFFIX,hakamrabious.rest,REJECT
DOMAIN-SUFFIX,haunchstart.com,REJECT
DOMAIN-SUFFIX,hbwqdvazi.com,REJECT
DOMAIN-SUFFIX,hdbmmpjli.com,REJECT
DOMAIN-SUFFIX,hffwxt.com,REJECT
DOMAIN-SUFFIX,hhqcqdaausfjw.online,REJECT
DOMAIN-SUFFIX,hillxdytvszyx.online,REJECT
DOMAIN-SUFFIX,hlqbpuenoslyj.online,REJECT
DOMAIN-SUFFIX,holmiumsedatecaplets.cfd,REJECT
DOMAIN-SUFFIX,hoysfrfmhnuhb.space,REJECT
DOMAIN-SUFFIX,hurupjtqpngdm.website,REJECT
DOMAIN-SUFFIX,hviyvozcpwlki.website,REJECT
DOMAIN-SUFFIX,hxhasxphmqhyf.website,REJECT
DOMAIN-SUFFIX,iaburdjxqnwoq.com,REJECT
DOMAIN-SUFFIX,ifverjmhgjpzq.online,REJECT
DOMAIN-SUFFIX,igpfsbwqohpbh.space,REJECT
DOMAIN-SUFFIX,iizravrqlhq.com,REJECT
DOMAIN-SUFFIX,ildsaagmtzefs.online,REJECT
DOMAIN-SUFFIX,ilezkybigxjqu.site,REJECT
DOMAIN-SUFFIX,imtcnuqvkgarg.space,REJECT
DOMAIN-SUFFIX,indyvnqumiryu.space,REJECT
DOMAIN-SUFFIX,iohkvsyefqeqg.space,REJECT
DOMAIN-SUFFIX,itzoqbrqnsbix.com,REJECT
DOMAIN-SUFFIX,iuncrcsimshlk.site,REJECT
DOMAIN-SUFFIX,iyvqmlalbnbhk.website,REJECT
DOMAIN-SUFFIX,izeczulkfstho.site,REJECT
DOMAIN-SUFFIX,j31pozck4v.com,REJECT
DOMAIN-SUFFIX,j439hek3qhp5hf.rest,REJECT
DOMAIN-SUFFIX,jaolyqfxwefee.website,REJECT
DOMAIN-SUFFIX,javtaku.com,REJECT
DOMAIN-SUFFIX,jbjpayvvbknna.website,REJECT
DOMAIN-SUFFIX,jeutkytrjcfcg.space,REJECT
DOMAIN-SUFFIX,jiartpjiowtvn.site,REJECT
DOMAIN-SUFFIX,jjypdfrxbgyfv.website,REJECT
DOMAIN-SUFFIX,jotmlpvassasq.site,REJECT
DOMAIN-SUFFIX,jrxolixgsveoq.website,REJECT
DOMAIN-SUFFIX,jsycwpazyzrfr.website,REJECT
DOMAIN-SUFFIX,jugataefunkerspottah.cfd,REJECT
DOMAIN-SUFFIX,jun83rrctqtzouhpe7hjpupzbe.cfd,REJECT
DOMAIN-SUFFIX,junweemjxevvi.website,REJECT
DOMAIN-SUFFIX,jwueebywttzbl.website,REJECT
DOMAIN-SUFFIX,jxuwhxgwftoqv.site,REJECT
DOMAIN-SUFFIX,k9ixrkp46fncvh.rest,REJECT
DOMAIN-SUFFIX,kanetolls.cyou,REJECT
DOMAIN-SUFFIX,kawakaukuleleistrian.cfd,REJECT
DOMAIN-SUFFIX,kcalbrill.click,REJECT
DOMAIN-SUFFIX,keimstjcudvmu.space,REJECT
DOMAIN-SUFFIX,kkwmewarhuuov.online,REJECT
DOMAIN-SUFFIX,kollerhool.cyou,REJECT
DOMAIN-SUFFIX,ksxkvyzhpiabi.space,REJECT
DOMAIN-SUFFIX,kyschtyhexerei.com,REJECT
DOMAIN-SUFFIX,larkthunder.me,REJECT
DOMAIN-SUFFIX,lashesduo.com,REJECT
DOMAIN-SUFFIX,ldbcpitschnvz.space,REJECT
DOMAIN-SUFFIX,lfjcljlwuwwvt.website,REJECT
DOMAIN-SUFFIX,lfjsiyhfwobbp.site,REJECT
DOMAIN-SUFFIX,ljoynsgqdnebi.site,REJECT
DOMAIN-SUFFIX,lmifiblkmsjzr.space,REJECT
DOMAIN-SUFFIX,lpjesrjwmfdwb.online,REJECT
DOMAIN-SUFFIX,lqhqrkxjvhokd.online,REJECT
DOMAIN-SUFFIX,lsnwufsobvd.com,REJECT
DOMAIN-SUFFIX,lxbqknmo.com,REJECT
DOMAIN-SUFFIX,lxdwht.com,REJECT
DOMAIN-SUFFIX,lxzxdjbukydjs.space,REJECT
DOMAIN-SUFFIX,mahuangproagon.cyou,REJECT
DOMAIN-SUFFIX,matanzaennia.cyou,REJECT
DOMAIN-SUFFIX,mgfofpxatunnn.space,REJECT
DOMAIN-SUFFIX,mgmsedcduudbx.space,REJECT
DOMAIN-SUFFIX,mindersiwan.com,REJECT
DOMAIN-SUFFIX,mmmumubktklfhl.com,REJECT
DOMAIN-SUFFIX,mountainwillow.pro,REJECT
DOMAIN-SUFFIX,mrfmoudskehdb.online,REJECT
DOMAIN-SUFFIX,naiskoiwottingvitrine.cfd,REJECT
DOMAIN-SUFFIX,nckwqvpngvlce.space,REJECT
DOMAIN-SUFFIX,nefujrvspmhmo.site,REJECT
DOMAIN-SUFFIX,njwywpwhswqku.space,REJECT
DOMAIN-SUFFIX,nmpuwupzfgilx.space,REJECT
DOMAIN-SUFFIX,noerrorwetlandsalomon.cyou,REJECT
DOMAIN-SUFFIX,nozzlerfunds.click,REJECT
DOMAIN-SUFFIX,npmiivlloceyf.website,REJECT
DOMAIN-SUFFIX,nq95ihw6l9bwzuy.cfd,REJECT
DOMAIN-SUFFIX,nsbaipqx.com,REJECT
DOMAIN-SUFFIX,nwvjsasqrxnvt.online,REJECT
DOMAIN-SUFFIX,nzuekqn.com,REJECT
DOMAIN-SUFFIX,oathayrhagite.com,REJECT
DOMAIN-SUFFIX,obepiiyefn.com,REJECT
DOMAIN-SUFFIX,obhlokehiqlij.space,REJECT
DOMAIN-SUFFIX,obljulpi.in,REJECT
DOMAIN-SUFFIX,obviousmoney.pro,REJECT
DOMAIN-SUFFIX,octopodouthut.cyou,REJECT
DOMAIN-SUFFIX,oehpisxqpylve.space,REJECT
DOMAIN-SUFFIX,oghxipocwoqx.in,REJECT
DOMAIN-SUFFIX,oioorkfekghfx.website,REJECT
DOMAIN-SUFFIX,olmqggqwmh.com,REJECT
DOMAIN-SUFFIX,omejqlcniheut.site,REJECT
DOMAIN-SUFFIX,oorydeign.rest,REJECT
DOMAIN-SUFFIX,ormoluschuvash.click,REJECT
DOMAIN-SUFFIX,oxyopiacactoid.cfd,REJECT
DOMAIN-SUFFIX,oyjtdthtoynft.space,REJECT
DOMAIN-SUFFIX,paintertanzeb.rest,REJECT
DOMAIN-SUFFIX,parsulotqo.in,REJECT
DOMAIN-SUFFIX,passatazinger.cfd,REJECT
DOMAIN-SUFFIX,photonssike.cyou,REJECT
DOMAIN-SUFFIX,phspywijwvjc.com,REJECT
DOMAIN-SUFFIX,phsztcaprimpd.online,REJECT
DOMAIN-SUFFIX,pkexgxjqtnjim.online,REJECT
DOMAIN-SUFFIX,pouletoutwin.cfd,REJECT
DOMAIN-SUFFIX,privrebinds.click,REJECT
DOMAIN-SUFFIX,probandfrizzes.com,REJECT
DOMAIN-SUFFIX,puadyhgguqrhd.website,REJECT
DOMAIN-SUFFIX,pxwcfmrrqcybi.online,REJECT
DOMAIN-SUFFIX,pxwugnasuvxl.com,REJECT
DOMAIN-SUFFIX,pyxyqanrjstoy.online,REJECT
DOMAIN-SUFFIX,qbzgfxak.com,REJECT
DOMAIN-SUFFIX,qceapxkry.in,REJECT
DOMAIN-SUFFIX,qcfw7x3u9nrt9uc7.rest,REJECT
DOMAIN-SUFFIX,qfgpgl.com,REJECT
DOMAIN-SUFFIX,qgpyyoipci.com,REJECT
DOMAIN-SUFFIX,qjinekihzfpwl.site,REJECT
DOMAIN-SUFFIX,qrubhrfilkwmc.website,REJECT
DOMAIN-SUFFIX,qshiqigownotd.site,REJECT
DOMAIN-SUFFIX,qubmedkjzaidi.space,REJECT
DOMAIN-SUFFIX,quknxthgigplz.space,REJECT
DOMAIN-SUFFIX,quqpdxjhdwruy.site,REJECT
DOMAIN-SUFFIX,qxwbklgpiftho.online,REJECT
DOMAIN-SUFFIX,ratterbrazier.click,REJECT
DOMAIN-SUFFIX,rbcmtzhpmrhgb.site,REJECT
DOMAIN-SUFFIX,rebaitsgomuti.rest,REJECT
DOMAIN-SUFFIX,rebecsunbarb.com,REJECT
DOMAIN-SUFFIX,redgbriaqtqgi.space,REJECT
DOMAIN-SUFFIX,reliablelinen.com,REJECT
DOMAIN-SUFFIX,remainder22.com,REJECT
DOMAIN-SUFFIX,remexdaimiosfragor.cyou,REJECT
DOMAIN-SUFFIX,renintamises.com,REJECT
DOMAIN-SUFFIX,rfiimntrbauqn.website,REJECT
DOMAIN-SUFFIX,rgcdcchqcmrka.space,REJECT
DOMAIN-SUFFIX,rgsampwohebpr.space,REJECT
DOMAIN-SUFFIX,rhizoidbrassic.cyou,REJECT
DOMAIN-SUFFIX,rhsrjxpkupaha.website,REJECT
DOMAIN-SUFFIX,riataunsane.cfd,REJECT
DOMAIN-SUFFIX,rllogiwmdwfws.website,REJECT
DOMAIN-SUFFIX,rnvpommdnuzoc.online,REJECT
DOMAIN-SUFFIX,rogssxuugpupx.space,REJECT
DOMAIN-SUFFIX,rongtwmtetmhh.site,REJECT
DOMAIN-SUFFIX,roubouhyarm.rest,REJECT
DOMAIN-SUFFIX,rpynajomkrwgq.website,REJECT
DOMAIN-SUFFIX,rpyplk.com,REJECT
DOMAIN-SUFFIX,rrmxaipuvpfbe.space,REJECT
DOMAIN-SUFFIX,rrttupskvzued.online,REJECT
DOMAIN-SUFFIX,sakiganched.click,REJECT
DOMAIN-SUFFIX,sandpine.me,REJECT
DOMAIN-SUFFIX,sapientoctoateanteva.cfd,REJECT
DOMAIN-SUFFIX,sausjlnmovyee.space,REJECT
DOMAIN-SUFFIX,sheriatomalgia.com,REJECT
DOMAIN-SUFFIX,skooswaggir.rest,REJECT
DOMAIN-SUFFIX,slewingflyteceleb.cfd,REJECT
DOMAIN-SUFFIX,slimgather.com,REJECT
DOMAIN-SUFFIX,slkyicluzksvu.site,REJECT
DOMAIN-SUFFIX,sltnjszvfppha.online,REJECT
DOMAIN-SUFFIX,smkdqihbobuxl.site,REJECT
DOMAIN-SUFFIX,snuggerbitypichitched.cfd,REJECT
DOMAIN-SUFFIX,soupy-objective.pro,REJECT
DOMAIN-SUFFIX,sparkbeach.me,REJECT
DOMAIN-SUFFIX,squigglysense.pro,REJECT
DOMAIN-SUFFIX,srvhqcwtpzwyq.space,REJECT
DOMAIN-SUFFIX,strjlkebymgdy.site,REJECT
DOMAIN-SUFFIX,svgkmgtnxbnno.online,REJECT
DOMAIN-SUFFIX,swdjiemumojat.space,REJECT
DOMAIN-SUFFIX,sweetlion.me,REJECT
DOMAIN-SUFFIX,sweetlion.pro,REJECT
DOMAIN-SUFFIX,sykqfitqdiwbo.online,REJECT
DOMAIN-SUFFIX,szjtgitvjaxty.website,REJECT
DOMAIN-SUFFIX,taiccldseyxui.website,REJECT
DOMAIN-SUFFIX,tarrasspumpman.click,REJECT
DOMAIN-SUFFIX,temptingwonder.pro,REJECT
DOMAIN-SUFFIX,teriannineristilty.cfd,REJECT
DOMAIN-SUFFIX,tfucajtkfvomv.online,REJECT
DOMAIN-SUFFIX,thereingriece.cfd,REJECT
DOMAIN-SUFFIX,thymelebuskersroker.cfd,REJECT
DOMAIN-SUFFIX,tibicencoelect.click,REJECT
DOMAIN-SUFFIX,tipzxdvzaducw.site,REJECT
DOMAIN-SUFFIX,tmaqdbudcsufd.space,REJECT
DOMAIN-SUFFIX,tmkziuhyhasal.space,REJECT
DOMAIN-SUFFIX,triariiforgift.com,REJECT
DOMAIN-SUFFIX,tsspositordatary.cfd,REJECT
DOMAIN-SUFFIX,tubifexascan.rest,REJECT
DOMAIN-SUFFIX,turioxylaria.cyou,REJECT
DOMAIN-SUFFIX,uagusoermohqt.website,REJECT
DOMAIN-SUFFIX,uibnyreijcmyc.space,REJECT
DOMAIN-SUFFIX,uidvuwfpybvnp.online,REJECT
DOMAIN-SUFFIX,uifkmubjsznpb.site,REJECT
DOMAIN-SUFFIX,ujhvmnquqxini.online,REJECT
DOMAIN-SUFFIX,ulhdalwihoqvy.space,REJECT
DOMAIN-SUFFIX,uluhflyvyihwfm.com,REJECT
DOMAIN-SUFFIX,unbeingamhar.cfd,REJECT
DOMAIN-SUFFIX,uniquewave.info,REJECT
DOMAIN-SUFFIX,uohjuatpvtmhy.website,REJECT
DOMAIN-SUFFIX,uranylsroovedsaughs.cyou,REJECT
DOMAIN-SUFFIX,uspiix.com,REJECT
DOMAIN-SUFFIX,ustgwwdrkrpjk.site,REJECT
DOMAIN-SUFFIX,uznelnuamjsxb.website,REJECT
DOMAIN-SUFFIX,vafvafnotif.com,REJECT
DOMAIN-SUFFIX,vehicleblawspreknow.cfd,REJECT
DOMAIN-SUFFIX,velatekanjiforwake.cfd,REJECT
DOMAIN-SUFFIX,vidssmvhmgome.online,REJECT
DOMAIN-SUFFIX,violettrail.pro,REJECT
DOMAIN-SUFFIX,vizevezhsvssp.space,REJECT
DOMAIN-SUFFIX,vlqvnbthchbba.online,REJECT
DOMAIN-SUFFIX,vmiloklnfszpc.website,REJECT
DOMAIN-SUFFIX,vsyvgvqylxxpk.site,REJECT
DOMAIN-SUFFIX,vtpetzzcrakgq.space,REJECT
DOMAIN-SUFFIX,vvhcuoqaxinfp.site,REJECT
DOMAIN-SUFFIX,whvmiov.com,REJECT
DOMAIN-SUFFIX,willetsparpal.rest,REJECT
DOMAIN-SUFFIX,wkxoekfewmfur.space,REJECT
DOMAIN-SUFFIX,wofulleafed.com,REJECT
DOMAIN-SUFFIX,wombiershlock.rest,REJECT
DOMAIN-SUFFIX,wonguprisen.click,REJECT
DOMAIN-SUFFIX,wplfigefidhrmw.com,REJECT
DOMAIN-SUFFIX,wprylluxfjrrh.space,REJECT
DOMAIN-SUFFIX,wpwulppgnx6h1u.cfd,REJECT
DOMAIN-SUFFIX,wvevcncamykpc.online,REJECT
DOMAIN-SUFFIX,wwlottiwu.com,REJECT
DOMAIN-SUFFIX,wxzpeizldnupa.website,REJECT
DOMAIN-SUFFIX,xapdygobaljmh.online,REJECT
DOMAIN-SUFFIX,xcviqklcuwzml.website,REJECT
DOMAIN-SUFFIX,xecnfeepzokjx.online,REJECT
DOMAIN-SUFFIX,xevedpsytttfp.site,REJECT
DOMAIN-SUFFIX,xfpzvcxzylppp.online,REJECT
DOMAIN-SUFFIX,xhphatlppluzk.site,REJECT
DOMAIN-SUFFIX,xjamtdyndy.com,REJECT
DOMAIN-SUFFIX,xjmjxjq.com,REJECT
DOMAIN-SUFFIX,xogzdcvdylxqg.site,REJECT
DOMAIN-SUFFIX,xswvoonrbxj.com,REJECT
DOMAIN-SUFFIX,xzlqiksfoihms.website,REJECT
DOMAIN-SUFFIX,yacgsaamnkiln.website,REJECT
DOMAIN-SUFFIX,yfilwkylyfnge.space,REJECT
DOMAIN-SUFFIX,yof9jg568k347e2nmzem6yi83oyhy4u15wr.rest,REJECT
DOMAIN-SUFFIX,yr1972kn5orxe4q.cfd,REJECT
DOMAIN-SUFFIX,yrlsmjdpscscn.website,REJECT
DOMAIN-SUFFIX,ywepfpptleofr.site,REJECT
DOMAIN-SUFFIX,ywhwgbmyylzxm.website,REJECT
DOMAIN-SUFFIX,yzbetezaitzew.online,REJECT
DOMAIN-SUFFIX,z989qkwjq2r12qwyc76bbx7yp5k7cp.cfd,REJECT
DOMAIN-SUFFIX,zjoacr.com,REJECT
DOMAIN-SUFFIX,zpmeimfikuacb.website,REJECT
DOMAIN-SUFFIX,zuukxvvp.com,REJECT
DOMAIN-SUFFIX,zvzlalhsmengo.website,REJECT
DOMAIN-SUFFIX,zwkpevnhhfjpt.online,REJECT
DOMAIN-SUFFIX,zwlhvuires.com,REJECT
DOMAIN-SUFFIX,zzwugofxijrfm.space,REJECT
```
</details>

## ⚠️ 敏感域名已自动过滤（银行/支付）

**原因**：域名包含银行/支付关键词，为防止隐私泄露，不加入解密列表。

<details>
<summary>展开查看被过滤的敏感域名（共 7 个）</summary>

```
lban.spdb.com.cn
m.creditcard.ecitic.com
webappcfg.paas.cmbchina.com
mpos-pic.helipay.com
creditcardapp.bankcomm.com
creditcardapp.bankcomm.cn
yunbusiness.ccb.com
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

🩺 Shield模块: 健康检查通过（290606 条规则，13.1 MB）

✅ Shield 模块已写入，代理 48810 条，去广告 241796 条

## 🩺 规则源健康状态

<details>
<summary>展开查看各上游源健康状态（共 13 个源）</summary>

- ✅ https://raw.githubusercontent.com/GMOogway/shadowrocket-rules/master/sr_direct_list.module
  - 成功 183 次，失败 0 次，连续失败 0 次
  - 最近成功: 2026-11-25 08:31:55
  - 最近失败: 无 

- ✅ https://raw.githubusercontent.com/GMOogway/shadowrocket-rules/master/sr_proxy_list.module
  - 成功 183 次，失败 0 次，连续失败 0 次
  - 最近成功: 2026-11-25 08:32:05
  - 最近失败: 无 

- ✅ https://raw.githubusercontent.com/LOWERTOP/Shadowrocket-First/main/Talkatone.sgmodule
  - 成功 183 次，失败 0 次，连续失败 0 次
  - 最近成功: 2026-11-25 08:32:05
  - 最近失败: 无 

- ✅ https://raw.githubusercontent.com/huijingfei/Shadowrocket-Rules/refs/heads/main/sr_app_ad.module
  - 成功 183 次，失败 0 次，连续失败 0 次
  - 最近成功: 2026-11-25 08:32:05
  - 最近失败: 无 

- ✅ https://raw.githubusercontent.com/deezertidal/shadowrocket-rules/refs/heads/main/modules/startingad.module
  - 成功 183 次，失败 0 次，连续失败 0 次
  - 最近成功: 2026-11-25 08:32:05
  - 最近失败: 无 

- ✅ https://raw.githubusercontent.com/GMOogway/shadowrocket-rules/master/sr_reject_list.module
  - 成功 183 次，失败 0 次，连续失败 0 次
  - 最近成功: 2026-11-25 08:32:06
  - 最近失败: 无 

- ✅ https://raw.githubusercontent.com/Unwhimsical/NetPilot/refs/heads/main/modules/%E6%B5%8B%E8%AF%95.module
  - 成功 183 次，失败 0 次，连续失败 0 次
  - 最近成功: 2026-11-25 08:32:06
  - 最近失败: 无 

- ✅ https://raw.githubusercontent.com/LOWERTOP/Shadowrocket-First/main/TalkatoneAntiAds.list
  - 成功 183 次，失败 0 次，连续失败 0 次
  - 最近成功: 2026-11-25 08:32:06
  - 最近失败: 无 

- ✅ https://johnshall.github.io/Shadowrocket-ADBlock-Rules-Forever/sr_top500_banlist_ad.conf
  - 成功 22 次，失败 0 次，连续失败 0 次
  - 最近成功: 2026-11-25 08:32:05
  - 最近失败: 无 

- ✅ https://johnshall.github.io/Shadowrocket-ADBlock-Rules-Forever/sr_cnip_ad.conf
  - 成功 22 次，失败 0 次，连续失败 0 次
  - 最近成功: 2026-11-25 08:32:05
  - 最近失败: 无 

- ✅ https://johnshall.github.io/Shadowrocket-ADBlock-Rules-Forever/sr_ad_only.conf
  - 成功 22 次，失败 0 次，连续失败 0 次
  - 最近成功: 2026-11-25 08:32:07
  - 最近失败: 无 

- ✅ https://yfamilys.com/module/AdBlock.module
  - 成功 22 次，失败 0 次，连续失败 0 次
  - 最近成功: 2026-11-25 08:32:07
  - 最近失败: 无 

- ✅ https://yfamilys.com/module/adultraplus.module
  - 成功 22 次，失败 0 次，连续失败 0 次
  - 最近成功: 2026-11-25 08:32:07
  - 最近失败: 无 

</details>

## 🔒 DNS 泄漏风险检测

### 🔴 高风险（89 条）

<details>
<summary>展开查看高风险详情</summary>

- **直连海外域名**
  直连规则包含海外域名: DOMAIN,adcdownload.apple.com.akadns.net,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **直连海外域名**
  直连规则包含海外域名: DOMAIN,amp-api-edge-lb-cn.itunes-apple.com.akadns.net,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **直连海外域名**
  直连规则包含海外域名: DOMAIN,amp-api-edge-lb.itunes-apple.com.akadns.net,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **直连海外域名**
  直连规则包含海外域名: DOMAIN,app-site-association.cdn-apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **直连海外域名**
  直连规则包含海外域名: DOMAIN,appleid.cdn-apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **直连海外域名**
  直连规则包含海外域名: DOMAIN,bag-cdn.itunes-apple.com.akadns.net,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

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
  直连规则包含海外域名: DOMAIN,cds.apple.com.akadns.net,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **直连海外域名**
  直连规则包含海外域名: DOMAIN,certs-lb.apple.com.akadns.net,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **直连海外域名**
  直连规则包含海外域名: DOMAIN,cl1-cdn.origin-apple.com.akadns.net,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **直连海外域名**
  直连规则包含海外域名: DOMAIN,cl2-cdn.origin-apple.com.akadns.net,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **直连海外域名**
  直连规则包含海外域名: DOMAIN,cl2.apple.com.edgekey.net.globalredir.akadns.net,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **直连海外域名**
  直连规则包含海外域名: DOMAIN,cl3-cdn.origin-apple.com.akadns.net,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **直连海外域名**
  直连规则包含海外域名: DOMAIN,cl4-cdn.origin-apple.com.akadns.net,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **直连海外域名**
  直连规则包含海外域名: DOMAIN,cl5-cdn.origin-apple.com.akadns.net,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **直连海外域名**
  直连规则包含海外域名: DOMAIN,clientflow.apple.com.akadns.net,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **直连海外域名**
  直连规则包含海外域名: DOMAIN,configuration.apple.com.akadns.net,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **直连海外域名**
  直连规则包含海外域名: DOMAIN,crl-lb.apple.com.akadns.net,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **直连海外域名**
  直连规则包含海外域名: DOMAIN,cstat.cdn-apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **直连海外域名**
  直连规则包含海外域名: DOMAIN,dd-cdn.origin-apple.com.akadns.net,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **直连海外域名**
  直连规则包含海外域名: DOMAIN,gsp4-cn.ls.apple.com.edgekey.net.globalredir.akadns.net,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **直连海外域名**
  直连规则包含海外域名: DOMAIN,gspe19-2-cn-ssl.ls-apple.com.akadns.net,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **直连海外域名**
  直连规则包含海外域名: DOMAIN,gspe19-cn.ls-apple.com.akadns.net,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **直连海外域名**
  直连规则包含海外域名: DOMAIN,images.apple.com.edgekey.net.globalredir.akadns.net,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **直连海外域名**
  直连规则包含海外域名: DOMAIN,inappcheck-cn.itunes-apple.com.akadns.net,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **直连海外域名**
  直连规则包含海外域名: DOMAIN,inappcheck-lb.itunes-apple.com.akadns.net,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **直连海外域名**
  直连规则包含海外域名: DOMAIN,init-p01md-lb.push-apple.com.akadns.net,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **直连海外域名**
  直连规则包含海外域名: DOMAIN,init-p01st-lb.push-apple.com.akadns.net,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **直连海外域名**
  直连规则包含海外域名: DOMAIN,init-s01st-lb.push-apple.com.akadns.net,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **直连海外域名**
  直连规则包含海外域名: DOMAIN,init.gc-lb.apple.com.akadns.net,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **直连海外域名**
  直连规则包含海外域名: DOMAIN,iphone-ld.origin-apple.com.akadns.net,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **直连海外域名**
  直连规则包含海外域名: DOMAIN,is-ssl.mzstatic.com-cn-lb.itunes-apple.com.akadns.net,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **直连海外域名**
  直连规则包含海外域名: DOMAIN,itunes-apple.com.akadns.net,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **直连海外域名**
  直连规则包含海外域名: DOMAIN,mensura.cdn-apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **直连海外域名**
  直连规则包含海外域名: DOMAIN,mesu-cdn.apple.com.akadns.net,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **直连海外域名**
  直连规则包含海外域名: DOMAIN,mesu-china.apple.com.akadns.net,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **直连海外域名**
  直连规则包含海外域名: DOMAIN,ml.cdn-apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **直连海外域名**
  直连规则包含海外域名: DOMAIN,oscdn.origin-apple.com.akadns.net,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **直连海外域名**
  直连规则包含海外域名: DOMAIN,prod-support.apple-support.akadns.net,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **直连海外域名**
  直连规则包含海外域名: DOMAIN,publicassets.cdn-apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **直连海外域名**
  直连规则包含海外域名: DOMAIN,shazam-insights.cdn-apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **直连海外域名**
  直连规则包含海外域名: DOMAIN,stocks-sparkline-lb.apple.com.akadns.net,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **直连海外域名**
  直连规则包含海外域名: DOMAIN,store.apple.com.edgekey.net,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **直连海外域名**
  直连规则包含海外域名: DOMAIN,store.apple.com.edgekey.net.globalredir.akadns.net,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **直连海外域名**
  直连规则包含海外域名: DOMAIN,store.storeimages.apple.com.akadns.net,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **直连海外域名**
  直连规则包含海外域名: DOMAIN,store.storeimages.cdn-apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **直连海外域名**
  直连规则包含海外域名: DOMAIN,support-china.apple-support.akadns.net,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **直连海外域名**
  直连规则包含海外域名: DOMAIN,swcatalog-cdn.apple.com.akadns.net,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **直连海外域名**
  直连规则包含海外域名: DOMAIN,swdist.apple.com.akadns.net,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **直连海外域名**
  直连规则包含海外域名: DOMAIN,swscan-cdn.apple.com.akadns.net,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **直连海外域名**
  直连规则包含海外域名: DOMAIN,updates-http.cdn-apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **直连海外域名**
  直连规则包含海外域名: DOMAIN,updates-http.cdn-apple.com.akadns.net,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **直连海外域名**
  直连规则包含海外域名: DOMAIN,updates.cdn-apple.com,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **直连海外域名**
  直连规则包含海外域名: DOMAIN,valid.origin-apple.com.akadns.net,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **直连海外域名**
  直连规则包含海外域名: DOMAIN,weather-data.apple.com.akadns.net,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

- **直连海外域名**
  直连规则包含海外域名: DOMAIN,www.apple.com.edgekey.net.globalredir.akadns.net,DIRECT，可能导致 DNS 查询在本地解析，暴露访问记录。

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
