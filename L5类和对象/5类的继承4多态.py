# 多态
class Animal(object):
    def __init__(self, name):
        self.name = name

    def run(self):
        print('动物再跑')


class Cat(Animal):
    def run(self):
        print('猫再跑')


class Dog(Animal):
    def run(self):
        print('狗再跳')
# 1 > 不同的类实例化，实例在调用自己的方法
# cat1 = Cat()
# dog1 = Dog()
# cat1.run()
# dog1.run()

# 2 > 把上面的语句封装成函数


def arty1_run(class_instance):
    class_instance.run()


cat1 = Cat('')
dog1 = Dog('')
arty1_run(cat1)
arty1_run(dog1)

"""
多态：一段已写好业务逻辑代码，传入的实例不同，最终运行出的代码也跟着变化。一种程序可以有多种运行状态，这就是多态。
多态是类的三大特性之一。
好处：代码灵活
"""