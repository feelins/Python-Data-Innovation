#!/usr/bin/env python
# -*-coding:utf-8 -*-
'''
@File    :   p02_007_6-1-2_write_to_csv.py
@Time    :   2023/07/03 18:38:21
@Author  :   Feelins Shao 
@Version :   1.0
@Contact :   feipengshao@163.com
@License :   (C)Copyright 2022-2023, Feelins Shao
@Desc    :   6.1.2 将数据写入csv文件
'''

import pandas as pd

data = pd.read_csv('Part-02/P02_007_Python_for_Data_Analysis/Chap06/ex1.csv')
print(data)
#    a   b   c   d   e          message
# 0  1   2   3   4   5      hello world
# 1  4   8  16  17  18      how are you
# 2  8   9  10  11  12  you are welcome

data.to_csv('Part-02/P02_007_Python_for_Data_Analysis/Chap06/ex1_out.csv') # 将数据导出为逗号分隔的文件
# ,a, b, c, d, e,message
# 0,1,2,3,4,5,hello world
# 1,4,8,16,17,18,how are you
# 2,8,9,10,11,12,you are welcome

data.to_csv('Part-02/P02_007_Python_for_Data_Analysis/Chap06/ex1_out2.csv', index=False, header=False) # 可以禁止写入索引，和表头
# 1,2,3,4,5,hello world
# 4,8,16,17,18,how are you
# 8,9,10,11,12,you are welcome

data.to_csv('Part-02/P02_007_Python_for_Data_Analysis/Chap06/ex1_out3.csv', sep='|')
# |a| b| c| d| e|message
# 0|1|2|3|4|5|hello world
# 1|4|8|16|17|18|how are you
# 2|8|9|10|11|12|you are welcome

data.to_csv('Part-02/P02_007_Python_for_Data_Analysis/Chap06/ex1_out4.csv', na_rep='NULL') # 缺失值替换为NULL
print(data.columns)
data.to_csv('Part-02/P02_007_Python_for_Data_Analysis/Chap06/ex1_out5.csv', index=False, columns=['a', 'd']) # 只保存指定的两列
# 这一句一直在报错