# 需求：软件需要有退出功能。循环中达到我们想要的条件时退出。节省计算机资源。
# 循环的中断

while True:
    s = input('请输入字符：')

    if s == 'quit':
        break

    print('你输入的字符长度是：{}'.format(len(s)))

print('完')

#break: 退出循环，跳出循环语句块。
# len(对象)：返回对象的长度。