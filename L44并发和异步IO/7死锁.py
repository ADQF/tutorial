# 死锁
# 加锁后还可能出现一种特殊情况。线程A和线程B互相需要等待对方资源，只能一个一个的借用，结果一人拿到了一半，都干等着不运行。

import threading, time

class X (threading.Thread):
    def run(self):
        c = C.acquire(True)
        if c:
            print(self.name + '拿到一半资源了')

            time.sleep(1)
            g = G.acquire(True)
            if g:
                print(self.name + '拿到另一半资源了')
                G.release()
            C.release()
            print(self.name + '拿到全部资源了')

class H (threading.Thread):
    def run(self):
        g = G.acquire(True)
        if g:
            print(self.name + '拿到另一半资源了')

            time.sleep(1)
            c = C.acquire(True)
            if c:
                print(self.name + '拿到一半资源了')
                C.release()
            G.release()
            print(self.name + '拿到全部资源了')

if __name__ == '__main__':
    C = threading.RLock()
    G = threading.RLock()

    t1 = X()
    t2 = H()
    t1.start()
    t2.start()

"""
运行程序，结果卡死。两人都拿到了一个资源，但第二个资源都在对方手里，但由于自己的功能未完成，导致自己拿的资源没释放。两个线程并不聪明，不会把自己的资源先借给对方，而是两方一直等待对方。

避免这种情况发生，改为递归锁。threading.Lock()改为threading.Rlock()
"""
"""
既然用户可以在代码中自由加锁控制，确保线程安全，那么为什么还有GIL？
因为GIL处于解释器层面，轮询查看有没有待销毁的垃圾，相当于执行某一项功能的线程。如果垃圾回收功能的线程跟代码功能的线程混在一块，容易出现数据冲突和安全问题，所以发明者分开设计了。
整体流程详见 8线程整体示意图.png
"""