#!/usr/bin/env python
# -*-coding:utf-8 -*-
'''
@File    :   p02_5-2-4_integer_index.py
@Time    :   2023/06/26 20:10:41
@Author  :   Feelins Shao 
@Version :   1.0
@Contact :   feipengshao@163.com
@License :   (C)Copyright 2022-2023, Feelins Shao
@Desc    :   5.2.4 整数索引
'''
import pandas as pd
import numpy as np

ser = pd.Series(np.arange(3.))
print(ser)
# print(ser[-1]) # 报错，没看懂书上的描述，到底这样算不算错？？？

ser2 = pd.Series(np.arange(3.), index=['a', 'b', 'c'])

# 为了保持一致性，数据选择时请始终使用标签索引，为了精确处理，使用loc, iloc更好