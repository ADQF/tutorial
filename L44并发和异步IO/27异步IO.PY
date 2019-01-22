def coroutine(c):
    time.sleep(10)
    c.switch()
    c.register(name=c, signal='Done')
    yield resp

if __name__ == '__main__':
    c1 = coroutine()
    c2 = coroutine()
    c3 = coroutine()

    next(c1)
    next(c2)

    while True:
        if event_list:
            respl = c1.send()
            save_img(respl.content)

