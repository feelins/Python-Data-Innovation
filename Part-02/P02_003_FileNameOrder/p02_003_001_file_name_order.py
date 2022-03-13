#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   p02_003_001_file_name_order.py
@Time    :   2022/03/13 09:18:04
@Author  :   feelins, shao 
@Version :   1.0
@Contact :   feipengshao@163.com
@License :   (C)Copyright 2022-2023, 极地语音工作室 
@Desc    :   文件名排序的问题
'''

import os

input_dir = r'./sample_data'
file_list = os.listdir(input_dir)
print(file_list)
file_list.sort() # 文件名 按字符串排序
print(file_list)

file_list.sort(key=lambda x: int(x[4:-4])) # 文件名 按数字排序
print(file_list)