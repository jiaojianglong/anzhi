##安智生医测试项目
######
####要求
以Flask建立一服务接口(API)，并具备以下功能：  
使用者登入功能  
登入后可给定基因名称取得资讯  
使用爬虫自网站(https://www.ensembl.org)获得基因资讯  
抓取之资讯同时存入资料库（资料库请自行选择，并提供选择理由）并回传
输入参数：基因名称（如：BLM）  
回传：将指定基因之transcripts资讯以JSON格式回传

#

整体项目使用Flask+BootStrap开发，数据库使用Mysql和MongoDB
1. 注册登录功能使用Flask_Login实现,用户信息存在Mysql中，
配合Flask_SQLAlchemy建立ORM,方便数据操作。登录和注册表单使用
Flask-WTF配合BootStrap实现表单验证。
2. 使用BeautifulSoup解析基因详情页内容，将transcripts
部分的内容解析为Json格式数据，储存到MongoDB并返回给前端。
3. 将数据储存到MongoDB主要考虑到我们的数据格式为Json,
MongoDB是文档型数据库，可以很方便的存入json数据。


####项目截图
1. 用户登录
![用户登录](https://github.com/jiaojianglong/anzhi/blob/master/app/static/image/20190805152716.png?raw=true)
2. 用户注册
![用户注册](https://github.com/jiaojianglong/anzhi/blob/master/app/static/image/20190805152740.png?raw=true)
3. 搜索基因
![搜索基因](https://github.com/jiaojianglong/anzhi/blob/master/app/static/image/20190805153000.png?raw=true)