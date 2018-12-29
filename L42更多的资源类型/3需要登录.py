# 3 需要登录的情况
"""
场景：个人信息页，订单页，需要登录权限验证后才可以访问。
权限验证：网站通过token或sessionid来限制页面访问。
sessionid：http无状态，http://www.baidu.com?kw=python,这个请求只包含目的地址和参数，不包含登录信息。登陆后只能保证本次请求，下一次请求服务器仍然不知道是否用户是否登录。为了解决用户登录后会话保持问题。
解决方式: 用户登录，服务器接收用户密码验证，通过则根据用户信息生成摘要字符串，即token或sessionid，返回响应告诉客户端保存token到cookie，浏览器接收响应后储存token到cookie。然后之后的每一次请求都会携带cookie，这样服务器就能认识客户端了。cookie好像额外的参数。token好像婚礼的请帖。
"""

"""
需求：模拟登陆，获取GitHub 个人页/emails/ 登录邮箱。

分析：直接访问个人页会重新定向到登录页。
1. 请求登录页，接收sessionid存入cookie
1) 先通过谷歌开发者工具找到login的请求（类型、url、参数）。刷新登录页，然后clear请求，然后点击登录，观察新出现的请求。
点击登录后发现https://github.com/session请求，302重定向，为了防止重定向后控制台信息被刷掉，勾选开发者工具中的preserve 


方法
参数，commit：Sign in
    utf-8：√
    authenticity_token: SbxCFPbfNbNPNW...
    login: 1770323960@qq.com
    password: xxx
    注意authenticity_token跟cookie中的user_sesssion不一样。authenticity_token
2. 请求个人页（携带cookie）

梳理步骤：
1. get请求 login页面

3.去登录，准备好各个参数。
4. post请求 去登陆 session
"""

import requests
from lxml import etree

login_url = 'http://github.com/login'
profile_url = 'https://github.com/settings/profile'

# 未登录时请求个人页

headers = {
'Host': 'github.com',
'Referer': 'https://github.com/',
'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36'
}

# requests

s = requests.Session()
login_resp = s.get(login_url, headers=headers)
if login_resp.status_code != 200:
    raise Exception("get请求登录页表单失败{}".format(login_resp.status_code))
login_html_content = login_resp.text

login_dom = etree.HTML(login_html_content)
pattern_auth

39499329







