# 生成器
"""
实际上平时一直在使用生成器
例如 range() jieba.cut()

语法特点：yield生成项：next(生成器对象)  得到一次返回值，每次生成的值会保存到生成器对象中，下一次调用next
"""

def c(n):
    print('c..')
    while n < 4:
        yield n
        print('increment', n)

