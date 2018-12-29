# 主题：if语句

age = 19
if age > 18:
    print('年龄大于18是成人')
else:
    print('未成年')


score = 75
if score < 0 or score > 100:
    print('分数不合法')
if score < 60:
    print('不及格')
elif 60 <= score < 70:
    print('及格')
elif 70 <= score and score < 90:
    print ('良')
elif score >= 90:
    print('优秀')
else:
    pass



# 如果···， 那么···
# if<条件>:
#       条件为True或(非空的字符串，非空的列表，非0)后执行的语句
# 关键字if判断条件，为True执行代码块中的语句，False的时候不执行。

# if<条件1>:
#     条件一为true执行语句
# else:
#     不满足上面条件的时候执行的语句
# #
# 更多的选择分支
# if <条件1>:
#     ···
# elif <条件2>:
#     ···
# elif <条件3>:
#     ···
# ···
# else:
#     ···
#
# 从上到下判断各个条件，如果走一个分支，其他分支不会再走。
# 设计项目需要注意条件怎么去设计。
# 注意控制语句的嵌套层数不要超过四层。
#
# pase: 不执行实际功能，只是为了占位置


# 表达式： 一句代码。
# 语句块：后面的代码是从属于前面的一个语句。语法特点：一条语句，然后:有一个冒号，然后语句块可以缩进(4个空格或一个Tab)开始,语句块具有明显的层级关系。

# 缩进：python要求语句块强制缩进。必须为4个空格。tab和shift+tab调整代码缩进。
# 缩进错误会报错'tndentationError; unexpected indent'


# if语句的单行写法
def foo(num1, num2):
    # if num1 > num2:
    #     return num1
    # else:
    #     return num2
    return num1 if num1 > num2 else num2
print(foo(1, 2))
print(foo(2, 1))
# 类似其他语言中的三元表达式 c = a>b?1:0
# if else语句块写成单行模式：