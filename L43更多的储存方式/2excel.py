# excel读写
# excel是一种广泛流传的办公文件格式，表格形式，比csv复杂一些，带一些功能样式，适合普通用户观看。由于带功能样式，所以需要专门的包负责解析。excel的后缀 老格式.xls 新格式.xlsx，新格式兼容老格式。
# 操作excel包选择 XlsxWriter xlrd pyexcel , start数、维护时间都较大同小异，下面以pyexcel讲解。

from pyexcel_io import save_data
from pyexcel_io import get_data

data = get_data('2readfile.xlsx')
print(type(data))
sheet1 = data['Sheet1']
print(sheet1)
for index, row in enumerate(sheet1):
    if index <= 0:
        continue
    print('第{}个学生，学生姓名{}'.format(index, row[1]))
