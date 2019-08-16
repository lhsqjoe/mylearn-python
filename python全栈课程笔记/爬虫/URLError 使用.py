from urllib import request, error

if __name__ == '__main__':
    # url = 'http://www.baidu.com'
    # url = 'http://10.10.200.4:18000'
    url = 'http://www.sipo.gov.cn/www'
    try:
        req = request.Request(url=url)
        rsp = request.urlopen(req, timeout=10)
        html = rsp.read().decode()
        print(html)
    except error.HTTPError as e:
        print('HTTPError:{}'.format(e.reason))
        print('HTTPError:{}'.format(e))
    except error.URLError as e:
        print('URLError:{}'.format(e.reason))
        print('URLError:{}'.format(e))
    except Exception as e:
        print(e)
