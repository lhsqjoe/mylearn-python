# 爬虫
 - 推荐资料
    - python 网络数据采集
    - 精通python爬虫框架 scrapy
    - 博客 http://blog.csdn.net/c406495762/article/details/72858983
    - 官方教程 http://scrapy-chs.readthedocs.io/zh_CN/0.24/intro/tutorial.html
 - 前提知识
    - url
    - http 协议
    - web 前端 html, css, js
    - ajax
    - re, xpath
    - xml

# 1. 爬虫简介
 - 定义: 网络爬虫(又被称为网页蜘蛛 网络机器人 在FOAF社区中间 更经常的成为网页追逐者)
 是一种按照一定的规则，自动抓取万维网信息的程序 或者脚本
 另外一些 不常使用的名字还有蚂蚁 自动索引 模拟程序或者蠕虫   
 - 两大特征
    - 能按照作者的要求下载数据或者内容
    - 能自动在网络上流窜 

 - 三大步骤
    - 下载网页
    - 提取正确的信息
    - 根据一定规则到另外的网页上执行上两步内容
 - 爬虫分类
    - 通用爬虫
    - 专业爬虫(聚焦爬虫)

 - python 网络包简介
    - python2.X：urllib，urllib2，urllib3，httplib，httplib2，requests
    - python3.X: urllib，urllib3，httplib2，requests 

# 2. urllib
 - 包含模块
    - urllib.request: 打开和读取urls
    - urllib.error： 包含urllib.request 产生的常见错误，使用try 捕捉
    - urllib.parse: 包含 即系 url的方法
    - urllib.robotparse: 解析robots.txt 文件   
 - 网页编码问题的解决
    - chardet 可以自动检测页面文件的编码格式，但是可能有错误 原理是检测 html `<head>` 部分的 `<charset>` 标签
    - 需要安装  activate mylearn  conda install chardet
 - urlopen 返回 response  
    - geturl
    - info: 头信息
    - getcode: 返回http code  

 - urllib.data  
    - 访问网络的方法
        - get
        - post 
            - post 是把信息自动加密处理 
        - request.Request 
 
 - urllib.error
    - URLError  原因
        - 没网
        - 服务器链接失败  
    - HTTPError, 是  URLError 的子类
 
 - UserAgent      
    - UserAgent： 用户代理，简称UA, 属于heads的一部分,  服务器通过UA来判断 访问者身份
    - 常见的UA值
        - Android    
        - firefox
        - Google chrome
            - Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36
        - ios   
 - ProxyHandler 处理（代理服务器)
    - 使用代理IP, 是爬虫的常用手段  
    - 获取代理服务器的地址
        - www.xicidaili.com
        - www.goubanjia.com
    - 代理用来隐藏真实访问中，代理也不允许频繁访问一个固定网站，所以，代理一定要很多很多
    - 基本 使用步骤：
        1. 设置代理地址
        2. 创建proxyHandler
        3. 创建Opener
        4. 安装Opener      