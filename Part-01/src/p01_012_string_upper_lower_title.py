#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   p01_012_string_upper_lower_title.py
@Time    :   2022/03/19 11:22:20
@Author  :   feelins, shao 
@Version :   1.0
@Contact :   feipengshao@163.com
@License :   (C)Copyright 2022-2023, 极地语音工作室 
@Desc    :   字符串的大写，小写，第一个字母大写用法
'''

# here put the import lib
str = "github.com"
print(str.upper())          # 把所有字符中的小写字母转换成大写字母
print(str.lower())          # 把所有字符中的大写字母转换成小写字母
print(str.capitalize())     # 把第一个字母转化为大写字母，其余小写
print(str.title())          # 把每个单词的第一个字母转化为大写，其余小写 