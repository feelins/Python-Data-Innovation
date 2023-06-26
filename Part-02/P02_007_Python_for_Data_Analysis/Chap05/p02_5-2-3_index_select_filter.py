#!/usr/bin/env python
# -*-coding:utf-8 -*-
'''
@File    :   p02_5-2-3_index_select_filter.py
@Time    :   2023/06/26 16:55:44
@Author  :   Feelins Shao 
@Version :   1.0
@Contact :   feipengshao@163.com
@License :   (C)Copyright 2022-2023, Feelins Shao
@Desc    :   5.2.3 索引、选择与过滤
'''

import pandas as pd
import numpy as np

obj = pd.Series(np.arange(7.), index=['a', 'b', 'c', 'd', 'e', 'f', 'g'])
print('===== 原始数据 =====')
print(obj)
print('===== 索引、选择各种灵活的使用方式 =====')
print(obj['b'])
print(obj[1])
print(obj[1:3])
print(obj[['b', 'c']]) # obj['b', 'c'] 是错误的！
print(obj[[1, 2, 5]])
print(obj[obj < 5])
# 普通的Python切片是不包括尾巴的，但是请注意这里的切片！是包括的！！！
obj[1] = 1.5
print(obj)
# obj.index[1] = 2.5 # 错误
# print(obj) # 错误
# 从DataFrame里索引出一列，或者多列，方法类似于上面
data = pd.DataFrame(np.arange(16).reshape((4,4)), 
                    index=['Ohio', 'Colorado', 'Utah', 'New York'], 
                    columns=['one', 'two', 'three', 'four'])
print('===== 原始数据 =====')
print(data)
print(data['two'])
print(data[['two', 'four']])
# 根据一个布尔值数组切片或者选择数据
print(data[:2]) # 这里表示是取整个数据的前2部分
print('===== data[data["three"] > 5] =====')
print(data[data['three'] > 5])
data[data > 5] = 0
print(data)

# loc iloc使用
data = pd.DataFrame(np.arange(16).reshape((4,4)), 
                    index=['Ohio', 'Colorado', 'Utah', 'New York'], 
                    columns=['one', 'two', 'three', 'four'])
print('===== 原始数据 =====')
print(data)
print(data.loc['Colorado', ['two', 'four']])
print(data.iloc[2, [3, 0, 1]])