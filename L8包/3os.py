# os
# os包： IOS macOS , operate system 操作系统。主要负责新建文件、改文件名、路径、操作电脑系统相关的功能。是一个内置包。os包实质调用的是windows上的编程接口。

import os
# from os import path, open
# from os import *

# 1>os.path.exists  判断是否存在文件
print(os.path.exists('1包引用.py'))    # True
print(os.path.exists('text.txt'))       # False
# 2> 重命名
# os.rename('aaa.txt', 'bbb.txt')
# 3> 删除文件
# os.remove('bbb.txt')
# 4> 创建文件夹  make directory
# os.mkdir('aaa')
# 5> 列出当前文件夹下的文件， 相当于cmd中dir命令、linux ls。
# os.listdir()
# 6> 切换当前文件夹  change ，相当于cmd中的cd命令
# os.chdir('aaa')
# 在cmd中尝试dir、cd命令
# 7> 获取当前工作目录路径  get work directory
print(os.getcwd())


# 相对路径和绝对路径(针对资源管理器路径)
# 绝对路径：从盘符或项目根目录写出每一层目录层级到文件。D:\PycharmProjects\tutorial\L8包\3os.py   。优点是准确，缺点写起来麻烦。
# 相对路径： .当前目录     ..表示父目录
# 相对3os.py而言， ./1包引用.py       L8包/1包引用.py    ../L7本地文件读写/xx.py
# 相对路径的优点写起来比较短，整个文件夹路径变化时里面的文件路径不用修改。缺点是容易写错、没有绝对路径准确。

# 表示目录层级斜杠：windows上 | 反斜杠， macOS linux 用的是/ 正斜杠。python解释器会把字符串中的反斜杠认为是转义字符,导致出错。
# 解决方案：
# 1. 反斜杠变成正斜杠 'D:/PycharmProjects/tutorial/L8包/3os.py'
# 2. 使用转义字符输出反斜杠 'D:\\PycharmProjects\\tutorial\\L8包\\3os.py '

# >8  （常用）拼接路径,获取脚本的绝对路径
print(os.path.join(os.getcwd(), '3os.py'))
# >9  返绝对路径  absolute
print(os.path.abspath('./1包引用.py'))
os.path.abspath(os.path.join(os.getcwd(), '3os.py'))
# >10 判断是否路径
print(os.path.isdir('aaa'))

# linux系统上操作可能需要权限


## 作业：使用绝对路径打开 L7/chinese_utf8.txt
with open('D:/PycharmProjects/tutorial/L7本地文件读写/chinese_utf8.txt', 'r',encoding='utf8') as f:
    content = f.read()
    print(content)