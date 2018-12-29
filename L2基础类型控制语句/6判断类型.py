# 判断变量类型

# 类型不同，input()返回字符串
# '1' + 3      '小明考了'+90   报错

# type()   判断变量类型
a = 1
b = 1.5
c = 'hello'
d = True
type(a)     #<class 'int'>
type(b)     #<class 'float'>
type(c)     #<class 'str'>
type(d)     #<class 'bool'>


score = input('请输入成绩：')
int(score)

# isinstance()   判断类型是否一致
isinstance(1, int) # True
isinstance(1, float) # false
isinstance('小明', float) # False