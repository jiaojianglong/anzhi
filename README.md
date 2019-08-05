##安智测试项目
######

以Flask建立一服务接口(API)，并具备以下功能：  
使用者登入功能  
登入后可给定基因名称取得资讯  
使用爬虫自网站(https://www.ensembl.org)获得基因资讯  
抓取之资讯同时存入资料库（资料库请自行选择，并提供选择理由）并回传
输入参数：基因名称（如：BLM）  
回传：将指定基因之transcripts资讯以JSON格式回传


##

整体项目使用Flask+BootStrap开发，数据库使用Mysql和MongoDB
1. 注册登录功能使用Flask_Login实现,用户信息存在Mysql中
2. 基因信息存在MongoDB中，因为我们爬取到的信息是json格式的，MongoDB是文档型数据库，可以很方便的存入json数据。


