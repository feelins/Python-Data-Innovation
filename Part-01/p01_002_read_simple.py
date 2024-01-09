#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   p01_001_read_simple.py
@Time    :   2022/02/16 12:12:45
@Author  :   feelins, shao 
@Version :   1.0
@Contact :   feipengshao@163.com
@License :   (C)Copyright 2022-2023, 极地语音工作室
@Desc    :   读文本文件内容，打印出来
'''

# here put the import lib
my_file = r'../samples/my_txt.txt'
with open(my_file, encoding='utf-8') as fid:
    file_content = [x.strip() for x in fid.readlines()]

for line in file_content:
    print(line)
print('Done!')