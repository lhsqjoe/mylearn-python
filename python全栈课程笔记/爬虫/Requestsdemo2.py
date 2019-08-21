import requests

baseurl = 'https://fanyi.baidu.com/sug'

data = {
    'kw': 'boy'
}
headers = {
    'Content-Length': str(len(data))
}
rsp = requests.post(baseurl, data=data, headers=headers)

json_data = rsp.text
print(type(json_data))
print(rsp.text)
print(rsp.json())
