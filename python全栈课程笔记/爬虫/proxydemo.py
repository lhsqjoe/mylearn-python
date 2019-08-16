from urllib import request, error

if __name__ == '__main__':
    url = 'http://www.baidu.com'
    proxy = {'http': '121.15.254.156:888'}
    proxy_handler = request.ProxyHandler(proxy)
    opener = request.build_opener(proxy_handler)
    request.install_opener(opener)
    try:
        headers = {}
        req = request.Request(url)
        req.add_header('User-Agent',
                       'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36')
        rsp = request.urlopen(req)
        html = rsp.read().decode()
        print(html)
    except error.HTTPError as e:
        print(e)
    except error.URLError as e:
        print(e)
    except Exception as e:
        print(e)
