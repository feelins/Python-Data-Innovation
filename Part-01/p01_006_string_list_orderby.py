#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   p01_006_string_list_orderby.py
@Time    :   2022/03/12 15:10:46
@Author  :   feelins, shao 
@Version :   1.0
@Contact :   feipengshao@163.com
@License :   (C)Copyright 2022-2023, 极地语音工作室 
@Desc    :   对字符串列表进行排序
'''

# here put the import lib
'''
sort 与 sorted 区别：
sort 是应用在 list 上的方法，sorted 可以对所有可迭代的对象进行排序操作。
list 的 sort 方法返回的是对已经存在的列表进行操作，无返回值，而内建函数 sorted 方法返回的是一个新的 list，而不是在原来的基础上进行的操作。
'''
color_list = ['yellow', 'red', 'Green', 'blue']

color_list.sort()
print(color_list) # ['Green', 'blue', 'red', 'yellow'], 在原来的基础上进行的操作
color_list = sorted(color_list, key=len)
print(color_list) # ['red', 'blue', 'Green', 'yellow'], 按照字符串长度排序
color_list = sorted(color_list, key=str.lower)
print(color_list) # ['blue', 'Green', 'red', 'yellow'], 将字符串转化为小写之后再排序