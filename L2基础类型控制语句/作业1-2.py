# 用户输入
while True:
    results = input('请输入成绩')
    results = int(results)
    # 判断成绩
    if results < 0 or results > 100:
        print('数值不合法')
    else:
            if results < 60:
                print('不及格')
            else:
                print('及格')
            if 60 <= results < 70:
                print('D')
            elif 70 <= results < 80:
                print('C')
            elif 80 <= results < 90:
                print('B')
            elif 90 <= results <= 100:
                print('A')




# 显示结果