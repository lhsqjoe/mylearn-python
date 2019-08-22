'''
content: 抓取51cto 首页信息
@Author qiao
date 2019-08-22
'''
import scrapy
from lxml import etree


class MySpider001(scrapy.Spider):
    name = '51cto001'
    start_urls = [
        'http://www.51cto.com/'
    ]

    def parse(self, response):
        # print(response.xpath('//title/text()').get())
        # my_content = response.xpath('//div[@class="zxf_menubot mt10 clearfix"]/dl/dt/span/text()').getall()
        # for item in my_content:
        #     print(item)
        # my_content_detail = response.xpath('//div[@class="zxf_menubot mt10 clearfix"]/dl/dd/ul/li/a/text()').getall()
        # print(my_content_detail)
        # my_content_other = response.xpath('//div[@class="zxf_menubot mt10 clearfix"]/dl/*').getall()
        # print(my_content_other)

        my_content_1 = response.xpath('//div[@class="zxf_menubot mt10 clearfix"]/*').getall()
        # print(my_content_1)
        res_file = 'res.md'
        res = ''
        for my_dl in my_content_1:
            html = etree.HTML(my_dl)
            # my_category = html.xpath('//dl/*/dt/span/text()')
            my_category = html.xpath('//dl/dt/span/text()|//dl/dt/a/span/text()')
            if len(my_category) != 0:
                res += '+ '+my_category[0]+'\n'
                # print(my_category[0])
            child_node = html.xpath('//dl/dd/ul/li/a/text()')
            for child in child_node:
                # print(' {0}'.format(child))
                res += '    - '+child+'\n'
        print(res)
        with open(res_file, 'wb') as f:
            f.write(res.encode(encoding='utf-8'))
