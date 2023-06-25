#!/usr/bin/env python
# -*-coding:utf-8 -*-
'''
@File    :   p02_5-1-3_index_object.py
@Time    :   2023/06/25 16:57:17
@Author  :   Feelins Shao 
@Version :   1.0
@Contact :   feipengshao@163.com
@License :   (C)Copyright 2022-2023, Feelins Shao
@Desc    :   None
'''
import pandas as pd

# pandas的索引对象是用于存储轴标签和其它元数据的，它的使用比较灵活，比如可以切片使用；
obj = pd.Series(range(3), index=['a', 'b', 'c'])
print(obj.index)
print(obj.index[1:])

# 上述索引对象可以共享给其它数据结构使用
# 索引对象是不可变的，比如index[1] = 'd'；是错误的，这使得共享比较安全
obj2 = pd.Series([1.5, -2.5, 3], index=obj.index)
print(obj2)