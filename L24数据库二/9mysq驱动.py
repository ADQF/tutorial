# mysql驱动
# 引题：已经学习了sql语法，sqlite驱动操作sqlite数据库，datagrip的jdbc java驱动操作mysql。所以我们要找python操作的mysql驱动
"""
驱动选择：
1. MySQLDB。 已经有C驱动mysql的成熟包。Mysqldb和python对这个C驱动包封装。优点是效率高，py2环境和众多项目中使用。
缺点
"""
import pymysql.cursors

connection = pymysql.connect(host='127.0.0.1',
                             port=3306,
                             user='root',
                             password='1770323960',
                             db='test',
                             # charset='utf-8mb4',
                             # sursorclass=pymysql.cursors.DictCursor
                             )

try:
    with connection.cursor() as cursor:
        sql = """ SELECT * FROM shirt; """
        cursor.execute(sql)
        result = cursor.fetchall()
        print(result)
        for row in result:
            print('小红有一件{}色的{}'.format(row[2], row[1]))

    # with connection.cursor() as cursor:
    #     sql = """ INSERT INTO shirt values (%s, %s, %s, %s)"""
    #     affected_rows = cursor.execute(sql, (None, '裙子', '绿', 2))
    #     print(affected_rows)
    # connection.commit()
except Exception as e:
    print(e)
finally:
    connection.close()





