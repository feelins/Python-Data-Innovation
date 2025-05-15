#!/usr/bin/env python
# -*-coding:utf-8 -*-
'''
@File    :   p02_6-1-1_read_chunk_file.py
@Time    :   2023/06/27 17:46:20
@Author  :   Feelins Shao 
@Version :   1.0
@Contact :   feipengshao@163.com
@License :   (C)Copyright 2022-2023, Feelins Shao
@Desc    :   6.1.1 分块读入文本文件
'''
import pandas as pd

pd.options.display.max_rows = 10

df = pd.read_csv('Part-02\P02_007_Python_for_Data_Analysis\Chap06\ex6.csv')
print(df)
#     a   b   c   d   e          message
# 0   1   2   3   4   5      hello world
# 1   4   8  16  17  18      how are you
# 2   8   9  10  11  12  you are welcome
# 3   1   2   3   4   5      hello world
# 4   4   8  16  17  18      how are you
# .. ..  ..  ..  ..  ..              ...
# 25  4   8  16  17  18      how are you
# 26  8   9  10  11  12  you are welcome
# 27  1   2   3   4   5      hello world
# 28  4   8  16  17  18      how are you
# 29  8   9  10  11  12  you are welcome

# [30 rows x 6 columns]

chunker = pd.read_csv('Part-02\P02_007_Python_for_Data_Analysis\Chap06\ex6.csv', chunksize=1000)
for chunk in chunker:
    print(chunk)