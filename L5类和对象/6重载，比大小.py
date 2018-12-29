# 重载
# 重写参考L5/5类的继承2.py一节

# 引题：写几个关于比大小的函数。
# 1> 给定两个数，返回最大的那个数
# 2> 给定三个数，返回最大的那个数
# 3> 传入数字组成的列表[1, 0, -1, 3.5], 返回最大的那项数字


def get_max1(num1, num2, num3, num4):
    max = num1
    if num2 > max:
        max = num2
    if num3 > max:
        max = num3
    if num4 > max:
        max = num4
    return max
print(get_max1(111, 222, 333, 888))



def get_m1(num1, num2, num3):
    if num1 < num2 > num3:
        return num2
    elif num1 < num3 > num2:
        return num3
    else:
        return num1
print(get_m1(10, 8, 15))

def get_max3(num_list):
    max = num_list[0]
    # for x in range(0, len(num_list)):
    #     if max < num_list[x]:
    #         max = num_list[x]
    for index, num in enumerate(num_list):
        print(index, num)
        if num > max:
            max = num
    return max

num_list = [1, 0, -1, 3.5]
print(get_max3(num_list))

class GetMaxNum(object):
    @staticmethod
    def get_max1(num1, num2):
        max = num1
        if num2 > max:
            max = num2
        return max

    @staticmethod
    def get_max2(num1, num2, num3):
        max = num1
        if num2 > max:
            max = num2
        if num3 > max:
            max = num3
        return max

    @staticmethod
    def get_max3(num_list):
        max = num_list[0]
        for index, num in enumerate(num_list):
            print(index, num)
            if num > max:
                max = num
        return max

print('最大值', GetMaxNum.get_max1(1, 3))
print('最大值', GetMaxNum.get_max2(1, 3, 2))
print('最大值', GetMaxNum.get_max3([1, 2, 3]))


"""
重写：子类重写父类中的同名方法。
重载：类中有多个同名方法，参数个数不同，或参数类型不同，这种情况叫重载。针对方法参数的不同状况。

Python当中没有重载机制。同名函数重复定义，以最后的为准。因为Python是动态类型语言，传实参什么类型都接收；形参和实参可以穿可变个数的参数。
"""