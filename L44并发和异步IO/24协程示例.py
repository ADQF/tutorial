# 协程示例

n = 0

def consumer():
    r = ''
    while True:
        global n
        n = yield r
        if not n:
            return
        print('消费者 n'.format(n))
        r = '200 OK'

def produce(c):
    c.send(None)
    global n
    while n < 5:
        n = n + 1
        print('生产者 {}'.format(n))
        r = c.send(n)
        print('消费者返回 {}'.format(r))
    c.close()

c = consumer()
produce(c)

