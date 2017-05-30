# itertools————为有效的循环创建迭代器

import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(3,2),index=list('abc'),columns=['A','B'])
print(round(df.iloc[1,1],2))

from  itertools import count
for i in zip(count(1,step=2),['a','b','c']):   # count产生无线个循环数，可以设置step
    print(i)

# 对于不等长度的数据，根据最短的数据来返回长度
for i in zip(list('abc'),list('abcde')):
    print(i,end='')    # 只会返回abc这个三个数据

# 使用cycle会把传入的一个序列无线重复下去，不过可以提供第二个参数制定重复次数
from itertools import cycle
for i in zip(range(6),cycle(['a','b','c'])):
    print(i,end = ' ')   # 对于abc无线重复数据
## (0, 'a') (1, 'b') (2, 'c') (3, 'a') (4, 'b') (5, 'c')

# repeat 返回一个元素无线重复下去的itertor，可以提供第二个参数限定重复次数
from itertools import repeat
for i,s in zip(count(1),repeat('over-and-over',5)):
    print(i,s)

from itertools import accumulate
import operator
list(accumulate([1,2,3,4,5],operator.add))
list(accumulate([1,2,3,4,5],operator.mul))

# itertools.chain(*iterables)可以将多个iterable组合成一个iterator。
from itertools import chain
print(list(chain([1,2,3],['a','b','c'])))

# chain.from_iterable和chain类似，但是只接收单个iterable，然后讲这个iterable中的元素组合iterator
from itertools import chain
print(list(chain.from_iterable(['ABC','DEF'])))  # ['A', 'B', 'C', 'D', 'E', 'F']

# compress 接收两个iterable作为参数，只返回selectors对应的元素为True的data
from itertools import compress
print(list(compress([1,2,3,4,5],[True,True,False,False,True]))) # 按照第二个参数返回数据

# zip_longest和zip类似，但是zip的缺陷是iterable中的某一个元素遍历完，整个遍历停止
from itertools import zip_longest
r1 = range(3)
r2 = range(2)
print('zip stops early:')
print(list(zip(r1,r2)))         # [(0, 0), (1, 1)]
r1 = range(3)
r2 = range(2)
print(list(zip_longest(r1,r2)))   # [(0, 0), (1, 1), (2, None)]
zip_longest('ABCD', 'xy', fillvalue='-')  # Ax By C- D-

# islice 进行切片
from itertools import islice
for i in islice(range(100),0,100,10):
    print(i,end=' ')

# tee 返回n个独立的itertor
from itertools import islice,tee
r = islice(count(),5)
i1,i2 = tee(r)
print('i1:',list(i1))
print('i2:',list(i2))
for i in r:
    print(i,end=' ')
    if i>3:
        break

# takewhile 只要predicate返回True,不停的返回itertable的元素，直到False结束
import itertools
def less_than_10(x):
    return(x<10)
print(list(itertools.takewhile(less_than_10,itertools.count())))

# dropwhile 在predict返回True时舍弃元素，然后返回其余迭代结果
# print(list(itertools.dropwhile(less_than_10,itertools.count())))

# groupby把相邻的元素挑出来
import itertools
for key,group in itertools.groupby('AAAABBBCCDAABBB'):
    print(key,list(group))

[k for k,g in itertools.groupby('AAAABBBCCDAABBB')]
[list(g) for k,g in itertools.groupby('AAAABBBCCD')]

# product 对于数据产生循环  组合生成器
import itertools
itertools.product('ABCD',2)  # AA AB AC AD BA BB BC BD CA CB CC CD DA DB DC DD
itertools.permutations('ABCD',2)  # 上述数据去除叠词  AA BB CC DD
itertools.combinations('ABCD',2)   # AB AC AD BC BD CD
itertools.combinations_with_replacement('ABCD',2)  # AA AB AC AD BB BC BD CC CD DD

# accumulate
def accumulate(iterable,func=operator.add):
    it = iter(iterable)
    try:
        total = next(it)
    except StopIteration:
        return
    yield total
    for element in it:
        total = func(total,element)
        yield total
data = [3,4,6,2,1,9,0,7,5,8]
list(accumulate(data,operator.mul))
list(accumulate(data,max))    # 比较最大值
cashflows = [1000,-90,-90.-90,-90]
list(accumulate(cashflows,lambda bal,pmt:bal*1.05+pmt))

# itertools.chain
def chain(*iterables):
    # chain('ABC', 'DEF') --> A B C D E F
    for it in iterables:
        for element in it:
            yield element

# itertools.chain.from_iterbale
def from_iterable(iterables):
    # chain.from_iterable(['ABC', 'DEF']) --> A B C D E F
    for it in iterables:
        for element in it:
            yield element

# itertools.combinations
def combinations(iterable,r):
    pool = tuple(iterable)   # 生成元组形式
    n = len(pool)
    if r>n:
        return
    indices = list(range(r))
    yield tuple(pool[i] for i in indices)
    while True:
        for i in reversed(range(r)):
            if indices[i] != i+n-r:
                break
            else:
                return
            indices[i] += 1
            for j in range(i+1,r):
                indices[j] = indices[j-1] + 1
            yield tuple(pool[i] for i in indices)
