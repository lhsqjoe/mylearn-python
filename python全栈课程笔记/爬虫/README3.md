# lxml  库
 - https://lxml.de
 - 功能
    - 解析HTML， 补全html标签
    - 文件读取


# css 选择器      beautifulsoup4
 - https://www.crummy.com/software/BeautifulSoup/bs4/doc.zh/
 - 几个常用提取信息工具的比较
    - 正则 很快，不好用
    - beautifulsoup4 慢，使用简单
    - lxml 比较块，使用简单
 - 四大对象
    - Tag
    - NavigableString
    - BeautifulSoup
    - Comment
 - 遍历
 - 搜索文档对象
 - css 选择器 (参照 css 选择器规则)
    - 使用 soup.select 返回一个列表 

# 动态HTML 
## 反爬虫   
## 动态网页
 - JavaScript
 - jQuery
 - Ajax      
 - DHTML  

 - Python 采集动态 数据
    - 从JavaScript代码入手采集，不建议，太lower，速度太慢了
    - Python第三方库运行js, 直接采集你在浏览器看到的数据
## Selenium + PhantomJS
 - Selenium  web自动化测试工具
    - 自动加载页面
    - 获取数据
    - 截屏
 - PhantomJS（幽灵）
    - 基于 webkit 的无界面浏览器
 - Selenium 库有一个webDriver 的API
 - webdriver 可以跟页面上的元素进行各种交互,用它可以来进行爬取

## Selenium + chrome(win10 下)
 - 下载 chrome
 - 下载 chrome driver 
 - 放在 C:\Program Files (x86)\Google\Chrome\Application 目录下
 - 配置Path 环境变量
 - 额，配置完成后一直提示Path 找不到 chromedriver ,重启 pycharm 后可以了，不知道是啥原因

## 验证码
 - 分类
    - 简单图片
    - 极验 https://www.geetest.com/
    - 12306
    - 电话（国内少）
    - Google 验证 
 - 破解
    - 通用方法
        - 下载网页和验证码
        - 手动输入验证号码
    - 简单图片
        - 使用图像识别软件或者文字识别软件 
        - 使用第三方图像验证码破解网站      https://www.chaojiying.com/  
    - 极验 https://www.geetest.com/    
        - 破解麻烦
        - 可以模拟鼠标等移动
        - 一直在进化
    - 12306 可以放弃了
    - 电话 （语音识别） 

## Tesseract (准确率相当的低。。。。)
 - 机器视觉领域的基础软件
 - OCR 光学文字识别
 -  Tesseract 一个OCR库, google赞助   
 - 安装 
    - apt install  tesseract-ocr
    - 使用
    - pip install  tesseract       
 

     