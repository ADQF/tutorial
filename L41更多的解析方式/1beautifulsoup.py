# beautifulsoup
# bs包把html按照节点的层级关系转换为树形文档，然后解析，简单易用
# 安装 pip install beautifulsoup4  注意beautifulsoup只能用于py2
# lxml是安全解析HTML标签到文档树，支持bs4和xpath。
# 安装 'pip install lxml

from bs4 import BeautifulSoup

html = """
<html>
    <body>
        <a id="aaa" href='http://www.baidu.com' name='aaa'
        class="aaa">百度一下</a>
        <a href='http://www.baidu.com'>百度一下2</a>
        <h1>大家好</h1>
    </body>
</html> 
"""
# 实例化bs，传入参数待解析html内容和解析器
# html.parser python内置， 方便兼容性好：lxml
bs = BeautifulSoup(html, 'lxml')
# bs = BeautifulSoup(html, 'html.parser')
# 格式化输出
print(bs.prettify())

# 查找标签
print(bs.head)
print(bs.a)
print(bs.find_all('a'))

# 返回标签名称
print(bs.name)
print(bs.a.name)

# 根据标签属性查找
print(bs.a['href'])

# (了解)删除标签属性
print(bs.a)
del bs.a['id']
print(bs.a.attrs)

# 标签内容
print(bs.a.string)

# 子节点和父节点
print(bs.body.contents)
print(bs.body.children)
for c in bs.body.children:
    print(c)

# 搜素
print(bs.find_all('a'))
print(bs.find_all(['a', 'h1']))

# 搜素 根据属性
print(bs.find(id='aaa'))
# 根据class
print(bs.find_all(class_='aaa'))
# 根据css选择器语法
print(bs.select('a'))
print(bs.select('.aaa'))
print(bs.select('#aaa'))
print(bs.select('body.aaa'))
