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

for i in range(3):
    # 生成子线程
    t = threading.Thread(target=run, args=('t{}'.format(i),))
    t.setDaemon(True)
    t.start()

# 主线程
time.sleep(1.5)     # time.sleep(1) 时结果有时打印'2s'有时没有,可以看出多线程对同一份资源操作时可能出现问题。
print(threading.active_count())     # 3+1   这个例子看出线程执行不同的工作

"""
输出结果：
task t0
task t1
task t2
2s
2s
2s
4
"""

# t.join()    # 主线程阻塞，让子线程先运行完，失去线程并发意义，但更容易研究一些线程的表现。
# t.setDaemon(True)   # 主线程结束后没运行完的子线程跟着结束