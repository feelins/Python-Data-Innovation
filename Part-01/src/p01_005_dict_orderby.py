#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   p01_005_dict_orderby.py
@Time    :   2022/03/12 14:38:17
@Author  :   feelins, shao 
@Version :   1.0
@Contact :   feipengshao@163.com
@License :   (C)Copyright 2022-2023, 极地语音工作室 
@Desc    :   对字典列表进行排序
'''

# here put the import lib
sample_lists = [
    {'Name': 'Tome', 'Age': 9},
    {'Name': 'Jerry', 'Age': 10},
    {'Name': 'Sara', 'Age': 5}
]

# 方法一
sample_lists.sort(key=lambda item: item.get('Age'))
print(sample_lists) # [{'Name': 'Sara', 'Age': 5}, {'Name': 'Tome', 'Age': 9}, {'Name': 'Jerry', 'Age': 10}]
sample_lists.sort(key=lambda item: item.get('Name'))
print(sample_lists) # [{'Name': 'Jerry', 'Age': 10}, {'Name': 'Sara', 'Age': 5}, {'Name': 'Tome', 'Age': 9}]

# 方法二
from operator import itemgetter
f = itemgetter('Name')
sample_lists.sort(key=f)
print(sample_lists) # [{'Name': 'Jerry', 'Age': 10}, {'Name': 'Sara', 'Age': 5}, {'Name': 'Tome', 'Age': 9}]