from urllib import request, parse
import chardet

if __name__ == '__main__':
    url = 'https://www.baidu.com/s?'
    wd = input('Input your keyword:')

    qs = {
        'wd': wd
    }
    rsp = request.urlopen(url+parse.urlencode(qs))
    html = rsp.read()
    cs = chardet.detect(html)
    print(type(cs))
    print(cs)

    html = html.decode(cs.get('encoding', 'utf-8'))
    print(html)
