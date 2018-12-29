# open() 更多模式

"""
open()第二个参数mode模式：
'r' ，read  读取信息
'w' , write  写信息
'rb' , read byte  读取字节信息
'wb' , write byte  写字节信息

"""

with open('8write.txt', 'w', encoding='utf8') as f:
    f.write('hello\n')
    f.write('你好\n')
    f.write('天天开心\n')
    f.write('站的好吗')

with open('8write.txt', 'w', encoding='utf8') as f:
    f.write('你好开心啊\n')

"""
w 写模式，每一次打开文件写信息，会将之前的信息覆盖掉。
"""

with open('8write.txt', 'a', encoding='utf8') as f:
    f.write('天天开心\n')

"""
a 模式append，打开文件并追加写入信息。
r+ 打开文件用于读写。
ab 追加写二进制信息。
"""








