# 综合项目：京东评论情感化分析

import pymysql
import pymysql
from wordcloud import WordCloud

# 1 从数据库把所有用户评论查出
def get_comments():
    db = pymysql.connect(host='127.0.0.1',
                                 port=3306,
                                 user='root',
                                 password='1770323960',
                                 db='jd',
                                 charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor
                                 )
    cursor = db.cursor()

    # SQL 查询语句
    cursor.execute("SELECT * FROM comment;")
    a = cursor.fetchall()
    for i in a:
        print(i['content'])

    # 连接数据库
    # 读表
    # select content from
    return [{}, {}]

def process_comments():
    stu_dict['name']
    # 所有用户评论拼成一个长字符串
    return ''

def cut_word(string):
    # 分词 ，返回wordcloud包使用的格式
    string
    ['手机', '好', '质量', '手机']

    return '手机 好 质量 手机'

def word_cloud(string):
    # 生成词云，保存到本地
    pass
    return None

def gen_pei():
    # 生成饼状图
    # select  count()  group by
    # 本地生成饼状图
    pass

# 1 查所有用户评论内容
# 2 所有用户评论拼成一个长字符串
# 3 长字符串用jieba分词
# 4 拼成wordcloud使用的结构，生成评论高频关键字词云。
# 5 pygal 根据用户productcolor 统计比例，查询pygal 饼状图文档。
get_comments()