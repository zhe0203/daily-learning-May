# -*- coding: utf-8 -*-

# 命名列表切割方式
a = [0,1,2,3,4,5]
# slice(start, stop[, step]))
lastthree = slice(-3,None,None)
print(a[lastthree])   # [3, 4, 5]

# 列表以及迭代器的压缩和解压缩
a = [1,2,3]
b = ['a','b','c']
z = zip(a,b)
print(list(zip(a,b)))  # [(1, 'a'), (2, 'b'), (3, 'c')]
print(list(zip(*z)))  # [(1, 2, 3), ('a', 'b', 'c')] 解压缩

# 列表相邻元素压缩器
a = [1,2,3,4,5,6]
print(list(zip(*([iter(a)]*2))))

group_adjacent = lambda a,k:zip(*([iter(a)] * k))
print(list(group_adjacent(a,3)))  # [(1, 2), (3, 4), (5, 6)]
group_adjacent(a, 2)
# [(1, 2), (3, 4), (5, 6)]
group_adjacent(a, 1)
# [(1,), (2,), (3,), (4,), (5,), (6,)]

# 相当于
zip(a[::2],a[1::2])
zip(a[::3],a[1::3],a[2::3])

group_adjacent = lambda a,k:zip(*(a[i::k] for i in range(k)))
group_adjacent(a, 3)
# [(1, 2, 3), (4, 5, 6)]
group_adjacent(a, 2)
# [(1, 2), (3, 4), (5, 6)]
group_adjacent(a, 1)
# [(1,), (2,), (3,), (4,), (5,), (6,)]

# 在列表中用压缩器和迭代器滑动取值窗口
def n_grams(a,n):
    z = [iter(a[i:]) for i in range(n)]
    return zip(*z)
a = [1,2,3,4,5,6]
n_grams(a, 3)
# [(1, 2, 3), (2, 3, 4), (3, 4, 5), (4, 5, 6)]
n_grams(a, 2)
# [(1, 2), (2, 3), (3, 4), (4, 5), (5, 6)]
n_grams(a, 4)
# [(1, 2, 3, 4), (2, 3, 4, 5), (3, 4, 5, 6)]

# 用压缩器反转字典
m = {'a':1,'b':2,'c':3,'d':4}
print(m.items())
print(m.values(),m.keys())
print(list(zip(m.values(), m.keys())))
# [(1, 'a'), (3, 'c'), (2, 'b'), (4, 'd')]
mi = dict(zip(m.values(),m.keys()))
print(mi)   # {1: 'a', 2: 'b', 3: 'c', 4: 'd'}

# 列表展开
import itertools
a = [[1,2],[3,4],[5,6]]
print(list(itertools.chain.from_iterable(a)))
# [1, 2, 3, 4, 5, 6]
sum(a,[])  # [1, 2, 3, 4, 5, 6]
print([x for l in a for x in l])  # [1, 2, 3, 4, 5, 6]

a = [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]
[x for l1 in a for l2 in l1 for x in l2]
# [1, 2, 3, 4, 5, 6, 7, 8]

a = [1, 2, [3, 4], [[5, 6], [7, 8]]]
flatten = lambda x:[y for l in x for y in flatten(l)] if type(x) is list else [x]
print(flatten(a))  # [1, 2, 3, 4, 5, 6, 7, 8]

# 生成器表达式
g = (x ** 2 for x in range(10))
print(next(g))
print(next(g))
print(next(g))
print(sum(x**3 for x in range(10)))

# 字典推导
m = {x:x**2 for x in range(5)}
print(m)
m = {x:'A'+str(x) for x in range(10)}
print(m)

# 用字典推导反转字典
m = {'a':1,'b':2,'c':3,'c':4}
print({v:k for k,v in m.items()})

# 命名元组
import collections
point = collections.namedtuple('ponit',['x','y'])
p = point(x=1,y=2)
print(p,p.x,p.y)

# 继承命名元组
class point(collections.namedtuple('pointbase',['x','y'])):
    __slots__ = ()
    def __add__(self,other):
        return point(x=self.x+other.x,y=self.y+other.y)
p = point(x=1,y=2)
q = point(x=2,y=3)
print(p+q)

# 操作集合
A = {1,2,3,3}
B = {3,4,5,6,7}
print(set(A))   # 去重
print(A | B)      # {1, 2, 3, 4, 5, 6, 7}
print(A & B)   # {3}
print(A-B)      # 取补集 [1, 2]
print(B-A)
print(A^B)     # [1, 2, 4, 5, 6, 7]

# 操作多重结合
A = collections.Counter([1,2,2])
B = collections.Counter([2,2,3])   # 返回每一元素个数的字典
print(A,B)
print(A | B,A & B,A + B,A - B,B - A)
A | B
#Counter({2: 2, 1: 1, 3: 1})
A & B
#Counter({2: 2})
A + B
#Counter({2: 4, 1: 1, 3: 1})
A - B
#Counter({1: 1})
B - A
#Counter({3: 1})

# 统计在可迭代器中最常出现的元素
A = collections.Counter([1,1,2,2,3,3,3,3,4,5,6,7])
print(A.most_common(1))   # [(3,4)] 最常出现的一个数
# 最常出现的三个数
print(A.most_common(3)) # [(3, 4), (1, 2), (2, 2)]

# 两端都可操作的队列
# deque	list-like container with fast appends and pops on either end
q = collections.deque()  #　产生队列
q.append(1)
q.appendleft(2)   # 左添加
q.extend([3,4])
q.extendleft([5,6]) # 左添加
print(q)  # deque([6, 5, 2, 1, 3, 4])

print(q.pop())   # 默认删除最后一个数，并返回该数字
print(q.popleft())   # 删除左边第一个数据
# rotate 旋转队列，默认时值为1，由右边开始旋转，负值代表左边旋转，n代表从队列的第一个元素开始，n从1开始计数
# deque([5, 2, 1, 3])
q.rotate(3)  # deque([2, 1, 3, 5])
q.rotate(-3)   # deque([5, 2, 1, 3])

# 有最大长度的双端队列
last_three = collections.deque(maxlen=3)
for i in range(10):
    last_three.append(i)
    print(', '.join(str(x) for x in last_three))
'''
0
0, 1
0, 1, 2
1, 2, 3
2, 3, 4
3, 4, 5
4, 5, 6
5, 6, 7
6, 7, 8
7, 8, 9
'''

# 可排序字典
m = dict((str(x),x) for x in range(10))
print(m)
print(', '.join(m.keys()))
m = collections.OrderedDict((str(x),x) for x in range(10))
print(m)
print(', '.join(m.keys()))

# 默认字典
m = dict()
# m['a']   错误
m = collections.defaultdict(lambda :9)  # 可设置为int
# 使用defaultdict这样的对对于无键值的字典将会返回设置的数值
print(m['a'],m['b'])
m = collections.defaultdict(str)
m['a']   # ''
m['b'] += 'a'
m['b']  # 'a'
m = collections.defaultdict(lambda: '[default value]')
m['a']   # '[default value]'
m['b']    # '[default value]'

# 默认字典的简单树状表达
import json
tree = lambda :collections.defaultdict(tree)
root = tree()
root['menu']['id'] = 'file'
root['menu']['value'] = 'File'
root['menu']['menuitems']['new']['value'] = 'New'
root['menu']['menuitems']['new']['onclick'] = 'new();'
root['menu']['menuitems']['open']['value'] = 'Open'
root['menu']['menuitems']['open']['onclick'] = 'open();'
root['menu']['menuitems']['close']['value'] = 'Close'
root['menu']['menuitems']['close']['onclick'] = 'close();'
print(json.dumps(root,sort_keys=True,indent=4,separators=(',',':')))

# 对象到唯一计数的映射
import itertools,collections
# value_to_numeric_map = collections.defaultdict(itertools.count()) # collections.defaultdict(itertools.count().next)
# value_to_numeric_map['a']  # 0
# value_to_numeric_map['b']  # 1
# value_to_numeric_map['c']  # 2
# value_to_numeric_map['a']  # 0

# 最大和最小的几个列表元素
import random,heapq
a = [random.randint(0,100) for __ in range(100)]
print(heapq.nsmallest(5,a))  # 返回其中最小的5个数
print(heapq.nlargest(5,a))   # 返回其中最大的5个数
# 关于字典返回的数据
portfolio = [
    {'name': 'IBM', 'shares': 100, 'price': 91.1},
    {'name': 'AAPL', 'shares': 50, 'price': 543.22},
    {'name': 'FB', 'shares': 200, 'price': 21.09},
    {'name': 'HPQ', 'shares': 35, 'price': 31.75},
    {'name': 'YHOO', 'shares': 45, 'price': 16.35},
    {'name': 'ACME', 'shares': 75, 'price': 115.65}]
cheap = heapq.nsmallest(3, portfolio, key=lambda s: s['price'])
print(cheap)
# [{'price': 16.35, 'name': 'YHOO', 'shares': 45}, {'price': 21.09, 'name': 'FB', 'shares': 200}, {'price': 31.75, 'name': 'HPQ', 'shares': 35}]
expensive = heapq.nlargest(3, portfolio, key=lambda s: s['price'])
print(expensive)
# [{'price': 543.22, 'name': 'AAPL', 'shares': 50}, {'price': 115.65, 'name': 'ACME', 'shares': 75}, {'price': 91.1, 'name': 'IBM', 'shares': 100}]

# 两个列表的笛卡尔积
print(list(itertools.product([1,2,3],[4,5])))
for p in itertools.product([0,1],repeat=4):
    print(''.join(str(x) for x in p))

#  列表组合和列表元素替代组合
for c in itertools.combinations([1,2,3,4,5],3):
    print(''.join(str(x) for x in c))
for c in itertools.combinations_with_replacement([1, 2, 3], 2):
    print(''.join(str(x) for x in c))

# 列表元素排列组合
for p in itertools.permutations([1,2,3,4]):
    print(''.join(str(x) for x in p))

# 可链接迭代器
a = [1, 2, 3, 4]
for p in itertools.chain(itertools.combinations(a, 2), itertools.combinations(a, 3)):
    print(p)
for subset in itertools.chain.from_iterable(itertools.combinations(a, n) for n in range(len(a) + 1))
    print(subset)

# 根据文件指定列类聚
with open('contactlenses.csv','r') as infile:
    data = [line.strip().split(',') for line in infile]
data = data[1:]
def print_data(rows):
    print('\n'.join('\t'.join('{:<16}'.format(s) for s in row) for row in rows))
