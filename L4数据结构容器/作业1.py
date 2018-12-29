list1 = ['小红', '小明', '小区', '小吴', '小白']
list2 = ['小红', '小明']
def ara (list1):
    if len(list1) >= 5:
        return list1[:2]
    else:
        return None

# 调用 不同参数传入方式
print(ara(list1=list1))
print(ara(['小红', '小明', '小区', '小吴', '小白']))
print(ara(list1=['小红', '小明', '小区', '小吴', '小白']))
print(ara(list1=list2))




list1 = ['小红','小明','小区','小吴','小白']
list2 = []
def cd(list1):
    for i in range(len(list1)):
        list2.append(list1[1::2])
        return list2[0]
print(cd(list1))

stu_list = ['小红', '小明', '小区', '小吴', '小白']
new_list = []

def fn2(stu_list):
    for i in range(0, len(stu_list)):
        if i % 2 == 1:
            print(stu_list[i])
            new_list.append(stu_list[i])
    return new_list

print(fn2(stu_list))

