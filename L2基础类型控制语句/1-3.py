a = int(input('输入一个数'))
b = int(input('输入一个数'))
c = int(input('输入一个数'))
f = a
if b > f:
    f = b
if c > f:
    f = c

print('最大值',f)


def get_max(a, b, c):
    max_num = a
    if b > max_num:
        max_num = b
    if c > max_num:
        max_num = c

    return max_num

max_unmber = get_max(a, b, c)
print('最大值', max_unmber)