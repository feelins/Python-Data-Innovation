#!/usr/bin/env python
# -*-coding:utf-8 -*-
'''
@File    :   p02_5-2-2_drop_items.py
@Time    :   2023/06/25 17:49:19
@Author  :   Feelins Shao 
@Version :   1.0
@Contact :   feipengshao@163.com
@License :   (C)Copyright 2022-2023, Feelins Shao
@Desc    :   5.2.2 轴向上删除条目
'''

import pandas as pd
import numpy as np

data = pd.DataFrame(np.arange(16).reshape((4,4)), 
                    index=['Ohio', 'Colorado', 'Utah', 'New York'], 
                    columns=['one', 'two', 'three', 'four'])
print('===== 原始数据 =====')
print(data)
print('===== 删除Colorado, Ohio =====')
print(data.drop(['Colorado', 'Ohio']))
print('===== 删除列轴上的two =====')
print(data.drop('two', axis=1))
print('===== 删除列轴上的four =====')
print(data.drop('two', axis='columns'))
print('===== 删除列轴上的four =====')
print(data.drop('two', axis='columns', inplace=True))
print('===== 原始数据已经发生变化 =====')
print(data)