#!/usr/bin/env python
# -*-coding:utf-8 -*-
'''
@File    :   p02_5-1-2_DataFrame.py
@Time    :   2023/06/21 15:05:48
@Author  :   Feelins Shao 
@Version :   1.0
@Contact :   feipengshao@163.com
@License :   (C)Copyright 2022-2023, Feelins Shao
@Desc    :   None
'''
import pandas as pd

data = {'state': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada', 'Nevada'],
        'year': [2000, 2001, 2002, 2001, 2003, 2003],
        'pop': [1.5, 1.7, 3.6, 2.4, 2.9, 3.2]}
frame = pd.DataFrame(data)
print(frame)
# DataFrame自动分配索引
#     state  year  pop
# 0    Ohio  2000  1.5
# 1    Ohio  2001  1.7
# 2    Ohio  2002  3.6
# 3  Nevada  2001  2.4
# 4  Nevada  2003  2.9
# 5  Nevada  2003  3.2

# 对于大型的DataFrame, head方法将会只显示前5行数据 
print(frame.head())

# 你可以指定列的显示顺序
print(pd.DataFrame(data, columns=['year', 'pop', 'state']))

# 同样，也可以指定索引
frame2 = pd.DataFrame(data, columns=['year', 'pop', 'state'], index=['i', 'ii', 'iii', 'iiii', 'v', 'vi'])
print(frame2)
# 可以象Series那样，检索字段
print(frame2.state)
print(frame2['state'])

# 我们可以将一个Series赋值给一列，Series的索引将会按照DataFrame的索引重新排列，在空缺的地方填上缺失值NaN，不存在的键，被舍弃
val = pd.Series([-1.6, 1.8, 2.2, -0.5], index=['ii', 'iii', 'v', 'vii'])
frame2['debt'] = val
# frame2.debt = val # 这里会报错，这个读法无法创建新的列，要使用上面的方法
print(frame2)
#       year  pop   state  debt
# i     2000  1.5    Ohio   NaN
# ii    2001  1.7    Ohio  -1.6
# iii   2002  3.6    Ohio   1.8
# iiii  2001  2.4  Nevada   NaN
# v     2003  2.9  Nevada   2.2
# vi    2003  3.2  Nevada   NaN

# 遇到包含字典的嵌套字典时，被赋值给DataFrame时，字典的键作为列，内部字典的键值作为行索引
pop = {'Nevada': {2001: 2.4, 2002: 2.9},
       'Ohio': {2000: 1.5, 2001: 1.7, 2002: 3.6}}
frame3 = pd.DataFrame(pop)
print(frame3)
#      Nevada  Ohio
# 2001     2.4   1.7
# 2002     2.9   3.6
# 2000     NaN   1.5
# 可以使用转置操作
print(frame3.T)