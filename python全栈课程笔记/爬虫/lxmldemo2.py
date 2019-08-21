from lxml import etree

html = etree.parse('./demo.xml')
# rst = etree.tostring(html, pretty_print=True)
# print(rst)

print(type(html))

rst = html.xpath('//book[@category="sport"]/price')
print(type(rst))
rst = rst[0]
print(rst.tag)
print(rst.text)
