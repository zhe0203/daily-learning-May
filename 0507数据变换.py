
import pandas as pd
import os
import time

os.chdir(r'C:\Users\jk\Desktop\诸葛兼职\050610')
df = pd.read_csv(r'2.csv',parse_dates=[12])

# 总计数据
new_df_1 = pd.DataFrame({'num':[1]*len(df)},index=df['审批通过时间'])
new_df_1 = new_df_1.resample('M').sum()
new_df_1.to_csv('总计数据2.csv')

# 分区域数据
# new_df_2 = pd.DataFrame({'num':[1]*len(df),'城市':df['城市'].values,
#                          '审批通过时间':df['审批通过时间'].values})
# print(new_df_2.iloc[1,1].split('-')[0])
# new_df_2['省份'] = list(map(lambda x:x.split('-')[0],new_df_2['城市']))
# new_df_3 = pd.DataFrame({'num':[1]*len(df),'省份':new_df_2['省份'].values}
#                          ,index=df['审批通过时间'].values)
# new_df_3 = new_df_3.groupby(['省份']).resample('M').sum()
# new_df_3.to_csv('分省份数据1.csv')
