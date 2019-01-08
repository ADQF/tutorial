import requests
from lxml import etree
import pymysql

for a in range(16):
    url = 'https://guofeng.yuedu.163.com/yc/category/7/'.format(a)     # 这里写网址
    a = requests.get(url)
    x = a.text
    # print(x)
    for i in range(1, 31):
        xpath1 = '//*[@id="page-163-com"]/div[2]/div[3]/div/div[2]/div[2]/div/div[2]/table/tbody/tr[{}]/td[2]/div[1]/a/text()'.format(i)
        xpath2 = '//*[@id="page-163-com"]/div[2]/div[3]/div/div[2]/div[2]/div/div[2]/table/tbody/tr[{}]/td[3]/text()'.format(i)
        xpath3 = '//*[@id="page-163-com"]/div[2]/div[3]/div/div[2]/div[2]/div/div[2]/table/tbody/tr[{}]/td[4]/text()'.format(i)
        xpath4 = '//*[@id="page-163-com"]/div[2]/div[3]/div/div[2]/div[2]/div/div[2]/table/tbody/tr[{}]/td[5]/text()'.format(i)
        xpath5 = etree.HTML(x)
        books = xpath5.xpath(xpath1)[0]
        author = xpath5.xpath(xpath2)[0]
        num = xpath5.xpath(xpath3)[0]
        time = xpath5.xpath(xpath4)[0]

        print(books)
        print(author)
        print(num)
        print(time)
        connect = pymysql.Connect(host='127.0.0.1', port=3306, user='root', password='123', db='new_schema')
        cursor = connect.cursor()
        cursor.execute("insert into book(书名,作者,字数,更新时间) values ('{}','{}','{}','{}')".format(books,author,num,time))
        connect.commit()
        cursor.close()
        connect.close()

