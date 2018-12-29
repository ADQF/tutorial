# 类的继承

"""
引题：生活例子。手机类，OPPO手机、华为手机看做是手机类里的对象；但OPPO手机也可以称作一个类，这个类又包含find系列、R系列类，R系列类又包含了某某具体型号对象。类有包含、继承的关系。
"""

# 引题2：写一个教师类：属性name age sex salary subject address phone, 方法say_hi(), go_work().



class Student():
    def __init__(self, name, age, sex, salary, subject, address, phone):
        self.name = name
        self.age = age
        self.sex = sex
        self.salary = salary
        self.subject = subject
        self.address = address
        self.phone = phone

    def print_name(self):
        print('hello')

    def sada(self):
        pass

class Studet():
    def __init__(self, name, age, sex, salary, subject, address, phone):
        self.name = name
        self.age = age
        self.sex = sex
        self.salary = salary
        self.subject = subject
        self.address = address
        self.phone = phone

    def print_name(self):
        print('hello')

    def sada(self):
        pass

# 上面的代码类与相似的类有重复的属性、方法，书写麻烦。
# 所以Python引入了类继承机制。继承是类的三大特性之一。


class Animal(object):
    def __init__(self, name):
        self.name = name

    def rnm(self):
        print('动物再跑')

class Dog(Animal):
    pass

class Cat(Animal):
    pass

dog1 = Dog('臭臭')
dog1.rnm()
cat1 = Cat('小红')
cat1.rnm()

"""
父类：上例中Animal类逻辑上、范围上包含Dog、Cat类。那么我们把Animal类叫做
“父类”、“超类”、“基类”：Dog、Cat类就叫做“子类”、“衍生类”

继承：语法 类定义时，类名后面小括号里填写父类名。注意跟类实例化时、函数后面的小括号里的内容不一样

object:Python中变量、方法万物皆对象，现实生活也是万物皆对象。为了面向对象体系完整，定义了一个默认的、抽象的顶级对象object。object是所以类的父类。每一个类都默认继承object类，具备一些关于类的基础方法如__init____del__。

子类继承父类的属性、方法: Dog类实例化用的是父类Animal类中的__init__() run()。例如华为手机类拥有父类手机打电话，发短信功能。

场景：类比较多而且相似的时候，适合抽象为父类、子类，比如游戏。过度抽象可能会使问题更加复杂，不要刻意去使用父子类。

好处：类与类关系更加清晰：代码量少；公共部分抽象出来，扩展更方便。
"""
