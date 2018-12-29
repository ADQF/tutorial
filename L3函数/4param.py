# 参数 、
# 不需要参数的函数


def mydey():
    print('起床')
    print('打算')
    print('饿')


mydey()
# 一个参数的函数


def calculate_area(r):
    print('圆面积', 3.14 * r * r)


calculate_area(3)


def calculate_absolute(num):
    if num < 0:
        return-num
    if num > 0:
        return num


print('绝对值',calculate_absolute(5))
print('绝对值',calculate_absolute(-3))
print(abs(-3))

# (了解)常用的内置之一
# 多个参数的函数


def get_max_min(a, b, c):
    max_num = a
    max_min = a
    if b > max_num:
        max_num = b
    if c > max_num:
        max_num = c

    if b < max_min:
        max_min = b
    if c < max_min:
        max_min = c

    return max_num, max_min


num1, num2 = get_max_min(1,2,3)
print('最大值{},最小值{}'. format(num1, num2))
# 参数：函数运行前需要告诉函数一些运行时需要的信息原料、数值，函数根据传入的参数，参与内部的逻辑运算。
# 形参：函数定义的时候。占位、将要传进数值的“形式上的代表”。形参名可变，我们只关注形参的类型。
# 实参：函数调用的时候。传入函数的“实际具体数值”。注意实参的值，要与形参的个数、类型保持一致。
# 可能出现的错误：实参和形参个数或类型不一致报错。
