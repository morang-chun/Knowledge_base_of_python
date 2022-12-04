import xlwt
# 创建一个工作簿
wb = xlwt.Workbook()

# 在工作簿中创建表
sh = wb.add_sheet("物品存量")
list1= ['牙刷','杯子','香水','眼罩','护发精油']
list2 = [2,4,2,2,1]

# 写入数据到单元格
sh.write(0,0,'物品名称')
sh.write(0,1,"存量")


for i in range(len(list1)):
    pro = list1[i]
    sh.write(i + 1, 0,pro)

for a in range(len(list2)):
    count = list2[a]
    sh.write(a+1,1,count)
wb.save('宿舍物品.xlsx')