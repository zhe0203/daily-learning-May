# Reshaping and Pivot Tables
import pandas as pd
import numpy as np

if __name__=='__main__':
    import pandas.util.testing as tm
    tm.N=3
    def unpivot(frame):
        N,K=frame.shape
        data={'value':frame.values.ravel('F'),
              'variable':np.asarray(frame.columns).repeat(N),
              'date':np.tile(np.asarray(frame.index),K)}
        return(pd.DataFrame(data,columns=['date','variable','value']))
    df=unpivot(tm.makeTimeDataFrame())
    ### 筛选出A的行数据
    print(df[df['variable']=='A'])

    # 如果我们想将数据进行转换，可进行如下操作
    print(df.pivot(index='date',columns='variable',values='value'))
    df['value2']=df['value']*2
    print(df)
    # 若未定义value的值，则会出现两个数值
    pivoted=df.pivot(index='date',columns='variable')
    # print(pivoted)
    # 若定义value的值，则会出现一个数值
    print(df.pivot(index='date',columns='variable',values='value2'))
    pivoted['value2']  # 选择values设置成value2的返回结果

# Reshaping by stacking and unstacking
    # 与pivot函数相似的函数是，stack unstack函数
    # stack 是将宽型数据转换成长型数据
    # unstack 是将长型数据转换成宽型数据
    tuples=list(zip(*[['bar','bar','baz','baz','foo','foo','qux','qux'],
                      ['one','two','one','two','one','two','one','two']]))
    #　print(tuples)  # zip将数组转换成元组
    index=pd.MultiIndex.from_tuples(tuples,names=['first','second'])
    df=pd.DataFrame(np.random.randn(8,2),index=index,columns=['A','B'])
    print(df)
    df2=df[:4]  # 选择0 1 2 3 行数据

    # 下面使用stack函数，将宽型数据转换成长型数据
    stacked=df2.stack()
    print(stacked)
    stacked.unstack()  # 相反的转换
    stacked.unstack(level=1)  # 选择level=1的因子作为转换
    stacked.unstack(level=0)  # 选择level=0的因子作为转换
    # 也可以直接使用因子的名称，如
    stacked.unstack('second')

    index=pd.MultiIndex.from_product([[2,1],['a','b']])
    df=pd.DataFrame(np.random.randn(4),index=index,columns=['A'])
    # print(df)
    all(df.unstack().stack()==df.sort_index())

# Multiple Levels
    columns=pd.MultiIndex.from_tuples([('A','cat','long'),
                                       ('B','cat','long'),
                                       ('A','dog','short'),
                                       ('B','dog','short')],
            names=['exp','animal','hair_length'])
    df=pd.DataFrame(np.random.randn(4,4),columns=columns)
    # print(df)
    # 使用多个因子进行数据的变换
    # print(df.stack(level=['animal','hair_length']))
    # 使用数字表示第几个因子
    df.stack(level=[1,2])

# Missing Data
    columns=pd.MultiIndex.from_tuples([('A','cat'),('B','dog'),
                                        ('B','cat'),('A','dog')],
                                      names=['exp','animal'])
    index = pd.MultiIndex.from_product([('bar', 'baz', 'foo', 'qux'),
                                        ('one', 'two')],
                                       names=['first', 'second'])
    df=pd.DataFrame(np.random.randn(8,4),index=index,columns=columns)
    print(df)
    df2=df.ix[[0,1,2,4,5,7]]   # 选择行数据
    # print(df2)
    # print(df2.stack('exp'))
    df3=df.iloc[[0,1,4,7],[1,2]]
    df3.unstack(fill_value=-1e9)  # 填充缺失值的方法

# with a mulitiindex
    df[:3].unstack(level=0)
    df2.unstack(1)   # 将因子1变成列名称数据

# Reshaping by Melt
    # 使用melt函数将数据转换成长型
    cheese=pd.DataFrame({'first':['John','Mary'],
                         'last':['Doe','Bo'],
                         'height':[5.5,6.0],
                         'weight':[130,150]})
    pd.melt(cheese,id_vars=['first','last'])
    # 也可以将变换后的数据进行命名
    pd.melt(cheese,id_vars=['first','last'],var_name='quantity')

# Combining with stats and GroupBy
    df.stack().mean(1).unstack()
    df.groupby(level=1,axis=1).mean()
    df.stack().groupby(level=1).mean()

# pivot tables
    import datetime
    df=pd.DataFrame({'A':['one','one','two','three']*6,
                     'B':['A','B','C']*8,
                     'C':['foo','foo','foo','bar','bar','bar']*4,
                     'D':np.random.randn(24),
                     'E':np.random.randn(24),
                     'F':[datetime.datetime(2013,i,1) for i in range(1,13)]+
                         [datetime.datetime(2013,i,15) for i in range(1,13)]})
    print(df)
    print(list(range(1,10)))
