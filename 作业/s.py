import pymysql

# 打开数据库连接
db = pymysql.connect(host='127.0.0.1', port=3306,
                                 user='root',
                                 password='1770323960',
                                 db='jd',
                                 charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor
                                 )

# 使用cursor()方法获取操作游标
cursor = db.cursor()

# SQL 查询语句
cursor.execute("SELECT * FROM comment;")
print(cursor.fetchall())


# 关闭数据库连接
db.close()