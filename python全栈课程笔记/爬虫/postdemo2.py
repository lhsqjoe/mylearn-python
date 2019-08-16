from urllib import request, parse
import json

baseurl = 'https://fanyi.baidu.com/sug'

data = {
    'kw': 'boy'
}
data = parse.urlencode(data).encode()
headers = {
    'Content-Length': len(data)
}

req = request.Request(url=baseurl, data=data, headers=headers)
rsp = request.urlopen(req, timeout=5)
json_data = rsp.read().decode('utf-8')
json_data = json.loads(json_data)
for item in json_data['data']:
    print('key:{} value:{}'.format(item['k'], item['v']))
