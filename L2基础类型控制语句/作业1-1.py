# 用户输入
while True:
    kilometers = input('请输入公里:')
    kilometers = float(kilometers)


    # 计算费用
    cost = 0
    if 0 <= kilometers <= 2:
        cost = 8
    elif 12 >= kilometers > 2:
        cost = 8 + (kilometers-2) * 1.2
    elif kilometers > 12:
        cost = 20 + (kilometers - 12)*1.5
    else:
        print('数值不合法')
    # 输出费用

    print('花费一共' + str(cost) + '元')

