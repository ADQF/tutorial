import sqlite3


class Student(object):

    def __init__(self, id, name, age, sex, phone):
        self.id = id
        self.name = name
        self.age = age
        self.sex = sex
        self.phone = phone


class Studentmanager(object):

    def __init__(self):

        self.db_path = 'test.db'
        self.connect = None
        self.cursor = None

    def connect_sql(self):

        self.connect = sqlite3.connect(self.db_path)
        self.cursor = self.connect.cursor()

    def close_sql(self):
        self.connect.commit()
        self.cursor.close()
        self.connect.close()

    def create_table(self):

        self.connect_sql()
        sql = "create table if not exists student (id integer primary key ,name char not null ,age int,sex char ,phone char )"
        self.cursor.execute(sql)
        self.close_sql()

    def add(self):
        id = int(input("请输入添加的学号:"))
        name = input("请输入添加的姓名:")
        age = int(input("请输入添加的年龄:"))
        sex = input("请输入添加的性别:")
        phone = input("请输入添加的手机号码:")

        stu = Student(id, name, age, sex, phone)
        self.insert_sql(stu)
        print('添加成功')

    def insert_sql(self, stu):
        self.connect_sql()
        sql = "INSERT INTO student (id,name,age,sex,phone)VALUES({},'{}',{},'{}','{}')".format(stu.id, stu.name,
                                                                                               stu.age, stu.sex,
                                                                                               stu.phone)
        self.cursor.execute(sql)
        self.close_sql()

    def update_sql(self):

        self.connect_sql()
        id = input("请输入要修改的学号：")
        sql = 'SELECT COUNT(*),id,name,age,sex,phone FROM student WHERE id={}'.format(id)
        result = self.cursor.execute(sql)
        for i in result:
            if i[0] == 0:
                print(" 您输入的学号不存在，请重新输入： ")
            else:
                name = input('*      请输入修改后的姓名（{}）：'.format(i[2]))
                age = input('*       请输入修改后的年龄 ({}):'.format(i[3]))
                sex = input('*       请输入修改后的性别 ({}):'.format(i[4]))
                phone = input('*     请输入修改后的号码  ({}):'.format(i[5]))

                sql = "UPDATE student SET name='{}',age={},sex='{}',phone='{}' WHERE id={}".format(name, age, sex,
                                                                                                   phone, id)
                self.cursor.execute(sql)
                self.connect.commit()

    def delete_sql(self):
        self.connect_sql()
        print('输入b根据学号删除')
        print('输入a删除所有信息')
        select = input('请输入您的选项：')

        while select != 'a' and select != 'b':
            select = input('输入不合法，请重新输入：')
        if select == 'a':
            is_del = input('是否删除所有信息？y/n:')
            if is_del == 'y':
                sql = "delete * from student"
                self.cursor.execute(sql)
                self.connect.commit()
        else:
            self.select_sql()
            while True:
                id = int(input('请输入要删除的学号：'))
                is_del = input('是否删除当前学生信息？d/l:')
                if is_del == 'd':
                    sql = "delete from student where id ={}".format(id)
                    self.cursor.execute(sql)
                    # self.connect.commit()
                    self.close_sql();
                    print('删除成功！')
                return

    def select_sql(self):
        print('行号\t\t学号\t\t姓名\t\t年龄\t\t性别\t\t电话')
        print('--------------------------------')
        self.connect_sql()
        sql = "select * from student"
        sql_list = self.cursor.execute(sql)
        a = 0
        for i in sql_list:
            a += 1
            print(a, '\t\t', i[0], '\t', i[1], '\t', i[2], '\t', i[3], '\t\t', i[4], )

    # for id,name,age,sex,phone in sql_list:
    #     print(id,'\t',name,'\t',age,'\t',sex,'\t',phone)


    def option(self):
        print("*  1添加学员")
        print("*  2修改学员")
        print("*  3删除学员")
        print("*  4查询学员")
        print("*  0退出")


    def run(self):
        self.create_table()
        while True:
            self.option()
            select = int(input('选择您的操作：'))
            if select < 0 or select > 4:
                print('输入有误 请重新输入：')

            elif select == 1:
                self.add()

            elif select == 2:
                self.update_sql()

            elif select == 3:
                self.delete_sql()

            elif select == 4:
                self.select_sql()
            else:
                print('感谢您的使用，下次再会！')
                break


if __name__ == '__main__':
    s = Studentmanager()
    s.run()


"""
sql 补充
1. 表不存在的话创建，存在就不创建。if not exists 
create table if not exists student (id integer primary key ,name char not null ,age int,sex char ,phone char )
"""