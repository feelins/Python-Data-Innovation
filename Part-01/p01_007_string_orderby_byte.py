#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   p01_007_string_orderby_byte.py
@Time    :   2022/03/12 15:39:39
@Author  :   feelins, shao 
@Version :   1.0
@Contact :   feipengshao@163.com
@License :   (C)Copyright 2022-2023, 极地语音工作室 
@Desc    :   以字节为单位获取字符串大小
'''

# here put the import lib
str1 = 'Hello'
str2 = '🥵'

def str_byte_size(s):
    return len(s.encode('utf-8'))

print(str_byte_size(str1)) # 5
print(str_byte_size(str2)) # 4