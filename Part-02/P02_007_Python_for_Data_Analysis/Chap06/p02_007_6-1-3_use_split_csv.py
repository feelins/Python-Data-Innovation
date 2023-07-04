#!/usr/bin/env python
# -*-coding:utf-8 -*-
'''
@File    :   p02_007_6-1-3_use_split_csv.py
@Time    :   2023/07/04 19:22:31
@Author  :   Feelins Shao 
@Version :   1.0
@Contact :   feipengshao@163.com
@License :   (C)Copyright 2022-2023, Feelins Shao
@Desc    :   6.1.3 使用分隔格式
'''
import pandas as pd
import csv

# 使用Python内置的csv模块读取CSV文件
input_file = r'Part-02/P02_007_Python_for_Data_Analysis/Chap06/ex2.csv'
# 原始文件
# 1,2,3,4,5,hello world
# 4,8,16,17,18,how are you
# 8,9,10,11,12,you are welcome
f = open(input_file)
reader = csv.reader(f)
for line in reader:
    print(line)
# 输出结果
# ['1', '2', '3', '4', '5', 'hello world']
# ['4', '8', '16', '17', '18', 'how are you']
# ['8', '9', '10', '11', '12', 'you are welcome']

with open(input_file) as f:
    lines = list(csv.reader(f))
header, values = lines[0], lines[1:]
data_dict = {h: v for h, v in zip(header, zip(*values))}
print(data_dict)
# {'1': ('4', '8'), '2': ('8', '9'), '3': ('16', '10'), '4': ('17', '11'), '5': ('18', '12'), 'hello world': ('how are you', 'you are welcome')}
