students = [
    {'name': '小明', 'age': 10, 'sex': 'male'},
    {'name': '小红', 'age': 12, 'sex': 'female'},
    {'name': '小李', 'age': 12, 'sex': 'male'}
]

class Student():
    @classmethod
    def show_students(cls):

        print("行号", '\t\t', "姓名", '\t\t', "年龄", '\t\t', "性别")
        print("----------------------------------------------")
        for i in range(0, len(students)):
            print(i + 1, '\t\t\t',students[i]['name'], '\t\t', students[i]['age'], '\t\t', students[i]['sex'])

    def __init__(self, name,age,sex):
        self.name = name
        self.age = age
        self.sex = sex

    def add_students(self):
        my_dict = {}
        my_dict['name'] = self.name
        my_dict['age'] = self.age
        my_dict['sex'] = self.sex
        students.append(my_dict)

    def update_students(self):

        students[d -1]['name'] = self.name

        students[d - 1]['age'] = self.age

        students[d-1]['sex'] = self.sex
        print("修改完毕！")

    def delete_students():

        if h == 1:
            j = int(input("要删除第几个学生？："))
            students.pop(j - 1)
            print("删除完毕。")
        elif h == 2:
            confirm = input("确定删除所有（Y/N)")
            if confirm == 'y' or confirm == 'Y':
                students.clear()
                print("删除完毕。")



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
        Student.show_students()
    elif num == 2:
        name = input('新的学生姓名')
        age = input('新的学生年龄')
        sex = input('新的学生性别')
        stu2 = Student(name, age, sex)
        stu2.add_students()
    elif num == 3:
        d = int(input('要修改第几个学生信息'))
        e = input('修改后的学生姓名')
        f = input('修改后的学生年龄')
        g = input('修改后的学生性别')
        stu1 = Student(e,f,g)
        stu1.update_students()
    elif num == 4:
        print("""
                          删除>请输入子选项:
                              1> 按序号删除
                              2> 全部清空
                          """)
        h = int(input("请选择选项输入对应序号："))


        Student.delete_students()
    elif num == 0:
        break
# 1. 不要过度使用@classmethod

