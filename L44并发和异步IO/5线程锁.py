# 线程锁
# 线程共享进程中的公共资源（execution context），但会导致一些不可以预料的错误。例如不同人对同一个git仓库中的文件进行修改，就会出现冲突。

# 下面是一个多线程公用同一份资源导致错误的例子。
import threading
import time

num = 100

def sub():
    global num
    temp = num
    time.sleep(0.001)
    num = temp - 1

l = []
for i in range(100):
    t = threading.Thread(target=sub)
    t.start()
    l.append(t)

for t in l:
    t.join()    # 子线程执行完再执行主线程，确保执行100次sub函数

print(num)


"""
打印结果80-90不等。每次运行结果不确定，因为有些线程同时启动，同时读取公共变量num，有的线程计算的是100-1，有的计算的98-1，执行一次后的结果相互覆盖，导致最终结果不正确。
"""
