# # 循环中断之continue

while True:
    s = input('随便输入点什么：')
    a = len(s)
    if a < 3:
        print('太短了，请输入三个以上字符的内容。')
        continue

    print('你输入的内容是：{}，长度是{}'.format(s, a))

# continue: 中断一次循环，但没有跳出循环语句块，下次循环正常

# sty = 'runood'
# len(sty
#             # 字符串长度

