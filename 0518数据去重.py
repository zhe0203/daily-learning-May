import pandas as pd
import os
os.chdir(r'C:\Users\jk\Desktop\诸葛兼职\051623-350')
frame = pd.read_excel(r'成立日期(完成).xls')
# newframe = frame[~frame[['Stkcd','Accper']].duplicated()]
frame.to_excel('分类.xls')

# 生成季度时间序列
date_1 = pd.date_range('2006-06-30', end='2009-12-31', freq='Q')
print(list(date_1))

frame = pd.read_excel(r'模型数据.xlsx')
newframe = frame[['Stkcd','危机后期']]
a = newframe.groupby('Stkcd').sum()
a.to_excel('c.xls')
