06【python读取excel表格数据】

python操作excel主要用到xlrd和xlwt两个库，xlrd读取表格数据，支持xlsx和xls格式的excel表格；xlwt写入excel表格数据

一、python读取excel表格数据

# 1、读取excel表格数据常用操作

```python
import xlrd
 
# 打开excel表格
data_excel = xlrd.open_workbook('data/dataset.xlsx')
 
 
# 获取所有sheet名称
names = data_excel.sheet_names()
 
 
# 获取book中的sheet工作表的三种方法,返回一个xlrd.sheet.Sheet()对象
table = data_excel.sheets()[0]     # 通过索引顺序获取sheet
table = data_excel.sheet_by_index(sheetx=0)     # 通过索引顺序获取sheet
table = data_excel.sheet_by_name(sheet_name='Sheet1')    # 通过名称获取
 
 
# excel工作表的行列操作
n_rows = table.nrows    # 获取该sheet中的有效行数
n_cols = table.ncols    # 获取该sheet中的有效列数
row_list = table.row(rowx=0)    # 返回某行中所有的单元格对象组成的列表
cols_list = table.col(colx=0)    # 返回某列中所有的单元格对象组成的列表
 
 
# 返回某行中所有单元格的数据组成的列表
row_data=table.row_values(0,start_colx=0,end_colx=None)
 
 
# 返回某列中所有单元格的数据组成的列表
cols_data=table.col_values(0,start_rowx=0,end_rowx=None)
row_lenth=table.row_len(0)   # 返回某行的有效单元格长度
 
 
# excel工作表的单元格操作
row_col=table.cell(rowx=0,colx=0) # 返回单元格对象
row_col_data=table.cell_value(rowx=0,colx=0) # 返回单元格中的数据
```

# 2、xlrd模块主要操作

```python
import xlrd
 
  
""" 打开excel表格 """
workbook = xlrd.open_workbook("data.xlsx")
print(workbook)       # 结果：<xlrd.book.Book object at 0x000000000291B128>
 
 
""" 获取所有sheet名称 """
sheet_names = workbook.sheet_names()
print(sheet_names)     # 结果：['表1', 'Sheet2']
 
 
""" 获取所有或某个sheet对象 """
# 获取所有的sheet对象
sheets_object = workbook.sheets()
print(sheets_object)    # 结果：[<xlrd.sheet.Sheet object at 0x0000000002956710>,<xlrd.sheet.Sheet object at 0x0000000002956AC8>]
 
 
# 通过index获取第一个sheet对象
sheet1_object = workbook.sheet_by_index(0)
print(sheet1_object)    # 结果：<xlrd.sheet.Sheet object at 0x0000000002956710>
 
 
# 通过name获取第一个sheet对象
sheet1_object = workbook.sheet_by_name(sheet_name="表1")
print(sheet1_object)    # 结果：<xlrd.sheet.Sheet object at 0x0000000002956710>
  
 
""" 判断某个sheet 是否已导入"""
# 通过index判断sheet1是否导入
sheet1_is_load = workbook.sheet_loaded(sheet_name_or_index=0)
print(sheet1_is_load)    # 结果：True
 
 
# 通过sheet名称判断sheet1是否导入
sheet1_is_load = workbook.sheet_loaded(sheet_name_or_index="表1")
print(sheet1_is_load)    # 结果：True
  
 
""" 对sheet对象中的行执行操作 """
# 获取sheet1中的有效行数
nrows = sheet1_object.nrows
print(nrows)        # 结果：5
 
 
# 获取sheet1中第3行的数据
all_row_values = sheet1_object.row_values(rowx=2)
print(all_row_values)      # 结果：[3.0, 'b', 1, '']
 
row_values = sheet1_object.row_values(rowx=2, start_colx=1, end_colx=3)
print(row_values)        # 结果：['b', 1]
 
 
# 获取sheet1中第3行的单元对象
row_object = sheet1_object.row(rowx=2)
print(row_object)        # 结果：[number:3.0, text:'b', bool:1, empty:'']
 
 
# 获取sheet1中第3行的单元
row_slice = sheet1_object.row_slice(rowx=2)
print(row_slice)        # 结果：[number:3.0, text:'b', bool:1, empty:'']
 
 
# 获取sheet1中第3行的单元类型
row_types = sheet1_object.row_types(rowx=2)
print(row_types)        # 结果：array('B', [2, 1, 4, 0])
 
 
# 获取sheet1中第3行的长度
row_len = sheet1_object.row_len(rowx=2)
print(row_len)         # 结果：4
 
 
# 获取sheet1所有行的生成器
rows_generator = sheet1_object.get_rows()
print(rows_generator)      # 结果：<generator object Sheet.get_rows.<locals>.<genexpr> at 0x00000000028D8BA0>
  
 
""" 对sheet对象中的列执行操作 """
# 获取sheet1中的有效列数
ncols = sheet1_object.ncols
print(ncols)        # 结果：4
 
 
# 获取sheet1中第colx=1列的数据
col_values = sheet1_object.col_values(colx=1)
print(col_values)      # 结果：['测试', 'a', 'b', 'c', 'd']
 
col_values1 = sheet1_object.col_values(1, 1, 3)
print(col_values1)     # 结果：['a', 'b']
 
 
# 获取sheet1中第2列的单元
col_slice = sheet1_object.col_slice(colx=1)
print(col_slice)      # 结果：[text:'测试', text:'a', text:'b', text:'c', text:'d']
 
 
# 获取sheet1中第2列的单元类型
col_types = sheet1_object.col_types(colx=1)
print(col_types)      # 结果：[1, 1, 1, 1, 1]
  
 
"""对sheet对象中的单元执行操作"""
# 获取sheet1中第rowx=1行，第colx=2列的单元对象
cell_info = sheet1_object.cell(rowx=1, colx=2)
print(cell_info)      # 结果: text:'m'
print(type(cell_info))   # 结果：<class 'xlrd.sheet.Cell'>
 
 
# 获取sheet1中第rowx=1行，第colx=2列的单元值
cell_value = sheet1_object.cell_value(rowx=1, colx=2)
print(cell_value)      # 结果: m
 
 
# 获取sheet1中第rowx=1行，第colx=2列的单元类型值
cell_type = sheet1_object.cell_type(rowx=1, colx=2)
print(cell_type)      # 结果：1
  
#单元类型ctype：empty为0，string为1，number为2，date为3，boolean为4，error为5；
```

#  3、读取单元格内容为日期时间的方式

若单元格内容的类型为date，即ctype值为3时，则代表此单元格的数据为日期
xlrd.xldate_as_tuple(xldate, datemode)：若xldate数据为日期/时间，则将转化为适用于datetime的元组 ， 返回值为元组，格式为：(year, month, day, hour, minute, nearest_second)
xldate：sheet对象中单元格的数据
datemode：日期模式

```python
import xlrd
import datetime
  
 
""" 读取sheet对象中的日期 """
workbook = xlrd.open_workbook("data.xlsx")
sheet2_object = workbook.sheet_by_name("Sheet2")
 
 
# value_type = sheet2_object.cell(0, 1).ctype
value_type = sheet2_object.cell_type(0, 1)
print(value_type) # 结果：3 ，表示该值为date
 
 
if value_type == 3:
  print("单元格数据为日期")
  cell_value = sheet2_object.cell_value(1, 0)
  print(cell_value) # 结果：43567.0
 
  date_tuple = xlrd.xldate_as_tuple(cell_value, workbook.datemode)
  print(date_tuple) # 结果：(2020, 4, 12, 0, 0, 0)
 
  date_value = datetime.date(*date_tuple[:3])
  print(date_value) # 结果：2020-04-12
 
  date_format = date_value.strftime('%Y/%m/%d')
  print(date_format) # 结果：2020/04/12
```

# 4、读取合并单元格的数据

若表格为xls格式的，打开workbook时需将formatting_info设置为True，然后再获取sheet中的合并单元格；若表格有xlsx格式的，打开workbook时保持formatting_info为默认值False，然后再获取sheet中的合并单元格；

SheetObject.merged_cells：获取sheet中合并单元格的信息，返回值为列表；若sheet对象中无合并单元格，则返回值为空列表；列表中每个单元格信息的格式为：(row_start, row_end, col_start, col_end)； row_start表示合并单元格的起始行； row_end表示合并单元格的结束行； col_start表示合并单元格的起始列；col_end表示合并单元格的结束列；合并单元格的行取值范围为[row_start, row_end)，包括row_start，不包括row_end；合并单元格的列取值范围为[col_start, col_end)，包括col_start，不包括col_end；如：(1, 3, 4, 6)：表示从第1到2行合并，从第4到第5列合并；

读取合并单元格数据仅需merged_cells数据中的row_start和col_start这两个索引即可
```python
import xlrd
 
  
""" 获取合并的单元格并读取单元格数据 """
# 获取xlsx格式的excel文件中的合并单元格
workbook = xlrd.open_workbook("data.xlsx")
sheet2_object = workbook.sheet_by_name("Sheet2")
print(sheet2_object.merged_cells)  # 结果: [(1, 2, 0, 2), (3, 6, 0, 2)]
 
 
# 获取xls格式的excel文件中的合并单元格
workbook1 = xlrd.open_workbook("data.xls", formatting_info=True)
sheet2_object1 = workbook1.sheet_by_name("Sheet2")
print(sheet2_object1.merged_cells)  # 结果: [(1, 2, 0, 2), (3, 6, 0, 2)]
  
 
# 读取合并单元格数据（仅需“起始行起始列”即可获取数据）
print(sheet2_object.cell_value(1, 0))  # 结果：总结1
print(sheet2_object.cell_value(3, 0))  # 结果：总结2
 
 
# 或使用for循环获取所有的合并单元格数据
for (row_start, row_end, col_start, col_end) in sheet2_object.merged_cells:
    print(sheet2_object.cell_value(rowx=row_start, colx=col_start))
```

#  二、python写入excel表格数据

# 1、写入excel表格数据常用操作和格式设置

```python
import xlwt
  import datetime
  # 创建一个workbook 设置编码
  workbook = xlwt.Workbook(encoding='utf-8')
 
 
  # 创建一个worksheet
  worksheet = workbook.add_sheet('Sheet1')
  
 
  #字体样式设置
  style = xlwt.XFStyle()  # 初始化样式
  font = xlwt.Font()  # 为样式创建字体
  font.name = 'Times New Roman'
  font.height = 20 * 11  # 字体大小，11为字号，20为衡量单位
  font.bold = True  # 黑体
  font.underline = True # 下划线
  font.italic = True # 斜体字
  style.font = font # 设定样式
  
 
  # 数据写入excel,参数对应 行, 列, 值
  worksheet.write(0, 0, 'test_data') # 不带样式的写入
  worksheet.write(1, 0, 'test_data', style) # 带字体样式的写入
  
 
  # 设置单元格宽度
  worksheet.col(0).width = 3333
  
 
  #设置单元格背景颜色
  pattern = xlwt.Pattern()
  pattern.pattern = xlwt.Pattern.SOLID_PATTERN
  pattern.pattern_fore_colour = 13
  style = xlwt.XFStyle() # Create the Pattern
  style.pattern = pattern # Add Pattern to Style
  worksheet.write(2, 0, 'colour', style)
  
 
  #给单元格添加边框方法一
  borders = xlwt.Borders() # Create Borders
  borders.left = xlwt.Borders.DASHED  #DASHED虚线，NO_LINE没有，THIN实线
  borders.right = xlwt.Borders.DASHED #borders.right=1 表示实线
  borders.top = xlwt.Borders.DASHED
  borders.bottom = xlwt.Borders.DASHED
  borders.left_colour=0x40
  borders.right_colour = 0x40
  borders.top_colour = 0x40
  borders.bottom_colour = 0x40
  style = xlwt.XFStyle() # Create Style
  style.borders = borders # Add Borders to Style
  worksheet.write(3,0 , 'border1', style)
  
 
  #给单元格添加边框方法二
  # 细实线:1，小粗实线:2，细虚线:3，中细虚线:4，大粗实线:5，双线:6，细点虚线:7，大粗虚线:8，细点划线:9，粗点划线:10，细双点划线:11，粗双点划线:12，斜点划线:13
  borders = xlwt.Borders()
  borders.left = 1  #设置为细实线
  borders.right = 1
  borders.top = 1
  borders.bottom = 1
  borders.left_colour = 2 #颜色设置为红色
  borders.right_colour = 2
  borders.top_colour = 2
  borders.bottom_colour = 2
  style = xlwt.XFStyle() # Create Style
  style.borders = borders # Add Borders to Style
  worksheet.write(4, 0, 'border2', style)
  
 
  #输入一个日期到单元格
  style = xlwt.XFStyle()
  style.num_format_str = 'M/D/YY' # Other options: D-MMM-YY, D-MMM, MMM-YY, h:mm, h:mm:ss, h:mm, h:mm:ss, M/D/YY h:mm, mm:ss, [h]:mm:ss, mm:ss.0
  worksheet.write(5, 0, datetime.datetime.now(), style)
  
 
  #单元格添加计算公式
  worksheet.write(0, 1, 2) # Outputs 2
  worksheet.write(0, 2, 3) # Outputs 3
  worksheet.write(1, 1, xlwt.Formula('B1*C1')) # Should output "6" (B1[2] * B2[6])
  worksheet.write(1, 2, xlwt.Formula('SUM(B1,C1)')) # Should output "5" (B1[2] + C1[3])
  
 
  #向单元格添加一个超链接
  worksheet.write(0, 3, xlwt.Formula('HYPERLINK("http://www.baidu.com";"baidu")')) # Outputs the text "baidu" linking to http://www.baidu.com
  
 
  #单元格合并
  worksheet.write_merge(0, 0, 4, 5, 'First Merge')  #合并0行的4到5列
  worksheet.write_merge(1, 2, 4, 5, 'Second Merge') #合并1和2行的4到5列
  
 
  #设置单元格内容的对其方式
  alignment=xlwt.Alignment() ## Create Alignment
  alignment.horz=xlwt.Alignment.HORZ_CENTER
  alignment.vert=xlwt.Alignment.VERT_CENTER
  style=xlwt.XFStyle()
  style.alignment=alignment  # Add Alignment to Style
  worksheet.write(0, 6, 'alignment', style)
  
 
  # 保存文件
  workbook.save('data_test.xls')
```

2、字体颜色和背景颜色对应索引号字体颜色：font.colour_index背景颜色：pattern.pattern_fore_colour

![](https://img-blog.csdnimg.cn/img_convert/d090e02f44e1afff61b58828cbbcaa39.png)