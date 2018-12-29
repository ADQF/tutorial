print( '第1题')
for x in range(1,5):
        print('*****')

print( '第2题')
for x in range(1, 11):
    for y in range(1, x+1):
        print('*', end='')
    print()
#
# print( '第3题')
# for x in range(1, 10):
#     for y in range(1, x+1):
#         print(y, end='')
#     print()
#
# print( '第4题')
total = 0
for i in range(1, 101):
    total = total + i
print(total)
#

# print( '第5题')
# total = 1
# for i in range(1, 11):
#     total = total * i
# print(total)
#
# # 非递归解法
# a = 1*2*3*4*5*6*7*8*9*10
# print(a)
#
# print( '第6题')
# total = 0
# for i in range(1, 1001, 2):
#     total = total + i
# print(total)
#
# print( '第7题')
# n = int(input('请输入整数'))
# if n > 1:
#     for i in range(2, n):
#         if n % i == 0:
#             print('不是质数')
#             break
#     else:
#         print('是质数')
#
# print( '第8题')
# total = 0
# for i in range(10000, 99999+1):
#     b5 = i // 10000
#     b4 = (i - b5*10000) // 1000
#     b3 = (i - b5*10000 - b4*1000) // 100
#     b2 = (i - b5 * 10000 - b4 * 1000 - b3*100) // 10
#     b1 = (i - b5 * 10000 - b4 * 1000 - b3 * 100 - b2*10)
#     if b5 == b1 and b4 ==b2:
#         total += 1
#         print(i)
# print(total)
#
# print( '第9题')
# for i in range(100, 999+1):
#     b3 = i // 100
#     b2 = (i - b3 * 100) // 10
#     b1 = (i - b3 * 100 - b2 * 10) // 1
#     if b3 ** 3 + b2 ** 3 + b1 ** 3 == i:
#         print(i)
#
# # 解法2
# for x in range(1, 10):
#     for y in range(0, 10):
#         for z in range(0, 10):
#             num = x * 100 + y * 10 + z
#             if x ** 3 + y ** 3 + z ** 3 == num:
#                 print(num)



print('1  ''1  ', end='')
a = 1
b = 1

for i in range(3, 30):
    c = a + b
    print(c, '  ', end='')
    a = b
    b = c



