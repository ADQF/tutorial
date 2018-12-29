# 类的补充内容和高阶知识
# 1 判断类型
a = 1
b = 'sdq'
class S():
    pass
c = S()
d = True

print(type(a)) # <class 'int'>
isinstance(a, int)      # True 。 int是一个内置类
# 学过类后对这两个函数更加理解。type()返回的是类型。
# isinstance()   判断第一个参数是不是第二个参数的实例。

# 2 @property装饰器，语法糖getter setter函数，具体见 2私有属性.py一节
# 3 diy() directory文件目录，列出一个类中的所有方法，返回列表。
class Animal(object):
    def __init__(self, name):
        self.name = name

    def run(self):
        print('动物再跑')
    def __str__(self):
        return ''

print(dir(Animal))        # ['__class__', '__delattr__', ……，'__weakref__', 'run']
# 4 形如__xxx___这些名字的函数都有特殊用途。
# __class__ 类自己  __doc__文档  __repr__ __str__类名信息

# 5 slot
# 由于Python是动态语言，类在运行的时候可能会被攻击添加新的属性存放恶意信息，导致安全问题。__slots__ = (属性1，属性2 …)确定了类中可以有哪些属性，在程序运行时，往类中添加属性，如果新添加的属性不在__slost__定义当中，就会报错。从而确保类属性不能被随意修改，确保安全。
class S():
    __slots__ = ('name', 'score')
    def __init__(self, name, score):
        self.name = name
        self.score = score

xiaoming = S('小明', 59)
xiaoming.score = 80
xiaoming.score1 = 'eca1("python xx.py")'
print(xiaoming.score1)

# 6 多重继承
# 一个子类具备多个父类的特征
class Animal(object):
    pass
class Cartoon(object):
    pass
class Dog(Animal):
    pass
class HelloKitty(Animal, Cartoon):      # 有几个父类写几个，逗号分隔
    pass

# 7 枚举类（课下搜索）
# Enum
# 8 基类（课下搜索 了解）
# 基类是生成普通类的类，它是普通类的爸爸。
# 9 软件设计模式（课下搜索 了解）
# https://www.cnblogs.com/microsoft-zyl/p/6279176.html
# 工厂模式、单例模式
# 面试题：什么是单例模式？用python实现一个单例模式。


























































































