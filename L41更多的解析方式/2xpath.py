# xpath
# 先转文档树再解析  需要lxml包
html = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8" />
    <title>lxml中xpath的用法</title>
</head>
<body>
    <ul>
        <li><a href="https://www.baidu.com" class="first_a">百度一下</a></li>
        <li><a href="https://mail.qq.com" id="second_a">QQ邮箱</a></li>
        <li><a href="https://www.taobao.com">淘宝网</a></li>
        <li>
            <a href="https://pypi.python.org" class="first_a">Python官网</a>
            <a href="https://pypi.python.org" class="second_a">Python</a>
        </li>
    </ul>
    <p class="one">first_p_tag</p>
    <p id="second">second_p_tag</p>
    <div class="one">
        first_div_tag
        <p class="first second third">11111111</p>
        <a href="#">22222222</a>
    </div>
</body>
</html>
"""

from lxml import etree

# etree对象 字符串互转
# html = etree.parse('index.html')
# rs = etree.tostring(html)

# 把html字符串转etree对象
html = etree.fromstring(html)
print(html)

# / 表示从文档顶层开始匹配 / body/ul/li
# //表示匹配标签，目标标签前可能有多级父节点  //li

# 搜索a标签
# etree.xpath(xpath表达式） 返回列表，每一项都是元素对象
print(html.xpath('//a'))  # [<Element a at 0x1358b7a6d08>,,]

# 提取标签属性值
# xpath 表达式  //标签查找/@属性名

# 获取标签内容
# //查找标签/text()
print(html.xpath('//a/text()'))
print(html.xpath('//a/@href'))

# 获取标签内容
# //查找标签/text()
print(html.xpath('//a/text()'))
# html.xpath('/body/ul/li/a/text()')

# 查找时根据属性限制标签
# 待查标签[@属性名 = 属性值]
# print(html.xpath('//ul/li/a[@id="second_a"/text()'))

# (了解）包含条件
# contains(@class,"class值")  适合没有id、name属性class属性多种情况
print(html.xpath('//div[@class="one"]/p[contains(@class,"first")]/text()')[0])

# //查询下一级节点，省略中间的层级
print(html.xpath('//ul//a[@class="first"]'))

# 根据css语法

# etree对象 字符串互转
# html = etree.parse('index.html')
# rs = etree.tostring(html)
