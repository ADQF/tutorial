def ara (student_list):
    print("""
    欢迎使用学员管理系统
    1-查询学员姓名
    2-添加学员姓名 
    3-修改学员姓名
    4-删除学员姓名
    0-退出程序
    """)
    while True:
        num = int(input('请输入数字：'))
        if num == 1:
            print('行号\t\t姓名')
            print('--------------------')
            for i in range(0, len(student_list)):
                print(i+1, '\t\t', student_list[i])
        elif num == 2:
            a = str(input('请输入名字：'))
            student_list.append(a)
        elif num == 3:
            print('行号\t\t姓名')
            print('--------------------')
            for i in range(0, len(student_list)):
                print(i + 1, '\t\t', student_list[i])
            d = int(input('第几个：'))
            c = str(input('请输入修改后的名字：'))
            student_list[d - 1] = c
            print('修改成功')
        elif num == 4:
            print('行号\t\t姓名')
            print('--------------------')
            for i in range(0, len(student_list)):
                print(i + 1, '\t\t', student_list[i])
            print("""
            删除 》请输入子操作编号
            1） 按学生编号删除
            2） 学生全部删除(谨慎)
                  """)
            m = int(input('请选择子操作：'))
            if m == 1:
                v = int(input('删除第几个：'))
                student_list.pop(v - 1)
                print('删除全部成功')
            elif m == 2:
                student_list.clear()
                print('删除成功')
        elif num == 0:
            print('谢谢使用')
            break

ara(['小红', '小明', '小区', '小吴', '小白'])