# 4.js异步请求
# 一些后端语言框架如django是把变量渲染到HTML模板最终在response返回，用户交互时需要刷新页面才能看到修改后的效果。为了更好的网页体验和前后端程序员工作分离。前端js工作中也有类似后端requests包的前端操作包。导致有些数据第一次HTML中并看不到。
"""
<html>
    <body>
        <h1>待爬取内容</h1>
        <script>
            document.onloads(
            function foo():{
                // 请求商品列表
                // 操作dom节点把商品信息渲染到页面中。
            {)

            $.get('button').ajax({
                url: xxx,
                params: page_no=1,
            })
        </script>

    </body>
</html>

js中情况—   类似后端的requests包， 发送http请求。开发者工具看响应是否是json数据。
js中情况二   ajax 相当于上面的封装。xml结构沟通。开发者工具XHR(XMLHttpRequest)
小技巧：网站请求非常多，1.排除jpg css这些请求 2.看XHR里有没有 3.看
"""


# 需求：爬取京东一个商品的评论
"""
分析： 商品评论原始url https://item.jd.com/100000287113.html#comment
当点击评论里的第二页的时候，url路由并没有变化没有参数。
如果django来做分页路由形式如下
http
其实评论信息的请求在js中，由浏览器后台执行。
所以我们需要在谷歌开发者工具中 找出js中的评论信息请求，requests包构造请求，模拟浏览器的执行过程

分析后得到的请求地址：
https://sclub.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98vv15261&productId=100000287113&score=0&sortType=5&page=0&pageSize=10&isShadowSku=0&fold=1
然后用requests包构造这个请求。
callback=fetchJSON_comment98vv15288&productId=100000287113&score=0&sortType=5&page=0&pageSize=10&isShadowSku=0&fold=1
分析参数：发现有参数不知含义
"""

import requests
import json
from lxml import etree

comment_url = 'https://sclub.jd.com/comment/productPageComments.action'

params = {
    # 'callback': 'fetchJSON_comment98vv15288',
    'productId': 100000287113,
    'score': 0,
    'sortType': 5,
    'page': 0,
    'pageSize': 10,
    # 'isShadowSku': 0,
    # 'fold': 1,
}



headers = {
        'cookie': '__jdu=1545965016566122167306; shshshfpa=91aaa0e4-7924-2ea5-1870-d0d653119b3f-1545965018; user-key=2e7a62ce-3569-47af-96f7-f8992f90722b; cn=0; __jdv=122270672|google|1111US|CPC|not set|1545965056641; unick=jd_176382uon; pin=jd_6d66c1bd51468; _tp=pBQJkiA7r%2BIY%2FhF%2FquydSDVy0R12L6v1XMNhEko7v%2BM%3D; _pst=jd_6d66c1bd51468; PCSYCityID=412; mt_xid=V2_52007VwMWV1lQVV4eSR5YAmADEVFdX1RYHk4pVQxhChBSXV9OUxweGEAANFdCTg0PAF8DSB4PATJQElZfWVZTL0oYXAx7AxFOXlFDWh5CHVUOYwAiUm1YYlgdSB1eBWEHFGJfXFNe; ipLoc-djd=1-72-4137-0; areaId=1; shshshfpb=vWY4pLrc3hhHfFHANk%2BPsTg%3D%3D; shshshfp=f2e3aaa6ac280d409f682075e6afc812; _gcl_au=1.1.2092516447.1545981775; __jda=122270672.1545965016566122167306.1545965017.1545995113.1546499133.4; __jdc=122270672; wlfstk_smdl=ef4r0muh5yg22ha0n8qadnmvof5r8oom; cid=NXhENTk2Nm1ZOTU4N2hCNTM2OHNLMTk4MWFKMjc2MmVQOTU4M2RWMTk0NG1aMTMw; thor=1F192C4506D4DB5F1A3E92FD905CDD534B53EA2E892A760FA59A8AFF26762A578371DD10754BA106515677E71E06E5C29B97592E0DD1D2032D1BDC08C5B881D8835C9FC022CC38F954FB70E93D0DD4D2B92FFA5A68F1CD99A13ED8A1447302E5EF069B81C1B43F0B727FDB4B13C01231F43357F40302CA0939EA765EDD18030A8B70D828EF087C9BABF6B4517BE036553D8FAA705BECE333E5E7ABE60459EFAF; pinId=im3RPgaRtzCc8aZ5IRnsRbV9-x-f3wj7; ceshi3.com=000; 3AB9D23F7A4B3C9B=E6WHA67OFAKMK3AGOERHNLWBOBPVRXWH4KBLVQTDYFKTHBEHTSOT2R6TDQQOWFEXRJ37LY6GYGGHQWCBCSUF6KBGXI; __jdb=122270672.7.1545965016566122167306|4.1546499133',
        'referer': 'https://item.jd.com/100000287113.html',
        'user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36'
    }

comment_resp = requests.get(url=comment_url, params=params, headers=headers)
print(comment_resp.status_code)
comment_str = comment_resp.text

comment_dict = json.loads(comment_str)
# comment_dict = json.load('4js接口-京东评论-评论数据.json')
comments = comment_dict['comments']
hotCommentTagStatistics = comment_dict['hotCommentTagStatistics']
productCommentSummary = comment_dict['productCommentSummary']
print(productCommentSummary['goodRateShow'])
for hotCommentTagStatistic in hotCommentTagStatistics:
    print(hotCommentTagStatistic['id'])
    print(hotCommentTagStatistic['name'])
    print(hotCommentTagStatistic['count'])
for comment in comments:
    print(comment['id'])
    print(comment['content'])
    print(comment['creationTime'])
    print(comment['score'])
    print(comment['nickname'])
    print(comment['usefulVoteCount'])
    images = comment['images']
    for image in images:
        print(image['imgUrl'])
