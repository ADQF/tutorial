class Robot():
    population = 0

    def __init__(self, name):
        self.name = name
        Robot.population += 1

    def say_hi(self):
        print('机器人姓名:{}'.format(self.name))

    # 1 类方法装饰器
    @classmethod
    def how_many(cls):
        print('机器人数:', cls.population)
    # 静态方法装饰器
    # @staticmethod
    # def how_many():
    #     print('机器人数:{}', Robot.population)

    # 3对象方法     不推荐这种写法
    # def how_many(self):    # 不推荐这种写法
    #     print('',Robot.population)

    def die(self):
        Robot.population -= 1

ROD1 = Robot('XR-01')
ROD1.say_hi()
# ROD1.how_many()
Robot.how_many()
ROD2 = Robot('XR-02')
Robot.how_many()
ROD2.die()
Robot.how_many()
# Robot.how_many()