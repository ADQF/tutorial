import requests
import json
import time
import requests
from lxml import etree
import pymysql
from wordcloud import WordCloud
import csv
import jieba

with open('tb_comments_1.json', encoding='utf-8') as f:
    commentsa = json.load(f)
    # print(comments)
rateDetail = commentsa['rateDetail']
rateList = rateDetail['rateList']

result_list = []
for rateLis in rateList:
    print(rateLis['rateDate'])
    print(rateLis['rateContent'])
    rateContent = rateLis['rateContent']
    print(rateLis['id'])
    print(rateLis['auctionSku'])
    result_list.append(rateContent)
    # 'appendComment': rateLis['appendComment'],
    rateDate = rateLis['rateDate']
    # rateContent = rateLis['rateContent']
    id = rateLis['id']
    auctionSku = rateLis['auctionSku']

    db = pymysql.connect(host='127.0.0.1', port=3306,
                         user='root',
                         password='1770323960',
                         db='taobao'
                         )

    cursor = db.cursor()


    cursor.execute("INSERT INTO comments VALUES (comment_id, rate_date, append_content, action_sku)")

    db.close()

