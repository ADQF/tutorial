# urllib代理示例
#为了防止同一个ip频繁访问服务器被封锁，需要不断变化ip通过别人的电脑代理访问服务器。

"""
从哪里找代理？
1. ip代理平台 http：/www.xicidaili.com/nn/
免费的不太稳定，有些不可用，付费的稳定。
2. 网友搜索爬取的ip代理池。
"""

import urllib.request
# import random
#
# proxies = [
#     {},
#     {},
#     {},
# ]
# proxy = random.choice(proxies)

proxy = urllib.request.ProxyHandler({'http': 'http://125.40.29.100:8118'})
opener = urllib.request.build_opener(proxy, urllib.request.HTTPHandler)
urllib.request.install_opener(opener)
# 请求百度搜索关键字ip
response = urllib.request.urlopen('http://www.baidu.com/s?wd=ip')
html_content = response.read().decode('utf-8')
print(html_content)


"""
可能出现的错误
"""