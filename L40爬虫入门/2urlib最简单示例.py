# urllib包，专门处理http请求响应的内置包。

# import urllib #urllib包下的__init__.py没写东西，import urllib写法并不会引入其他文件。
import urllib.request
# from urllib.request import urlopen
response = urllib.request.urlopen('http://www.baidu.com')
# urlopen(url, data={参数1:值1, 参数2:值2}, timeout=网页响应超时时间)
print(response)
# 从响应读信息
print(response.code)
html_content = response.read()
print(html_content)      # 字节类型的网页信息
print(html_content.decode(encoding='utf-8'))     # 字节解码成字符串信息


# 网上教程urllib urlib2 , urllib3。
# Python2.3时代内置处理http的包是urllib。增加改进发布urllib2包，这两个包都是内置。
# urllib3是第三方开发者开发，语法比较自然，request包基于urllib3包。
# Python3时代吧Python2时代的urllib、urllib2包合并成urllib
# 总结：现在我们用的http相关处理包，主要有内置的urllib和第三方urllib3包组成






