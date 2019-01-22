# yield和协程

import time

def coroutine(task):
    print('start')
    time.sleep(5)
    print('end')
    yield 'a'

if __name__ == '__main__':
    c1 = coroutine('c1')
    c2 = coroutine('c2')

    next(c1)
    next(c2)

"""
coroutine 方法的yield并不像上个例子在循环中为了生成一个序列，而是为了
1. 从子方法跳回到main方法中
2. 上节例子一个生成器对象，不断next取值。生成了多个生成器对象
"""
