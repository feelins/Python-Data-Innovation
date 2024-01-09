#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   p01_009_swap.py
@Time    :   2022/03/13 10:44:24
@Author  :   feelins, shao 
@Version :   1.0
@Contact :   feipengshao@163.com
@License :   (C)Copyright 2022-2023, 极地语音工作室 
@Desc    :   Python是如何简单的实现两个变量交换的
'''

# here put the import lib
a = 3
b = 4
print('a: ' + str(a) + ', ' + 'b: ' + str(b)) # a: 3, b: 4

# swap
a, b = b, a
print('a: ' + str(a) + ', ' + 'b: ' + str(b)) # a: 4, b: 3