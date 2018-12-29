# 学生管理v1-函数封装
# 之前的非函数版本 打印学生列表代码重复，如果要修改需要处处修改。while if 嵌套，代码越来越长，不容易维护。所以我们封装成函数。



students = [{'name': '小明', 'age':10, 'sex': 'male'},{'name':'小红', 'age':12, 'sex':'female'},{'name':'小李', 'age':12, 'sex':'male'}]


def show_students():
    print('行号\t\t姓名\t\t年龄\t\t性别')
    print('---------------------------------------')
    for i in range(0, len(students)):
        student = students[i]
        print(i + 1, '\t\t', student['name'], '\t\t', student['age'], '\t\t', student['sex'])


def add_student():
    adda = {}
    a = str(input('请输入名字：'))
    adda['name'] = a
    b = int(input('请输入年龄：'))
    adda['age'] = b
    c = str(input('请输入性别：'))
    adda['sex'] = c
    students.append(adda)

def update_students():
    print('行号\t\t姓名\t\t年龄\t\t性别')
    print('---------------------------------------')
    for i in range(0, len(students)):
        student = students[i]
        print(i + 1, '\t\t', student['name'], '\t\t', student['age'], '\t\t', student['sex'])
    d = int(input('第几个：'))
    h = str(input('修改后的名字是：'))
    c = int(input('修改后的年龄是：'))
    j = str(input('修改后的性别是：'))
    k = students[d-1]
    k['name'] = h
    k['age'] = c
    k['sex'] = j
    print('修改成功')


def delete_students():
    print('行号\t\t姓名\t\t年龄\t\t性别')
    print('---------------------------------------')
    for i in range(0, len(students)):
        student = students[i]
        print(i + 1, '\t\t', student['name'], '\t\t', student['age'], '\t\t', student['sex'])
    print("""
                           删除 》请输入子操作编号
                           1） 按学生编号删除
                           2） 学生全部删除(谨慎)
                                 """)
    m = int(input('请选择子操作：'))
    if m == 1:
        v = int(input('删除第几个学生：'))
        students.pop(v - 1)
        print('删除成功')
    elif m == 2:
        d = str(input('确认全部删除？（Y/N）:'))
        if d == 'Y':
            students.clear()
        print('删除全部成功')



students = [{'name': '小明', 'age':10, 'sex': 'male'},{'name':'小红', 'age':12, 'sex':'female'},{'name':'小李', 'age':12, 'sex':'male'}]
def main():
    while True:
            print("""欢迎使用学员管理系统
    1-查询学员姓名
    2-添加学员姓名 
    3-修改学员姓名
    4-删除学员姓名
    0-退出程序""")

            num = int(input('请输入数字：'))
            if num == 1:
                show_students()
            if num == 2:
                add_student()
            if num == 3:
                update_students()
            if num == 4:
                delete_students()
            elif num == 0:
                print('谢谢使用')
                break
# main()
if __name__=='__main__':      # 这种写法含义将会在“包，模块”一节中介绍
    main()