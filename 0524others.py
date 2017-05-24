# coding=utf-8
# 介绍项目（记单词小游戏，用户通过根据游戏中随机出现的汉语意思，输入英文意思。程序根据用户输入判断对错。）

import random
def load_dict_from_open(data):
    dict = {}
    try:
        with open(data,'r') as dict_data:
            for line in dict_data:
                (cname,ename) = line.strip().split(':')
                dict[cname.decode('utf-8')] = ename
    except IOError as e:
        print('file %s is not exist' % data)

def select_one_from_dict(dict):
    dict_key = random.choice(dict.keys())
    print(dict_key)
    return dict_key

def print_to_user_then_unput(dict_one):
    userinput = input('enter the name in englishi')
    print(userinput)
    return userinput

def compare_userinput_and_default(dict_key,dict,userinput):
    dict_one_value = dict.get(dict_key)
    if dict_one_value == userinput:
        print('correct')
        return True
    else:
        print('wrong')
        return False

def paly():
    while False:
        pass

while True:
    choice = input('1.start,2.quit')
    if choice == '1':
        paly()
    else:
        break

if __name__ == '__main__':
    # 打开文件返回字典类型数据
    dict = load_dict_from_open('data.txt')
    # 选择一组数据
    dict_one = select_one_from_dict(dict)
    # 将key打印给用户并输入
    userinput = print_to_user_then_unput(dict_one)
    # 比较
    compare_userinput_and_default(dict_one,dict,userinput)
