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
rsp = request.urlopen(baseurl, data=data)

json_data = rsp.read().decode('utf-8')
print(type(json_data))
json_data = json.loads(json_data)
print(json_data)

for item in json_data['data']:
    print('key:{} value:{}'.format(item['k'], item['v']))
