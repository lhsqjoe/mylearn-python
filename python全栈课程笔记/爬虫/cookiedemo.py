from urllib import request, parse, error
from http import cookiejar
import chardet

cookie = cookiejar.CookieJar()
cookie_handler = request.HTTPCookieProcessor(cookie)
http_handler = request.HTTPHandler()
https_handler = request.HTTPSHandler()

opener = request.build_opener(http_handler, https_handler, cookie_handler)


def login():
    url = 'http://www.renren.com/PLogin.do'
    data = {
        'email': '13119144223',
        'password': '123456'
    }
    data = parse.urlencode(data).encode()
    req = request.Request(url, data=data)
    rsp = opener.open(req)


def getHomePage():
    url = 'http://www.renren.com/965187997/profile'
    rsp = opener.open(url)
    html = rsp.read()
    cs = chardet.detect(html)
    html = html.decode(cs.get('encoding', 'utf-8'))
    with open('rsp.html', 'w', encoding='utf-8') as f:
        f.write(html)


if __name__ == '__main__':
    login()
    getHomePage()
