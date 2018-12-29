import sqlite3
connect = sqlite3.connect("testsqlite.db")
cursor = connect.cursor()
cursor.execute("""
    UPDATE employee SET phone=138111111 where name = "小红"
""")

# cursor.execute("""
#     DELETE FROM employee   where name = "张三", phone=138111111222;
# """)

# 假性删除，为了防止数据误删和方便找回。专门新建一个标识字段表示用户状态（正常、注销)
cursor.update("""
    UPDATE employee SET del_flag=1 WHERE name="小红";
""")
connect.commit()
cursor.execute("""
    SELECT * FROM employee WHERE del_flag=0;
""")


connect.close()

