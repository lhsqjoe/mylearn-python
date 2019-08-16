from urllib import request

if __name__ == '__main__':
    url = 'https://blog.csdn.net/u013920536/article/details/81274035'
    rsp = request.urlopen(url)
    html = rsp.read()
    # print(html.decode())
    print(html.decode('utf-8'))

    print(rsp.geturl())
    print(rsp.info())
    print(rsp.getcode())
