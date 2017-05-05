# -*- coding: utf-8 -*-

'''
python操作excel主要用到xlrd和xlwt两个库
即xlrd是读取excel，xlwt是写excel库，可以解析微软.xls和.xlsx；两种格式表格
'''
import xlrd,xlwt,os
os.chdir(r'C:\Users\jk\Desktop\Python学习\每日一学习\5月')

# 如何读取一个excel文件
file_name = '计算机科学与技术学院.xlsx'
rdata = xlrd.open_workbook(file_name)
print(type(rdata))  # <class 'xlrd.book.Book'>
'''
我们用open_workbook这个函数打开一个excel文件，
并返回一个rdata对象，我们type一下发现data是:
xlrd这个模块下面的book文件下面的Book类的实例对象
'''

# 获取表格的基本信息
print('sheets nums:',rdata.nsheets)   # 返回表格中sheet文件的个数
print('sheets names:',rdata.sheet_names())  # 返回每个sheet文件的名字

# 每个sheet的行列总数，比如第一个sheet
sheet1 = rdata.sheet_by_index(0)  # 第一个sheet文件
print('rows:',sheet1.nrows)  # 返回第一个sheet文件的行数
print('cols:',sheet1.ncols)  # 返回第一个sheet文件的列数

# 获取行、列对象
# 获取第一行的内容
sh1 = rdata.sheet_by_index(0)
print(sh1.row(0))  #　获取第一个sheet文件的第一行内容
print(sh1.row_values(1)) #　返回的是列表对象，中文会转成的unicode显示
print(sh1.col(1))   # 获取第二列的内容，返回的是列表对象，text表示是文本对象,number是数字
print(sh1.col_values(1))  # 返回第一列的数值
# 这里可以利用列表切片访问，第二列到第五列
print(sh1.col_values(1)[1:5])
# 也可以利用默认的col_values参数
# col_values(self, colx, start_rowx=0, end_rowx=None)
print(sh1.col_values(1,1,5))

# 获取单元格cell的内容 xlrd对excel里面内容分成下面7种的,是枚举类型
(
    XL_CELL_EMPTY,
    XL_CELL_TEXT,
    XL_CELL_NUMBER,
    XL_CELL_DATE,
    XL_CELL_BOOLEAN,
    XL_CELL_ERROR,
    XL_CELL_BLANK, # for use in debugging, gathering stats, etc
) = range(7)
# 看下第一行第一列的单元格是个字符串
sh1 = rdata.sheet_by_index(0)
cell_0_0 = sh1.cell(0,0)
print(cell_0_0,cell_0_0.ctype,cell_0_0.value)
# 第二行第一列的单元格
cell_1_0=sh1.cell(1,0)

# 写数据进表格
# 创建一个wbook对象，生成一个新的sheet
wbook = xlwt.Workbook()
wsheet = wbook.add_sheet(sh1.name)

# 在写入第一行，标题栏
# wsheet这个函数(row,col,value,style),这个style其实就是这个内容单元格的格式
style=xlwt.easyxf('align: vertical center, horizontal center')
wsheet.write(0,0,u'时间',style)
wsheet.write(0,1,u'人数1',style)
wsheet.write(0,2,u'人数2',style)
wsheet.write(0,3,u'总分',style)

# 写成文件new_data.xls
try:
    wbook.save('new_data.xls')
except Exception as e:
    print(e)
else:
    print('write excel file successful')
