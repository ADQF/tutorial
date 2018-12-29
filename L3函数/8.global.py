#
# (老写法 total是全局变量)从1 加100和
# totnl = 0
# for i in range(1, 101):
#     totnl = totnl +i
# print(totnl)

## glodal 显示声明变量为全局变量
# tota1 = 0
# def add1():
#     global tota1
#     tota1 = tota1 + 1
#
# add1()
# add1()
# add1()
# print(tota1)


# (了解)nonlocal
# def outer():
#     num = 10
#     def inner():
#         nonlocal num
#         num = 100
#         print(num)
#     inner()
#     print(num)
# outer()