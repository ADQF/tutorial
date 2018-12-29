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