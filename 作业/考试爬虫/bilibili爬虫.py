import requests
import json
from lxml import etree
import csv

l = []
for n in range(1, 11):
    comment_url = 'https://api.bilibili.com/x/web-interface/newlist'

    params = {
        # 'callback': 'jqueryCallback_bili_39533930546307805',
        'rid': '33',
        'type': '0',
        'pn': n,
        'ps': '20',
        # 'jsonp': 'jsonp',
        # '_': '1546830335139'
    }


    #
    headers = {
        'Cookie': '_uuid=CD8C3F83-F1E6-9592-F280-119B07E4594214080infoc; buvid3=5C8F8F00-708A-4EE4-96F4-6878408ABE5248801infoc; fts=1546831714; sid=a9o2xf4s; DedeUserID=250949143; DedeUserID__ckMd5=620c5966c69dab24; SESSDATA=d0cfb4a3%2C1549424241%2C78619211; bili_jct=694f8939e57e717c0633221a2d6e27ac',
    'Referer': 'https://www.bilibili.com/v/anime/serial/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36'
        }

    comment_resp = requests.get(url=comment_url, params=params, headers=headers)
    # print(comment_resp.status_code)
    comment_str = comment_resp.text
    comment_dict = json.loads(comment_str)
    # comment_dict = json.load('4js接口-京东评论-评论数据.json')
    data = comment_dict['data']
    archives = data['archives']
    with open('testwrite.csv', mode='w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
    f = []
    for archive in archives:
        # print(archive['pic'])
        # print(archive['title'])
        stat = archive['stat']
        # print(stat['view'])
        a = archive['pic']
        b = archive['title']
        c = stat['view']
        d = [a, b, c]
        # print(d)
        f.append(d)

    l.append(f)
print(l)
with open('bilibili.csv', mode='w', newline='', encoding='utf-8') as h:
    writer = csv.writer(h)
    for j in l:
        for row in j:
            writer.writerow(row)
