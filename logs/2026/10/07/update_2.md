# 更新日志 2026-10-07

**运行时间**: 2026-10-07 18:50:01 北京时间

---

## 直连模块

### 🔍 过滤海外/强制代理直连规则（共 935 条）

**原因**：规则域名匹配海外黑名单关键词，或属于强制代理域名（如定位模块）。

<details>
<summary>展开查看被过滤规则及命中关键词</summary>

```
- DOMAIN-SUFFIX,vz.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,facri.com,DIRECT  (命中: acr)
- DOMAIN-SUFFIX,whichmba.net,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,awsdns-cn-38.net,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,flyertea.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,awsonamazon.com,DIRECT  (命中: amazon)
- DOMAIN-SUFFIX,awsdns-cn-20.biz,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,mcohmygod.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,hifly.tv,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,chmti.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,shms-expo.com,DIRECT  (命中: hm)
- DOMAIN,oemsocuat.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- URL-REGEX,"^https?:\/\/r+[0-9]+(---|\.)sn-(2x3|ni5|j5o)\w{5}\.googlevideo\.com.*$",DIRECT  (命中: google)
- DOMAIN-SUFFIX,glhmmr.com,DIRECT  (命中: hm)
- DOMAIN,rsm.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,awsdns-cn-17.net,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,digcredit.com,DIRECT  (命中: gcr)
- DOMAIN-SUFFIX,ylxhmy.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,inflyway.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,02hm.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,dcg.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,hmadgz.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,flyfunny.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,awsdns-cn-11.biz,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,lzghmy.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,awsdns-cn-15.net,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,msdn.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN,c.android.clients.google.com,DIRECT  (命中: google)
- DOMAIN-SUFFIX,hmrsrc.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,azurestackhub.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,iflyrec.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,awsdns-cn-00.com,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,unpmcc.com,DIRECT  (命中: npm)
- DOMAIN-SUFFIX,hmltec.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,ayhmjy.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,megahugo.net,DIRECT  (命中: mega)
- DOMAIN-SUFFIX,ugdocker.link,DIRECT  (命中: docker)
- DOMAIN-SUFFIX,gxhmdjt.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,myvs.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,ovhlb.com,DIRECT  (命中: ovh)
- DOMAIN-SUFFIX,awsdns-cn-52.biz,DIRECT  (命中: aws)
- DOMAIN,gs-loc.apple.com,DIRECT  (命中: 强制代理域名)
- DOMAIN-SUFFIX,awsdns-cn-07.com,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,azuremigratetest.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,likeaboat2023.com,DIRECT  (命中: ikea)
- DOMAIN-SUFFIX,awsdns-cn-16.net,DIRECT  (命中: aws)
- DOMAIN,oemsoc.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,googlenav.com,DIRECT  (命中: google)
- DOMAIN-SUFFIX,htyhm.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,flyingeffect.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,haitianpm.com,DIRECT  (命中: npm)
- DOMAIN,googleadservices-cn.com,DIRECT  (命中: google)
- DOMAIN-SUFFIX,acrossmetals.com,DIRECT  (命中: acr)
- DOMAIN-SUFFIX,macrounion.com,DIRECT  (命中: acr)
- DOMAIN-SUFFIX,cloudflareanycast.net,DIRECT  (命中: cloudflare)
- DOMAIN-SUFFIX,airtofly.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,51render.com,DIRECT  (命中: render)
- DOMAIN-SUFFIX,awsdns-cn-55.com,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,cloudflarecn.net,DIRECT  (命中: cloudflare)
- DOMAIN-SUFFIX,glflyy.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,awsdns-cn-41.com,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,akamai.com,DIRECT  (命中: akamai)
- DOMAIN-SUFFIX,chinacraa.org,DIRECT  (命中: acr)
- DOMAIN-SUFFIX,chinacrops.org,DIRECT  (命中: acr)
- DOMAIN-SUFFIX,awsdns-cn-54.net,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,eflybird.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,googlevoice.org,DIRECT  (命中: google)
- DOMAIN-SUFFIX,flymeyun.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,dockerone.com,DIRECT  (命中: docker)
- DOMAIN-SUFFIX,fly63.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,abcdocker.com,DIRECT  (命中: docker)
- DOMAIN,download.mlcc.google.com,DIRECT  (命中: google)
- DOMAIN,googletraveladservices-cn.com,DIRECT  (命中: google)
- DOMAIN-SUFFIX,ztrhmall.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,jinshmgw.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,thwgetsy.com,DIRECT  (命中: etsy)
- DOMAIN,googletagmanager-cn.com,DIRECT  (命中: google)
- DOMAIN-SUFFIX,secrss.com,DIRECT  (命中: ecr)
- DOMAIN-SUFFIX,hyahm.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,shmengyang.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,awsdns-cn-51.biz,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,azureflying.com,DIRECT  (命中: azure)
- DOMAIN-SUFFIX,iflysec.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,syfly007.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,xn--nmqp78hmufjwu.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,ntrailway.com,DIRECT  (命中: railway)
- DOMAIN,pagead-googlehosted.l.google.com,DIRECT  (命中: google)
- DOMAIN-SUFFIX,hmeili.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,fly139.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,whmlcy.net,DIRECT  (命中: hm)
- DOMAIN,lexuat.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,awsdns-cn-58.com,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,wish-hightech.com,DIRECT  (命中: wish)
- DOMAIN-SUFFIX,hmsemi.com,DIRECT  (命中: hm)
- URL-REGEX,"^https?:\/\/.+\.awsdns-cn-[0-9][0-9]\.(biz|com|net|top).*$",DIRECT  (命中: aws)
- DOMAIN-SUFFIX,flymeauto.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,thmall.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,1fly.fun,DIRECT  (命中: fly)
- DOMAIN,firebase-settings.crashlytics.com,DIRECT  (命中: firebase)
- DOMAIN-SUFFIX,facebookol.com,DIRECT  (命中: facebook)
- DOMAIN-SUFFIX,szpowerfly.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,bshmzx.com,DIRECT  (命中: hm)
- DOMAIN,cache.pack.google.com,DIRECT  (命中: google)
- DOMAIN-SUFFIX,hmnst.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,fly-exp.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,withmedia.net,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,awsdns-cn-02.net,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,secretgardenresorts.com,DIRECT  (命中: ecr)
- DOMAIN-SUFFIX,smogflycloud.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,macrr.com,DIRECT  (命中: acr)
- DOMAIN-SUFFIX,fhmv.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,flytcloud.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,volic.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,ceolaws.net,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,moonfly.net,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,awsdns-cn-62.biz,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,ncjrailway.com,DIRECT  (命中: railway)
- DOMAIN-SUFFIX,wecrm.net,DIRECT  (命中: ecr)
- DOMAIN-SUFFIX,awsdns-cn-19.biz,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,vultrcn.com,DIRECT  (命中: vultr)
- DOMAIN,storeedge.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,awsdns-cn-39.com,DIRECT  (命中: aws)
- DOMAIN,vz.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,sdhmkj.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,hm120.com,DIRECT  (命中: hm)
- DOMAIN,redirector.c.play.google.com,DIRECT  (命中: google)
- DOMAIN-SUFFIX,osrelease.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,azuretouch.net,DIRECT  (命中: azure)
- DOMAIN-SUFFIX,yingyecraft.com,DIRECT  (命中: ecr)
- DOMAIN-SUFFIX,awsdns-cn-28.net,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,awsdns-cn-48.net,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,whmeigao.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,zhmf.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,awsdns-cn-63.biz,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,officecdn.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,awsdns-cn-36.net,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,sunnyfly.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,azureflame.cloud,DIRECT  (命中: azure)
- DOMAIN-SUFFIX,tshmkj.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,awsdns-cn-42.com,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,mbs.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,xrender.com,DIRECT  (命中: render)
- DOMAIN-SUFFIX,hmx-led.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,whmzkf.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,thmzedu.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,flyai.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,wishtec.com,DIRECT  (命中: wish)
- DOMAIN-SUFFIX,openailab.com,DIRECT  (命中: openai)
- DOMAIN-SUFFIX,zhmzqi.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,iva-schmetz.com,DIRECT  (命中: hm)
- DOMAIN,download.tensorflow.google.com,DIRECT  (命中: google)
- DOMAIN,dg-meta.video.google.com,DIRECT  (命中: google)
- DOMAIN-SUFFIX,googlebbs.net,DIRECT  (命中: google)
- DOMAIN,crashlyticsreports-pa.googleapis.com,DIRECT  (命中: google)
- DOMAIN-SUFFIX,smogflycloud.net,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,2google.com,DIRECT  (命中: google)
- DOMAIN-SUFFIX,eflycloud.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,hmwdj.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,officemktuat.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,haofly.net,DIRECT  (命中: fly)
- DOMAIN,cache-management-prod.google.com,DIRECT  (命中: google)
- DOMAIN-SUFFIX,qhm123.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,awsdns-cn-40.com,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,whmvc.net,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,macroprocess.com,DIRECT  (命中: acr)
- DOMAIN-SUFFIX,shmengzhong.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,ggshmy.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,youtube-dubbing.com,DIRECT  (命中: youtube)
- DOMAIN-SUFFIX,qdhmsoft.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,bfhmj.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,cdnchatgpt.com,DIRECT  (命中: chatgpt)
- DOMAIN-SUFFIX,npmtrend.com,DIRECT  (命中: npm)
- DOMAIN-SUFFIX,megasig.com,DIRECT  (命中: mega)
- DOMAIN-SUFFIX,shmet.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,iwishwed.com,DIRECT  (命中: wish)
- DOMAIN-SUFFIX,codeflying.net,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,flysheeep.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,ahmky.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,hnpm.cc,DIRECT  (命中: npm)
- DOMAIN-SUFFIX,macrosan.com,DIRECT  (命中: acr)
- DOMAIN,windbg.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,applysquare.net,DIRECT  (命中: square)
- DOMAIN-SUFFIX,24hmb.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,iflyresearch.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,itgemini.net,DIRECT  (命中: gemini)
- DOMAIN-SUFFIX,hmqjsb.com,DIRECT  (命中: hm)
- DOMAIN,redirector.c.youtubeeducation.com,DIRECT  (命中: youtube)
- DOMAIN-SUFFIX,hmz8.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,beijing-hmo.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,flysand.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,awsdns-cn-46.net,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,mikecrm.com,DIRECT  (命中: ecr)
- URL-REGEX,"^https?:\/\/.+-mihayo\.akamaized\.net.*$",DIRECT  (命中: akamai)
- DOMAIN-SUFFIX,secretmine.net,DIRECT  (命中: ecr)
- DOMAIN-SUFFIX,awsdns-cn-46.com,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,e-flyinc.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,dragonfly.fun,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,fishflying.net,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,hmgreat.com,DIRECT  (命中: hm)
- DOMAIN,gstaticadssl.l.google.com,DIRECT  (命中: google)
- DOMAIN-SUFFIX,tecreal.com,DIRECT  (命中: ecr)
- DOMAIN-SUFFIX,cloudflare-cn.com,DIRECT  (命中: cloudflare)
- DOMAIN-SUFFIX,whmf8.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,sxhm.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,dmhmusic.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,machenike.com,DIRECT  (命中: nike)
- DOMAIN,vscode.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,flyenglish.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,szhmkeji.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,yz-proton.com,DIRECT  (命中: proton)
- DOMAIN-SUFFIX,googleppy.com,DIRECT  (命中: google)
- DOMAIN-SUFFIX,githubim.com,DIRECT  (命中: github)
- DOMAIN-SUFFIX,hfhm.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,vscode.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,tinsecret.com,DIRECT  (命中: ecr)
- DOMAIN-SUFFIX,awsdns-cn-06.com,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,hm588.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,flyadx.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,applysquare.com,DIRECT  (命中: square)
- DOMAIN-SUFFIX,whmnls.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,openai.wf,DIRECT  (命中: openai)
- DOMAIN-SUFFIX,hmrczp.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,chinacrankshaft.com,DIRECT  (命中: acr)
- DOMAIN-SUFFIX,cnpmjs.org,DIRECT  (命中: npm)
- DOMAIN-SUFFIX,drugoogle.com,DIRECT  (命中: google)
- DOMAIN-SUFFIX,awsdns-cn-39.biz,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,awsdns-cn-55.biz,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,awsdns-cn-45.net,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,rohm-chip.com,DIRECT  (命中: hm)
- DOMAIN,googlesyndication-cn.com,DIRECT  (命中: google)
- DOMAIN-SUFFIX,ghmba.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,awsdns-cn-39.net,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,chinacreator.com,DIRECT  (命中: acr)
- DOMAIN-SUFFIX,awsdns-cn-51.com,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,awsdns-cn-09.net,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,fishmobi.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,qmacro.com,DIRECT  (命中: acr)
- DOMAIN-SUFFIX,hmtnew.com,DIRECT  (命中: hm)
- DOMAIN,fontfiles.googleapis.com,DIRECT  (命中: google)
- DOMAIN-SUFFIX,zhmodaoli.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,sdhmdp.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,hmarathon.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,msdprod-ad.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,wishisp.com,DIRECT  (命中: wish)
- DOMAIN-SUFFIX,awsdns-cn-44.biz,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,lenovo.com.cdn.cloudflare.net,DIRECT  (命中: cloudflare)
- DOMAIN-SUFFIX,daiwofly.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,awsdns-cn-18.biz,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,awsdns-cn-09.biz,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,pihmh.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,awsdns-cn-42.biz,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,collaborateppe.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,ctrender.com,DIRECT  (命中: render)
- DOMAIN,volic.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,macrowing.com,DIRECT  (命中: acr)
- DOMAIN-SUFFIX,vdfly.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,shmog.org,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,awsdns-cn-35.net,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,storeedge.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,awsdns-cn-03.biz,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,91hmi.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,lawsdata.com,DIRECT  (命中: aws)
- DOMAIN,itacademy.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,bixuecrm.com,DIRECT  (命中: ecr)
- DOMAIN-SUFFIX,yzhmyy.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,hmzs.net,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,shmusicschool.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,awsdns-cn-14.com,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,gyhm.cc,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,iflyread.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,happypingpang.com,DIRECT  (命中: pypi)
- DOMAIN-SUFFIX,kphm88.com,DIRECT  (命中: hm)
- DOMAIN,tac.googleapis.com,DIRECT  (命中: google)
- DOMAIN-SUFFIX,hyundai-hmtc.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,iflyiot.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,flytexpress.com,DIRECT  (命中: fly)
- DOMAIN,osrelease.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,3zhm.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,jiansujihm.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,shmaas.net,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,whmc2005.com,DIRECT  (命中: hm)
- DOMAIN,lex.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,njnaws.com,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,zchmbx.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,jhm2012.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,gxhhmed.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,aftersale-amazon.com,DIRECT  (命中: amazon)
- DOMAIN-SUFFIX,grender.com,DIRECT  (命中: render)
- DOMAIN-SUFFIX,msproduct.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,gamegamept.com,DIRECT  (命中: mega)
- DOMAIN-SUFFIX,smogfly.net,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,awsdns-cn-14.biz,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,hbhm.net,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,bghmj.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,edgeone-browser-rendering.com,DIRECT  (命中: render)
- DOMAIN-SUFFIX,bjhmyq.com,DIRECT  (命中: hm)
- DOMAIN,azurestackhubuat.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,wodecrowd.com,DIRECT  (命中: ecr)
- DOMAIN-SUFFIX,awsdns-cn-07.biz,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,awsdns-cn-60.biz,DIRECT  (命中: aws)
- DOMAIN,vlportal.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,iflydatahub.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,hnsyhm.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,chinaflashmarket.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,esdhm.net,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,welchmat.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,azureyun.com,DIRECT  (命中: azure)
- DOMAIN-SUFFIX,shmylike.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,aliexpress-media.com,DIRECT  (命中: aliexpress)
- DOMAIN-SUFFIX,hmtgo.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,jyhmz.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,whmnrc.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,lhmp.cc,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,testshm.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,hmyzs.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,zgxhm.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,megajoy.com,DIRECT  (命中: mega)
- DOMAIN-SUFFIX,nike666.com,DIRECT  (命中: nike)
- DOMAIN-SUFFIX,awsdns-cn-60.net,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,shmzgroup.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,iflying.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,vecrp.com,DIRECT  (命中: ecr)
- DOMAIN-SUFFIX,awsdns-cn-56.biz,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,acrel-microgrid.com,DIRECT  (命中: acr)
- DOMAIN,dl.l.google.com,DIRECT  (命中: google)
- DOMAIN,surface.downloads.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,awsdns-cn-37.com,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,yytiflytek.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,whmoocs.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,xhmedia.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,seersecret.com,DIRECT  (命中: ecr)
- DOMAIN,cbdstest.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN,msproduct.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,dreamsparkuat.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,chmgames.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,flyme.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,fulinpm.com,DIRECT  (命中: npm)
- DOMAIN-SUFFIX,bjhmcm.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,googleplus.party,DIRECT  (命中: google)
- DOMAIN,storecorefulfillment.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,awsdns-cn-40.net,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,whmxrj.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,smogfly.cloud,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,hmchina.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,xn--vhq4ut2dsxd5xqnicjxxo55a756aovhik0aunm.com,DIRECT  (命中: ovh)
- DOMAIN,mpnbenefitsrtl.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,zzfly.net,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,squarecn.com,DIRECT  (命中: square)
- DOMAIN-SUFFIX,simplecreator.net,DIRECT  (命中: ecr)
- DOMAIN-SUFFIX,hmszkj.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,whmj.org,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,algorithmart.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,openai-hub.com,DIRECT  (命中: openai)
- DOMAIN-SUFFIX,officemkt.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,fireflyacg.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,sdx.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,megawords.cc,DIRECT  (命中: mega)
- DOMAIN-SUFFIX,chmc.cc,DIRECT  (命中: hm)
- DOMAIN,gs-loc-cn.apple.com,DIRECT  (命中: 强制代理域名)
- DOMAIN-SUFFIX,awsdns-cn-07.net,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,iflytoy.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,xawscu.com,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,hwrecruit.com,DIRECT  (命中: ecr)
- DOMAIN-SUFFIX,awspony.com,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,feidacrusher.com,DIRECT  (命中: acr)
- DOMAIN-SUFFIX,lzarays.com,DIRECT  (命中: zara)
- DOMAIN-SUFFIX,awsdns-cn-44.com,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,aliexpress.us,DIRECT  (命中: aliexpress)
- DOMAIN-SUFFIX,ideacreated.com,DIRECT  (命中: acr)
- DOMAIN-SUFFIX,flygo.net,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,oecr.com,DIRECT  (命中: ecr)
- DOMAIN-SUFFIX,dl.delivery.mp.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,edrawsoft.com,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,awsdns-cn-55.net,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,qjhm.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,hm152n.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,acrel-znyf.com,DIRECT  (命中: acr)
- DOMAIN,mpnbenefits.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN,safebrowsing-cache.google.com,DIRECT  (命中: google)
- DOMAIN-SUFFIX,hmxx.net,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,awsdns-cn-04.net,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,cofly.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,awsdns-cn-21.biz,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,mikeauth.com,DIRECT  (命中: ikea)
- DOMAIN-SUFFIX,nike.host,DIRECT  (命中: nike)
- DOMAIN-SUFFIX,awsdns-cn-40.biz,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,awsdns-cn-17.com,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,cbdstest.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,hbhml.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,awsdns-cn-37.net,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,edgeone-browser-rendering-dev.com,DIRECT  (命中: render)
- DOMAIN-SUFFIX,zhmu.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,elitecrm.com,DIRECT  (命中: ecr)
- DOMAIN-SUFFIX,awstar.net,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,cproton.com,DIRECT  (命中: proton)
- DOMAIN-SUFFIX,sphmc.org,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,iflyaiedu.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,download.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,hmfxw.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,windbg.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,sectigochina.com.cdn.cloudflare.net,DIRECT  (命中: cloudflare)
- DOMAIN-SUFFIX,awsdns-cn-22.com,DIRECT  (命中: aws)
- DOMAIN,azuremigrate.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,cacre.org,DIRECT  (命中: acr)
- DOMAIN-SUFFIX,flycua.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,awsdns-cn-46.biz,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,hlnpm.com,DIRECT  (命中: npm)
- DOMAIN-SUFFIX,wishcad.com,DIRECT  (命中: wish)
- DOMAIN-SUFFIX,surface.downloads.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,flyco.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,arefly.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,vultrvps.com,DIRECT  (命中: vultr)
- DOMAIN-SUFFIX,awsdns-cn-28.biz,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,yunqifly.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,minecraftxz.com,DIRECT  (命中: ecr)
- DOMAIN-SUFFIX,awsdns-cn-49.biz,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,awsdns-cn-35.biz,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,volcecr.com,DIRECT  (命中: ecr)
- DOMAIN-SUFFIX,xn--vhqqbz2p62hm92e04p.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,ghmcchina.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,fawsoft.com,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,lexuat.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,chmia.org,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,tb-whatsapp.com,DIRECT  (命中: whatsapp)
- DOMAIN,qpx.googleflights.net,DIRECT  (命中: google)
- DOMAIN-SUFFIX,gdlinefly.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,awsdns-cn-33.biz,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,awsdns-cn-41.net,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,surface-microsoftstore.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,i-firefly.com,DIRECT  (命中: fly)
- URL-REGEX,"^https?:\/\/.+\.awsdns-cn-[0-9][a-e0-9]\.cn.*$",DIRECT  (命中: aws)
- DOMAIN-SUFFIX,bulbsquare.com,DIRECT  (命中: square)
- DOMAIN-SUFFIX,awsdns-cn-25.com,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,hhmage.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,lnwish.com,DIRECT  (命中: wish)
- DOMAIN-SUFFIX,seaflysoft.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,3hmedicalgroup.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,rcolab.com,DIRECT  (命中: colab)
- DOMAIN,officecdn.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,zhmold.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,weflywifi.com,DIRECT  (命中: fly)
- DOMAIN,google-analytics-cn.com,DIRECT  (命中: google)
- DOMAIN,update.googleapis.com,DIRECT  (命中: google)
- DOMAIN-SUFFIX,macrozheng.com,DIRECT  (命中: acr)
- DOMAIN-SUFFIX,gx-hm.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,awsdns-cn-50.biz,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,fly1999.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,sqshmzx.net,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,qhmsg.com,DIRECT  (命中: hm)
- DOMAIN,download.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,secretflow.com,DIRECT  (命中: ecr)
- DOMAIN-SUFFIX,acrel-eem.com,DIRECT  (命中: acr)
- DOMAIN-SUFFIX,dreamspark.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,hearfly.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,t-firefly.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,awsdns-cn-25.net,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,shmockup.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,ttfly.com,DIRECT  (命中: fly)
- DOMAIN,officemktuat.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,targetportion.com,DIRECT  (命中: target)
- DOMAIN-SUFFIX,hmzixin.com,DIRECT  (命中: hm)
- DOMAIN,azurestackhub.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,azurestackhubuat.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,awsdns-cn-45.biz,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,flypy.cc,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,cloudflare.fun,DIRECT  (命中: cloudflare)
- DOMAIN-SUFFIX,awsdns-cn-17.biz,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,t-npm.com,DIRECT  (命中: npm)
- DOMAIN-SUFFIX,secrui.com,DIRECT  (命中: ecr)
- DOMAIN-SUFFIX,gxhmba.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,hmj666.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,qzynhhmm.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,awsdns-cn-52.net,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,czxthmls.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,cthhmu.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,aliexpress.ru,DIRECT  (命中: aliexpress)
- DOMAIN-SUFFIX,awsdns-cn-54.biz,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,hmkp.org,DIRECT  (命中: hm)
- DOMAIN,googleflights-cn.net,DIRECT  (命中: google)
- DOMAIN-SUFFIX,cloudflarestaging.com,DIRECT  (命中: cloudflare)
- DOMAIN-SUFFIX,hhmajiang.com,DIRECT  (命中: hm)
- DOMAIN,ssl-google-analytics.l.google.com,DIRECT  (命中: google)
- DOMAIN-SUFFIX,ecr-global.com,DIRECT  (命中: ecr)
- DOMAIN-SUFFIX,flyneutron.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,szhmjp.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,qflyinc.com,DIRECT  (命中: fly)
- DOMAIN,collaborateppe.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,mpnbenefits.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,orasos.com,DIRECT  (命中: asos)
- DOMAIN-SUFFIX,neihanfly.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,shmusic.org,DIRECT  (命中: hm)
- DOMAIN,googletagservices.com,DIRECT  (命中: google)
- DOMAIN-SUFFIX,hm-optics.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,shmaur.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,zgzhmz.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,flygon.net,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,fwfly.com,DIRECT  (命中: fly)
- DOMAIN,msdprod-ad.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,awsdns-cn-24.net,DIRECT  (命中: aws)
- DOMAIN,googletagservices-cn.com,DIRECT  (命中: google)
- DOMAIN-SUFFIX,whmnx.com,DIRECT  (命中: hm)
- DOMAIN,googleapis-cn.com,DIRECT  (命中: google)
- DOMAIN-SUFFIX,kindechem.com,DIRECT  (命中: kinde)
- DOMAIN,dreamsparkuat.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,square16.org,DIRECT  (命中: square)
- DOMAIN-SUFFIX,brighticecream.com,DIRECT  (命中: ecr)
- DOMAIN-SUFFIX,flylinking.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,sheinet.com,DIRECT  (命中: shein)
- DOMAIN,developer.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,meiji-icecream.com,DIRECT  (命中: ecr)
- DOMAIN-SUFFIX,whhmmbl.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,oemsoc.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,appsflyer-cn.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,gzhm.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,imags-google.com,DIRECT  (命中: google)
- DOMAIN-SUFFIX,awsdns-cn-57.com,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,awsdns-cn-12.net,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,hellogitlab.com,DIRECT  (命中: gitlab)
- DOMAIN-SUFFIX,iflytek.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,fhmion.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,zhmxchina.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,vlportal.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,cloudflareprod.com,DIRECT  (命中: cloudflare)
- DOMAIN-SUFFIX,hkgcr.com,DIRECT  (命中: gcr)
- DOMAIN-SUFFIX,minecraftzw.com,DIRECT  (命中: ecr)
- DOMAIN-SUFFIX,awsdns-cn-24.com,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,ecrrc.com,DIRECT  (命中: ecr)
- DOMAIN-SUFFIX,collaborate.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,nnpml.com,DIRECT  (命中: npm)
- DOMAIN,googletagmanager.com,DIRECT  (命中: google)
- DOMAIN-SUFFIX,fly998.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,awsdns-cn-62.net,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,bebhmongb.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,mecru.com,DIRECT  (命中: ecr)
- DOMAIN-SUFFIX,whminwei.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,victoriassecretclearance.online,DIRECT  (命中: ecr)
- DOMAIN-SUFFIX,whmylike.cc,DIRECT  (命中: hm)
- DOMAIN,redirector.c.pack.google.com,DIRECT  (命中: google)
- DOMAIN-SUFFIX,awsdns-cn-21.net,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,hifly.mobi,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,hmxixie.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,iflytektstd.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,mysecrettop.com,DIRECT  (命中: ecr)
- DOMAIN-SUFFIX,megaemoji.com,DIRECT  (命中: mega)
- DOMAIN-SUFFIX,ifireflygame.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,thmins.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,jhmnew.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,khmhvlw.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,hmf-china.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,cdnhwcohm19.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,awsdns-cn-59.net,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,wbecrisfro.com,DIRECT  (命中: ecr)
- DOMAIN-SUFFIX,oneflys.com,DIRECT  (命中: fly)
- DOMAIN,sdx.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,awsdns-cn-24.biz,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,hmxw.com,DIRECT  (命中: hm)
- DOMAIN,dl.google.com,DIRECT  (命中: google)
- DOMAIN,www-googletagmanager.l.google.com,DIRECT  (命中: google)
- DOMAIN-SUFFIX,macrosilicon.com,DIRECT  (命中: acr)
- DOMAIN-SUFFIX,zchmh.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,renderbus.com,DIRECT  (命中: render)
- DOMAIN-SUFFIX,azure.cc,DIRECT  (命中: azure)
- DOMAIN,surface.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN,software.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,awsdns-cn-59.biz,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,protontechcn.com,DIRECT  (命中: proton)
- DOMAIN-SUFFIX,dhmsnyy.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,rainbutterfly.xyz,DIRECT  (命中: fly)
- DOMAIN,safebrowsing.googleapis.com,DIRECT  (命中: google)
- DOMAIN-SUFFIX,haiqianghm.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,md-hmjt.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,acloudrender.com,DIRECT  (命中: render)
- DOMAIN-SUFFIX,chinawssdxh.com,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,oacrm.com,DIRECT  (命中: acr)
- DOMAIN-SUFFIX,awsdns-cn-20.net,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,shtimessquare.com,DIRECT  (命中: square)
- DOMAIN-SUFFIX,awsdns-cn-44.net,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,itacademyuat.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,pmphmooc.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,hmqg.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,hm5988.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,myhm.org,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,aquayee.com,DIRECT  (命中: quay)
- DOMAIN-SUFFIX,iflynote.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,iflydocs.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,fingerflyapp.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,qixingcr.com,DIRECT  (命中: gcr)
- DOMAIN-SUFFIX,jxhmjx.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,originalkindergarten.com,DIRECT  (命中: kinde)
- DOMAIN-SUFFIX,flymobi.biz,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,shmhzp.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,acroview.com,DIRECT  (命中: acr)
- DOMAIN-SUFFIX,awsdns-cn-47.biz,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,yfldocker.com,DIRECT  (命中: docker)
- DOMAIN-SUFFIX,pkulaws.com,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,chinacrane.net,DIRECT  (命中: acr)
- DOMAIN-SUFFIX,shmljm.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,cloudfront-cn.net,DIRECT  (命中: cloudfront)
- DOMAIN-SUFFIX,awsdns-cn-52.com,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,cloudhvacr.com,DIRECT  (命中: acr)
- DOMAIN-SUFFIX,alltechmed.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,protong.com,DIRECT  (命中: proton)
- DOMAIN-SUFFIX,forcecreat.com,DIRECT  (命中: ecr)
- DOMAIN-SUFFIX,iflyadx.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,jxhmxxjs.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,chnrailway.com,DIRECT  (命中: railway)
- DOMAIN,performanceparameters.googleapis.com,DIRECT  (命中: google)
- DOMAIN-SUFFIX,asosoaiid.com,DIRECT  (命中: asos)
- DOMAIN-SUFFIX,xhmwxy.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,smogfly.club,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,3richman.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,hminvestment.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,hm025.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,citichmc.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,squarefong.com,DIRECT  (命中: square)
- DOMAIN-SUFFIX,hmlan.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,whoami.akamai.net,DIRECT  (命中: akamai)
- DOMAIN-SUFFIX,ahmif.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,awsdns-cn-23.com,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,yjdatasos.com,DIRECT  (命中: asos)
- DOMAIN-SUFFIX,techmiao.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,qihangcrrc.com,DIRECT  (命中: gcr)
- DOMAIN-SUFFIX,awsdns-cn-43.biz,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,awsdns-cn-01.biz,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,iflyhealth.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,hmmachine.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,flymopaper.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,awsdns-cn-62.com,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,shmedia.tech,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,awsdns-cn-29.biz,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,ihmch.com,DIRECT  (命中: hm)
- DOMAIN,googleadservices.com,DIRECT  (命中: google)
- DOMAIN-SUFFIX,awsdns-cn-01.net,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,fhmooc.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,awsdns-cn-05.net,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,bzmhm.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,iqhmh.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,chinaacryl.com,DIRECT  (命中: acr)
- DOMAIN-SUFFIX,cyhm.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,southmoney.com,DIRECT  (命中: hm)
- DOMAIN,googleoptimize-cn.com,DIRECT  (命中: google)
- DOMAIN-SUFFIX,cn-railway.net,DIRECT  (命中: railway)
- DOMAIN-SUFFIX,awsdns-cn-11.com,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,iflygse.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,gxlzhm.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,awsdns-cn-05.biz,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,sdhmjt.net,DIRECT  (命中: hm)
- DOMAIN,dreamspark.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN,mbs.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,mpnbenefitsrtluat.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,sfecr.com,DIRECT  (命中: ecr)
- DOMAIN-SUFFIX,bjhdhm.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,oemssl.cn.cdn.cloudflare.net,DIRECT  (命中: cloudflare)
- DOMAIN-SUFFIX,awsdns-cn-09.com,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,cloudflareip.com,DIRECT  (命中: cloudflare)
- DOMAIN-SUFFIX,znhhmedical.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,awsdns-cn-45.com,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,nnhmcj.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,qeoagphm.com,DIRECT  (命中: hm)
- DOMAIN,storeedgefd.dsx.mp.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,gshmhotels.com,DIRECT  (命中: hm)
- DOMAIN,adservice.google.com,DIRECT  (命中: google)
- DOMAIN-SUFFIX,telegramtoke.com,DIRECT  (命中: telegram)
- DOMAIN-SUFFIX,zxhmjj.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,yhmob.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,awsdns-cn-48.biz,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,awsdns-cn-16.biz,DIRECT  (命中: aws)
- DOMAIN,googlevads-cn.com,DIRECT  (命中: google)
- DOMAIN-SUFFIX,flyfishx.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,netsyq.com,DIRECT  (命中: etsy)
- DOMAIN-SUFFIX,englishmasterclub.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,megagamelog.com,DIRECT  (命中: mega)
- DOMAIN-SUFFIX,thmz.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,xhma.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,zjecredit.org,DIRECT  (命中: ecr)
- DOMAIN-SUFFIX,awsdns-cn-12.biz,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,gemini-galaxy.com,DIRECT  (命中: gemini)
- DOMAIN-SUFFIX,4hmodel.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,awsdns-vip.com,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,hlhmf.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,c-thme.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,njhmmr.com,DIRECT  (命中: hm)
- DOMAIN,www-google-analytics.l.google.com,DIRECT  (命中: google)
- DOMAIN,redirector.c.mail.google.com,DIRECT  (命中: google)
- DOMAIN-SUFFIX,jcodecraeer.com,DIRECT  (命中: ecr)
- DOMAIN-SUFFIX,xn--y8jhmm6gn.moe,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,renderincloud.com,DIRECT  (命中: render)
- DOMAIN-SUFFIX,ghsmpwalmart.com,DIRECT  (命中: walmart)
- DOMAIN-SUFFIX,xczhmzb.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,azuremigrate.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN,googleapps-cn.com,DIRECT  (命中: google)
- DOMAIN-SUFFIX,awsdns-cn-27.biz,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,weighment.com,DIRECT  (命中: hm)
- DOMAIN,redirector.c.chat.google.com,DIRECT  (命中: google)
- DOMAIN-SUFFIX,cqs-hm.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,cloudflareperf.com,DIRECT  (命中: cloudflare)
- DOMAIN,googleoptimize.com,DIRECT  (命中: google)
- DOMAIN-SUFFIX,hmting.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,chiconysquare.com,DIRECT  (命中: square)
- DOMAIN-SUFFIX,ahmwgroup.com,DIRECT  (命中: hm)
- DOMAIN,imasdk.googleapis.com,DIRECT  (命中: google)
- DOMAIN-SUFFIX,awsdns-cn-36.biz,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,cheetahmobile.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,hm163.net,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,wecrm.com,DIRECT  (命中: ecr)
- DOMAIN,images-cn-8.ssl-images-amazon.com,DIRECT  (命中: amazon)
- DOMAIN-SUFFIX,lhmj.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,whuznhmedj.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,hm16888.net,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,9125flying.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,hnlshm.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,hmzhtc.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,scratchmirror.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,flyingpigeon1936.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,hfly.net,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,awsdns-cn-34.com,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,chinamaven.com,DIRECT  (命中: maven)
- DOMAIN-SUFFIX,npmmirror.com,DIRECT  (命中: npm)
- DOMAIN-SUFFIX,awsdns-cn-31.net,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,lex.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,shmds.vip,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,whmdedu.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,download.visualstudio.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,flashmemoryworld.com,DIRECT  (命中: hm)
- DOMAIN,pki-goog.l.google.com,DIRECT  (命中: google)
- DOMAIN,collaborate.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,uuu.ovh,DIRECT  (命中: ovh)
- DOMAIN-SUFFIX,software.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN,myvs.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN,time.amazonaws.cn,DIRECT  (命中: amazon)
- DOMAIN-SUFFIX,awsdns-cn-34.net,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,awsdns-cn-47.com,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,armfly.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,cmacredit.org,DIRECT  (命中: acr)
- DOMAIN-SUFFIX,3hmlg.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,awsdns-cn-58.biz,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,chihm.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,imgs.ovh,DIRECT  (命中: ovh)
- DOMAIN-SUFFIX,ovhlb.net,DIRECT  (命中: ovh)
- DOMAIN-SUFFIX,jshmrcb.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,hmgj.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,shmtu.net,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,oktamall.com,DIRECT  (命中: okta)
- DOMAIN,mpnbenefitsrtluat.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,luxtarget.com,DIRECT  (命中: target)
- DOMAIN-SUFFIX,shmfmr.net,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,awsdns-cn-22.net,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,flymeos.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,whmama.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,hbysfhm.com,DIRECT  (命中: hm)
- DOMAIN,officemkt.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,fly3949.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,wishdown.com,DIRECT  (命中: wish)
- DOMAIN-SUFFIX,googley8rb.com,DIRECT  (命中: google)
- DOMAIN-SUFFIX,jhqshfly.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,ylhmgz.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,hmtrhf.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,hmlcar.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,zhmedcenter.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,hmus.net,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,zhmag.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,aflytec.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,hicnhm.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,724pridecryogenics.com,DIRECT  (命中: ecr)
- DOMAIN-SUFFIX,hmoe.link,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,tlhmhd.com,DIRECT  (命中: hm)
- DOMAIN,wear.googleapis.com,DIRECT  (命中: google)
- DOMAIN-SUFFIX,omegatravel.net,DIRECT  (命中: mega)
- DOMAIN-SUFFIX,awsdns-cn-63.com,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,chatgptboke.com,DIRECT  (命中: chatgpt)
- DOMAIN-SUFFIX,rsm.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,google-hub.com,DIRECT  (命中: google)
- DOMAIN-SUFFIX,shmhtv.com,DIRECT  (命中: hm)
- DOMAIN,googletraveladservices.com,DIRECT  (命中: google)
- DOMAIN-SUFFIX,hyundai-chhm.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,likeacg.com,DIRECT  (命中: ikea)
- DOMAIN-SUFFIX,awsdns-cn-63.net,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,dylyghm.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,hmgbtv.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,hmplay.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,dagongcredit.com,DIRECT  (命中: gcr)
- DOMAIN-SUFFIX,awsdns-cn-27.com,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,touchmark.art,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,microsoftuwp.com,DIRECT  (命中: microsoft)
- DOMAIN,google-analytics.com,DIRECT  (命中: google)
- DOMAIN-SUFFIX,chmod0777kk.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,awsdns-cn-60.com,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,storecorefulfillment.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,awsdns-cn-23.net,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,honchmedia.com,DIRECT  (命中: hm)
- DOMAIN,images-cn.ssl-images-amazon.com,DIRECT  (命中: amazon)
- DOMAIN-SUFFIX,railwaybill.com,DIRECT  (命中: railway)
- DOMAIN-SUFFIX,cqhma.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,lzhmmr.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,scratchmirror.net,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,flydigi.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,lzbhmy.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,magentochina.org,DIRECT  (命中: magento)
- DOMAIN-SUFFIX,cnflyinghorse.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,d5render.com,DIRECT  (命中: render)
- DOMAIN-SUFFIX,bwfhmall.com,DIRECT  (命中: hm)
- DOMAIN,itacademyuat.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,hmjc.org,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,chmecc.org,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,cloudflareglobal.net,DIRECT  (命中: cloudflare)
- DOMAIN-SUFFIX,bmp.ovh,DIRECT  (命中: ovh)
- DOMAIN-SUFFIX,dhmeri.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,hmwzjs.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,gemini530.net,DIRECT  (命中: gemini)
- DOMAIN-SUFFIX,shhmbio.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,awsdns-cn-33.net,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,chinaws.net,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,mysecretrainbow.com,DIRECT  (命中: ecr)
- DOMAIN-SUFFIX,awsdns-cn-00.net,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,awsdns-cn-36.com,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,qualcomm.cn.cdn.cloudflare.net,DIRECT  (命中: cloudflare)
- DOMAIN-SUFFIX,awsdns-cn-41.biz,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,googleyixia.com,DIRECT  (命中: google)
- DOMAIN-SUFFIX,yhchmo.com,DIRECT  (命中: hm)
- DOMAIN,msdn.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,chinacrt.com,DIRECT  (命中: acr)
- DOMAIN-SUFFIX,flyml.net,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,awsdns-cn-61.biz,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,ucfly.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,wish3d.com,DIRECT  (命中: wish)
- DOMAIN-SUFFIX,zjgcreative.com,DIRECT  (命中: gcr)
- DOMAIN-SUFFIX,flyme.net,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,jdhmediajd.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,shmama.net,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,awsamazonlab.com,DIRECT  (命中: amazon)
- DOMAIN-SUFFIX,shmbjy.org,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,awsdns-cn-02.biz,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,macrolake.com,DIRECT  (命中: acr)
- DOMAIN-SUFFIX,awsdns-cn-50.net,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,flyhand.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,cloudflareinsights-cn.com,DIRECT  (命中: cloudflare)
- DOMAIN-SUFFIX,yhm11.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,awsdns-cn-48.com,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,awsdns-cn-06.net,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,officebay.net,DIRECT  (命中: ebay)
- DOMAIN-SUFFIX,whhmgroup.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,mightsquare.com,DIRECT  (命中: square)
- DOMAIN-SUFFIX,gacrnd.com,DIRECT  (命中: acr)
- DOMAIN-SUFFIX,1818hm.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,awsdns-cn-26.com,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,mrwish.net,DIRECT  (命中: wish)
- DOMAIN-SUFFIX,hmly666.cc,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,fly160.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,sun-wish.com,DIRECT  (命中: wish)
- DOMAIN-SUFFIX,hbhmxx.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,toprender.com,DIRECT  (命中: render)
- DOMAIN-SUFFIX,awsdns-cn-56.net,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,hmzhtc.cc,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,asosde.com,DIRECT  (命中: asos)
- DOMAIN-SUFFIX,yindo-ohm.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,awsdns-cn-18.net,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,jinshasitemuseum.com,DIRECT  (命中: temu)
- DOMAIN-SUFFIX,machmall.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,fly84.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,awsdns-cn-58.net,DIRECT  (命中: aws)
- DOMAIN,clickserver.googleads.com,DIRECT  (命中: google)
- DOMAIN-SUFFIX,megarobo.com,DIRECT  (命中: mega)
- DOMAIN-SUFFIX,rushmail.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,shmetro.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,hm-3223.net,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,phmacn.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,gzrecruit.com,DIRECT  (命中: ecr)
- DOMAIN-SUFFIX,thmnet.com,DIRECT  (命中: hm)
- DOMAIN,azuremigratetest.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,chmed.net,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,awsdns-cn-19.net,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,google444.com,DIRECT  (命中: google)
- DOMAIN-SUFFIX,52kfly.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,itacademy.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,megagenchina.com,DIRECT  (命中: mega)
- DOMAIN,download.visualstudio.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,awsdns-cn-37.biz,DIRECT  (命中: aws)
- DOMAIN,tools.google.com,DIRECT  (命中: google)
- DOMAIN-SUFFIX,gdsunfly.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,thmovie.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,chinahvacr.com,DIRECT  (命中: acr)
- DOMAIN-SUFFIX,sharjahmadrasa.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,chinacrosspoint.com,DIRECT  (命中: acr)
- DOMAIN-SUFFIX,smogfly.com,DIRECT  (命中: fly)
- DOMAIN,avail.googleflights.net,DIRECT  (命中: google)
- DOMAIN-SUFFIX,itfly.net,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,nikefans.com,DIRECT  (命中: nike)
- DOMAIN,clientservices.googleapis.com,DIRECT  (命中: google)
- DOMAIN-SUFFIX,awsdns-cn-47.net,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,azure-wave.com,DIRECT  (命中: azure)
- DOMAIN-SUFFIX,shmarathon.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,hmedu.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,dockerinfo.net,DIRECT  (命中: docker)
- DOMAIN-SUFFIX,51google.com,DIRECT  (命中: google)
- DOMAIN-SUFFIX,hefeilaws.com,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,shmondial.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,shlawserve.com,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,bjwhmedia.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,shhmu.net,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,nhmuni.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,athmapp.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,lubanpm.com,DIRECT  (命中: npm)
- DOMAIN-SUFFIX,iflyink.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,cqrailway.com,DIRECT  (命中: railway)
- DOMAIN-SUFFIX,mpnbenefitsrtl.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,cloudflarestoragegw.com,DIRECT  (命中: cloudflare)
- DOMAIN,googleanalytics.com,DIRECT  (命中: google)
- DOMAIN-SUFFIX,hzhm888.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,xahmqy.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,ddwhm.com,DIRECT  (命中: hm)
- DOMAIN,googlesyndication.com,DIRECT  (命中: google)
- DOMAIN-SUFFIX,gdhmgc.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,hmbzfjt.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,oemsocuat.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,czhmjx.com,DIRECT  (命中: hm)
- DOMAIN,cdn.globalsigncdn.com.cdn.cloudflare.net,DIRECT  (命中: cloudflare)
- DOMAIN-SUFFIX,bjhmdkj.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,aliexpress.com,DIRECT  (命中: aliexpress)
- DOMAIN-SUFFIX,awsdns-cn-53.com,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,shmds.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,gogofly.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,elecrystal.com,DIRECT  (命中: ecr)
- DOMAIN-SUFFIX,awsdns-cn-20.com,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,zhinikefu.com,DIRECT  (命中: nike)
- DOMAIN-SUFFIX,hf-iflysse.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,ghmd448.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,facebooksx.com,DIRECT  (命中: facebook)
- DOMAIN-SUFFIX,surface.download.prss.microsoft.com,DIRECT  (命中: microsoft)
- DOMAIN-SUFFIX,zztfly.com,DIRECT  (命中: fly)
- DOMAIN-SUFFIX,awspaas.com,DIRECT  (命中: aws)
- DOMAIN-SUFFIX,githubshare.com,DIRECT  (命中: github)
- DOMAIN-SUFFIX,cuahmap.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,natywish.com,DIRECT  (命中: wish)
- DOMAIN-SUFFIX,techmoris.com,DIRECT  (命中: hm)
- DOMAIN-SUFFIX,awsdns-cn-10.com,DIRECT  (命中: aws)
```
</details>

### 上游源状态

- ✅ https://raw.githubusercontent.com/GMOogway/shadowrocket-rules/master/sr_direct_list.module

**原有规则数**: 110775
**新增规则数**: 0
**更新后总数**: 110775

🩺 直连模块: 健康检查通过（110775 条规则，3.6 MB）

✅ 直连模块已写入，共 110775 条规则

## 代理分流模块

### 🛡️ 白名单豁免（代理规则，共 15 条）

**原因**：这些域名在 `direct_whitelist.txt` 中，已从代理规则中移除，确保走直连。

<details>
<summary>展开查看被豁免的代理规则（15 条）</summary>


- `DOMAIN,metacubex.github.io,PROXY`
  - 匹配白名单：`github.io`
  - 用途：GitHub Pages 站点
- `DOMAIN,matsuridayo.github.io,PROXY`
  - 匹配白名单：`github.io`
  - 用途：GitHub Pages 站点
- `DOMAIN-SUFFIX,github.io,PROXY`
  - 匹配白名单：`github.io`
  - 用途：GitHub Pages 站点
- `DOMAIN,xtls.github.io,PROXY`
  - 匹配白名单：`github.io`
  - 用途：GitHub Pages 站点
- `DOMAIN-SUFFIX,github.com,PROXY`
  - 匹配白名单：`github.com`
  - 用途：GitHub 主站
- `DOMAIN-SUFFIX,bytegecko.com,PROXY`
  - 匹配白名单：`bytegecko.com`
  - 用途：字节跳动 CDN（网页资源）
- `DOMAIN,nix-community.github.io,PROXY`
  - 匹配白名单：`github.io`
  - 用途：GitHub Pages 站点
- `DOMAIN,throneproj.github.io,PROXY`
  - 匹配白名单：`github.io`
  - 用途：GitHub Pages 站点
- `DOMAIN-SUFFIX,githubusercontent.com,PROXY`
  - 匹配白名单：`githubusercontent.com`
  - 用途：GitHub 用户内容（raw 文件、图片、附件等）
- `DOMAIN,trojan-gfw.github.io,PROXY`
  - 匹配白名单：`github.io`
  - 用途：GitHub Pages 站点
- `DOMAIN,copilot-proxy.githubusercontent.com,PROXY`
  - 匹配白名单：`githubusercontent.com`
  - 用途：GitHub 用户内容（raw 文件、图片、附件等）
- `DOMAIN,bybit-exchange.github.io,PROXY`
  - 匹配白名单：`github.io`
  - 用途：GitHub Pages 站点
- `DOMAIN-SUFFIX,snssdk.com,PROXY`
  - 匹配白名单：`snssdk.com`
  - 用途：字节跳动基础域名（短视频、直播等）
- `DOMAIN-SUFFIX,ru.ccb.com,PROXY`
  - 匹配白名单：`ccb.com`
  - 用途：中国建设银行
- `DOMAIN-SUFFIX,githubassets.com,PROXY`
  - 匹配白名单：`githubassets.com`
  - 用途：GitHub 静态资源（CSS、JS、头像等）

</details>

### 🛡️ 白名单豁免（去广告规则，共 18 条）

**原因**：这些域名在 `direct_whitelist.txt` 中，已从去广告规则中移除，避免误拦截。

<details>
<summary>展开查看被豁免的去广告规则（18 条）</summary>


- `DOMAIN-SUFFIX,ads.cup.com.cn,REJECT`
  - 匹配白名单：`cup.com.cn`
  - 用途：银联
- `DOMAIN-SUFFIX,adv.ccb.com,REJECT`
  - 匹配白名单：`ccb.com`
  - 用途：中国建设银行
- `DOMAIN-SUFFIX,googleads.github.io,REJECT`
  - 匹配白名单：`github.io`
  - 用途：GitHub Pages 站点
- `DOMAIN-SUFFIX,dm.pstatp.com,REJECT`
  - 匹配白名单：`pstatp.com`
  - 用途：字节跳动基础域名（推荐、API 等）
- `DOMAIN-SUFFIX,copilot-telemetry.githubusercontent.com,REJECT`
  - 匹配白名单：`githubusercontent.com`
  - 用途：GitHub 用户内容（raw 文件、图片、附件等）
- `DOMAIN-SUFFIX,collector-cdn.github.com,REJECT`
  - 匹配白名单：`github.com`
  - 用途：GitHub 主站
- `DOMAIN-SUFFIX,collector.github.com,REJECT`
  - 匹配白名单：`github.com`
  - 用途：GitHub 主站
- `DOMAIN-SUFFIX,mihoutao1868.github.io,REJECT`
  - 匹配白名单：`github.io`
  - 用途：GitHub Pages 站点
- `DOMAIN-SUFFIX,log.snssdk.com,REJECT`
  - 匹配白名单：`snssdk.com`
  - 用途：字节跳动基础域名（短视频、直播等）
- `DOMAIN-SUFFIX,log-hl.snssdk.com,REJECT`
  - 匹配白名单：`snssdk.com`
  - 用途：字节跳动基础域名（短视频、直播等）
- `DOMAIN-SUFFIX,xlog.snssdk.com,REJECT`
  - 匹配白名单：`snssdk.com`
  - 用途：字节跳动基础域名（短视频、直播等）
- `DOMAIN-SUFFIX,analytics.githubassets.com,REJECT`
  - 匹配白名单：`githubassets.com`
  - 用途：GitHub 静态资源（CSS、JS、头像等）
- `DOMAIN-SUFFIX,ib.snssdk.com,REJECT`
  - 匹配白名单：`snssdk.com`
  - 用途：字节跳动基础域名（短视频、直播等）
- `DOMAIN-SUFFIX,log0-misc-hl.amemv.com,REJECT`
  - 匹配白名单：`amemv.com`
  - 用途：字节跳动短视频（抖音、火山等）
- `DOMAIN-SUFFIX,devgottia.github.io,REJECT`
  - 匹配白名单：`github.io`
  - 用途：GitHub Pages 站点
- `DOMAIN-SUFFIX,mon.snssdk.com,REJECT`
  - 匹配白名单：`snssdk.com`
  - 用途：字节跳动基础域名（短视频、直播等）
- `DOMAIN-SUFFIX,mcs.snssdk.com,REJECT`
  - 匹配白名单：`snssdk.com`
  - 用途：字节跳动基础域名（短视频、直播等）
- `DOMAIN-SUFFIX,p3-ad-sign.byteimg.com,REJECT`
  - 匹配白名单：`byteimg.com`
  - 用途：字节跳动图片 CDN

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

### 上游源状态

- ✅ https://raw.githubusercontent.com/GMOogway/shadowrocket-rules/master/sr_proxy_list.module
- ✅ https://raw.githubusercontent.com/LOWERTOP/Shadowrocket-First/main/Talkatone.sgmodule

**原有代理规则数**: 27357
**新增代理规则数**: 29
**更新后代理规则总数**: 27386

#### 新增代理规则明细

<details>
<summary>展开查看新增代理规则（共 29 条）</summary>

```
DOMAIN-SUFFIX,ipac.global,PROXY
DOMAIN-SUFFIX,tfd.org.tw,PROXY
DOMAIN-SUFFIX,ttl.com.tw,PROXY
DOMAIN-SUFFIX,eximbank.com.tw,PROXY
DOMAIN-SUFFIX,matichon.co.th,PROXY
DOMAIN-SUFFIX,nstc.org.tw,PROXY
DOMAIN-SUFFIX,blue-plus.net,PROXY
DOMAIN-SUFFIX,khc.edu.tw,PROXY
DOMAIN-SUFFIX,vscc.org.tw,PROXY
DOMAIN-SUFFIX,csc.com.tw,PROXY
DOMAIN-SUFFIX,moeli-desu.com,PROXY
DOMAIN-SUFFIX,tybio.com.tw,PROXY
DOMAIN-SUFFIX,icdf.org.tw,PROXY
DOMAIN-SUFFIX,aidc.com.tw,PROXY
DOMAIN-SUFFIX,ned.org,PROXY
DOMAIN-SUFFIX,rocmgov.org,PROXY
DOMAIN-SUFFIX,nationthailand.com,PROXY
DOMAIN-SUFFIX,poland.tw,PROXY
DOMAIN-SUFFIX,hanime1.com,PROXY
DOMAIN-SUFFIX,cangku.moe,PROXY
DOMAIN-SUFFIX,hanimeone.me,PROXY
DOMAIN-SUFFIX,landbank.com.tw,PROXY
DOMAIN-SUFFIX,xx.net,PROXY
DOMAIN-SUFFIX,cpc.com.tw,PROXY
DOMAIN-SUFFIX,dh.net,PROXY
DOMAIN-SUFFIX,javchu.com,PROXY
DOMAIN-SUFFIX,mirdc.org.tw,PROXY
DOMAIN-SUFFIX,indsr.org.tw,PROXY
DOMAIN-SUFFIX,twfhcsec.com.tw,PROXY
```
</details>

## 去广告模块

### 上游源状态

- ✅ https://raw.githubusercontent.com/huijingfei/Shadowrocket-Rules/refs/heads/main/sr_app_ad.module
- ✅ https://raw.githubusercontent.com/deezertidal/shadowrocket-rules/refs/heads/main/modules/startingad.module
- ✅ https://raw.githubusercontent.com/GMOogway/shadowrocket-rules/master/sr_reject_list.module
- ✅ https://raw.githubusercontent.com/Unwhimsical/NetPilot/refs/heads/main/modules/%E6%B5%8B%E8%AF%95.module
- ✅ https://raw.githubusercontent.com/LOWERTOP/Shadowrocket-First/main/TalkatoneAntiAds.list

**原有去广告规则数**: 200347
**新增去广告规则数**: 314
**更新后去广告规则总数**: 200661

#### 新增去广告规则明细

<details>
<summary>展开查看新增去广告规则（共 314 条）</summary>

```
DOMAIN-SUFFIX,landedcols.cfd,REJECT
DOMAIN-SUFFIX,rufflywahoo.cfd,REJECT
DOMAIN-SUFFIX,gcqgmgq.com,REJECT
DOMAIN-SUFFIX,yphenxyyazpfv.com,REJECT
DOMAIN-SUFFIX,warslesasking.cyou,REJECT
DOMAIN-SUFFIX,treeingforagedligas.cyou,REJECT
DOMAIN-SUFFIX,gmcrxnkdru.com,REJECT
DOMAIN-SUFFIX,qrjtjidfd.com,REJECT
DOMAIN-SUFFIX,dish.yippeeidle.com,REJECT
DOMAIN-SUFFIX,pzbsnubguitvd.site,REJECT
DOMAIN-SUFFIX,naqcmtpruisyh.space,REJECT
DOMAIN-SUFFIX,boqzpzzvazeke.space,REJECT
DOMAIN-SUFFIX,qacrzgtrflica.site,REJECT
DOMAIN-SUFFIX,bfksnozigjoeu.online,REJECT
DOMAIN-SUFFIX,sccnsjhqneqwp.online,REJECT
DOMAIN-SUFFIX,irdedwaxgtocx.website,REJECT
DOMAIN-SUFFIX,ymrsivimmsots.online,REJECT
DOMAIN-SUFFIX,qsifmdjtagkcn.site,REJECT
DOMAIN-SUFFIX,officeafifi.cfd,REJECT
DOMAIN-SUFFIX,pp3-sdk-api.profilepassport.jp,REJECT
DOMAIN-SUFFIX,yqtycbpvwpfpu.site,REJECT
DOMAIN-SUFFIX,swatskarvar.qpon,REJECT
DOMAIN-SUFFIX,sircmxqajxuis.online,REJECT
DOMAIN-SUFFIX,ciefzrxtdqxgf.site,REJECT
DOMAIN-SUFFIX,vdhqxwawhltll.online,REJECT
DOMAIN-SUFFIX,pectatedopa.qpon,REJECT
DOMAIN-SUFFIX,yoljzzzezqlxs.online,REJECT
DOMAIN-SUFFIX,4rzt1z5kgj21c6oznw.rest,REJECT
DOMAIN-SUFFIX,pkanmmxkvqfme.space,REJECT
DOMAIN-SUFFIX,quarryjoshing.cyou,REJECT
DOMAIN-SUFFIX,fqdqgeulweele.site,REJECT
DOMAIN-SUFFIX,maiaccaurceole.cfd,REJECT
DOMAIN-SUFFIX,vetandamix.cfd,REJECT
DOMAIN-SUFFIX,iisffduwhphnw.online,REJECT
DOMAIN-SUFFIX,ywriearzqniwc.online,REJECT
DOMAIN-SUFFIX,z6x5e11rcm98m5zbruvfb.cfd,REJECT
DOMAIN-SUFFIX,rapidlylassoed.qpon,REJECT
DOMAIN-SUFFIX,undconeisduvf.site,REJECT
DOMAIN-SUFFIX,vnxteieekotae.website,REJECT
DOMAIN-SUFFIX,xtorbk1g3f.com,REJECT
DOMAIN-SUFFIX,lgzfuwyecnuml.com,REJECT
DOMAIN-SUFFIX,azotinmacle.cfd,REJECT
DOMAIN-SUFFIX,ktnvonvmnzsl.com,REJECT
DOMAIN-SUFFIX,sappedbebled.com,REJECT
DOMAIN-SUFFIX,agreesnooper.com,REJECT
DOMAIN-SUFFIX,viikpgnddsyqb.website,REJECT
DOMAIN-SUFFIX,ltowbcoyjcmsd.site,REJECT
DOMAIN-SUFFIX,unsolefumbled.cfd,REJECT
DOMAIN-SUFFIX,undomedharlemmnesic.cfd,REJECT
DOMAIN-SUFFIX,pluggedaskings.cfd,REJECT
DOMAIN-SUFFIX,ergadx.com,REJECT
DOMAIN-SUFFIX,rakitsangriatoffing.cyou,REJECT
DOMAIN-SUFFIX,evenyippee.com,REJECT
DOMAIN-SUFFIX,gcxrfpknabaop.site,REJECT
DOMAIN-SUFFIX,kernoioxhouse.com,REJECT
DOMAIN-SUFFIX,dishinglucilia.cfd,REJECT
DOMAIN-SUFFIX,limpidunburnt.cfd,REJECT
DOMAIN-SUFFIX,cosmistfills.cfd,REJECT
DOMAIN-SUFFIX,tubbedempanel.cyou,REJECT
DOMAIN-SUFFIX,itystouring.cyou,REJECT
DOMAIN-SUFFIX,steroidamusive.qpon,REJECT
DOMAIN-SUFFIX,eolithlippia.com,REJECT
DOMAIN-SUFFIX,pourrispodzols.com,REJECT
DOMAIN-SUFFIX,wuoqjamhloput.online,REJECT
DOMAIN-SUFFIX,sneerpiperlystarve.cyou,REJECT
DOMAIN-SUFFIX,pp3-sdkdata-v2-ut.profilepassport.jp,REJECT
DOMAIN-SUFFIX,droningaced.cyou,REJECT
DOMAIN-SUFFIX,pastysupples.com,REJECT
DOMAIN-SUFFIX,shieldsompay.qpon,REJECT
DOMAIN-SUFFIX,wpiadbxpy.in,REJECT
DOMAIN-SUFFIX,zgvheawkcjoqb.online,REJECT
DOMAIN-SUFFIX,seizinogrisms.qpon,REJECT
DOMAIN-SUFFIX,kalomethol.cyou,REJECT
DOMAIN-SUFFIX,matlesstoledan.cyou,REJECT
DOMAIN-SUFFIX,jlonte.xyz,REJECT
DOMAIN-SUFFIX,entrapsviands.cyou,REJECT
DOMAIN-SUFFIX,kokamamimmest.cfd,REJECT
DOMAIN-SUFFIX,kyjhrlbwjrizk.site,REJECT
DOMAIN-SUFFIX,qrduzyfrddusq.website,REJECT
DOMAIN-SUFFIX,unfussyvivax.com,REJECT
DOMAIN-SUFFIX,udubohmpbkdem.space,REJECT
DOMAIN-SUFFIX,tyvfjuapkxhji.space,REJECT
DOMAIN-SUFFIX,pekeloused.com,REJECT
DOMAIN-SUFFIX,eohnvfkxzsrrp.com,REJECT
DOMAIN-SUFFIX,pmvpwivspdlvl.online,REJECT
DOMAIN-SUFFIX,etveoyriuqlxg.site,REJECT
DOMAIN-SUFFIX,tartrylwaned.cfd,REJECT
DOMAIN-SUFFIX,cuhtgextakvil.online,REJECT
DOMAIN-SUFFIX,qvpzbgwlndimh.online,REJECT
DOMAIN-SUFFIX,mcjwsxoodhyxo.site,REJECT
DOMAIN-SUFFIX,lmrebuyskosjy.online,REJECT
DOMAIN-SUFFIX,9kcut8werch6hbker1yub.cfd,REJECT
DOMAIN-SUFFIX,juggingfeinter.qpon,REJECT
DOMAIN-SUFFIX,xv5w8wipiry424qu8ppt58hcj3nv6f64pw7z.cfd,REJECT
DOMAIN-SUFFIX,lilstts.com,REJECT
DOMAIN-SUFFIX,keircereous.cfd,REJECT
DOMAIN-SUFFIX,burseragooier.qpon,REJECT
DOMAIN-SUFFIX,hotemediant.cyou,REJECT
DOMAIN-SUFFIX,hamlahbooing.qpon,REJECT
DOMAIN-SUFFIX,phruk.org,REJECT
DOMAIN-SUFFIX,blackrednecks.com,REJECT
DOMAIN-SUFFIX,yvqniyisazjxy.website,REJECT
DOMAIN-SUFFIX,qwkunzuhtgbyu.site,REJECT
DOMAIN-SUFFIX,sildoccurs.qpon,REJECT
DOMAIN-SUFFIX,itjzltjhglfzl.website,REJECT
DOMAIN-SUFFIX,smoothhmph.com,REJECT
DOMAIN-SUFFIX,sdamqhaqxwujd.website,REJECT
DOMAIN-SUFFIX,qnwapxtpzorpn.site,REJECT
DOMAIN-SUFFIX,amblerpisky.cfd,REJECT
DOMAIN-SUFFIX,loanedcylices.cfd,REJECT
DOMAIN-SUFFIX,orcsaraldom.in,REJECT
DOMAIN-SUFFIX,lukasplaicesassoil.cfd,REJECT
DOMAIN-SUFFIX,esculicshouts.cyou,REJECT
DOMAIN-SUFFIX,durianbishops.qpon,REJECT
DOMAIN-SUFFIX,jwypttgoaylfa.website,REJECT
DOMAIN-SUFFIX,unkentpillage.cfd,REJECT
DOMAIN-SUFFIX,su4wxsrtku.com,REJECT
DOMAIN-SUFFIX,lulusdunair.cyou,REJECT
DOMAIN-SUFFIX,nuchaldino.cfd,REJECT
DOMAIN-SUFFIX,vicingnutate.com,REJECT
DOMAIN-SUFFIX,wiggergossips.com,REJECT
DOMAIN-SUFFIX,gallusdrewite.cfd,REJECT
DOMAIN-SUFFIX,fgiybaritaeiv.com,REJECT
DOMAIN-SUFFIX,lollyhuckles.com,REJECT
DOMAIN-SUFFIX,reworkbufidin.cfd,REJECT
DOMAIN-SUFFIX,westanice.qpon,REJECT
DOMAIN-SUFFIX,ipdfqnxlimfcr.site,REJECT
DOMAIN-SUFFIX,declzpiio.com,REJECT
DOMAIN-SUFFIX,rjxuhhqpuwlvj.site,REJECT
DOMAIN-SUFFIX,23j1p9497we2k5cqf4.rest,REJECT
DOMAIN-SUFFIX,mkszmtwseijwh.site,REJECT
DOMAIN-SUFFIX,rqvaevbltjmjh.online,REJECT
DOMAIN-SUFFIX,cobwebsfrenum.cyou,REJECT
DOMAIN-SUFFIX,ztsgftfoxqhqz.site,REJECT
DOMAIN-SUFFIX,kmmpspzvukhrx.online,REJECT
DOMAIN-SUFFIX,delvefencescrewdriver.com,REJECT
DOMAIN-SUFFIX,hillockpippenberust.cyou,REJECT
DOMAIN-SUFFIX,syllabebaskingmilks.cyou,REJECT
DOMAIN-SUFFIX,ehcecws.com,REJECT
DOMAIN-SUFFIX,cumvblpbkivcy.website,REJECT
DOMAIN-SUFFIX,rdsotaaivsebq.website,REJECT
DOMAIN-SUFFIX,outcastalisp.shop,REJECT
DOMAIN-SUFFIX,29tj4fufueo4im.cfd,REJECT
DOMAIN-SUFFIX,onedollarstats.com,REJECT
DOMAIN-SUFFIX,p5zrfflrhbhtp8img5995x.rest,REJECT
DOMAIN-SUFFIX,musicenforcer.com,REJECT
DOMAIN-SUFFIX,cheapromaunt.com,REJECT
DOMAIN-SUFFIX,ogivalacknow.cfd,REJECT
DOMAIN-SUFFIX,lamentmungy.com,REJECT
DOMAIN-SUFFIX,goshupward.com,REJECT
DOMAIN-SUFFIX,hamestaretscravo.cyou,REJECT
DOMAIN-SUFFIX,gorcocklinustramp.qpon,REJECT
DOMAIN-SUFFIX,omeletscarsoncairene.cfd,REJECT
DOMAIN-SUFFIX,rcvfvkgglbvya.website,REJECT
DOMAIN-SUFFIX,imecvabtszpnz.space,REJECT
DOMAIN-SUFFIX,biprx.n12.co.il,REJECT
DOMAIN-SUFFIX,xfvqdbpowwkxj.space,REJECT
DOMAIN-SUFFIX,tenutishutoff.qpon,REJECT
DOMAIN-SUFFIX,p7pw9x11fronifcgn3292r5wc675f7.rest,REJECT
DOMAIN-SUFFIX,tbvjqbdybmyiae.com,REJECT
DOMAIN-SUFFIX,yyoxtiokbcmkukeiggq8h.rest,REJECT
DOMAIN-SUFFIX,wemddgeyqungo.website,REJECT
DOMAIN-SUFFIX,brasencracket.cyou,REJECT
DOMAIN-SUFFIX,xzoxfwmmnnnjfv.com,REJECT
DOMAIN-SUFFIX,pliantdecimus.cyou,REJECT
DOMAIN-SUFFIX,exertsgarten.cfd,REJECT
DOMAIN-SUFFIX,musersicasmvalyl.cyou,REJECT
DOMAIN-SUFFIX,ckixtul6tb65cv2hje.cfd,REJECT
DOMAIN-SUFFIX,vwbjzcgvlydxf.online,REJECT
DOMAIN-SUFFIX,bpucmkg.com,REJECT
DOMAIN-SUFFIX,marascaliny.cyou,REJECT
DOMAIN-SUFFIX,dextralravi.cyou,REJECT
DOMAIN-SUFFIX,deheymjqgdkys.online,REJECT
DOMAIN-SUFFIX,ionicstamine.qpon,REJECT
DOMAIN-SUFFIX,semipedyese.cfd,REJECT
DOMAIN-SUFFIX,lainagecullers.com,REJECT
DOMAIN-SUFFIX,uncitedenims.cfd,REJECT
DOMAIN-SUFFIX,curserswoesome.com,REJECT
DOMAIN-SUFFIX,thasianhyenine.com,REJECT
DOMAIN-SUFFIX,inflameunmeth.cfd,REJECT
DOMAIN-SUFFIX,wkduza2x10.com,REJECT
DOMAIN-SUFFIX,mongolsroodlesandman.cyou,REJECT
DOMAIN-SUFFIX,phacdnaeopmkr.com,REJECT
DOMAIN-SUFFIX,woodygrownup.com,REJECT
DOMAIN-SUFFIX,qfioffacmnaw.in,REJECT
DOMAIN-SUFFIX,ywgtzagvalcaiy.com,REJECT
DOMAIN-SUFFIX,kudrunmismazeslicker.cyou,REJECT
DOMAIN-SUFFIX,nlodtzqlcmbqn.online,REJECT
DOMAIN-SUFFIX,wdmtjjzjhpful.site,REJECT
DOMAIN-SUFFIX,tightrope23.com,REJECT
DOMAIN-SUFFIX,analytics.infomaniak.com,REJECT
DOMAIN-SUFFIX,ealgzcqoehebi.site,REJECT
DOMAIN-SUFFIX,yqjqykyunmpcn.website,REJECT
DOMAIN-SUFFIX,zonedphenosebetroth.cfd,REJECT
DOMAIN-SUFFIX,qzyyvctvjqiqz.com,REJECT
DOMAIN-SUFFIX,tqvozybmajoya.site,REJECT
DOMAIN-SUFFIX,stamensfootingfanger.cfd,REJECT
DOMAIN-SUFFIX,moonratjiffzeks.cyou,REJECT
DOMAIN-SUFFIX,gillyspencie.com,REJECT
DOMAIN-SUFFIX,gtbihltbcdngv.online,REJECT
DOMAIN-SUFFIX,eveningunarmed.cfd,REJECT
DOMAIN-SUFFIX,ceriumsaueto.cfd,REJECT
DOMAIN-SUFFIX,naggingfroglet.cfd,REJECT
DOMAIN-SUFFIX,bbillmkzarhwh.online,REJECT
DOMAIN-SUFFIX,neaevwledp.com,REJECT
DOMAIN-SUFFIX,one01.stright.bizris.com,REJECT
DOMAIN-SUFFIX,anagramyappish.cfd,REJECT
DOMAIN-SUFFIX,rqhsfmwwy.com,REJECT
DOMAIN-SUFFIX,fastiiainless.com,REJECT
DOMAIN-SUFFIX,ulcgleqeazcuo.site,REJECT
DOMAIN-SUFFIX,vsedyfpddfpyz.site,REJECT
DOMAIN-SUFFIX,chawanunfast.qpon,REJECT
DOMAIN-SUFFIX,ddnjehedgudbs.website,REJECT
DOMAIN-SUFFIX,zoyqmdjtfiddp.site,REJECT
DOMAIN-SUFFIX,laiciselobbers.qpon,REJECT
DOMAIN-SUFFIX,tbpykhosbxybb.online,REJECT
DOMAIN-SUFFIX,ulaacsljlamnl.online,REJECT
DOMAIN-SUFFIX,standpeise.qpon,REJECT
DOMAIN-SUFFIX,encoresweaved.com,REJECT
DOMAIN-SUFFIX,xsoydwkwqheuh.online,REJECT
DOMAIN-SUFFIX,tx142ccf5vlmpnvkby3ey4b7xk2w93.cfd,REJECT
DOMAIN-SUFFIX,roseinebespiceinsecta.qpon,REJECT
DOMAIN-SUFFIX,zimvlqwrtadmi.space,REJECT
DOMAIN-SUFFIX,pittedshends.cfd,REJECT
DOMAIN-SUFFIX,azdnagaekyivd.site,REJECT
DOMAIN-SUFFIX,ktzrfjxaglbxc.site,REJECT
DOMAIN-SUFFIX,chdelbdljersf.online,REJECT
DOMAIN-SUFFIX,widdlemonoid.com,REJECT
DOMAIN-SUFFIX,azzmtrfehtqce.site,REJECT
DOMAIN-SUFFIX,0cvo4ebbpk.com,REJECT
DOMAIN-SUFFIX,yjjvzmruicyav.online,REJECT
DOMAIN-SUFFIX,muttonssels.com,REJECT
DOMAIN-SUFFIX,covrvjzcjcnoj.site,REJECT
DOMAIN-SUFFIX,kkfopriojkuro.site,REJECT
DOMAIN-SUFFIX,3ylj411rdn.com,REJECT
DOMAIN-SUFFIX,mmftbznbhguvw.space,REJECT
DOMAIN-SUFFIX,uqmrpdwvshsci.website,REJECT
DOMAIN-SUFFIX,dlgzwnalpxske.site,REJECT
DOMAIN-SUFFIX,eaeaetoimoqkd.site,REJECT
DOMAIN-SUFFIX,ofhlddcsmwtpk.website,REJECT
DOMAIN-SUFFIX,pednhqumosxpt.space,REJECT
DOMAIN-SUFFIX,rfeqcdggqwuww.online,REJECT
DOMAIN-SUFFIX,ranevictee.cfd,REJECT
DOMAIN-SUFFIX,elvetcautela.cfd,REJECT
DOMAIN-SUFFIX,auctionr.org,REJECT
DOMAIN-SUFFIX,uahvjbwddzoki.com,REJECT
DOMAIN-SUFFIX,fz6g5l9v8kmnrq.cfd,REJECT
DOMAIN-SUFFIX,85hozvg7r9pb8hm.rest,REJECT
DOMAIN-SUFFIX,eprisimports.cfd,REJECT
DOMAIN-SUFFIX,crdema.com,REJECT
DOMAIN-SUFFIX,ricnrpnijosnm.site,REJECT
DOMAIN-SUFFIX,dunchencycbrazes.cyou,REJECT
DOMAIN-SUFFIX,gaywaymetamer.com,REJECT
DOMAIN-SUFFIX,heavierpristishoplite.cfd,REJECT
DOMAIN-SUFFIX,tips.delt.io,REJECT
DOMAIN-SUFFIX,c3.wildwolf.name,REJECT
DOMAIN-SUFFIX,abtykeajetlyv.online,REJECT
DOMAIN-SUFFIX,dxsbchijnhiwo.website,REJECT
DOMAIN-SUFFIX,zhziofscdxvjh.online,REJECT
DOMAIN-SUFFIX,kneedchanges.cyou,REJECT
DOMAIN-SUFFIX,rtlthwjmiqyqh.site,REJECT
DOMAIN-SUFFIX,limiestcephid.cfd,REJECT
DOMAIN-SUFFIX,heighthdharnasamhita.cfd,REJECT
DOMAIN-SUFFIX,ignkabayasneezer.qpon,REJECT
DOMAIN-SUFFIX,idbrfpiznfdrv.online,REJECT
DOMAIN-SUFFIX,malaisetripler.cfd,REJECT
DOMAIN-SUFFIX,markebramstriamin.qpon,REJECT
DOMAIN-SUFFIX,midriffdarby.cyou,REJECT
DOMAIN-SUFFIX,belugascompte.cfd,REJECT
DOMAIN-SUFFIX,rewardskouros.com,REJECT
DOMAIN-SUFFIX,ofymjcdwjuvdi.online,REJECT
DOMAIN-SUFFIX,martelchanson.cfd,REJECT
DOMAIN-SUFFIX,rqiepklpcmiuw.space,REJECT
DOMAIN-SUFFIX,ringiteinsect.cfd,REJECT
DOMAIN-SUFFIX,vudnpysryo.in,REJECT
DOMAIN-SUFFIX,gushedbewares.cfd,REJECT
DOMAIN-SUFFIX,573df7c52b.com,REJECT
DOMAIN-SUFFIX,clewfyrdung.com,REJECT
DOMAIN-SUFFIX,j3ossmqgmc.com,REJECT
DOMAIN-SUFFIX,nxrvwzzojfnkp.website,REJECT
DOMAIN-SUFFIX,trigosfascismhoutou.cyou,REJECT
DOMAIN-SUFFIX,6y10di5jko.com,REJECT
DOMAIN-SUFFIX,abdncdbuocpvf.space,REJECT
DOMAIN-SUFFIX,pizzadak.cyou,REJECT
DOMAIN-SUFFIX,nt-stream-log.profilepassport.jp,REJECT
DOMAIN-SUFFIX,zigankatiu.cyou,REJECT
DOMAIN-SUFFIX,camanaytact.cfd,REJECT
DOMAIN-SUFFIX,sidlesunfall.com,REJECT
DOMAIN-SUFFIX,hmymkrsiidpze.online,REJECT
DOMAIN-SUFFIX,jcjxtxmmigeoc.website,REJECT
DOMAIN-SUFFIX,nzfhhfkqtwgyv.online,REJECT
DOMAIN-SUFFIX,zvvfinnpxsscn.site,REJECT
DOMAIN-SUFFIX,ekurgxhwtesjp.website,REJECT
DOMAIN-SUFFIX,lamnoidmegohm.com,REJECT
DOMAIN-SUFFIX,jerkerlagen.qpon,REJECT
DOMAIN-SUFFIX,ex17zo915pi77xm3.rest,REJECT
DOMAIN-SUFFIX,frshery.com,REJECT
DOMAIN-SUFFIX,yhjzqlnhlxxms.space,REJECT
DOMAIN-SUFFIX,wfloqxrwhkryj.website,REJECT
DOMAIN-SUFFIX,dyf08yha87tii.cloudfront.net,REJECT
DOMAIN-SUFFIX,njbvylypblfhb.online,REJECT
DOMAIN-SUFFIX,sonancejingals.qpon,REJECT
DOMAIN-SUFFIX,zhzrvjmyqvdhrc.com,REJECT
DOMAIN-SUFFIX,dgcuojdzhkoaq.website,REJECT
DOMAIN-SUFFIX,bluesygayal.cfd,REJECT
DOMAIN-SUFFIX,abacgycrrawaa.online,REJECT
DOMAIN-SUFFIX,heliaczygomaklaxons.cyou,REJECT
DOMAIN-SUFFIX,tyl4th3rtk94k9b6k1tlwl.rest,REJECT
DOMAIN-SUFFIX,glhjrjohcdbam.com,REJECT
DOMAIN-SUFFIX,rlympytqnjtqx.website,REJECT
DOMAIN-SUFFIX,ilianbrined.cyou,REJECT
DOMAIN-SUFFIX,cenotesbotein.qpon,REJECT
DOMAIN-SUFFIX,f53kzx5xr214nbhz4uoh.cfd,REJECT
DOMAIN-SUFFIX,unami.delt.io,REJECT
```
</details>

## ⚠️ 敏感域名已自动过滤（银行/支付）

**原因**：域名包含银行/支付关键词，为防止隐私泄露，不加入解密列表。

<details>
<summary>展开查看被过滤的敏感域名（共 7 个）</summary>

```
webappcfg.paas.cmbchina.com
yunbusiness.ccb.com
creditcardapp.bankcomm.com
m.creditcard.ecitic.com
mpos-pic.helipay.com
creditcardapp.bankcomm.cn
lban.spdb.com.cn
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

🩺 Shield模块: 健康检查通过（228047 条规则，10.5 MB）

✅ Shield 模块已写入，代理 27386 条，去广告 200661 条

## 🩺 规则源健康状态

<details>
<summary>展开查看各上游源健康状态（共 8 个源）</summary>

- ✅ https://raw.githubusercontent.com/GMOogway/shadowrocket-rules/master/sr_direct_list.module
  - 成功 84 次，失败 0 次，连续失败 0 次
  - 最近成功: 2026-10-07 18:50:02
  - 最近失败: 无 

- ✅ https://raw.githubusercontent.com/GMOogway/shadowrocket-rules/master/sr_proxy_list.module
  - 成功 84 次，失败 0 次，连续失败 0 次
  - 最近成功: 2026-10-07 18:50:18
  - 最近失败: 无 

- ✅ https://raw.githubusercontent.com/LOWERTOP/Shadowrocket-First/main/Talkatone.sgmodule
  - 成功 84 次，失败 0 次，连续失败 0 次
  - 最近成功: 2026-10-07 18:50:18
  - 最近失败: 无 

- ✅ https://raw.githubusercontent.com/huijingfei/Shadowrocket-Rules/refs/heads/main/sr_app_ad.module
  - 成功 84 次，失败 0 次，连续失败 0 次
  - 最近成功: 2026-10-07 18:50:18
  - 最近失败: 无 

- ✅ https://raw.githubusercontent.com/deezertidal/shadowrocket-rules/refs/heads/main/modules/startingad.module
  - 成功 84 次，失败 0 次，连续失败 0 次
  - 最近成功: 2026-10-07 18:50:18
  - 最近失败: 无 

- ✅ https://raw.githubusercontent.com/GMOogway/shadowrocket-rules/master/sr_reject_list.module
  - 成功 84 次，失败 0 次，连续失败 0 次
  - 最近成功: 2026-10-07 18:50:20
  - 最近失败: 无 

- ✅ https://raw.githubusercontent.com/Unwhimsical/NetPilot/refs/heads/main/modules/%E6%B5%8B%E8%AF%95.module
  - 成功 84 次，失败 0 次，连续失败 0 次
  - 最近成功: 2026-10-07 18:50:20
  - 最近失败: 无 

- ✅ https://raw.githubusercontent.com/LOWERTOP/Shadowrocket-First/main/TalkatoneAntiAds.list
  - 成功 84 次，失败 0 次，连续失败 0 次
  - 最近成功: 2026-10-07 18:50:20
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
