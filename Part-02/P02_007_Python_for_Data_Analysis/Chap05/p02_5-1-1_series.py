#!/usr/bin/env python
# -*-coding:utf-8 -*-
'''
@File    :   p02_5-1-1_series.py
@Time    :   2023/06/19 20:46:30
@Author  :   Feelins Shao 
@Version :   1.0
@Contact :   feipengshao@163.com
@License :   (C)Copyright 2022-2023, Feelins Shao
@Desc    :   None
'''
import pandas as pd
import numpy as np
from pandas import Series, DataFrame

obj = Series([4, 7, -5, 3])
print('------- The basic usage, like 1d-Array Numpy -------')
print(obj)
print(obj.values)
print(obj.index) # default index from 0 --> N-1

# 我们可以指定索引，甚至是各种类型
print('------- The given index values -------')
obj2 = Series([4, 7, -5, 3], index=['d', 'e', 'a', 'b'])
print(obj2)
print(obj2.values)
print(obj2.index)

# 以下这两种方式都可以访问到第2个元素，第一种甚至比较优雅，第二种是直接可以使用默认的索引值；这是Series的优点
print(obj2.e)
print(obj2[1])

# 以下的过滤更是简练，我们直接通过比较得到比0大的元素，作为index，输出所有元素
print(obj2[obj2 > 0])

# 同样，也可以直接计算
print(obj2 * 3)
print(np.exp(obj2))

# 判断是否存在，直接使用键是可以的，使用值不可以 by Feelins Shao
print(4 in obj2) # False
print('d' in obj2) # True

# 我们已经有一个字典，可以将它转化成Series
formant_values = {'a': 1200, 'o': 899, 'i': 700, 'u': 2000}
series_formant = pd.Series(formant_values)
print(series_formant)
# 得到的结果是，并不是象书上写的，是排序好的？？？
# a    1200
# o     899
# i     700
# u    2000

vowels = ['a', 'i', 'u', 'e']
series_formant_order = pd.Series(series_formant, index=vowels)
print(series_formant_order)
# Series对象本身，和索引都可以指定name属性
series_formant_order.name = 'Formant - F1'
series_formant_order.index.name = 'Vowel'
print(series_formant_order)
# 可以直接按位，修改索引值
series_formant_order.index = ['aa', 'ii', 'uu', 'ee']
print(series_formant_order)
