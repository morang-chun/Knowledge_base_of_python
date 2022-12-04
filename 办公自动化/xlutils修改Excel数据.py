import xlutils
import xlrd
from xlutils.copy import copy
# 打开Excel表格
read_book = xlrd.open_workbook('宿舍物品.xlsx')
# 复制数据
wb = copy(read_book)

# 选择表格
sh = wb.get_sheet(0)

# 增加数据：
sh.write(6,0,'小台灯')
sh.write(6,1,'1')

# 增加工作表
sh2 = wb.add_sheet('宿舍所有物品数据汇总')

# 创建一个计数器
count = 0
rs = read_book.sheet_by_index(0)
for i in range(1,rs.nrows):
    num = rs.cell_value(i,1)
    count += num

sh2.write(0,0,'宿舍物品汇总')
sh2.write(0,1,count)

# 保存修改的表格（新的表格）
wb.save('宿舍物品汇总表.xlsx')