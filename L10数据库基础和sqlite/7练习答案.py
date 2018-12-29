# 学生管理v4 sqlite版
import sqlite3

def create_table():
    connect = sqlite3.connect("testsqlite.db")
    cursor = connect.cursor()
    cursor.execute("""
        CREATE TABLE students
        (
            id integer PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            sex TEXT,
            age INTEGER,
            phone TEXT
        );
    """)
    connect.commit()
    cursor.close()
    connect.close()

def show_students():
    """
    展示学生列表
    """
    print('行号\t\t姓名\t\t性别\t\t年龄\t\t电话')
    print('--------------------------------')
    connect = sqlite3.connect("testsqlite.db")
    cursor = connect.cursor()
    cursor.execute("""
        SELECT * FROM students;
    """)
    student_list = cursor.fetchall()    # [(1,小明,), ()]

    for index, student in enumerate(student_list):
        print(f'{index+1}\t\t{student[1]}\t\t{student[2]}\t\t{student[3]}\t\t{student[4]}')
    cursor.close()
    connect.close()


def add_student():
    name = input('新学生姓名：')
    sex = input('新学生性别：')
    age = input('新学生年龄：')
    phone = input('新学生电话：')

    connect = sqlite3.connect("testsqlite.db")
    cursor = connect.cursor()
    # sql = """
    #     INSERT INTO students (name, sex, age, phone) VALUES ("%s", "%s", %s, "%s");
    # """ % (name, sex, age, phone)
    sql = f"""
        INSERT INTO students (name, sex, age, phone) VALUES ("{name}", "{sex}", {age}, "{phone}");
    """
    print(sql)
    cursor.execute(sql)
    connect.commit()
    connect.close()

    print('学生添加成功')

def update_student():
    # 数据库设计 应该多一列 学生编号。id列面向数据库为了安全不适合向用户展示。行号每一次不固定。
    stu_name = input('要修改哪个学生？学生姓名：')
    new_phone = input('修改后的学生电话：')

    connect = sqlite3.connect("testsqlite.db")
    cursor = connect.cursor()
    # 先查询输入的学生是否存在，存在的话更新，不存在的给出用户提示
    sql = f"""
        SELECT 1 FROM students WHERE name="{stu_name}";
    """
    cursor.execute(sql)
    student = cursor.fetchall()
    if student:
        sql2 = f"""
                UPDATE students SET phone="{new_phone}" WHERE name="{stu_name}";
            """
        # print(sql2)
        cursor.execute(sql2)
        connect.commit()
    else:
        print('学生姓名不存在，请重新操作。')
    connect.close()

    print('学生修改成功')

def delete_student():
    sub_select = input("""
    删除>请选择删除子操作
    1.按学生姓名删除
    2.全部删除
    """)
    if sub_select == '1':
        stu_name = input('要删除的学生姓名：')
        """ delete from students where name='{stu_name}'  """
    elif sub_select == '2':
        """ delete from students;"""
        confirm = input('要删除全部学生？（Y/N）:')
        if confirm == 'Y':
            # cursor.execute()
            pass

def main():
    # 主函数，程序入口
    while True:
        print("""
            欢迎使用学生管理系统
            1-查看学员姓名
            2-添加学员姓名
            3-修改学员姓名
            4-删除学员姓名
            0-退出程序
            """)

        num = int(input('请输入操作编号：'))

        if num == 1:
            show_students()
        elif num == 2:
            add_student()
        elif num == 3:
            update_student()
        elif num == 4:
            delete_student()
        elif num == 0:
            break

if __name__ == '__main__':
    # create_table()
    main()



# 可能出现的错误：
# 插入功能
# sql = """
#         INSERT INTO students (name, sex, age, phone) VALUES (%s, %s, %d, %s);
#     """ % (name, sex, int(age), phone)
#     print(sql)
# 报错 sqlite3.OperationalError: no such column: aaa
# 原因 sql INSERT INTO students (name, sex, age, phone) VALUES (aaa, nan, 13, 13000);   值并不是sql解释器理解的字符串。
# 解决 %s两侧加引号。 INSERT INTO students (name, sex, age, phone) VALUES ("%s", %s, %d, %s) % (name, sex, int(age), phone);

# sql补充
# SELECT 1 FROM students WHERE name="{stu_name}";    -- 只关心一行数据是否存在。效率比select * 高。

