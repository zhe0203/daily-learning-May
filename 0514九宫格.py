# -*- coding: utf-8 -*-
# 首先从1-9这个数字中找出遍历找出所有3个数字的组合，并且计算和未15
import itertools
import numpy as np
nums = [x for x in range(1,10)]
sequence_3nums = [p for p in itertools.permutations(nums,3) if sum(p)==15]
print(sequence_3nums)
# 利用迭代神器itertools很容易搞定
# 从48行中各选出3行来，形成一个新的3*3的矩阵
for row1 in sequence_3nums:
    for row2 in sequence_3nums:
        for row3 in sequence_3nums:
            np_array_3d = np.array([row1,row2,row3])
            # 计算3*3矩阵的行、列对角线的和
            if sum(np_array_3d[:,0]) == 15\
                    and sum(np_array_3d[:,1])==15\
                    and np_array_3d.trace() == 15\
                    and np_array_3d[0,2]+np_array_3d[1,1]+np_array_3d[2,0]==15:
               a = np_array_3d.tolist()
               if len(set(list(itertools.chain.from_iterable(a)))) == 9:
                   print(np_array_3d)

# Crossin神奇的九宫格
'''
首先是 N 为奇数时：
    将1放在第一行中间一列；
    从2开始直到n×n止各数依次按下列规则存放，按 45°方向行走，如向右上，每一个数存放的行比前一个数的行数减1，列数加1
    如果行列范围超出矩阵范围，则回绕。例如1在第1行，则2应放在最下一行，列数同样加1;
    如果按上面规则确定的位置上已有数，或上一个数是第1行第n列时，则把下一个数放在上一个数的下面。
'''
def oddn(n):
    # 构造二维列表
    lst = [[0 for i in range(n)] for i in range(n)]
    # 初始化列表位置
    x,y = 0,n//2
    for num in range(1,n*n+1):
        lst[x][y] = num
        xa,ya = x-1,y+1
        # 回绕情况
        if xa < 0:
            xa = n-1
        if ya > n-1:
            ya = 0
        # 占位情况
        if lst[xa][ya] != 0:
            x= x + 1
            if x > n-1:
                x = 0
        else:
            x,y = xa,ya
        return lst
lst = oddn(3)
for row in lst:
    print(row)


# 累加子矩阵
def acc(p, lst):
    # print(lst)
    for row in lst:
        for index in range(len(row)):
            row[index] += p

    return lst


def fourNplus2(n):
    m = n // 2
    A, B, C, D = oddN(m), oddN(m), oddN(m), oddN(m)
    B = acc(m ** 2, B)
    C = acc(m ** 2 * 2, C)
    D = acc(m ** 2 * 3, D)
    for row_index in range(len(A)):
        A[row_index].extend(C[row_index])
        D[row_index].extend(B[row_index])
    # 合并子矩阵
    matrix = A + D
    t = (n - 2) // 4
    # 列交换
    for col_index in range(len(matrix[0])):
        if col_index < t or col_index > n - t:
            for row_index in range(len(matrix) // 2):
                matrix[row_index][col_index], matrix[row_index + m][col_index] = \
                    matrix[row_index + m][col_index], matrix[row_index][col_index]
                # 交换特殊位置
    matrix[t][0], matrix[m + t][0] = matrix[m + t][0], matrix[t][0]
    matrix[t][t], matrix[m + t][t] = matrix[m + t][t], matrix[t][t]
    return matrix


lst = fourNplus2(6)
for row in lst:
    print(row)
