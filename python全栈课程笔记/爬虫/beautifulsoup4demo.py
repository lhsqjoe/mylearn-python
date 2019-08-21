from urllib import request
from bs4 import BeautifulSoup

url = 'http://www.baidu.com'
rsp = request.urlopen(url)
content = rsp.read()
soup = BeautifulSoup(content, 'lxml')
content = soup.prettify()
print(content)

print('*' * 20)
# print(soup.meta)
print(soup.link)
print(soup.link.name)
print(soup.link.attrs)
print('*' * 20)
print(soup.title.string)
print('*' * 20)

print(soup.find_all(name='link'))
print('*' * 20)

print(soup.select('.mnav'))
