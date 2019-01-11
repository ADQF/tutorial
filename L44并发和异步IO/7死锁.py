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

""""
# 既然用户程序已经自己有锁了，那为什么C python还需要GIL呢？加入GIL主要的原因是为了降低程序的开发的复杂度，比如现在的你写python不需要关心内存回收的问题，因为Python解释器帮你自动定期进行内存回收，你可以理解为python解释器里有一个独立的线程，每过一段时间它起wake up做一次全局轮询看看哪些内存数据是可以被清空的，此时你自己的程序 里的线程和 py解释器自己的线程是并发运行的，假设你的线程删除了一个变量，py解释器的垃圾回收线程在清空这个变量的过程中的clearing时刻，可能一个其它线程正好又重新给这个还没来及得清空的内存空间赋值了，结果就有可能新赋值的数据被删除了，为了解决类似的问题，python解释器简单粗暴的加了锁，即当一个线程运行时，其它人都不能动，这样就解决了上述的问题，这可以说是Python早期版本的遗留问题。
"""
