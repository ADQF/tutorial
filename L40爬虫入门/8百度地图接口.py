import urllib.request
import urllib.parse
import json

# resp = urllib.request.urlopen('http://api.map.baidu.com/place/v2/search?query=ATM机&tag=银行&region=北京&output=json&ak=您的ak //GET请求',
origin_args = {'query': '', 'region': '全国', 'output': 'json', 'ak': 'lmPbC0aomYsMIsg4V891vwQvczUKrsPy'}
# 将中文参数base64编码
b64_args = urllib.parse.urlencode(origin_args)
print(b64_args)
# 拼url 请求
base_url = 'http://api.map.baidu.com/place/v2/search'
url = base_url + '?' + b64_args
print('偏好的url', url)
resp = urllib.request.urlopen(url)
content_json = resp.read().decode()
print(content_json)
# json转对象
content_obj = json.loads(content_json)
print(content_obj)
results = content_obj['results']
for row in results:
    print(row['name'], row['address'])
