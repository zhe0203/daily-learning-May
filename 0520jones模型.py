# -*- coding: utf-8 -*-
import pandas as pd
import os
os.chdir(r'C:\Users\jk\Desktop\诸葛兼职\052011-250')

# df_2010 = pd.read_excel(r'审计质量.xls',sheetname='2010')
# df_2011 = pd.read_excel(r'审计质量.xls',sheetname='2011')
# df_2012 = pd.read_excel(r'审计质量.xls',sheetname='2012')
# df_2013 = pd.read_excel(r'审计质量.xls',sheetname='2013')
# df_2014 = pd.read_excel(r'审计质量.xls',sheetname='2014')
# df_2015 = pd.read_excel(r'审计质量.xls',sheetname='2015')

# 数据去重
# for i in [df_2010,df_2011,df_2012,df_2013,df_2014,df_2015]:
#     i = i[~i.iloc[:,2].duplicated()]

# 求2010-2015年股票代码的交集
# a = set(df_2010.iloc[:,2])
# for i in [df_2011,df_2012,df_2013,df_2014,df_2015]:
#     a = a.intersection(set(i.iloc[:,2]))
# new_df_2010 = df_2010[[df_2010.iloc[x,2] in a for x in range(len(df_2010))]]
# # new_df_2010.to_excel('2010.xls')
# new_df_2011 = df_2011[[df_2011.iloc[x,2] in a for x in range(len(df_2011))]]
# # new_df_2011.to_excel('2011.xls')
# new_df_2012 = df_2012[[df_2012.iloc[x,2] in a for x in range(len(df_2012))]]
# # new_df_2012.to_excel('2012.xls')
# new_df_2013 = df_2013[[df_2013.iloc[x,2] in a for x in range(len(df_2013))]]
# # new_df_2013.to_excel('2013.xls')
# new_df_2014 = df_2014[[df_2014.iloc[x,2] in a for x in range(len(df_2014))]]
# # new_df_2014.to_excel('2014.xls')
# new_df_2015 = df_2015[[df_2015.iloc[x,2] in a for x in range(len(df_2015))]]
# # new_df_2015.to_excel('2015.xls')

# 计算jons模型所需要的数据
# 计算TA
# for i in [new_df_2011,new_df_2012,new_df_2013,new_df_2014,new_df_2015]:
#     i.loc[:,'TA'] = i.iloc[:,8].values - i.iloc[:,9].values
#
# new_df_2010.to_excel('2010.xls')
# new_df_2011.to_excel('2011.xls')
# new_df_2012.to_excel('2012.xls')
# new_df_2013.to_excel('2013.xls')
# new_df_2014.to_excel('2014.xls')
# new_df_2015.to_excel('2015.xls')

# # 固定资产数据清洗
# mydata_2010 = pd.read_excel(r'固定资产.xls',sheetname='2010')
# mydata_2011 = pd.read_excel(r'固定资产.xls',sheetname='2011')
# mydata_2012 = pd.read_excel(r'固定资产.xls',sheetname='2012')
# mydata_2013 = pd.read_excel(r'固定资产.xls',sheetname='2013')
# mydata_2014 = pd.read_excel(r'固定资产.xls',sheetname='2014')
# mydata_2015 = pd.read_excel(r'固定资产.xls',sheetname='2015')
# # 数据去重
#
# mydata_2010 = mydata_2010[~mydata_2010.iloc[:,2].duplicated()]
# mydata_2011 = mydata_2011[~mydata_2011.iloc[:,2].duplicated()]
# mydata_2012 = mydata_2012[~mydata_2012.iloc[:,2].duplicated()]
# mydata_2013 = mydata_2013[~mydata_2013.iloc[:,2].duplicated()]
# mydata_2014 = mydata_2014[~mydata_2014.iloc[:,2].duplicated()]
# mydata_2015 = mydata_2015[~mydata_2015.iloc[:,2].duplicated()]
#
# mydata_2010.to_excel('gd_2010.xls')
# mydata_2011.to_excel('gd_2011.xls')
# mydata_2012.to_excel('gd_2012.xls')
# mydata_2013.to_excel('gd_2013.xls')
# mydata_2014.to_excel('gd_2014.xls')
# mydata_2015.to_excel('gd_2015.xls')

# 进行参数估计
from sklearn import linear_model
for i in ['2011.xls','2012.xls','2013.xls','2014.xls','2015.xls']:
    mydata = pd.read_excel(i)
    x = mydata[['X1','X2']]
    y = mydata['Y']
    reg = linear_model.LinearRegression(copy_X=True, fit_intercept=True, normalize=False)
    reg.fit(x,y)
    print(reg.intercept_,reg.coef_)
