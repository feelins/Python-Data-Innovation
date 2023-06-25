#!/usr/bin/env python
# -*-coding:utf-8 -*-
'''
@File    :   p02_5-2-1_rebuild_index.py
@Time    :   2023/06/25 17:16:52
@Author  :   Feelins Shao 
@Version :   1.0
@Contact :   feipengshao@163.com
@License :   (C)Copyright 2022-2023, Feelins Shao
@Desc    :   5.2.1 重建索引
'''
import pandas as pd

obj = pd.Series([4.5, 7.2, -5.3, 3.6], index=['d', 'a', 'c', 'b'])
print(obj)

# Series调用reindex方法时，会将数据按新的索引进行排列，不存在的索引值会引入缺失值
obj2 = obj.reindex(['a', 'b', 'c', 'd', 'e', 'f'])
print(obj2)
# a    7.2
# b    3.6
# c   -5.3
# d    4.5
# e    NaN
# f    NaN

# 顺序数据，比如时间序列等，需要插值或者填值，method允许我们使用如ffill，向前插值的方法填充
obj3 = pd.Series(['blue', 'purple', 'yellow'], index=[0, 3, 7])
print(obj3)
print(obj3.reindex(range(10), method='nearest')) # method: backfill, ffill, bfill, nearest, pad

# DataFrame中，reindex可以改变行索引、列索引