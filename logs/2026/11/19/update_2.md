# 更新日志 2026-11-19

**运行时间**: 2026-11-19 20:28:06 北京时间

---

## 直连模块

### 🔍 过滤海外/强制代理直连规则（共 944 条）

**原因**：规则域名匹配海外黑名单关键词，或属于强制代理域名（如定位模块）。

<details>
<summary>展开查看被过滤规则及命中关键词</summary>

```
- DOMAIN-SUFFIX,ghmd448.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,oemssl.cn.cdn.cloudflare.net,DIRECT  (命中: cloudflare)
- DOMAIN-SUFFIX,beijing-hmo.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,awsdns-vip.com,DIRECT  (命中: aws)
- URL-REGEX,"^https?:\/\/r+[0-9]+(---|\.)sn-(2x3|ni5|j5o)\w{5}\.googlevideo\.com.*$",DIRECT  (命中: google)
- DOMAIN,ssl.gstatic.com,DIRECT  (命中: gstatic.com)
- DOMAIN-SUFFIX,cbdstest.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,awsdns-cn-40.biz,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,flygon.net,DIRECT  (命中: fly)
- DOMAIN,azuremigratetest.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN,clickserver.googleads.com,DIRECT  (命中: google)
- DOMAIN-SUFFIX,aliexpress-media.com,DIRECT  (命中: aliexpress)
- DOMAIN-SUFFIX,npmtrend.com,DIRECT  (命中: npm)
- DOMAIN-SUFFIX,awsonamazon.com,DIRECT  (命中: amazon)
- DOMAIN-SUFFIX,iflytektstd.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,lhmp.cc,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,lhmj.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,jiansujihm.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,acrel-znyf.com,DIRECT  (命中: acr)
- DOMAIN-SUFFIX,awsdns-cn-56.net,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,fireflyacg.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,ctrender.com,DIRECT  (命中: render)
- DOMAIN-SUFFIX,awsdns-cn-24.biz,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,hmwdj.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,citichmc.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,gzrecruit.com,DIRECT  (命中: ecr)
- DOMAIN-SUFFIX,njhmmr.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,whoami.akamai.net,DIRECT  (命中: akamai)
- DOMAIN-SUFFIX,flyenglish.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,welchmat.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,iflyink.com,DIRECT  (命中: fly)
- DOMAIN,safebrowsing.googleapis.com,DIRECT  (命中: google)
- DOMAIN-SUFFIX,awsdns-cn-03.biz,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,jhmnew.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,3hmedicalgroup.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,jhqshfly.com,DIRECT  (命中: fly)
- DOMAIN,mpnbenefitsrtluat.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,hmxw.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,xhma.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,shmtu.net,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,flyai.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,toprender.com,DIRECT  (命中: render)
- DOMAIN-SUFFIX,flyme.net,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,sfecr.com,DIRECT  (命中: ecr)
- DOMAIN-SUFFIX,hm16888.net,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,awsdns-cn-21.biz,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,t-firefly.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,ddwhm.com,DIRECT  (命中: hm)
- DOMAIN,redirector.c.mail.google.com,DIRECT  (命中: google)
- DOMAIN-SUFFIX,nnpml.com,DIRECT  (命中: npm)
- DOMAIN-SUFFIX,flymeyun.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,seersecret.com,DIRECT  (命中: ecr)
- DOMAIN-SUFFIX,awsdns-cn-28.net,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,awsdns-cn-25.net,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,awsdns-cn-12.biz,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,awsdns-cn-05.net,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,testshm.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,hfhm.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,hmz8.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,bjhdhm.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,flysheeep.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,chinacrankshaft.com,DIRECT  (命中: acr)
- DOMAIN-SUFFIX,wishcad.com,DIRECT  (命中: wish)
- DOMAIN-SUFFIX,shmet.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,azure.cc,DIRECT  (命中: azure)
- DOMAIN-SUFFIX,googleyixia.com,DIRECT  (命中: google)
- DOMAIN-SUFFIX,awsdns-cn-29.biz,DIRECT  (命中: aws)
- DOMAIN,redirector.c.play.google.com,DIRECT  (命中: google)
- DOMAIN-SUFFIX,dockerone.com,DIRECT  (命中: docker)
- DOMAIN-SUFFIX,awsdns-cn-49.biz,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,fhmion.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,awsdns-cn-38.net,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,awsdns-cn-54.biz,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,ahmif.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,mbs.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,gxlzhm.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,cnpmjs.org,DIRECT  (命中: npm)
- DOMAIN-SUFFIX,gxhhmed.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,bulbsquare.com,DIRECT  (命中: square)
- DOMAIN-SUFFIX,awsdns-cn-46.net,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,officecdn.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,3hmlg.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,fulinpm.com,DIRECT  (命中: npm)
- DOMAIN-SUFFIX,iflying.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,hlnpm.com,DIRECT  (命中: npm)
- DOMAIN,firebase-settings.crashlytics.com,DIRECT  (命中: firebase)
- DOMAIN-SUFFIX,vultrvps.com,DIRECT  (命中: vultr)
- DOMAIN-SUFFIX,hlhmf.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,smogfly.cloud,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,ghsmpwalmart.com,DIRECT  (命中: walmart)
- DOMAIN-SUFFIX,iwishwed.com,DIRECT  (命中: wish)
- DOMAIN-SUFFIX,mpnbenefits.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,syfly007.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,cloudflareinsights-cn.com,DIRECT  (命中: cloudflare)
- DOMAIN-SUFFIX,hmqjsb.com,DIRECT  (命中: hm)
- DOMAIN,ssl-google-analytics.l.google.com,DIRECT  (命中: google)
- DOMAIN-SUFFIX,3zhm.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,hmlcar.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,edgeone-browser-rendering.com,DIRECT  (命中: render)
- DOMAIN,googlevads-cn.com,DIRECT  (命中: google)
- DOMAIN-SUFFIX,sdhmkj.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,volic.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,chmgames.com,DIRECT  (命中: hm)
- DOMAIN,crashlyticsreports-pa.googleapis.com,DIRECT  (命中: google)
- DOMAIN-SUFFIX,fly1999.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,officebay.net,DIRECT  (命中: ebay)
- DOMAIN-SUFFIX,facebooksx.com,DIRECT  (命中: facebook)
- DOMAIN-SUFFIX,megarobo.com,DIRECT  (命中: mega)
- DOMAIN-SUFFIX,netsyq.com,DIRECT  (命中: etsy)
- DOMAIN,googletagmanager-cn.com,DIRECT  (命中: google)
- DOMAIN-SUFFIX,hmhpay.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,ghmcchina.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,scratchmirror.net,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,minecraftxz.com,DIRECT  (命中: ecr)
- DOMAIN-SUFFIX,scratchmirror.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,githubshare.com,DIRECT  (命中: github)
- DOMAIN-SUFFIX,akamai.com,DIRECT  (命中: akamai)
- DOMAIN-SUFFIX,zxhmjj.com,DIRECT  (命中: hm)
- DOMAIN,googleadservices.com,DIRECT  (命中: google)
- DOMAIN-SUFFIX,dl.delivery.mp.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,digcredit.com,DIRECT  (命中: gcr)
- DOMAIN-SUFFIX,bzmhm.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,cloudflareanycast.net,DIRECT  (命中: cloudflare)
- DOMAIN-SUFFIX,awsdns-cn-50.net,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,awsdns-cn-02.biz,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,googlevoice.org,DIRECT  (命中: google)
- DOMAIN,software.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,yz-proton.com,DIRECT  (命中: proton)
- DOMAIN-SUFFIX,awsamazonlab.com,DIRECT  (命中: amazon)
- DOMAIN-SUFFIX,hm152n.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,dmhmusic.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,dcg.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN,googleoptimize-cn.com,DIRECT  (命中: google)
- DOMAIN,redirector.c.youtubeeducation.com,DIRECT  (命中: youtube)
- DOMAIN-SUFFIX,shmbjy.org,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,awsdns-cn-48.biz,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,awsdns-cn-57.com,DIRECT  (命中: aws)
- DOMAIN,oemsocuat.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- URL-REGEX,"^https?:\/\/.+\.awsdns-cn-[0-9][0-9]\.(biz|com|net|top).*$",DIRECT  (命中: aws)
- DOMAIN-SUFFIX,megasig.com,DIRECT  (命中: mega)
- DOMAIN-SUFFIX,wecrm.com,DIRECT  (命中: ecr)
- DOMAIN-SUFFIX,zchmh.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,whmeigao.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,glhmmr.com,DIRECT  (命中: hm)
- DOMAIN,g0.gstatic.com,DIRECT  (命中: gstatic.com)
- DOMAIN-SUFFIX,simplecreator.net,DIRECT  (命中: ecr)
- DOMAIN-SUFFIX,awsdns-cn-52.biz,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,awsdns-cn-43.biz,DIRECT  (命中: aws)
- DOMAIN,imasdk.googleapis.com,DIRECT  (命中: google)
- DOMAIN-SUFFIX,xhmedia.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,grender.com,DIRECT  (命中: render)
- DOMAIN-SUFFIX,ahmky.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,bjhmcm.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,hmxixie.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,flyfunny.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,weighment.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,awsdns-cn-17.biz,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,flydigi.com,DIRECT  (命中: fly)
- DOMAIN,checkin.gstatic.com,DIRECT  (命中: gstatic.com)
- DOMAIN,vz.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,thmz.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,gxhmdjt.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,edrawsoft.com,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,ecrrc.com,DIRECT  (命中: ecr)
- DOMAIN-SUFFIX,pmphmooc.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,macrozheng.com,DIRECT  (命中: acr)
- DOMAIN-SUFFIX,jshmrcb.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,1fly.fun,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,azuremigrate.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,megajoy.com,DIRECT  (命中: mega)
- DOMAIN-SUFFIX,awsdns-cn-44.net,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,cnflyinghorse.com,DIRECT  (命中: fly)
- DOMAIN,googletraveladservices-cn.com,DIRECT  (命中: google)
- DOMAIN-SUFFIX,flyml.net,DIRECT  (命中: fly)
- DOMAIN,fonts.gstatic.com,DIRECT  (命中: gstatic.com)
- DOMAIN-SUFFIX,shmondial.com,DIRECT  (命中: hm)
- DOMAIN,redirector.c.chat.google.com,DIRECT  (命中: google)
- DOMAIN-SUFFIX,flyhand.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,download.visualstudio.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,fly3949.com,DIRECT  (命中: fly)
- DOMAIN,qpx.googleflights.net,DIRECT  (命中: google)
- DOMAIN-SUFFIX,ylxhmy.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,whuznhmedj.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,ztrhmall.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,awsdns-cn-45.com,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,shmfmr.net,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,dylyghm.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,aliexpress.us,DIRECT  (命中: aliexpress)
- DOMAIN-SUFFIX,shmhzp.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,acloudrender.com,DIRECT  (命中: render)
- DOMAIN-SUFFIX,awsdns-cn-50.biz,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,elongstatic.com,DIRECT  (命中: gstatic.com)
- DOMAIN-SUFFIX,awsdns-cn-55.com,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,lzbhmy.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,flyco.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,zhmxchina.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,awsdns-cn-14.biz,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,awsdns-cn-20.net,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,secrui.com,DIRECT  (命中: ecr)
- DOMAIN-SUFFIX,nhmuni.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,thmovie.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,iva-schmetz.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,hmlan.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,surface-microsoftstore.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,shmaas.net,DIRECT  (命中: hm)
- DOMAIN,windbg.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,azurestackhub.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,chinacrops.org,DIRECT  (命中: acr)
- DOMAIN,cache.pack.google.com,DIRECT  (命中: google)
- DOMAIN,volic.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,awsdns-cn-33.net,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,sphmc.org,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,awsdns-cn-17.net,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,gshmhotels.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,awsdns-cn-16.net,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,wodecrowd.com,DIRECT  (命中: ecr)
- DOMAIN,lexuat.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,kindechem.com,DIRECT  (命中: kinde)
- DOMAIN-SUFFIX,ifireflygame.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,microsoftuwp.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,rsm.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,sxhm.com,DIRECT  (命中: hm)
- DOMAIN,wear.googleapis.com,DIRECT  (命中: google)
- DOMAIN-SUFFIX,azureyun.com,DIRECT  (命中: azure)
- DOMAIN-SUFFIX,npmmirror.com,DIRECT  (命中: npm)
- DOMAIN-SUFFIX,collaborate.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,megagenchina.com,DIRECT  (命中: mega)
- DOMAIN-SUFFIX,qiantangcredit.com,DIRECT  (命中: gcr)
- DOMAIN-SUFFIX,awsdns-cn-15.net,DIRECT  (命中: aws)
- DOMAIN,google-analytics-cn.com,DIRECT  (命中: google)
- DOMAIN-SUFFIX,fawsoft.com,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,hm5988.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,hearfly.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,qzynhhmm.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,unpmcc.com,DIRECT  (命中: npm)
- DOMAIN-SUFFIX,bwfhmall.com,DIRECT  (命中: hm)
- DOMAIN,vscode.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,awsdns-cn-46.biz,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,chinacreator.com,DIRECT  (命中: acr)
- DOMAIN-SUFFIX,oemsoc.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,hyundai-hmtc.com,DIRECT  (命中: hm)
- URL-REGEX,"^https?:\/\/.+\.awsdns-cn-[0-9][a-e0-9]\.cn.*$",DIRECT  (命中: aws)
- DOMAIN-SUFFIX,awsdns-cn-41.com,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,secretflow.com,DIRECT  (命中: ecr)
- DOMAIN-SUFFIX,awsdns-cn-06.net,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,shmaur.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,mikecrm.com,DIRECT  (命中: ecr)
- DOMAIN-SUFFIX,tokenrhythm.studio,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,iflyread.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,azureflame.cloud,DIRECT  (命中: azure)
- DOMAIN-SUFFIX,qhm123.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,awsdns-cn-12.net,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,itfly.net,DIRECT  (命中: fly)
- DOMAIN,officemkt.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,awsdns-cn-62.net,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,macrolake.com,DIRECT  (命中: acr)
- DOMAIN-SUFFIX,shlawserve.com,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,awspaas.com,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,osrelease.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,hmadgz.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,awsdns-cn-59.net,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,zhmag.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,jxhmjx.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,eflycloud.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,vdfly.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,mysecretrainbow.com,DIRECT  (命中: ecr)
- DOMAIN-SUFFIX,awsdns-cn-55.net,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,awsdns-cn-37.net,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,rushmail.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,qjhm.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,whmylike.cc,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,rcolab.com,DIRECT  (命中: colab)
- DOMAIN-SUFFIX,openai.wf,DIRECT  (命中: openai)
- DOMAIN-SUFFIX,brighticecream.com,DIRECT  (命中: ecr)
- DOMAIN-SUFFIX,awsdns-cn-19.net,DIRECT  (命中: aws)
- DOMAIN,adservice.google.com,DIRECT  (命中: google)
- DOMAIN-SUFFIX,chinacraa.org,DIRECT  (命中: acr)
- DOMAIN,www-googletagmanager.l.google.com,DIRECT  (命中: google)
- DOMAIN-SUFFIX,wecrm.net,DIRECT  (命中: ecr)
- DOMAIN-SUFFIX,hmxx.net,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,likeacg.com,DIRECT  (命中: ikea)
- DOMAIN-SUFFIX,awsdns-cn-24.com,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,software.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,cn-railway.net,DIRECT  (命中: railway)
- DOMAIN-SUFFIX,awsdns-cn-20.com,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,flyneutron.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,ahmwgroup.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,hmwzjs.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,cqrailway.com,DIRECT  (命中: railway)
- DOMAIN-SUFFIX,xhmwxy.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,natywish.com,DIRECT  (命中: wish)
- DOMAIN-SUFFIX,awsdns-cn-41.biz,DIRECT  (命中: aws)
- DOMAIN,collaborate.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,dagongcredit.com,DIRECT  (命中: gcr)
- DOMAIN-SUFFIX,seaflysoft.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,appsflyer-cn.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,oneflys.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,awsdns-cn-19.biz,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,collaborateppe.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,hm588.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,hmplay.com,DIRECT  (命中: hm)
- DOMAIN,tools.google.com,DIRECT  (命中: google)
- DOMAIN-SUFFIX,squarecn.com,DIRECT  (命中: square)
- DOMAIN-SUFFIX,hmzhtc.cc,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,haofly.net,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,applysquare.net,DIRECT  (命中: square)
- DOMAIN-SUFFIX,protontechcn.com,DIRECT  (命中: proton)
- DOMAIN-SUFFIX,awsdns-cn-39.biz,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,nnhmcj.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,protong.com,DIRECT  (命中: proton)
- DOMAIN-SUFFIX,awsdns-cn-34.com,DIRECT  (命中: aws)
- DOMAIN,msproduct.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,vlportal.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN,googleanalytics.com,DIRECT  (命中: google)
- DOMAIN-SUFFIX,xahmqy.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,omegatravel.net,DIRECT  (命中: mega)
- DOMAIN-SUFFIX,armfly.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,dhmeri.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,renderbus.com,DIRECT  (命中: render)
- DOMAIN-SUFFIX,chmia.org,DIRECT  (命中: hm)
- DOMAIN,download.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,asosoaiid.com,DIRECT  (命中: asos)
- DOMAIN-SUFFIX,cloudflarestoragegw.com,DIRECT  (命中: cloudflare)
- DOMAIN-SUFFIX,zjecredit.org,DIRECT  (命中: ecr)
- DOMAIN-SUFFIX,sharjahmadrasa.com,DIRECT  (命中: hm)
- DOMAIN,googletagmanager.com,DIRECT  (命中: google)
- DOMAIN-SUFFIX,awsdns-cn-24.net,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,hhmage.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,wishdown.com,DIRECT  (命中: wish)
- DOMAIN-SUFFIX,hmting.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,whmzkf.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,squarefong.com,DIRECT  (命中: square)
- DOMAIN-SUFFIX,hmarathon.com,DIRECT  (命中: hm)
- DOMAIN,googleapps-cn.com,DIRECT  (命中: google)
- DOMAIN-SUFFIX,whmoocs.com,DIRECT  (命中: hm)
- DOMAIN,dreamspark.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,hmus.net,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,jcodecraeer.com,DIRECT  (命中: ecr)
- DOMAIN-SUFFIX,ovhlb.net,DIRECT  (命中: ovh)
- DOMAIN-SUFFIX,jinshmgw.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,zhmedcenter.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,yytiflytek.com,DIRECT  (命中: fly)
- DOMAIN,pagead-googlehosted.l.google.com,DIRECT  (命中: google)
- DOMAIN-SUFFIX,awsdns-cn-36.net,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,c-thme.com,DIRECT  (命中: hm)
- DOMAIN,gs-loc-cn.apple.com,DIRECT  (命中: 强制代理域名)
- DOMAIN,surface.downloads.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,edgeone-browser-rendering-dev.com,DIRECT  (命中: render)
- DOMAIN-SUFFIX,awsdns-cn-60.biz,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,awsdns-cn-07.com,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,meiji-icecream.com,DIRECT  (命中: ecr)
- DOMAIN-SUFFIX,tecreal.com,DIRECT  (命中: ecr)
- DOMAIN-SUFFIX,flysand.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,whmnls.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,jyhmz.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,cqhma.com,DIRECT  (命中: hm)
- DOMAIN,lex.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,nikefans.com,DIRECT  (命中: nike)
- DOMAIN-SUFFIX,chinawssdxh.com,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,mecru.com,DIRECT  (命中: ecr)
- DOMAIN-SUFFIX,fly63.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,wishetin.com,DIRECT  (命中: wish)
- DOMAIN,googlesyndication.com,DIRECT  (命中: google)
- DOMAIN-SUFFIX,southmoney.com,DIRECT  (命中: hm)
- DOMAIN,g1.gstatic.com,DIRECT  (命中: gstatic.com)
- DOMAIN-SUFFIX,hzhm888.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,awsdns-cn-22.net,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,awsdns-cn-06.com,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,hifly.mobi,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,telegramtoke.com,DIRECT  (命中: telegram)
- DOMAIN-SUFFIX,02hm.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,flymeos.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,hmnst.com,DIRECT  (命中: hm)
- DOMAIN,google-analytics.com,DIRECT  (命中: google)
- DOMAIN-SUFFIX,openailab.com,DIRECT  (命中: openai)
- DOMAIN-SUFFIX,surface.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN,download.visualstudio.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN,gstaticadssl.l.google.com,DIRECT  (命中: google)
- DOMAIN,msdprod-ad.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,cacre.org,DIRECT  (命中: acr)
- DOMAIN-SUFFIX,honchmedia.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,zhmold.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,mikeauth.com,DIRECT  (命中: ikea)
- DOMAIN-SUFFIX,macroprocess.com,DIRECT  (命中: acr)
- DOMAIN,download.mlcc.google.com,DIRECT  (命中: google)
- DOMAIN-SUFFIX,whmf8.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,qdhmsoft.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,qmacro.com,DIRECT  (命中: acr)
- DOMAIN-SUFFIX,awsdns-cn-42.com,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,secretgardenresorts.com,DIRECT  (命中: ecr)
- DOMAIN-SUFFIX,flypy.cc,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,awsdns-cn-27.biz,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,chinaacryl.com,DIRECT  (命中: acr)
- DOMAIN-SUFFIX,zhmu.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,awsdns-cn-07.net,DIRECT  (命中: aws)
- DOMAIN,clientservices.googleapis.com,DIRECT  (命中: google)
- DOMAIN,azurestackhub.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,flyfishx.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,whmdedu.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,awsdns-cn-59.biz,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,esdhm.net,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,cloudflareglobal.net,DIRECT  (命中: cloudflare)
- DOMAIN-SUFFIX,iflyrec.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,flyingeffect.com,DIRECT  (命中: fly)
- DOMAIN,storecorefulfillment.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN,itacademyuat.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,flashmemoryworld.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,elitecrm.com,DIRECT  (命中: ecr)
- DOMAIN-SUFFIX,gogofly.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,awsdns-cn-09.net,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,qihangcrrc.com,DIRECT  (命中: gcr)
- DOMAIN,googleflights-cn.net,DIRECT  (命中: google)
- DOMAIN-SUFFIX,azuremigratetest.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,awsdns-cn-48.net,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,wbecrisfro.com,DIRECT  (命中: ecr)
- DOMAIN-SUFFIX,chinaws.net,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,zztfly.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,myvs.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,officemktuat.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,xrender.com,DIRECT  (命中: render)
- DOMAIN-SUFFIX,azuretouch.net,DIRECT  (命中: azure)
- DOMAIN-SUFFIX,iflyadx.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,tinsecret.com,DIRECT  (命中: ecr)
- DOMAIN-SUFFIX,awsdns-cn-37.biz,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,lzhmmr.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,itgemini.net,DIRECT  (命中: gemini)
- DOMAIN-SUFFIX,dreamsparkuat.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,thmnet.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,bjhmyq.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,awsdns-cn-28.biz,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,cofly.com,DIRECT  (命中: fly)
- DOMAIN,pki-goog.l.google.com,DIRECT  (命中: google)
- DOMAIN,safebrowsing-cache.google.com,DIRECT  (命中: google)
- DOMAIN,download.tensorflow.google.com,DIRECT  (命中: google)
- DOMAIN-SUFFIX,hmtnew.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,shmljm.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,whhmmbl.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,hm-optics.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,iflytek.com,DIRECT  (命中: fly)
- DOMAIN,cdn.globalsigncdn.com.cdn.cloudflare.net,DIRECT  (命中: cloudflare)
- DOMAIN-SUFFIX,awsdns-cn-44.biz,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,awsdns-cn-09.com,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,awsdns-cn-18.biz,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,fly139.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,awsdns-cn-44.com,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,chinaflashmarket.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,shmockup.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,targetportion.com,DIRECT  (命中: target)
- DOMAIN-SUFFIX,yindo-ohm.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,acrossmetals.com,DIRECT  (命中: acr)
- DOMAIN-SUFFIX,hmtrhf.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,hmzs.net,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,hifly.tv,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,awsdns-cn-01.biz,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,ayhmjy.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,whmama.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,ttfly.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,thmins.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,gdsunfly.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,chmc.cc,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,daiwofly.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,fishflying.net,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,kphm88.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,zhmodaoli.com,DIRECT  (命中: hm)
- DOMAIN,googletagservices.com,DIRECT  (命中: google)
- DOMAIN-SUFFIX,qhmsg.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,hnsyhm.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,hmf-china.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,2google.com,DIRECT  (命中: google)
- DOMAIN-SUFFIX,cmacredit.org,DIRECT  (命中: acr)
- DOMAIN-SUFFIX,sdhmdp.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,arefly.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,volcecr.com,DIRECT  (命中: ecr)
- DOMAIN-SUFFIX,cloudflareperf.com,DIRECT  (命中: cloudflare)
- DOMAIN-SUFFIX,machmall.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,flymopaper.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,shmhtv.com,DIRECT  (命中: hm)
- DOMAIN,images-cn.ssl-images-amazon.com,DIRECT  (命中: amazon)
- DOMAIN,mpnbenefitsrtl.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,51google.com,DIRECT  (命中: google)
- DOMAIN-SUFFIX,mysecrettop.com,DIRECT  (命中: ecr)
- DOMAIN-SUFFIX,cdnchatgpt.com,DIRECT  (命中: chatgpt)
- DOMAIN,www-google-analytics.l.google.com,DIRECT  (命中: google)
- DOMAIN-SUFFIX,railwaybill.com,DIRECT  (命中: railway)
- DOMAIN-SUFFIX,cqs-hm.com,DIRECT  (命中: hm)
- DOMAIN,csi.gstatic.com,DIRECT  (命中: gstatic.com)
- DOMAIN-SUFFIX,awsdns-cn-51.com,DIRECT  (命中: aws)
- DOMAIN,googleoptimize.com,DIRECT  (命中: google)
- DOMAIN-SUFFIX,awsdns-cn-46.com,DIRECT  (命中: aws)
- DOMAIN,myvs.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN,dreamsparkuat.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN,azurestackhubuat.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,hmmachine.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,haiqianghm.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,whmxrj.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,luxtarget.com,DIRECT  (命中: target)
- DOMAIN-SUFFIX,e-flyinc.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,inflyway.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,thmall.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,awsdns-cn-35.net,DIRECT  (命中: aws)
- DOMAIN,dl.google.com,DIRECT  (命中: google)
- DOMAIN-SUFFIX,awsdns-cn-45.net,DIRECT  (命中: aws)
- DOMAIN,gs-loc.apple.com,DIRECT  (命中: 强制代理域名)
- DOMAIN-SUFFIX,sdx.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,flyingpigeon1936.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,flymeauto.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,hmgbtv.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,awsdns-cn-09.biz,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,thmzedu.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,cheetahmobile.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,awsdns-cn-51.biz,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,aliexpress.ru,DIRECT  (命中: aliexpress)
- DOMAIN,redirector.c.pack.google.com,DIRECT  (命中: google)
- DOMAIN-SUFFIX,vscode.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,awsdns-cn-52.net,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,feidacrusher.com,DIRECT  (命中: acr)
- DOMAIN-SUFFIX,yzhmyy.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,ihmch.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,awsdns-cn-61.biz,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,webclose-whatsapp.com,DIRECT  (命中: whatsapp)
- URL-REGEX,"^https?:\/\/.+-mihayo\.akamaized\.net.*$",DIRECT  (命中: akamai)
- DOMAIN-SUFFIX,oecr.com,DIRECT  (命中: ecr)
- DOMAIN-SUFFIX,ggshmy.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,gzhm.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,zhmf.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,ghmba.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,zbwhmedia.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,vecrp.com,DIRECT  (命中: ecr)
- DOMAIN-SUFFIX,ugdocker.link,DIRECT  (命中: docker)
- DOMAIN-SUFFIX,aftersale-amazon.com,DIRECT  (命中: amazon)
- DOMAIN-SUFFIX,hmgj.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,rainbutterfly.xyz,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,mpnbenefitsrtl.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,storeedge.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,googlenav.com,DIRECT  (命中: google)
- DOMAIN-SUFFIX,zgzhmz.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,hfly.net,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,awsdns-cn-17.com,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,happypingpang.com,DIRECT  (命中: pypi)
- DOMAIN,mpnbenefits.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,flyme.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,oacrm.com,DIRECT  (命中: acr)
- DOMAIN-SUFFIX,awsdns-cn-34.net,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,awsdns-cn-04.net,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,awsdns-cn-14.com,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,fly160.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,1818hm.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,hwrecruit.com,DIRECT  (命中: ecr)
- DOMAIN-SUFFIX,njnaws.com,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,iflydatahub.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,awsdns-cn-25.com,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,zzfly.net,DIRECT  (命中: fly)
- DOMAIN,googleapis-cn.com,DIRECT  (命中: google)
- DOMAIN-SUFFIX,rohm-chip.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,wish-hightech.com,DIRECT  (命中: wish)
- DOMAIN-SUFFIX,whmnx.com,DIRECT  (命中: hm)
- DOMAIN,g3.gstatic.com,DIRECT  (命中: gstatic.com)
- DOMAIN-SUFFIX,awsdns-cn-31.net,DIRECT  (命中: aws)
- DOMAIN,googletraveladservices.com,DIRECT  (命中: google)
- DOMAIN-SUFFIX,smogflycloud.net,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,shmama.net,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,chatgptboke.com,DIRECT  (命中: chatgpt)
- DOMAIN-SUFFIX,flytexpress.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,bebhmongb.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,hbhm.net,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,awsdns-cn-63.net,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,flytcloud.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,cloudhvacr.com,DIRECT  (命中: acr)
- DOMAIN-SUFFIX,awsdns-cn-35.biz,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,zgxhm.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,square16.org,DIRECT  (命中: square)
- DOMAIN-SUFFIX,pkulaws.com,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,secrss.com,DIRECT  (命中: ecr)
- DOMAIN-SUFFIX,fly998.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,yhm11.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,hm163.net,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,fly-exp.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,mpnbenefitsrtluat.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,wishtec.com,DIRECT  (命中: wish)
- DOMAIN-SUFFIX,uuu.ovh,DIRECT  (命中: ovh)
- DOMAIN-SUFFIX,sectigochina.com.cdn.cloudflare.net,DIRECT  (命中: cloudflare)
- DOMAIN-SUFFIX,iqhmh.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,xn--y8jhmm6gn.moe,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,msdn.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,whhmgroup.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,yjdatasos.com,DIRECT  (命中: asos)
- DOMAIN,msdn.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,flygo.net,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,azureflying.com,DIRECT  (命中: azure)
- DOMAIN-SUFFIX,youtube-dubbing.com,DIRECT  (命中: youtube)
- DOMAIN,googleadservices-cn.com,DIRECT  (命中: google)
- DOMAIN-SUFFIX,iflysec.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,awsdns-cn-11.com,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,cloudflareprod.com,DIRECT  (命中: cloudflare)
- DOMAIN,oemsoc.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN,rsm.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,znhhmedical.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,chinacrane.net,DIRECT  (命中: acr)
- DOMAIN,officemktuat.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,hmoe.link,DIRECT  (命中: hm)
- DOMAIN,storeedgefd.dsx.mp.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,4hmodel.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,iflygse.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,awspony.com,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,tshmkj.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,itacademyuat.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,macrr.com,DIRECT  (命中: acr)
- DOMAIN-SUFFIX,aflytec.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,awsdns-cn-62.biz,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,szhmjp.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,cproton.com,DIRECT  (命中: proton)
- DOMAIN-SUFFIX,zjgcreative.com,DIRECT  (命中: gcr)
- DOMAIN-SUFFIX,originalkindergarten.com,DIRECT  (命中: kinde)
- DOMAIN-SUFFIX,hnpm.cc,DIRECT  (命中: npm)
- DOMAIN-SUFFIX,hmj666.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,wishisp.com,DIRECT  (命中: wish)
- DOMAIN-SUFFIX,ceolaws.net,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,awsdns-cn-36.com,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,abcdocker.com,DIRECT  (命中: docker)
- DOMAIN-SUFFIX,googlebbs.net,DIRECT  (命中: google)
- DOMAIN,avail.googleflights.net,DIRECT  (命中: google)
- DOMAIN-SUFFIX,ucfly.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,xn--nmqp78hmufjwu.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,shmds.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,52kfly.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,lubanpm.com,DIRECT  (命中: npm)
- DOMAIN-SUFFIX,renderincloud.com,DIRECT  (命中: render)
- DOMAIN,surface.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,hkgcr.com,DIRECT  (命中: gcr)
- DOMAIN-SUFFIX,aliexpress.com,DIRECT  (命中: aliexpress)
- DOMAIN-SUFFIX,gyhm.cc,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,awsdns-cn-01.net,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,chinamaven.com,DIRECT  (命中: maven)
- DOMAIN-SUFFIX,sdhmjt.net,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,glflyy.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,smogfly.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,hicnhm.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,t-npm.com,DIRECT  (命中: npm)
- DOMAIN-SUFFIX,hmkp.org,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,czhmjx.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,xn--vhq4ut2dsxd5xqnicjxxo55a756aovhik0aunm.com,DIRECT  (命中: ovh)
- DOMAIN-SUFFIX,zhinikefu.com,DIRECT  (命中: nike)
- DOMAIN,c.android.clients.google.com,DIRECT  (命中: google)
- DOMAIN-SUFFIX,whmc2005.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,shmarathon.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,hbysfhm.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,whmvc.net,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,hmbzfjt.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,24hmb.com,DIRECT  (命中: hm)
- DOMAIN,osrelease.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,gemini530.net,DIRECT  (命中: gemini)
- DOMAIN-SUFFIX,hmrsrc.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,bshmzx.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,flymobi.biz,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,ntrailway.com,DIRECT  (命中: railway)
- DOMAIN-SUFFIX,bixuecrm.com,DIRECT  (命中: ecr)
- DOMAIN-SUFFIX,awsdns-cn-55.biz,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,awsdns-cn-54.net,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,hmzhtc.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,awsdns-cn-23.com,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,mightsquare.com,DIRECT  (命中: square)
- DOMAIN-SUFFIX,awsdns-cn-48.com,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,airtofly.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,jdhmediajd.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,awsdns-cn-53.com,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,awsdns-cn-18.net,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,szhmkeji.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,cyhm.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,lexuat.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,weflywifi.com,DIRECT  (命中: fly)
- DOMAIN,connectivitycheck.gstatic.com,DIRECT  (命中: gstatic.com)
- DOMAIN-SUFFIX,smogfly.club,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,megahugo.net,DIRECT  (命中: mega)
- DOMAIN-SUFFIX,91hmi.com,DIRECT  (命中: hm)
- DOMAIN,googletagservices-cn.com,DIRECT  (命中: google)
- DOMAIN,sdx.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN,cbdstest.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,awsdns-cn-10.com,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,englishmasterclub.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,hyahm.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,megagamelog.com,DIRECT  (命中: mega)
- DOMAIN-SUFFIX,awsdns-cn-36.biz,DIRECT  (命中: aws)
- DOMAIN,cache-management-prod.google.com,DIRECT  (命中: google)
- DOMAIN-SUFFIX,jhm2012.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,itacademy.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,cloudflare-cn.com,DIRECT  (命中: cloudflare)
- DOMAIN-SUFFIX,cloudflarestaging.com,DIRECT  (命中: cloudflare)
- DOMAIN,mbs.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,iflyaiedu.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,fishmobi.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,hnlshm.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,awsdns-cn-63.com,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,drugoogle.com,DIRECT  (命中: google)
- DOMAIN-SUFFIX,fingerflyapp.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,flyadx.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,ncjrailway.com,DIRECT  (命中: railway)
- DOMAIN-SUFFIX,dragonfly.fun,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,shmengzhong.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,gdhmgc.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,iflyhealth.com,DIRECT  (命中: fly)
- DOMAIN,dg-meta.video.google.com,DIRECT  (命中: google)
- DOMAIN-SUFFIX,smogfly.net,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,applysquare.com,DIRECT  (命中: square)
- DOMAIN-SUFFIX,mrwish.net,DIRECT  (命中: wish)
- DOMAIN-SUFFIX,iflynote.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,acroview.com,DIRECT  (命中: acr)
- DOMAIN-SUFFIX,shms-expo.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,czxthmls.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,yingyecraft.com,DIRECT  (命中: ecr)
- DOMAIN-SUFFIX,shmetro.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,hmtgo.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,azure-wave.com,DIRECT  (命中: azure)
- DOMAIN-SUFFIX,ecr-global.com,DIRECT  (命中: ecr)
- DOMAIN-SUFFIX,hminvestment.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,xn--vhqqbz2p62hm92e04p.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,gx-hm.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,lenovo.com.cdn.cloudflare.net,DIRECT  (命中: cloudflare)
- DOMAIN-SUFFIX,surface.downloads.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,bmp.ovh,DIRECT  (命中: ovh)
- DOMAIN-SUFFIX,imgs.ovh,DIRECT  (命中: ovh)
- DOMAIN-SUFFIX,pihmh.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,yhchmo.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,724pridecryogenics.com,DIRECT  (命中: ecr)
- DOMAIN-SUFFIX,whmnrc.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,facri.com,DIRECT  (命中: acr)
- DOMAIN-SUFFIX,flycua.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,hmedu.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,mcohmygod.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,megawords.cc,DIRECT  (命中: mega)
- DOMAIN-SUFFIX,dhmsnyy.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,awsdns-cn-52.com,DIRECT  (命中: aws)
- DOMAIN,www.gstatic.com,DIRECT  (命中: gstatic.com)
- DOMAIN-SUFFIX,neihanfly.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,awsdns-cn-58.biz,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,awsdns-cn-39.com,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,dreamspark.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,chinahvacr.com,DIRECT  (命中: acr)
- DOMAIN-SUFFIX,hbhmxx.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,githubim.com,DIRECT  (命中: github)
- DOMAIN-SUFFIX,awsdns-cn-11.biz,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,bjwhmedia.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,awsdns-cn-62.com,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,awsdns-cn-42.biz,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,szpowerfly.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,chinacrosspoint.com,DIRECT  (命中: acr)
- DOMAIN-SUFFIX,awsdns-cn-33.biz,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,hmgreat.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,hmltec.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,msproduct.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,awsdns-cn-05.biz,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,awsdns-cn-47.biz,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,victoriassecretclearance.online,DIRECT  (命中: ecr)
- DOMAIN-SUFFIX,bjhmdkj.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,hmx-led.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,hm-3223.net,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,shmzgroup.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,awsdns-cn-60.net,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,withmedia.net,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,gamegamept.com,DIRECT  (命中: mega)
- DOMAIN,time.amazonaws.cn,DIRECT  (命中: amazon)
- DOMAIN-SUFFIX,thwgetsy.com,DIRECT  (命中: etsy)
- DOMAIN-SUFFIX,moonfly.net,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,jxhmxxjs.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,xczhmzb.com,DIRECT  (命中: hm)
- DOMAIN,vlportal.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,hmly666.cc,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,smogflycloud.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,aquayee.com,DIRECT  (命中: quay)
- DOMAIN-SUFFIX,macrowing.com,DIRECT  (命中: acr)
- DOMAIN-SUFFIX,flylinking.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,qflyinc.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,qeoagphm.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,chmod0777kk.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,tlhmhd.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,awsdns-cn-47.com,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,dockerinfo.net,DIRECT  (命中: docker)
- DOMAIN-SUFFIX,magentochina.org,DIRECT  (命中: magento)
- DOMAIN-SUFFIX,ovhlb.com,DIRECT  (命中: ovh)
- DOMAIN-SUFFIX,flyertea.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,cloudflareip.com,DIRECT  (命中: cloudflare)
- DOMAIN-SUFFIX,algorithmart.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,qixingcr.com,DIRECT  (命中: gcr)
- DOMAIN,developer.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,lgstatic.com,DIRECT  (命中: gstatic.com)
- DOMAIN-SUFFIX,acrel-eem.com,DIRECT  (命中: acr)
- DOMAIN-SUFFIX,awsdns-cn-00.com,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,shhmbio.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,cloudfront-cn.net,DIRECT  (命中: cloudfront)
- DOMAIN-SUFFIX,whmlcy.net,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,macrosilicon.com,DIRECT  (命中: acr)
- DOMAIN-SUFFIX,shhmu.net,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,forcecreat.com,DIRECT  (命中: ecr)
- DOMAIN-SUFFIX,hmsemi.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,megaemoji.com,DIRECT  (命中: mega)
- DOMAIN-SUFFIX,googleppy.com,DIRECT  (命中: google)
- DOMAIN-SUFFIX,zchmbx.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,awsdns-cn-27.com,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,shmusicschool.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,athmapp.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,myhm.org,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,hefeilaws.com,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,cuahmap.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,bghmj.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,iflytoy.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,hmeili.com,DIRECT  (命中: hm)
- DOMAIN,update.googleapis.com,DIRECT  (命中: google)
- DOMAIN-SUFFIX,gacrnd.com,DIRECT  (命中: acr)
- DOMAIN-SUFFIX,yunqifly.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,codeflying.net,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,orasos.com,DIRECT  (命中: asos)
- DOMAIN-SUFFIX,hmqg.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,oktamall.com,DIRECT  (命中: okta)
- DOMAIN-SUFFIX,bfhmj.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,awsdns-cn-39.net,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,awsdns-cn-63.biz,DIRECT  (命中: aws)
- DOMAIN,g2.gstatic.com,DIRECT  (命中: gstatic.com)
- DOMAIN,officecdn.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,sunnyfly.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,iflydocs.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,awsdns-cn-20.biz,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,vz.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,iflyresearch.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,macrounion.com,DIRECT  (命中: acr)
- DOMAIN-SUFFIX,nike666.com,DIRECT  (命中: nike)
- DOMAIN,collaborateppe.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,3richman.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,hhmajiang.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,hmyzs.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,touchmark.art,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,msdprod-ad.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,shmengyang.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,elecrystal.com,DIRECT  (命中: ecr)
- DOMAIN-SUFFIX,lnwish.com,DIRECT  (命中: wish)
- DOMAIN,googlesyndication-cn.com,DIRECT  (命中: google)
- DOMAIN,images-cn-8.ssl-images-amazon.com,DIRECT  (命中: amazon)
- DOMAIN-SUFFIX,google-hub.com,DIRECT  (命中: google)
- DOMAIN-SUFFIX,awsdns-cn-58.net,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,macrosan.com,DIRECT  (命中: acr)
- DOMAIN-SUFFIX,hmszkj.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,machenike.com,DIRECT  (命中: nike)
- DOMAIN-SUFFIX,storecorefulfillment.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,gdlinefly.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,alltechmed.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,lzghmy.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,d5render.com,DIRECT  (命中: render)
- DOMAIN-SUFFIX,hmchina.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,awsdns-cn-40.net,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,likeaboat2023.com,DIRECT  (命中: ikea)
- DOMAIN-SUFFIX,awsdns-cn-26.com,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,awsdns-cn-02.net,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,i-firefly.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,jinshasitemuseum.com,DIRECT  (命中: temu)
- DOMAIN-SUFFIX,hyundai-chhm.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,chnrailway.com,DIRECT  (命中: railway)
- DOMAIN,itacademy.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,awsdns-cn-07.biz,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,hellogitlab.com,DIRECT  (命中: gitlab)
- DOMAIN-SUFFIX,iflyiot.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,shtimessquare.com,DIRECT  (命中: square)
- DOMAIN-SUFFIX,shmylike.com,DIRECT  (命中: hm)
- DOMAIN,azuremigrate.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,shmog.org,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,shmds.vip,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,hf-iflysse.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,eflybird.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,gxhmba.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,hmzixin.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,phmacn.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,cloudflare.fun,DIRECT  (命中: cloudflare)
- DOMAIN-SUFFIX,secretmine.net,DIRECT  (命中: ecr)
- DOMAIN-SUFFIX,cthhmu.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,haitianpm.com,DIRECT  (命中: npm)
- DOMAIN-SUFFIX,fly84.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,nike.host,DIRECT  (命中: nike)
- DOMAIN-SUFFIX,shmusic.org,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,awsdns-cn-60.com,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,awsdns-cn-56.biz,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,wish3d.com,DIRECT  (命中: wish)
- DOMAIN,fontfiles.googleapis.com,DIRECT  (命中: google)
- DOMAIN-SUFFIX,techmoris.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,cloudflarecn.net,DIRECT  (命中: cloudflare)
- DOMAIN-SUFFIX,fhmooc.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,zhmzqi.com,DIRECT  (命中: hm)
- DOMAIN,dl.l.google.com,DIRECT  (命中: google)
- DOMAIN-SUFFIX,awsdns-cn-23.net,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,awsdns-cn-40.com,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,awstar.net,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,officemkt.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,azurestackhubuat.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,awsdns-cn-21.net,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,chinacrt.com,DIRECT  (命中: acr)
- DOMAIN-SUFFIX,sheinet.com,DIRECT  (命中: shein)
- DOMAIN,performanceparameters.googleapis.com,DIRECT  (命中: google)
- DOMAIN-SUFFIX,awsdns-cn-16.biz,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,chihm.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,9125flying.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,vultrcn.com,DIRECT  (命中: vultr)
- DOMAIN-SUFFIX,hm025.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,whminwei.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,acrel-microgrid.com,DIRECT  (命中: acr)
- DOMAIN,storeedge.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,openai-hub.com,DIRECT  (命中: openai)
- DOMAIN-SUFFIX,awsdns-cn-58.com,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,chmed.net,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,qualcomm.cn.cdn.cloudflare.net,DIRECT  (命中: cloudflare)
- DOMAIN-SUFFIX,chmecc.org,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,yfldocker.com,DIRECT  (命中: docker)
- DOMAIN-SUFFIX,htyhm.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,lawsdata.com,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,fhmv.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,awsdns-cn-00.net,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,windbg.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,awsdns-cn-41.net,DIRECT  (命中: aws)
- DOMAIN,tac.googleapis.com,DIRECT  (命中: google)
- DOMAIN-SUFFIX,hm120.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,cdnhwcohm19.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,imags-google.com,DIRECT  (命中: google)
- DOMAIN-SUFFIX,whmj.org,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,bbgstatic.com,DIRECT  (命中: gstatic.com)
- DOMAIN-SUFFIX,hmjc.org,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,awsdns-cn-45.biz,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,hmrczp.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,hbhml.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,hmfxw.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,gemini-galaxy.com,DIRECT  (命中: gemini)
- DOMAIN-SUFFIX,lex.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,ideacreated.com,DIRECT  (命中: acr)
- DOMAIN-SUFFIX,oemsocuat.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,sun-wish.com,DIRECT  (命中: wish)
- DOMAIN-SUFFIX,xawscu.com,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,awsdns-cn-37.com,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,whichmba.net,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,techmiao.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,51render.com,DIRECT  (命中: render)
- DOMAIN-SUFFIX,chiconysquare.com,DIRECT  (命中: square)
- DOMAIN-SUFFIX,ylhmgz.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,chmti.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,lzarays.com,DIRECT  (命中: zara)
- DOMAIN-SUFFIX,shmedia.tech,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,awsdns-cn-22.com,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,awsdns-cn-47.net,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,tb-whatsapp.com,DIRECT  (命中: whatsapp)
- DOMAIN-SUFFIX,asosde.com,DIRECT  (命中: asos)
- DOMAIN-SUFFIX,minecraftzw.com,DIRECT  (命中: ecr)
```
</details>

### 🧹 直连规则去重删除（共 262 条）

**处理动作**：同一域名、同一策略的重复规则已删除，只保留一条；跨策略的不删。

<details>
<summary>展开查看去重样例（前 20 条）</summary>

```
- DOMAIN,sh-pod3-smp-device.apple.com,DIRECT  （被同策略父级 DOMAIN-SUFFIX,apple.com 覆盖）
- DOMAIN,cn.alibabacloud.com,DIRECT  （被同策略父级 DOMAIN-SUFFIX,alibabacloud.com 覆盖）
- DOMAIN,cds.apple.com,DIRECT  （被同策略父级 DOMAIN-SUFFIX,apple.com 覆盖）
- DOMAIN,api.blipsandchitz.me,DIRECT  （被同策略父级 DOMAIN-SUFFIX,blipsandchitz.me 覆盖）
- DOMAIN,bj1.api.bing.com,DIRECT  （被同策略 DOMAIN-SUFFIX,bj1.api.bing.com 覆盖）
- DOMAIN,storage.moegirl.org.cn,DIRECT  （被同策略父级 DOMAIN-SUFFIX,cn 覆盖）
- DOMAIN,dejavu.apple.com,DIRECT  （被同策略父级 DOMAIN-SUFFIX,apple.com 覆盖）
- DOMAIN,p6-juejin.byteimg.com,DIRECT  （被同策略父级 DOMAIN-SUFFIX,byteimg.com 覆盖）
- DOMAIN,iosapps.itunes.apple.com,DIRECT  （被同策略父级 DOMAIN-SUFFIX,apple.com 覆盖）
- DOMAIN,p9-juejin.byteimg.com,DIRECT  （被同策略父级 DOMAIN-SUFFIX,byteimg.com 覆盖）
- DOMAIN,p05.upd.kaspersky.com,DIRECT  （被同策略父级 DOMAIN-SUFFIX,upd.kaspersky.com 覆盖）
- DOMAIN,dnl-18.geo.kaspersky.com,DIRECT  （被同策略父级 DOMAIN-SUFFIX,geo.kaspersky.com 覆盖）
- DOMAIN,ntp4.aliyun.com,DIRECT  （被同策略父级 DOMAIN-SUFFIX,aliyun.com 覆盖）
- DOMAIN,amp-api.apps.apple.com,DIRECT  （被同策略父级 DOMAIN-SUFFIX,apple.com 覆盖）
- DOMAIN,km.support.apple.com,DIRECT  （被同策略父级 DOMAIN-SUFFIX,apple.com 覆盖）
- DOMAIN,s10.upd.kaspersky.com,DIRECT  （被同策略父级 DOMAIN-SUFFIX,upd.kaspersky.com 覆盖）
- DOMAIN,dnl-13.geo.kaspersky.com,DIRECT  （被同策略父级 DOMAIN-SUFFIX,geo.kaspersky.com 覆盖）
- DOMAIN,play.itunes.apple.com,DIRECT  （被同策略父级 DOMAIN-SUFFIX,apple.com 覆盖）
- DOMAIN,dnl-08.geo.kaspersky.com,DIRECT  （被同策略父级 DOMAIN-SUFFIX,geo.kaspersky.com 覆盖）
- DOMAIN,dnl-14.geo.kaspersky.com,DIRECT  （被同策略父级 DOMAIN-SUFFIX,geo.kaspersky.com 覆盖）
... 另有 242 条未列出
```
</details>

### 上游源状态

- ✅ https://raw.githubusercontent.com/GMOogway/shadowrocket-rules/master/sr_direct_list.module

**原有规则数**: 111362
**新增规则数**: 4
**更新后总数**: 111366

#### 新增规则明细

<details>
<summary>展开查看新增规则（共 4 条）</summary>

```
DOMAIN-SUFFIX,qpmcn.com,DIRECT
DOMAIN-SUFFIX,lenovofuturecenter.com,DIRECT
DOMAIN-SUFFIX,zhaoliangjipc.com,DIRECT
DOMAIN-SUFFIX,trpcdn.com,DIRECT
```
</details>

🩺 直连模块: 健康检查通过（111366 条规则，3.6 MB）

✅ 直连模块已写入，共 111366 条规则

## 代理分流模块

### 🛡️ 白名单豁免（代理规则，共 30 条）

**原因**：这些域名在 `direct_whitelist.txt` 中，已从代理规则中移除，确保走直连。

<details>
<summary>展开查看被豁免的代理规则（30 条）</summary>


- `DOMAIN,np-edge.itunes.apple.com,PROXY`
  - 匹配白名单：`itunes.apple.com`
  - 用途：iTunes/App Store 传统商店内容
- `DOMAIN,xtls.github.io,PROXY`
  - 匹配白名单：`github.io`
  - 用途：GitHub Pages 站点
- `DOMAIN,copilot-telemetry.githubusercontent.com,PROXY`
  - 匹配白名单：`githubusercontent.com`
  - 用途：GitHub 用户内容（raw 文件、图片、附件等）
- `DOMAIN,copilot-telemetry-service.githubusercontent.com,PROXY`
  - 匹配白名单：`githubusercontent.com`
  - 用途：GitHub 用户内容（raw 文件、图片、附件等）
- `DOMAIN-SUFFIX,githubusercontent.com,PROXY`
  - 匹配白名单：`githubusercontent.com`
  - 用途：GitHub 用户内容（raw 文件、图片、附件等）
- `DOMAIN,uts-api.itunes.apple.com,PROXY`
  - 匹配白名单：`itunes.apple.com`
  - 用途：iTunes/App Store 传统商店内容
- `DOMAIN-SUFFIX,githubassets.com,PROXY`
  - 匹配白名单：`githubassets.com`
  - 用途：GitHub 静态资源（CSS、JS、头像等）
- `DOMAIN,matsuridayo.github.io,PROXY`
  - 匹配白名单：`github.io`
  - 用途：GitHub Pages 站点
- `DOMAIN,metacubex.github.io,PROXY`
  - 匹配白名单：`github.io`
  - 用途：GitHub Pages 站点
- `DOMAIN,bybit-exchange.github.io,PROXY`
  - 匹配白名单：`github.io`
  - 用途：GitHub Pages 站点
- `DOMAIN,nix-community.github.io,PROXY`
  - 匹配白名单：`github.io`
  - 用途：GitHub Pages 站点
- `DOMAIN,play-edge.itunes.apple.com,PROXY`
  - 匹配白名单：`itunes.apple.com`
  - 用途：iTunes/App Store 传统商店内容
- `DOMAIN-SUFFIX,mzstatic.com,PROXY`
  - 匹配白名单：`mzstatic.com`
  - 用途：苹果商店静态资源 CDN（截图、图标等）
- `DOMAIN,copilot-proxy.githubusercontent.com,PROXY`
  - 匹配白名单：`githubusercontent.com`
  - 用途：GitHub 用户内容（raw 文件、图片、附件等）
- `DOMAIN-SUFFIX,github.com,PROXY`
  - 匹配白名单：`github.com`
  - 用途：GitHub 主站
- `DOMAIN,trojan-gfw.github.io,PROXY`
  - 匹配白名单：`github.io`
  - 用途：GitHub Pages 站点
- `DOMAIN-SUFFIX,bytegecko.com,PROXY`
  - 匹配白名单：`bytegecko.com`
  - 用途：字节跳动 CDN（网页资源）
- `DOMAIN,throneproj.github.io,PROXY`
  - 匹配白名单：`github.io`
  - 用途：GitHub Pages 站点
- `DOMAIN-SUFFIX,github.io,PROXY`
  - 匹配白名单：`github.io`
  - 用途：GitHub Pages 站点
- `DOMAIN-SUFFIX,snssdk.com,PROXY`
  - 匹配白名单：`snssdk.com`
  - 用途：字节跳动基础域名（短视频、直播等）
- `DOMAIN-SUFFIX,ru.ccb.com,PROXY`
  - 匹配白名单：`ccb.com`
  - 用途：中国建设银行
- `DOMAIN,hls-amt.itunes.apple.com,PROXY`
  - 匹配白名单：`itunes.apple.com`
  - 用途：iTunes/App Store 传统商店内容
- `DOMAIN,hls.itunes.apple.com,PROXY`
  - 匹配白名单：`itunes.apple.com`
  - 用途：iTunes/App Store 传统商店内容
- `DOMAIN-SUFFIX,play.itunes.apple.com,PROXY`
  - 匹配白名单：`itunes.apple.com`
  - 用途：iTunes/App Store 传统商店内容
- `DOMAIN-SUFFIX,bag.itunes.apple.com,PROXY`
  - 匹配白名单：`itunes.apple.com`
  - 用途：iTunes/App Store 传统商店内容
- `DOMAIN-SUFFIX,raw.githubusercontent.com,PROXY`
  - 匹配白名单：`githubusercontent.com`
  - 用途：GitHub 用户内容（raw 文件、图片、附件等）
- `DOMAIN-SUFFIX,www.douyin.com,PROXY`
  - 匹配白名单：`douyin.com`
  - 用途：抖音主站
- `DOMAIN-SUFFIX,media.githubusercontent.com,PROXY`
  - 匹配白名单：`githubusercontent.com`
  - 用途：GitHub 用户内容（raw 文件、图片、附件等）
- `DOMAIN-SUFFIX,gist.github.com,PROXY`
  - 匹配白名单：`github.com`
  - 用途：GitHub 主站
- `DOMAIN-SUFFIX,avatars2.githubusercontent.com,PROXY`
  - 匹配白名单：`githubusercontent.com`
  - 用途：GitHub 用户内容（raw 文件、图片、附件等）

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
- `DOMAIN-SUFFIX,dm.pstatp.com,REJECT`
  - 匹配白名单：`pstatp.com`
  - 用途：字节跳动基础域名（推荐、API 等）
- `DOMAIN-SUFFIX,devgottia.github.io,REJECT`
  - 匹配白名单：`github.io`
  - 用途：GitHub Pages 站点
- `DOMAIN-SUFFIX,log0-misc-hl.amemv.com,REJECT`
  - 匹配白名单：`amemv.com`
  - 用途：字节跳动短视频（抖音、火山等）
- `DOMAIN-SUFFIX,collector-cdn.github.com,REJECT`
  - 匹配白名单：`github.com`
  - 用途：GitHub 主站
- `DOMAIN-SUFFIX,log.snssdk.com,REJECT`
  - 匹配白名单：`snssdk.com`
  - 用途：字节跳动基础域名（短视频、直播等）
- `DOMAIN-SUFFIX,collector.github.com,REJECT`
  - 匹配白名单：`github.com`
  - 用途：GitHub 主站
- `DOMAIN-SUFFIX,xlog.snssdk.com,REJECT`
  - 匹配白名单：`snssdk.com`
  - 用途：字节跳动基础域名（短视频、直播等）
- `DOMAIN-SUFFIX,mcs.snssdk.com,REJECT`
  - 匹配白名单：`snssdk.com`
  - 用途：字节跳动基础域名（短视频、直播等）
- `DOMAIN-SUFFIX,p3-ad-sign.byteimg.com,REJECT`
  - 匹配白名单：`byteimg.com`
  - 用途：字节跳动图片 CDN
- `DOMAIN-SUFFIX,mon.snssdk.com,REJECT`
  - 匹配白名单：`snssdk.com`
  - 用途：字节跳动基础域名（短视频、直播等）
- `DOMAIN-SUFFIX,analytics.githubassets.com,REJECT`
  - 匹配白名单：`githubassets.com`
  - 用途：GitHub 静态资源（CSS、JS、头像等）
- `DOMAIN-SUFFIX,copilot-telemetry.githubusercontent.com,REJECT`
  - 匹配白名单：`githubusercontent.com`
  - 用途：GitHub 用户内容（raw 文件、图片、附件等）
- `DOMAIN-SUFFIX,log-hl.snssdk.com,REJECT`
  - 匹配白名单：`snssdk.com`
  - 用途：字节跳动基础域名（短视频、直播等）
- `DOMAIN-SUFFIX,ib.snssdk.com,REJECT`
  - 匹配白名单：`snssdk.com`
  - 用途：字节跳动基础域名（短视频、直播等）
- `DOMAIN-SUFFIX,metrics.mzstatic.com,REJECT`
  - 匹配白名单：`mzstatic.com`
  - 用途：苹果商店静态资源 CDN（截图、图标等）
- `DOMAIN-SUFFIX,mihoutao1868.github.io,REJECT`
  - 匹配白名单：`github.io`
  - 用途：GitHub Pages 站点
- `DOMAIN-SUFFIX,googleads.github.io,REJECT`
  - 匹配白名单：`github.io`
  - 用途：GitHub Pages 站点
- `DOMAIN-SUFFIX,log.cmbchina.com,REJECT`
  - 匹配白名单：`cmbchina.com`
  - 用途：招商银行

</details>

### ❌ 代理规则质量检查异常（共 6 条）

**处理动作**：异常规则已从最终模块中移除。

<details>
<summary>展开查看异常规则及原因</summary>

```
- DOMAIN-SUFFIX,IP-CIDR,24.199.123.28/32,no-resolve,PROXY  (原因: 策略 '24.199.123.28/32' 不合法)
- DOMAIN-SUFFIX,IP-CIDR,143.198.200.27/32,no-resolve,PROXY  (原因: 策略 '143.198.200.27/32' 不合法)
- DOMAIN-SUFFIX,IP-CIDR,45.76.214.191/32,no-resolve,PROXY  (原因: 策略 '45.76.214.191/32' 不合法)
- DOMAIN-SUFFIX,IP-CIDR,159.89.204.203/32,no-resolve,PROXY  (原因: 策略 '159.89.204.203/32' 不合法)
- DOMAIN-SUFFIX,OMAIN-SUFFIX,BING.NET,PROXY  (原因: 策略 'BING.NET' 不合法)
- DOMAIN-SUFFIX,IP-CIDR,64.23.132.171/32,no-resolve,PROXY  (原因: 策略 '64.23.132.171/32' 不合法)
```
</details>

### 🧹 代理规则去重删除（共 3077 条）

**处理动作**：同一域名、同一策略的重复规则已删除，只保留一条；跨策略的不删。

<details>
<summary>展开查看去重样例（前 20 条）</summary>

```
- DOMAIN-SUFFIX,gsp-ssl.ls.apple.com,PROXY  （被同策略父级 DOMAIN-SUFFIX,ls.apple.com 覆盖）
- DOMAIN,lm.licenses.adobe.com,PROXY  （被同策略父级 DOMAIN-SUFFIX,adobe.com 覆盖）
- DOMAIN,asahishimbun.sc.omtrdc.net,PROXY  （被同策略父级 DOMAIN-SUFFIX,omtrdc.net 覆盖）
- DOMAIN,d29vzk4ow07wi7.cloudfront.net,PROXY  （被同策略父级 DOMAIN-SUFFIX,cloudfront.net 覆盖）
- DOMAIN,wwis-dubc1-vip124.adobe.com,PROXY  （被同策略父级 DOMAIN-SUFFIX,adobe.com 覆盖）
- DOMAIN,images-eu.ssl-images-amazon.com,PROXY  （被同策略父级 DOMAIN-SUFFIX,ssl-images-amazon.com 覆盖）
- DOMAIN,cloudsync-prod.s3.amazonaws.com,PROXY  （被同策略父级 DOMAIN-SUFFIX,amazonaws.com 覆盖）
- DOMAIN,wwis-dubc1-vip56.adobe.com,PROXY  （被同策略父级 DOMAIN-SUFFIX,adobe.com 覆盖）
- DOMAIN,wwis-dubc1-vip32.adobe.com,PROXY  （被同策略父级 DOMAIN-SUFFIX,adobe.com 覆盖）
- DOMAIN,d2v9yioq9zuuq2.cloudfront.net,PROXY  （被同策略父级 DOMAIN-SUFFIX,cloudfront.net 覆盖）
- DOMAIN,ubistatic23-a.akamaihd.net,PROXY  （被同策略父级 DOMAIN-SUFFIX,akamaihd.net 覆盖）
- DOMAIN,scholar.google.gr,PROXY  （被同策略父级 DOMAIN-SUFFIX,google.gr 覆盖）
- DOMAIN,wwis-dubc1-vip67.adobe.com,PROXY  （被同策略父级 DOMAIN-SUFFIX,adobe.com 覆盖）
- DOMAIN,github-production-repository-image-32fea6.s3.amazonaws.com,PROXY  （被同策略父级 DOMAIN-SUFFIX,amazonaws.com 覆盖）
- DOMAIN,pplx-res.cloudinary.com,PROXY  （被同策略父级 DOMAIN-SUFFIX,cloudinary.com 覆盖）
- DOMAIN,d2nvs31859zcd8.cloudfront.net,PROXY  （被同策略父级 DOMAIN-SUFFIX,cloudfront.net 覆盖）
- DOMAIN,wwis-dubc1-vip47.adobe.com,PROXY  （被同策略父级 DOMAIN-SUFFIX,adobe.com 覆盖）
- DOMAIN,wwis-dubc1-vip68.adobe.com,PROXY  （被同策略父级 DOMAIN-SUFFIX,adobe.com 覆盖）
- DOMAIN,openaicom-api-bdcpf8c6d2e9atf6.z01.azurefd.net,PROXY  （被同策略父级 DOMAIN-SUFFIX,azurefd.net 覆盖）
- DOMAIN,scholar.google.com.gt,PROXY  （被同策略父级 DOMAIN-SUFFIX,google.com.gt 覆盖）
... 另有 3057 条未列出
```
</details>

### 🧹 去广告规则去重删除（共 841 条）

**处理动作**：同一域名、同一策略的重复规则已删除，只保留一条；跨策略的不删。

<details>
<summary>展开查看去重样例（前 20 条）</summary>

```
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
- DOMAIN,adclick.g.doubleclick.net,REJECT  （被同策略父级 DOMAIN-SUFFIX,doubleclick.net 覆盖）
- DOMAIN,adcolony.com,REJECT  （被同策略 DOMAIN-SUFFIX,adcolony.com 覆盖）
- DOMAIN,adeng.hpplay.cn,REJECT  （被同策略 DOMAIN-SUFFIX,adeng.hpplay.cn 覆盖）
- DOMAIN,adexp.liftoff.io,REJECT  （被同策略父级 DOMAIN-SUFFIX,liftoff.io 覆盖）
... 另有 821 条未列出
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

**原有代理规则数**: 48767
**新增代理规则数**: 13
**更新后代理规则总数**: 48779

#### 新增代理规则明细

<details>
<summary>展开查看新增代理规则（共 13 条）</summary>

```
DOMAIN,api-siri-prod.apple.com,PROXY
DOMAIN-SUFFIX,ls.apple.com,PROXY
DOMAIN-SUFFIX,mask-h2.icloud.com,PROXY
DOMAIN-SUFFIX,mask.icloud.com,PROXY
DOMAIN-SUFFIX,gateway.icloud.com,PROXY
DOMAIN-SUFFIX,elevenlabsusercontent.com,PROXY
DOMAIN-SUFFIX,apple-cloudcompute.com,PROXY
DOMAIN-SUFFIX,apple-ai.com,PROXY
DOMAIN-SUFFIX,mask-api.icloud.com,PROXY
DOMAIN-SUFFIX,smoot.apple.com,PROXY
DOMAIN-SUFFIX,apple-relay.apple.com,PROXY
DOMAIN-KEYWORD,siri,PROXY
DOMAIN,swallow.apple.com,PROXY
```
</details>

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

**原有去广告规则数**: 235090
**新增去广告规则数**: 374
**更新后去广告规则总数**: 235464

#### 新增去广告规则明细

<details>
<summary>展开查看新增去广告规则（共 374 条）</summary>

```
DOMAIN-SUFFIX,ad.syncad.kr,REJECT
DOMAIN-SUFFIX,handierslacksstria.cfd,REJECT
DOMAIN-SUFFIX,qnagjjdsrhdsz.online,REJECT
DOMAIN-SUFFIX,hdgzmborowqng.online,REJECT
DOMAIN-SUFFIX,liniyanowhat.cyou,REJECT
DOMAIN-SUFFIX,vbyalehwxsppw.space,REJECT
DOMAIN-SUFFIX,xr6urwu85226qn4623ru.cfd,REJECT
DOMAIN-SUFFIX,72q1jyn2gxr7248xkwmti.rest,REJECT
DOMAIN-SUFFIX,avatarindolyl.click,REJECT
DOMAIN-SUFFIX,pnxotngpentgt.site,REJECT
DOMAIN-SUFFIX,ompfctkaynndf.website,REJECT
DOMAIN-SUFFIX,geloxptsfekia.website,REJECT
DOMAIN-SUFFIX,grunthpuzzles.com,REJECT
DOMAIN-SUFFIX,yo5t2u94obx933cxbt39rhec46.rest,REJECT
DOMAIN-SUFFIX,bxeddekzfmimn.space,REJECT
DOMAIN-SUFFIX,illupisuld.cfd,REJECT
DOMAIN-SUFFIX,opctikzijfib.in,REJECT
DOMAIN-SUFFIX,xyvoegypltdos.website,REJECT
DOMAIN-SUFFIX,cphajtqwblaje.online,REJECT
DOMAIN-SUFFIX,m4pw95xrbltl8ckg93l6qw.rest,REJECT
DOMAIN-SUFFIX,xgdxxxysjqpsim.com,REJECT
DOMAIN-SUFFIX,choyaannulsvibex.cyou,REJECT
DOMAIN-SUFFIX,tepbsdqyuoqzn.website,REJECT
DOMAIN-SUFFIX,jnswzmqfvzmfib.com,REJECT
DOMAIN-SUFFIX,vejovisspikerolpae.cyou,REJECT
DOMAIN-SUFFIX,germima.click,REJECT
DOMAIN-SUFFIX,athbagyidpvog.site,REJECT
DOMAIN-SUFFIX,ii4mju7bta.com,REJECT
DOMAIN-SUFFIX,1uei2j0mz0.com,REJECT
DOMAIN-SUFFIX,gioycisuthxxe.space,REJECT
DOMAIN-SUFFIX,sirwiubfbpqbt.online,REJECT
DOMAIN-SUFFIX,jufbglqdpbidb.space,REJECT
DOMAIN-SUFFIX,qwpgaahuwo.com,REJECT
DOMAIN-SUFFIX,mardydemareewant.cyou,REJECT
DOMAIN-SUFFIX,jswgcctolbobd.space,REJECT
DOMAIN-SUFFIX,event.prod.asgard.hullabalook.com,REJECT
DOMAIN-SUFFIX,fungiaobsign.cfd,REJECT
DOMAIN-SUFFIX,aquuxhozhgnnj.online,REJECT
DOMAIN-SUFFIX,dibres.xyz,REJECT
DOMAIN-SUFFIX,gheddaenzyms.com,REJECT
DOMAIN-SUFFIX,jyprvthqonbxi.online,REJECT
DOMAIN-SUFFIX,ixwpseujisuyx.website,REJECT
DOMAIN-SUFFIX,opybofbydoquo.site,REJECT
DOMAIN-SUFFIX,dpmnzkkkpgxzv.space,REJECT
DOMAIN-SUFFIX,efpzwwfgmblee.site,REJECT
DOMAIN-SUFFIX,versingpaintszingers.cfd,REJECT
DOMAIN-SUFFIX,exposalmund.cfd,REJECT
DOMAIN-SUFFIX,yadwfcwutipim.space,REJECT
DOMAIN-SUFFIX,uypaoyvudkbqm.online,REJECT
DOMAIN-SUFFIX,phaseflotter.cfd,REJECT
DOMAIN-SUFFIX,aedsnlyeqsenc.website,REJECT
DOMAIN-SUFFIX,atwzxdiiutcqw.space,REJECT
DOMAIN-SUFFIX,jxhaohxzsrvch.space,REJECT
DOMAIN-SUFFIX,hxdaevqueqpnv.site,REJECT
DOMAIN-SUFFIX,oncettagantsl.cyou,REJECT
DOMAIN-SUFFIX,paesgrdyrbqgp.website,REJECT
DOMAIN-SUFFIX,ramtaperla.com,REJECT
DOMAIN-SUFFIX,jtnjuzidtzzsb.website,REJECT
DOMAIN-SUFFIX,associesashoonconks.cyou,REJECT
DOMAIN-SUFFIX,ixfbdmdduqypv.online,REJECT
DOMAIN-SUFFIX,gguphuaatdwtd.online,REJECT
DOMAIN-SUFFIX,danaideuptower.cyou,REJECT
DOMAIN-SUFFIX,eygbgbthsrqfx.site,REJECT
DOMAIN-SUFFIX,gloriousberry.pro,REJECT
DOMAIN-SUFFIX,ohruawdrnwxuk.online,REJECT
DOMAIN-SUFFIX,acroamaconvoy.cfd,REJECT
DOMAIN-SUFFIX,zcnwrtkwtcf.com,REJECT
DOMAIN-SUFFIX,lakeacorn.mobi,REJECT
DOMAIN-SUFFIX,nngyltqynrjvd.space,REJECT
DOMAIN-SUFFIX,variance36.com,REJECT
DOMAIN-SUFFIX,daffodilfrost.mobi,REJECT
DOMAIN-SUFFIX,p2c8gbckn32qw5.cfd,REJECT
DOMAIN-SUFFIX,gatemenrheboks.cyou,REJECT
DOMAIN-SUFFIX,slybffrfdmhpw.site,REJECT
DOMAIN-SUFFIX,girbarosella.cfd,REJECT
DOMAIN-SUFFIX,yourownexpert.com,REJECT
DOMAIN-SUFFIX,yzeduowhwgufg.space,REJECT
DOMAIN-SUFFIX,flemertroys.click,REJECT
DOMAIN-SUFFIX,vhadaveqtqhqy.online,REJECT
DOMAIN-SUFFIX,xframbahdxnur.site,REJECT
DOMAIN-SUFFIX,arcticsdargue.rest,REJECT
DOMAIN-SUFFIX,hgloczbkkwyto.online,REJECT
DOMAIN-SUFFIX,knisshbszwxry.online,REJECT
DOMAIN-SUFFIX,guzbespot.com,REJECT
DOMAIN-SUFFIX,fidholjxlidfg.website,REJECT
DOMAIN-SUFFIX,gxfymazebhlln.site,REJECT
DOMAIN-SUFFIX,bbngdsqkbsnyv.website,REJECT
DOMAIN-SUFFIX,nngtoklcnfrix.space,REJECT
DOMAIN-SUFFIX,iqareoownsabn.site,REJECT
DOMAIN-SUFFIX,qfmvgndngiksk.online,REJECT
DOMAIN-SUFFIX,madeupproblem.com,REJECT
DOMAIN-SUFFIX,vuzfmaofzw.in,REJECT
DOMAIN-SUFFIX,ywquymtdswhxj.website,REJECT
DOMAIN-SUFFIX,dshjbu.com,REJECT
DOMAIN-SUFFIX,kyvnescqndohl.site,REJECT
DOMAIN-SUFFIX,croiseebrusque.cfd,REJECT
DOMAIN-SUFFIX,yjndyqxuzly.com,REJECT
DOMAIN-SUFFIX,laqkhkpvecsvh.website,REJECT
DOMAIN-SUFFIX,kutchyephede.com,REJECT
DOMAIN-SUFFIX,hkhrzdczjfmwx.website,REJECT
DOMAIN-SUFFIX,vnrmmyktredhl.space,REJECT
DOMAIN-SUFFIX,wruzanrip.in,REJECT
DOMAIN-SUFFIX,tunisiadoozies.click,REJECT
DOMAIN-SUFFIX,ymomwupyfgqhz.space,REJECT
DOMAIN-SUFFIX,gelatiaeupnoea.rest,REJECT
DOMAIN-SUFFIX,dswcce.com,REJECT
DOMAIN-SUFFIX,jdnkqfbrovcol.site,REJECT
DOMAIN-SUFFIX,dcujytxymslst.site,REJECT
DOMAIN-SUFFIX,cstqwzdchkjvn.site,REJECT
DOMAIN-SUFFIX,tasetodhjxdqj.online,REJECT
DOMAIN-SUFFIX,asqawnbcap.in,REJECT
DOMAIN-SUFFIX,deccaeycnc.com,REJECT
DOMAIN-SUFFIX,fexmjbiamfmkx.site,REJECT
DOMAIN-SUFFIX,lwvilvoaclifn.site,REJECT
DOMAIN-SUFFIX,sxbthsfkfzwko.online,REJECT
DOMAIN-SUFFIX,atifhylrgtiwx.online,REJECT
DOMAIN-SUFFIX,fqgogpouhtjlp.space,REJECT
DOMAIN-SUFFIX,utksgr.com,REJECT
DOMAIN-SUFFIX,vmtpubrmqsete.site,REJECT
DOMAIN-SUFFIX,repugnsfuttah.cyou,REJECT
DOMAIN-SUFFIX,gmngiieibpsqf.online,REJECT
DOMAIN-SUFFIX,toakdlgygrkdt.space,REJECT
DOMAIN-SUFFIX,hvotqprpfpabz.site,REJECT
DOMAIN-SUFFIX,kjiwhmprvqbzt.online,REJECT
DOMAIN-SUFFIX,zvexyioyzipry.website,REJECT
DOMAIN-SUFFIX,zeroizemoved.click,REJECT
DOMAIN-SUFFIX,sg-fp.apitd.net,REJECT
DOMAIN-SUFFIX,rinuorwuoyoqg.space,REJECT
DOMAIN-SUFFIX,wzzsehjozo.com,REJECT
DOMAIN-SUFFIX,daxnqytedjvry.website,REJECT
DOMAIN-SUFFIX,commswap.com,REJECT
DOMAIN-SUFFIX,ikjpqfqy33p2zzgw2zz1htw8r77k.rest,REJECT
DOMAIN-SUFFIX,unsuitmeatily.click,REJECT
DOMAIN-SUFFIX,biztowsgairwa.space,REJECT
DOMAIN-SUFFIX,vtktaxymfzkvt.space,REJECT
DOMAIN-SUFFIX,brusuresororal.rest,REJECT
DOMAIN-SUFFIX,cfoxeeannedjv.website,REJECT
DOMAIN-SUFFIX,kgzkzzvnalepm.space,REJECT
DOMAIN-SUFFIX,fzadhejdrwtic.online,REJECT
DOMAIN-SUFFIX,flrhfzdwwiran.online,REJECT
DOMAIN-SUFFIX,prawnspieltragia.cfd,REJECT
DOMAIN-SUFFIX,krroqqqgdpqlp.site,REJECT
DOMAIN-SUFFIX,nytwwclx2zrq7y83jcn95.cfd,REJECT
DOMAIN-SUFFIX,fuffitjeanniebotches.cfd,REJECT
DOMAIN-SUFFIX,cwmpqjhxixfxc.website,REJECT
DOMAIN-SUFFIX,highlowcamisia.cfd,REJECT
DOMAIN-SUFFIX,qjzrfhuri.com,REJECT
DOMAIN-SUFFIX,puruhawilrone.com,REJECT
DOMAIN-SUFFIX,crusdezalgozq.space,REJECT
DOMAIN-SUFFIX,gratefulmeadow.info,REJECT
DOMAIN-SUFFIX,ifaalumqmiiqb.site,REJECT
DOMAIN-SUFFIX,coomydroil.com,REJECT
DOMAIN-SUFFIX,guesicvkdrolu.site,REJECT
DOMAIN-SUFFIX,platearangale.rest,REJECT
DOMAIN-SUFFIX,hhkdchsioeizp.online,REJECT
DOMAIN-SUFFIX,fsblrfvaooojp.online,REJECT
DOMAIN-SUFFIX,hhdeqkgwmnndd.website,REJECT
DOMAIN-SUFFIX,bxhmqeiyqicht.online,REJECT
DOMAIN-SUFFIX,zybwdihuzdgwd.site,REJECT
DOMAIN-SUFFIX,wiredcarts.com,REJECT
DOMAIN-SUFFIX,dslvnp.com,REJECT
DOMAIN-SUFFIX,sowishcabaho.click,REJECT
DOMAIN-SUFFIX,euploidpalayanailuro.cfd,REJECT
DOMAIN-SUFFIX,fwgoogxackrqd.online,REJECT
DOMAIN-SUFFIX,hy851xvexj.com,REJECT
DOMAIN-SUFFIX,azyjrqcjgumwk.space,REJECT
DOMAIN-SUFFIX,ofdigrnikzqvp.space,REJECT
DOMAIN-SUFFIX,ehjfywvuslmpe.site,REJECT
DOMAIN-SUFFIX,nu5jqpfxg4q6lg.cfd,REJECT
DOMAIN-SUFFIX,agaritagabling.com,REJECT
DOMAIN-SUFFIX,couponraghusweeten.cyou,REJECT
DOMAIN-SUFFIX,ifqieoxkkghff.space,REJECT
DOMAIN-SUFFIX,gwbaxdwwmlmzm.site,REJECT
DOMAIN-SUFFIX,peccavikino.rest,REJECT
DOMAIN-SUFFIX,snvbmwrqewuko.site,REJECT
DOMAIN-SUFFIX,nabbrinescretin.cyou,REJECT
DOMAIN-SUFFIX,pv-track.venatus.com,REJECT
DOMAIN-SUFFIX,hwrvfohqyxdnur.com,REJECT
DOMAIN-SUFFIX,laveersbumfchasers.cyou,REJECT
DOMAIN-SUFFIX,wucukyxnsybyv.space,REJECT
DOMAIN-SUFFIX,nkglxtahsprjj.website,REJECT
DOMAIN-SUFFIX,lkuawjxzqywzl.space,REJECT
DOMAIN-SUFFIX,hbvrrsvvkhxrh.online,REJECT
DOMAIN-SUFFIX,lmajjygd.com,REJECT
DOMAIN-SUFFIX,sfqxepbilnadn.space,REJECT
DOMAIN-SUFFIX,ked61ojxow.com,REJECT
DOMAIN-SUFFIX,gqcyumr.com,REJECT
DOMAIN-SUFFIX,37dfc5e536.com,REJECT
DOMAIN-SUFFIX,cvepwpgfbnicq.site,REJECT
DOMAIN-SUFFIX,cuprumbenet.com,REJECT
DOMAIN-SUFFIX,abampuniateducky.cfd,REJECT
DOMAIN-SUFFIX,tantonykobu.cfd,REJECT
DOMAIN-SUFFIX,zplbvwptmabab.space,REJECT
DOMAIN-SUFFIX,hbewas.com,REJECT
DOMAIN-SUFFIX,kernelstubulet.click,REJECT
DOMAIN-SUFFIX,ibttkneskpejk.space,REJECT
DOMAIN-SUFFIX,profuse-wind.pro,REJECT
DOMAIN-SUFFIX,retypedwormilsumbrose.cfd,REJECT
DOMAIN-SUFFIX,crzzbyrea5.com,REJECT
DOMAIN-SUFFIX,jbitlealofwcv.website,REJECT
DOMAIN-SUFFIX,ev62ycku2feh6kfevvv.rest,REJECT
DOMAIN-SUFFIX,krqoupgigtqch.website,REJECT
DOMAIN-SUFFIX,suljrkzq.com,REJECT
DOMAIN-SUFFIX,gpzhmclomgogo.website,REJECT
DOMAIN-SUFFIX,messetcanopicclavial.cyou,REJECT
DOMAIN-SUFFIX,pulasjourneychebecs.cfd,REJECT
DOMAIN-SUFFIX,othoxnahsrf.in,REJECT
DOMAIN-SUFFIX,enar18ahs1.com,REJECT
DOMAIN-SUFFIX,eqohinzqkwiuh.website,REJECT
DOMAIN-SUFFIX,kiggypdjqlyut.site,REJECT
DOMAIN-SUFFIX,urploujzpctfi.online,REJECT
DOMAIN-SUFFIX,levinerkremsdybbuks.cyou,REJECT
DOMAIN-SUFFIX,dvhhudfpjdpbm.website,REJECT
DOMAIN-SUFFIX,zrmejhrldvsqr.online,REJECT
DOMAIN-SUFFIX,lakeacorn.pro,REJECT
DOMAIN-SUFFIX,kdzyieiqfynpx.space,REJECT
DOMAIN-SUFFIX,ncggqfjh.com,REJECT
DOMAIN-SUFFIX,ntmunhlaxbsrp.online,REJECT
DOMAIN-SUFFIX,eryngoslunches.com,REJECT
DOMAIN-SUFFIX,idetaarchgod.cyou,REJECT
DOMAIN-SUFFIX,gloriousberry.info,REJECT
DOMAIN-SUFFIX,warlowwrittenevang.cfd,REJECT
DOMAIN-SUFFIX,mlfzxpeyfebpw.space,REJECT
DOMAIN-SUFFIX,2ppz5u2mn57k2jc8.cfd,REJECT
DOMAIN-SUFFIX,titmenmachzor.com,REJECT
DOMAIN-SUFFIX,gfwgffdexugiv.space,REJECT
DOMAIN-SUFFIX,slimslohar.cfd,REJECT
DOMAIN-SUFFIX,0x2jt61f3l.com,REJECT
DOMAIN-SUFFIX,hjzfncxfojt.com,REJECT
DOMAIN-SUFFIX,rcftcrtutkqyk.website,REJECT
DOMAIN-SUFFIX,aqsoxbwa.in,REJECT
DOMAIN-SUFFIX,hanseazido.com,REJECT
DOMAIN-SUFFIX,fsfxzllaw.com,REJECT
DOMAIN-SUFFIX,inopwdjmiqqlv.website,REJECT
DOMAIN-SUFFIX,abkxkejotqfgu.site,REJECT
DOMAIN-SUFFIX,wzrqmimutdbfp.website,REJECT
DOMAIN-SUFFIX,argeersattical.click,REJECT
DOMAIN-SUFFIX,uconvjvfzlahy.space,REJECT
DOMAIN-SUFFIX,cdnmmhybpknfc.online,REJECT
DOMAIN-SUFFIX,lttevtdmhafol.website,REJECT
DOMAIN-SUFFIX,alenreysonglirine.cfd,REJECT
DOMAIN-SUFFIX,lqqjxcsqzozrq.online,REJECT
DOMAIN-SUFFIX,thyorctdsailep.com,REJECT
DOMAIN-SUFFIX,visibleeelshopearnful.cyou,REJECT
DOMAIN-SUFFIX,hsmcvmjrkxekd.website,REJECT
DOMAIN-SUFFIX,ibhmnhnbtdixx.website,REJECT
DOMAIN-SUFFIX,poemaround.cyou,REJECT
DOMAIN-SUFFIX,vbfwzrjbzn.com,REJECT
DOMAIN-SUFFIX,g9c4juir3jt8y8ho9r.rest,REJECT
DOMAIN-SUFFIX,hjbszlkwnobeg.site,REJECT
DOMAIN-SUFFIX,aspshalers.com,REJECT
DOMAIN-SUFFIX,wuvvpfgbqlfxy.site,REJECT
DOMAIN-SUFFIX,igbvimoabemop.website,REJECT
DOMAIN-SUFFIX,frzclvrvehksl.space,REJECT
DOMAIN-SUFFIX,atazirarock.com,REJECT
DOMAIN-SUFFIX,vanesfounte.click,REJECT
DOMAIN-SUFFIX,kcsyawoxclttg.space,REJECT
DOMAIN-SUFFIX,reindeermaple.biz,REJECT
DOMAIN-SUFFIX,uojybigasgycc.site,REJECT
DOMAIN-SUFFIX,gdbzsrfzfryvj.space,REJECT
DOMAIN-SUFFIX,mnylquykeysgb.website,REJECT
DOMAIN-SUFFIX,kettfvvxvdjci.site,REJECT
DOMAIN-SUFFIX,ebqdvizwnogbp.site,REJECT
DOMAIN-SUFFIX,dolesskin.click,REJECT
DOMAIN-SUFFIX,gtegruazcrfpo.online,REJECT
DOMAIN-SUFFIX,endhcxqryggam.online,REJECT
DOMAIN-SUFFIX,fzdxxgixeymfx.website,REJECT
DOMAIN-SUFFIX,iqlytcmnfnkag.site,REJECT
DOMAIN-SUFFIX,mtrdqxymqsloq.space,REJECT
DOMAIN-SUFFIX,fermeryinarkrecooks.cfd,REJECT
DOMAIN-SUFFIX,zccwvoexupzwa.site,REJECT
DOMAIN-SUFFIX,holsteracool.com,REJECT
DOMAIN-SUFFIX,98m6lo9wovj2km.cfd,REJECT
DOMAIN-SUFFIX,othhxcgwdtpl.com,REJECT
DOMAIN-SUFFIX,grandbook.pro,REJECT
DOMAIN-SUFFIX,kvemorapiraig.site,REJECT
DOMAIN-SUFFIX,softaseelier.cfd,REJECT
DOMAIN-SUFFIX,dkzqeqvdfdqyj.com,REJECT
DOMAIN-SUFFIX,specifykomarch.rest,REJECT
DOMAIN-SUFFIX,xqyudvcuxqgfz.website,REJECT
DOMAIN-SUFFIX,apnoeicporella.cyou,REJECT
DOMAIN-SUFFIX,rrhcocgfiommn.website,REJECT
DOMAIN-SUFFIX,jsdikro5nj.com,REJECT
DOMAIN-SUFFIX,elydkznpltm.com,REJECT
DOMAIN-SUFFIX,kyijgnsgbdrgo.website,REJECT
DOMAIN-SUFFIX,extroverted-election.com,REJECT
DOMAIN-SUFFIX,agmffsouzfdzs.space,REJECT
DOMAIN-SUFFIX,wqecuoywtysai.online,REJECT
DOMAIN-SUFFIX,jbwj6158e9rbk2cru.cfd,REJECT
DOMAIN-SUFFIX,handsabdal.com,REJECT
DOMAIN-SUFFIX,kraolkazv.in,REJECT
DOMAIN-SUFFIX,vjsjalvojohlc.space,REJECT
DOMAIN-SUFFIX,jfwyibhc.com,REJECT
DOMAIN-SUFFIX,nvbjxiupil.com,REJECT
DOMAIN-SUFFIX,mzdgwgeisucxy.site,REJECT
DOMAIN-SUFFIX,sblitlemryhbv.site,REJECT
DOMAIN-SUFFIX,centrefdop.com,REJECT
DOMAIN-SUFFIX,mbpfacwfxnahh.site,REJECT
DOMAIN-SUFFIX,seskutp.com,REJECT
DOMAIN-SUFFIX,wiuoafupzxewv.space,REJECT
DOMAIN-SUFFIX,qcinj6zhut5j93fzztmo275hgj37rg19gxvrw.cfd,REJECT
DOMAIN-SUFFIX,ukgfsqh.com,REJECT
DOMAIN-SUFFIX,wfsxxuptbajkg.space,REJECT
DOMAIN-SUFFIX,eosaedvbjx.com,REJECT
DOMAIN-SUFFIX,woodishrhaphes.click,REJECT
DOMAIN-SUFFIX,rusffkoxwqqfr.online,REJECT
DOMAIN-SUFFIX,axcii.com,REJECT
DOMAIN-SUFFIX,dlvkjmaibuade.online,REJECT
DOMAIN-SUFFIX,nitentmousing.cfd,REJECT
DOMAIN-SUFFIX,mtenzafvslu.com,REJECT
DOMAIN-SUFFIX,drzwloikkfnty.site,REJECT
DOMAIN-SUFFIX,hsgeqpkmyjhek.website,REJECT
DOMAIN-SUFFIX,iguanidcoy.com,REJECT
DOMAIN-SUFFIX,ypqnkscnkdcnq.online,REJECT
DOMAIN-SUFFIX,ocrruiyzxicvz.website,REJECT
DOMAIN-SUFFIX,mbrigtiyslekh.space,REJECT
DOMAIN-SUFFIX,jbfdwgpcsvebs.website,REJECT
DOMAIN-SUFFIX,eu4as22g0c.com,REJECT
DOMAIN-SUFFIX,spyholeengines.rest,REJECT
DOMAIN-SUFFIX,borneopoutier.rest,REJECT
DOMAIN-SUFFIX,itfubkgusqrez.website,REJECT
DOMAIN-SUFFIX,riotousglaked.click,REJECT
DOMAIN-SUFFIX,mgqzqmwxgqqml.online,REJECT
DOMAIN-SUFFIX,allezmahalla.click,REJECT
DOMAIN-SUFFIX,yxkckeaeq.com,REJECT
DOMAIN-SUFFIX,iwsbffmhqkmki.website,REJECT
DOMAIN-SUFFIX,gefdnapkoycth.online,REJECT
DOMAIN-SUFFIX,dmtxcjmbjdtio.space,REJECT
DOMAIN-SUFFIX,axlkzqidmiuzx.website,REJECT
DOMAIN-SUFFIX,gumvnjvakljpy.online,REJECT
DOMAIN-SUFFIX,secourscutch.com,REJECT
DOMAIN-SUFFIX,peakquartz.com,REJECT
DOMAIN-SUFFIX,sipsmaggle.cyou,REJECT
DOMAIN-SUFFIX,qxgfqfdbsdbsw.site,REJECT
DOMAIN-SUFFIX,xmaseseveners.click,REJECT
DOMAIN-SUFFIX,iotptwwkspcvy.space,REJECT
DOMAIN-SUFFIX,fbqehotinnkwq.space,REJECT
DOMAIN-SUFFIX,mundifycormoidarrope.cyou,REJECT
DOMAIN-SUFFIX,lgpngvkjl.com,REJECT
DOMAIN-SUFFIX,heaversteelscarved.cyou,REJECT
DOMAIN-SUFFIX,urzcdepq.com,REJECT
DOMAIN-SUFFIX,5htvm2buhe37pn.rest,REJECT
DOMAIN-SUFFIX,zivtmzjnjcilx.space,REJECT
DOMAIN-SUFFIX,nysflneusinnh.space,REJECT
DOMAIN-SUFFIX,lepxtxsbucqzl.space,REJECT
DOMAIN-SUFFIX,enwctarabilef.online,REJECT
DOMAIN-SUFFIX,ywnptndtofrvi.website,REJECT
DOMAIN-SUFFIX,phmsyticbimcr.site,REJECT
DOMAIN-SUFFIX,xezuzkxp.com,REJECT
DOMAIN-SUFFIX,bghivvoygrywm.site,REJECT
DOMAIN-SUFFIX,chaletsheens.com,REJECT
DOMAIN-SUFFIX,dyrjbabposnvu.website,REJECT
DOMAIN-SUFFIX,bvxwlvzmmgnsb.space,REJECT
DOMAIN-SUFFIX,mashlamchyack.click,REJECT
DOMAIN-SUFFIX,wfjt4eq57eflcmwb5p6xbvjcxx.rest,REJECT
DOMAIN-SUFFIX,willcollect.com,REJECT
DOMAIN-SUFFIX,xswayxfyi.com,REJECT
DOMAIN-SUFFIX,oticlemures.cyou,REJECT
DOMAIN-SUFFIX,lakzzeog.in,REJECT
DOMAIN-SUFFIX,wkohojldytcsj.site,REJECT
DOMAIN-SUFFIX,qloddgoeaqgre.space,REJECT
DOMAIN-SUFFIX,amazingaster.com,REJECT
DOMAIN-SUFFIX,chattigreeks.click,REJECT
DOMAIN-SUFFIX,cxmqsrqinbtnx.website,REJECT
DOMAIN-SUFFIX,gjbxjnbufkibp.website,REJECT
DOMAIN-SUFFIX,hhqiglbfabbdf.space,REJECT
DOMAIN-SUFFIX,hwkftvcicrgwe.website,REJECT
DOMAIN-SUFFIX,matirmg.com,REJECT
DOMAIN-SUFFIX,noisyorals.cfd,REJECT
DOMAIN-SUFFIX,reawaitinsoleapodan.cyou,REJECT
DOMAIN-SUFFIX,sslyqxezmsehc.website,REJECT
DOMAIN-SUFFIX,vxhhxwmomvaot.website,REJECT
DOMAIN-SUFFIX,yhaknyoqjenbl.website,REJECT
DOMAIN-SUFFIX,zhtgzsvpdhhge.website,REJECT
```
</details>

## ⚠️ 敏感域名已自动过滤（银行/支付）

**原因**：域名包含银行/支付关键词，为防止隐私泄露，不加入解密列表。

<details>
<summary>展开查看被过滤的敏感域名（共 7 个）</summary>

```
mpos-pic.helipay.com
creditcardapp.bankcomm.com
yunbusiness.ccb.com
lban.spdb.com.cn
webappcfg.paas.cmbchina.com
m.creditcard.ecitic.com
creditcardapp.bankcomm.cn
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

🩺 Shield模块: 健康检查通过（284243 条规则，12.8 MB）

✅ Shield 模块已写入，代理 48779 条，去广告 235464 条

## 🩺 规则源健康状态

<details>
<summary>展开查看各上游源健康状态（共 13 个源）</summary>

- ✅ https://raw.githubusercontent.com/GMOogway/shadowrocket-rules/master/sr_direct_list.module
  - 成功 172 次，失败 0 次，连续失败 0 次
  - 最近成功: 2026-11-19 20:28:07
  - 最近失败: 无 

- ✅ https://raw.githubusercontent.com/GMOogway/shadowrocket-rules/master/sr_proxy_list.module
  - 成功 172 次，失败 0 次，连续失败 0 次
  - 最近成功: 2026-11-19 20:28:14
  - 最近失败: 无 

- ✅ https://raw.githubusercontent.com/LOWERTOP/Shadowrocket-First/main/Talkatone.sgmodule
  - 成功 172 次，失败 0 次，连续失败 0 次
  - 最近成功: 2026-11-19 20:28:14
  - 最近失败: 无 

- ✅ https://raw.githubusercontent.com/huijingfei/Shadowrocket-Rules/refs/heads/main/sr_app_ad.module
  - 成功 172 次，失败 0 次，连续失败 0 次
  - 最近成功: 2026-11-19 20:28:15
  - 最近失败: 无 

- ✅ https://raw.githubusercontent.com/deezertidal/shadowrocket-rules/refs/heads/main/modules/startingad.module
  - 成功 172 次，失败 0 次，连续失败 0 次
  - 最近成功: 2026-11-19 20:28:15
  - 最近失败: 无 

- ✅ https://raw.githubusercontent.com/GMOogway/shadowrocket-rules/master/sr_reject_list.module
  - 成功 172 次，失败 0 次，连续失败 0 次
  - 最近成功: 2026-11-19 20:28:16
  - 最近失败: 无 

- ✅ https://raw.githubusercontent.com/Unwhimsical/NetPilot/refs/heads/main/modules/%E6%B5%8B%E8%AF%95.module
  - 成功 172 次，失败 0 次，连续失败 0 次
  - 最近成功: 2026-11-19 20:28:16
  - 最近失败: 无 

- ✅ https://raw.githubusercontent.com/LOWERTOP/Shadowrocket-First/main/TalkatoneAntiAds.list
  - 成功 172 次，失败 0 次，连续失败 0 次
  - 最近成功: 2026-11-19 20:28:16
  - 最近失败: 无 

- ✅ https://johnshall.github.io/Shadowrocket-ADBlock-Rules-Forever/sr_top500_banlist_ad.conf
  - 成功 11 次，失败 0 次，连续失败 0 次
  - 最近成功: 2026-11-19 20:28:14
  - 最近失败: 无 

- ✅ https://johnshall.github.io/Shadowrocket-ADBlock-Rules-Forever/sr_cnip_ad.conf
  - 成功 11 次，失败 0 次，连续失败 0 次
  - 最近成功: 2026-11-19 20:28:14
  - 最近失败: 无 

- ✅ https://johnshall.github.io/Shadowrocket-ADBlock-Rules-Forever/sr_ad_only.conf
  - 成功 11 次，失败 0 次，连续失败 0 次
  - 最近成功: 2026-11-19 20:28:16
  - 最近失败: 无 

- ✅ https://yfamilys.com/module/AdBlock.module
  - 成功 11 次，失败 0 次，连续失败 0 次
  - 最近成功: 2026-11-19 20:28:17
  - 最近失败: 无 

- ✅ https://yfamilys.com/module/adultraplus.module
  - 成功 11 次，失败 0 次，连续失败 0 次
  - 最近成功: 2026-11-19 20:28:17
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
