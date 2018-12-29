tnt = input('请随便输入点什么:')
alpha_num = 0
space_num = 0
digit_num = 0
cud = 0
for i in tnt:
    if i.isalpha():
        alpha_num += 1
    # print(tnt.count('True'))
    elif i.isspace():
        space_num += 1
    # print(tnt.count('True'))
    elif i.isdigit():
        digit_num += 1
    # print(tnt.count('True'))
    else:
        cud += 1
    # print(tnt.count('True'))
print('字母：{}\n空格：{}\n数字：{}\n字符：{}' .format(alpha_num, space_num, digit_num, cud))
