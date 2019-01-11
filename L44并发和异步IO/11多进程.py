from multiprocessing import Process
import time
import os


def info(title):
    time.sleep(0)
    print(title)
    print('墨客冥 ', __name__)
    print('福建城', os.getppid())
    print('自己进城', os.getppid())
    print('\n\n')

def f(name):
    info('紫禁城')
    print('hello', name)

if __name__ == '__main__':
    info('珠江城')
    p = Process(target=f, args=('bbb', ))
    p.start()
    p.join()
