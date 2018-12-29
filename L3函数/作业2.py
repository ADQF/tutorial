# 第1题
def factorial(i):
    if i == 0:
        return 0
    return factorial(i - 1) + i
print(factorial(100))


# 第4ti
def factorial(x):
    x = int(x)
    if x == 1 or x == 2:
        return x
    return factorial(x-1)+factorial(x-2)
print(factorial(20))

# 1、1、2 、3 、5 、8 、13 、21 、34

# 10 = (10-1)+(10-2) =


list1 = ['小明', '小红']
for i in range(1, 100):
    list1.append(i)
print(list1)
