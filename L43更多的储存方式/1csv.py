# csv
# csv 一种逗号分隔的简单语法的一种类似表格的文件储存结构。远比数据库简单，比excel也简单。
# 场景：备份数据，适合非电脑专业人士观看。
# 准备： 新建 testexcel.xlsx excel文档，编辑几行学生信息，另存csv格式。用sublime打开excel文件发现是字节信息，打开csv文件是文本信息。

import csv

# 读取数据
file_path = 'D:\\testcsv.csv'
with open(file_path) as f:
    reader = csv.reader(f)
    result = tuple(reader)
    print(result[0][1])

datas = [
    ['编号', '姓名', '年龄'],
    ['1', '小明', '13'],
    ['2', '小红', '10'],
    ['3', '小青', '80']
]
with open('testwrite.csv', mode='w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    for row in datas:
        writer.writerow(row)











with open('D:\\testcsv.csv') as f:
    lines = f.readlines()
    for line in lines:
        line.split(',')
