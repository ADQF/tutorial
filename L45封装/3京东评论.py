# 京东评论写数据库
import requests
import json
from lxml import etree
import pymysql.cursors
import time


def get_comments(product_id=None, page=None, page_size=10):
    """
    取评论
    :return: [[id,username,score,], []]或 [{'id':123123, 'username': 'zzdxyz', 'score': 5}]
    """
    comment_url = 'https://sclub.jd.com/comment/productPageComments.action'

    params = {
        'productId': product_id,  # 商品id。先写死 苹果手机。
        'score': 0,
        'sortType': 5,
        'page': page,
        'pageSize': page_size,
        # 'callback': 'fetchJSON_comment98vv15261',
        # 'isShadowSku': 0,
        # 'fold': 1
    }

    # 伪造headers。 降低被封禁的概率。
    # cookie中有jsessionid和trackid和用户名等信息。referer请求前的页面地址。useragent浏览器标识。
    headers = {
        'cookie': '__jdu=1545965016566122167306; shshshfpa=91aaa0e4-7924-2ea5-1870-d0d653119b3f-1545965018; user-key=2e7a62ce-3569-47af-96f7-f8992f90722b; cn=0; __jdv=122270672|google|1111US|CPC|not set|1545965056641; unick=jd_176382uon; pin=jd_6d66c1bd51468; _tp=pBQJkiA7r%2BIY%2FhF%2FquydSDVy0R12L6v1XMNhEko7v%2BM%3D; _pst=jd_6d66c1bd51468; PCSYCityID=412; mt_xid=V2_52007VwMWV1lQVV4eSR5YAmADEVFdX1RYHk4pVQxhChBSXV9OUxweGEAANFdCTg0PAF8DSB4PATJQElZfWVZTL0oYXAx7AxFOXlFDWh5CHVUOYwAiUm1YYlgdSB1eBWEHFGJfXFNe; ipLoc-djd=1-72-4137-0; areaId=1; shshshfpb=vWY4pLrc3hhHfFHANk%2BPsTg%3D%3D; shshshfp=f2e3aaa6ac280d409f682075e6afc812; _gcl_au=1.1.2092516447.1545981775; __jda=122270672.1545965016566122167306.1545965017.1545995113.1546499133.4; __jdc=122270672; wlfstk_smdl=ef4r0muh5yg22ha0n8qadnmvof5r8oom; cid=NXhENTk2Nm1ZOTU4N2hCNTM2OHNLMTk4MWFKMjc2MmVQOTU4M2RWMTk0NG1aMTMw; thor=1F192C4506D4DB5F1A3E92FD905CDD534B53EA2E892A760FA59A8AFF26762A578371DD10754BA106515677E71E06E5C29B97592E0DD1D2032D1BDC08C5B881D8835C9FC022CC38F954FB70E93D0DD4D2B92FFA5A68F1CD99A13ED8A1447302E5EF069B81C1B43F0B727FDB4B13C01231F43357F40302CA0939EA765EDD18030A8B70D828EF087C9BABF6B4517BE036553D8FAA705BECE333E5E7ABE60459EFAF; pinId=im3RPgaRtzCc8aZ5IRnsRbV9-x-f3wj7; ceshi3.com=000; 3AB9D23F7A4B3C9B=E6WHA67OFAKMK3AGOERHNLWBOBPVRXWH4KBLVQTDYFKTHBEHTSOT2R6TDQQOWFEXRJ37LY6GYGGHQWCBCSUF6KBGXI; __jdb=122270672.7.1545965016566122167306|4.1546499133',
        'referer': 'https://item.jd.com/100000287113.html',
        'user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36'
    }

    comment_resp = requests.get(url=comment_url, params=params, headers=headers)
    print(comment_resp.status_code)
    comment_str = comment_resp.text

    comment_dict = json.loads(comment_str)
    # comment_dict = json.load('4js接口-京东评论-评论数据.json')
    comments = comment_dict['comments']

    result_list = []
    for comment in comments:
        result_list.append({
            'id': comment['id'],
            'content': comment['content'],
            'creation_time': comment['creationTime'],
            'score': comment['score'],
            'nickname': comment['nickname'],
            'product_color': comment['productColor'],
            'product_size': comment['productSize']
        })

    return result_list


def save_db(comments):
    """
    :param: comments: {list} [{'id':123123, 'content':'物美价廉东西不错', },{}]
    :return: affected_rows : {int} 成功写入的行数
    """
    connection = pymysql.connect(host='127.0.0.1', port=3306,
                                 user='root',
                                 password='1770323960',
                                 db='jd',
                                 charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor
                                 )
    affected_rows = 0  # 成功计数

    for comment in comments:  # 循环评论
        cursor = connection.cursor()  # 创建游标
        # 先判断一下是否已存储过
        sql1 = "select id from comment where comment_id=%s " % (comment['id'])
        cursor.execute(sql1)
        rs_set = cursor.fetchone()  # 有值返回{'id':23} 无值返回None
        if rs_set:
            print('这条评论已存在在数据库中')
            continue
        # 不存在的写入数据库
        # 写法一： 参数为列表或元组  占位符 %s
        # sql2 = """
        # insert into comment (comment_id, content, creation_time, score, nickname, product_color, product_size)
        # values (%s, %s, %s, %s, %s,   %s, %s,)
        # """
        # 注意不要在拼sql的时候通过python字符串格式化（% .formate f''）传参，应该cursor.execute(args=)传参。
        # cursor.execute(sql2, args=(comment['id'], comment['content'], ...))     # 参数为列表或元组

        # 写法二：参数为字典
        sql2 = """
        insert into comment (comment_id, content, creation_time, score, nickname, product_color, product_size)
         values (%(id)s, %(content)s, %(creation_time)s, %(score)s, %(nickname)s,   %(product_color)s, %(product_size)s)
        """
        affected_row = cursor.execute(sql2, args=comment)
        if affected_row:
            print('本条评论插入成功')
            affected_rows += affected_row

        # 写法三：批量插入，拼sql
        # 写法四：批量插入，用现成方法executemany
    connection.commit()
    return affected_rows


if __name__ == '__main__':
    product_id = 100000287113  # 先写死，固定为一个商品下的评论
    page_amount = 10  # 爬取总页数，注意不要传给get_comments()函数导致每次请求固定的一页
    page_size = 10  # 每页10条评论
    time_sleep = 2

    for page in range(0, page_amount):
        comments_list = get_comments(product_id, page, page_size)
        affected_rows = save_db(comments=comments_list)
        print(f'成功写入{affected_rows}')
        time.sleep(2)

    print('Done')
"""
报错：
1. id int默认4字节太短  应该bigint
2. content中有单引号导致拼出的sql错误，应该在cursor.excute
sql = 'insert into comment (comment_id, content) values (%s, %s);' % (111232, '物美价廉')
sql = 'insert into comment (comment_id, content) values ({}, {});'.format(111232, '这个商品'太好'了！')
'insert into comment (comment_id, content) values (111232, '这个商品'太好'了！');'导致报错
cursor.execute(sql)
所以参数应该在cursor.execute(sql, args=(111232, '这个商品'太好'了！'))
3. indent error 缩进错误。  怀疑sql三引号中有一个空格，换行后变为5个空格。
"""

"""
批量插入：
 原始sql：insert into comment (comment_id, content) values (111232, '这个商品"太好"了！'),(111233, '不错') ,(111234, '还可以');
方法一.手动拼sql思路，伪代码。
sql = 'insert into comment (comment_id, content) values '
for comment in comments:
    sql += '('
    sql += comment['id']
    sql += comment['content']
    sql += ')'
    sql += ','
cursor.execute(sql)
方法二. 手动拼比较麻烦容易出错，所以用现成的 cursor.executemany()
sql = 'insert into comment comment_id, content) values (%s, %s)'
cursor.executemany(sql, args=[(111232, '这个商品"太好"了！'), (111233, '不错'),(111234, '还可以')])
"""