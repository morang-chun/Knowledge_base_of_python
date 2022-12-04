import xlrd
# 打开表格
wb = xlrd.open_workbook('宿舍物品.xlsx')

# 查看工作簿中的工作表情况
print(f'excel中有{wb.nsheets}个工作表')
print(f'excel中sheet的名字:{wb.sheet_names()}')

# 选择工作簿
# 方法一：通过表的名字来选择
sh1 = wb.sheet_by_name('物品存量')
# 方法二：通过sheet_by_index()传入表的位置参数就可以
sh2 = wb.sheet_by_index(0)

# 查看表格里面的数据情况
print(f'sheet里面一共有{sh1.nrows}行{sh2.ncols}列')

# 获取单元格里面的值
# 一共有4种方法：
print(f'第一行第一列的数据：{sh1.cell_value(0,0)}')
print(f'第一行第一列的数据：{sh1.cell(0,0).value}')
print(f'第一行第一列的数据：{sh1.row(0)[0].value}')
print(f'第一行第一列的数据：{sh1.col(0)[0].value}')

# 获取整行或列的数据
print(sh1.row_values(0))
print(sh1.col_values(0))

# 遍历所有的数据
for r in range(sh1.nrows):#遍历行
    for c in range(sh1.ncols):#遍历列
        print(f'第{r}行 第{c}列的数据是：{sh1.cell_value(r,c)}')
for i in sh1.row(0):
    print(i.value)  # 获取单元格数据
for i in sh1.col(0):
    print(i.value)
