from urllib import request, error

if __name__ == '__main__':
    url = 'http://www.baidu.com'
    try:
        headers = {}
        # headers[
        #     'User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'
        # req = request.Request(url=url, headers=headers)
        req = request.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36')
        rsp = request.urlopen(req)
        html = rsp.read().decode()
        print(html)
    except error.HTTPError as e:
        print(e)
    except error.URLError as e:
        print(e)
    except Exception as e:
        print(e)
