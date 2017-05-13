# -*- coding: utf-8 -*-
'''
杨辉三角形，也称帕斯卡三角，其定义为：顶端是 1,视为(row0).第1行(row1)(1&1)两个1,
这两个1是由他们上头左右两数之和 (不在三角形内的数视为0).
依此类推产生第2行(row2):0+1=1;1+1=2;1+0=1.
第3行(row3):0+1=1;1+2=3; 2+1=3;1+0=1.
循此法可以产生以下诸行，如下图所示。
'''
import itertools
def yanghui(m,n):
    if m+1 < n:
        print('invalid query')
    else:
        result = [[1]]
        for k in range(m):
            a = list(itertools.chain.from_iterable([[0],result[-1],[0]]))
            result.append([a[i] + a[i+1] for i in range(len(a)-1)])
        print(result[m][n])
yanghui(5,5)

def generate_yh(m):
    result = [[1]]
    for k in range(m):
        a = list(itertools.chain.from_iterable([[0], result[-1], [0]]))
        result.append([a[i] + a[i + 1] for i in range(len(a) - 1)])
    for i in result:
        print(i)
generate_yh(5)
