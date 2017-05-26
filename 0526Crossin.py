# -*- coding: utf-8 -*-

from itertools import combinations
import math
import datetime

starttime_1 = datetime.datetime.now()
def Goldbach_1(num):
    # 生成小于等于num的所有质数
    # prime_num = filter(lambda x:not [x % j for j in range(2,int(math.sqrt(x))+1) if x % j == 0],range(2,num+1))
    # 为了减少运算复杂度，只保留个位数相加等于所求数的个位数的所有质数
    filter_num_first = []                       # 筛选第一个质数
    filter_num_second = []                      # 筛选第二个质数
    filter_num = []
    for j in combinations([1,2,3,5,7,9],2):
        if int(str(sum(j))[-1]) == int(str(num)[-1]):
            filter_num_first.append(j[0])
            filter_num_second.append(j[1])
            filter_num.extend([j[0],j[1]])
    prime_num = list(filter(lambda x: not [x % j for j in range(2, int(math.sqrt(x)) + 1) if x % j == 0 and x not in filter_num],range(2, num + 1)))

    # prime_num_filter = filter(lambda x:int(str(x)[-1]) in filter_num,prime_num)
    # for i in list(filter(lambda x:int(str(x)[-1]) in filter_num_first,prime_num)):
    #     if num - i in list(filter(lambda x:int(str(x)[-1]) in filter_num_second,prime_num)):
    #         print(i,num-i)
    #         break
    for i in prime_num:
        if num - i in prime_num:
            print(i,num-i)
            break
Goldbach_1(123456)
endtime_1 = datetime.datetime.now()
print(endtime_1 - starttime_1)             # 0:02:20.537586


starttime_2 = datetime.datetime.now()
def Goldbach_2(num):
    prime_num = list(filter(lambda x:not [x % j for j in range(2,int(math.sqrt(x))+1) if x % j == 0],range(2,num+1)))
    for i in prime_num:
        if num - i in prime_num:
            print(i,num-i)
            break
Goldbach_2(923456)
endtime_2 = datetime.datetime.now()
print(endtime_2 - starttime_2)                #

starttime_3 = datetime.datetime.now()
def Goldbach_3(num):
    num_range = list(range(3,num+1,2))
    num_range.insert(0,2)
    prime_num = list(filter(lambda x:not [x % j for j in range(2,int(math.sqrt(x))+1) if x % j == 0],num_range))
    for i in prime_num:
        if num - i in prime_num:
            print(i,num-i)
            break
Goldbach_3(923456)
endtime_3 = datetime.datetime.now()
print(endtime_3 - starttime_3)                #
