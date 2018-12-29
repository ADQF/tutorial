import urllib.request
import json

url = 'ttp://example.python-scraping.com/places/default/view/United-States-234'
resp = urllib.request.urlopen(url)
print("第一种方法")

# 获取状态码，200表示成功
print(resp.getcode())
# 获取网页内容的长度
print(len(resp.read()))