###Installing Scrapy
 `conda install -c conda-forge scrapy # 我的环境安装失败，还是做下记录吧` <br/>
 pip 安装 <br/>
 `pip install Scrapy`
 
### 纯python编写,使用到的库
 - lxml
 - parsel
 - w3lib
 - twisted
 - cryptography and pyOpenSSL

### 推荐安装在虚拟环境 

### creating a project
`scrapy startproject tutorial`

目录结构

`
tutorial/
    scrapy.cfg            # deploy configuration file

    tutorial/             # project's Python module, you'll import your code from here
        __init__.py

        items.py          # project items definition file

        middlewares.py    # project middlewares file

        pipelines.py      # project pipelines file

        settings.py       # project settings file

        spiders/          # a directory where you'll later put your spiders
            __init__.py
`

### Our first Spider
在 spiders, 新建myspider.py 文件，内容去看代码 必须是scrapy.Spider 的子类

### run spider
`scrapy crawl quotes`

### scrapy shell
`scrapy shell "http://quotes.toscrape.com/page/1/"`

### Storing the scraped data
`scrapy crawl quotes -o quotes.json`
 - JSON Lines （）
### Following links
 - 爬取页面内的连接
 - 示例：spidermylearn 项目的 my_spider3.py 