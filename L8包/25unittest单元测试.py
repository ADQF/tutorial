# 单元测试
# 优点：提前暴露问题 。缺点：跟业务逻辑代码重复，额外代码量，麻烦。单元测试的逻辑如果测试不出来问题。极限值的考虑不一定正确。所以建议中小型项目，时间充足的话建议写，时间紧张公司不要求的话做好黑盒测试。


# 待测试函数
# 需求 通过，访问字典中的键
# student = {'name': '', 'age': 13}
# name = student['name']
# student.name

class Dict(dict):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError('Dict 对象没有属性{}'.format(key))

    def __setattr__(self, key, value):
        self[key] = value

# student_dict = Dict(**{'name': '小明', 'age': 13})
# # print(student_dict.name)


# 开始单元测试

import unittest

# 类名以test开头
class TestDict(unittest.TestCase):
    def test_init(self):
        stu = Dict(name='小明', age=13)
        self.assertEqual(stu.name, '小明')
        self.assertEqual(stu.age, 13)
        self.assertTrue(isinstance(stu, dict))

    def test_key(self):
        d = Dict()
        d['key'] = 'value'
        self.assertEqual(d.key, 'value')

    def test_attr(self):

        d = Dict()
        d.key = 'value'
        self.assertTrue('key'in d)
        self.assertEqual(d['key'], 'value')

    def test_keyerror(self):
        d = Dict()
        with self.assertRaises(E):
            print('')