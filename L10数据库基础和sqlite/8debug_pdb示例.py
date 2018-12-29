# pdb包示例
# import pdb      # python debug包
# def test(arg):
#     pdb.set_trace()     # 设置跟踪
#     for i in range(arg):
#         print(i)
#     return arg
#
# pdb.run("test(3)")

"""
断点：debug运行到某一句代码时暂时停住。一句一句向下执行太慢，我们只需要在可能出现问题的代码前设置断点。
1. 打断点。运行程序
2. (Pdb)模式下 输入 “c" 回车，程序会执行到第一个断点处。 信息提示，运行到第几行，在哪个函数哪个文件下。
3. (Pdb)模式下 输入 “s" 回车,向下执行一句代码
4. (Pdb)模式下 输入 “a" 回车,查看相关变量的值。

debug好处：代码一句一句执行，不断查看变量的值，为编程提供信息支持。
pdb缺点：打断点不方便，命令行调试不方便。
"""

"""
为了使debug更加方便，pycharm提供了图形化工具。
1. 编辑器左侧行号区域，单击设置断点
2. 以debug模式运行。
"""

def test2(arg):
    for i in range(arg):
        print(i)
    return arg
# test2(10)

def test3():
    test2(10)
    print('world')
    print('world')
    print('world')
test3()

"""
可能出现的错误：
1. no  module pytest      。 CPython错误。
pip install pytest
或重装python解释器
2. win32 错误
pip install pywin32
最好安装主流操作系统   win7x64 win10x64
"""