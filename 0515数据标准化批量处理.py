
import os
import pandas as pd

os.chdir(r'C:\Users\jk\Desktop\诸葛兼职\051412')

# 读取数据
for k in ['2012','2013','2014','2015','2016']:
    mydata = pd.read_excel('因子分析数据.xls',sheetname=[k],index_col=[0])
    for i in mydata[k].columns:
        if i in ['流动比率','速动比率','资产负债率']:
            mydata[k][i] = list(map(lambda x:abs((x-mydata[k][i].mean())/mydata[k][i].std()),
                                     mydata[k][i]))
        else:
            mydata[k][i] = list(map(lambda x: (x - mydata[k][i].mean()) / mydata[k][i].std(),
                                     mydata[k][i]))
    name = k + '.xls'
    mydata[k].to_excel(name)
