# 递归 recursion
# 非递归写法
# total = 1
# for i in range(1, 11):
#     total = total * i
# print(total)

# 换一种思路
# 例如计算 5!
# 5! = (1*2*3*4) *5 = 4! * 5
# 4! = (1*2*3) *4 = 3! * 4
# 3! = 2!*3  2! = 1! * 2
# 所以 5! = (((1!*2)*3)*4)*5
# 所以 n! = (n-1)! * n      n >= 1
# 结论：f(n) = f(n-1) * n     n >= 2

def factorial(n):
    if n == 1:
        return 1
    return factorial(n-1) * n


print(factorial(5))

# 分析，当f(5)开始调用时
# 表达式变化为 第一次函数返回值 f(4) * 5
# 表达式变化为 第二次 (f(3)*4)* 5
# 表达式变化为 第三次 ((f(2)*3)*4) * 5
# 表达式变化为 第四次 (((f(1)*2)*3）*4) * 5
# 表达式变化为 第五次 (((1*2)*3)*4) * 5

# 可能出现的错误：超过最大的递归深度 RecursionError: maximum recursion depth exceeded
# 递归深度：递归需要函数调用自身，调用一次递归函数实际会调用多次函数，没调用一次深度加1，都会增加系统内存开支，所以python搞定了最大深度998
# 递归思维分析问题一般步骤：1.找函数调用自己的规律。2.找参数偏移规律。3.找跳出条件.
# 递归好处，个别问题用循环难以解决，递归思维教自然可以方便解决。
# 应用场景：目录树
"""
dirnamel  1      None   level1
name2     2      1      level2
name3     3      1      level3
name4     4      2      level4
"""