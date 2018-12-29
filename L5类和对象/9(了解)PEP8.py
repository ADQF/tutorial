# (了解)PEP8代码风格指导

"""
PEP8 意思 Python官方第8号文件，这个文件说明了Python语言代码应该这么书写，指导了书写风格。当你的代码没有做到文件要求的时候，pycharm会报灰线轻度提示。没有完全遵守规则不影响代码执行。但建议遵守。
"""



# 操作符前后应该有一个空格
a=3
b = 3
# 方法与方法间有两个空行
def foo():
    pass


def boo():
    pass
# 类中的方法相隔一行
class S(object):
    def foo(self):
        pass

    def boo(self):
        pass

# 类与类之间空两行
# 如果没有父类不写括号
# 类名应该用驼峰风格
class aaa():
    pass


class Bbb:
    pass
# 方法名、类名不要重复使用
def boo():
    pass
# 两个条件有时可以写成链式
if 1 < a and a < 2:
    pass
if 1 < a < 2:
    pass
# 不建议代码写的过长，80个字符。pycharm的提示灰线在120个字符
print('哒哒gggggggggggggggggggggggggggggggggggggggggg'
 'gggggggggggggggggggggggggggggggggggggggg多多')
# 文件末尾代码时另起一新行
print('end')















