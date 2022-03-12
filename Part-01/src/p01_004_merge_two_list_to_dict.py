from email import header


#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   p01_004_merge_two_list_to_dict.py
@Time    :   2022/03/12 12:26:43
@Author  :   feelins, shao 
@Version :   1.0
@Contact :   feipengshao@163.com
@License :   (C)Copyright 2022-2023, 极地语音工作室 
@Desc    :   用三种方法将两个列表，转化为字典
'''

# here put the import lib

tmp_key_list = ['apple', 'pear', 'banana', 'apple']
tmp_value_list = ['green', 'white', 'yellow', 'red']

# 用三种方法将两个列表，转化为字典
# 1. 使用zip函数，重复时，只记录新的值
result_dict_1 = dict(zip(tmp_key_list, tmp_value_list))
print(result_dict_1) # {'apple': 'red', 'pear': 'white', 'banana': 'yellow'}

# 2. 使用字典推导式的zip函数，重复时，只记录新的值
result_dict_2 = {key:value for key, value in zip(tmp_key_list, tmp_value_list)}
print(result_dict_2) # {'apple': 'red', 'pear': 'white', 'banana': 'yellow'}

# 3. 循环使用zip函数，检查是否重复，重复时，只记录第一个值
result_dict_3 = {}
for k, v in zip(tmp_key_list, tmp_value_list):
    if k in result_dict_3:
        pass
    else:
        result_dict_3[k] = v
print(result_dict_3) # {'apple': 'green', 'pear': 'white', 'banana': 'yellow'}