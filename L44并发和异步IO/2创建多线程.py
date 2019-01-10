# 创建多线程

# import _thread        #  多线程底层操作包，主要使用threading包
# 创建多线程：方式一 threading.Thread() 生成线程实例然后运行     方式二  class xxx(Thread):  def run() 继承父类重写run方法。

import threading
import time

def run(n):
    """ 倒计时 """
    print('task', n)
    time.sleep(1)
    print('2s')
    time.sleep(1)
    print('1s')
    time.sleep(1)
    print('0s')
    time.sleep(1)

# run(99)     # 单线程运行，忽略参数，是一个普通的计时器功能函数。

t1 = threading.Thread(target=run, args=('t1'))
t2 = threading.Thread(target=run, args=('t2',))
t1.start()
t2.start()




# 复习：函数的引用、调用
# def foo():
#     print('hello')
#
# foo() # 调用
#
# a = foo # 引用
# a()

# 复习：元组写法
# a = (1) # 错误
# type(a)    # <class int>
# a = (1,)
# len(a)  # 1
# type(a)     # <class tuple>


