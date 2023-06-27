#!/usr/bin/env python
# -*-coding:utf-8 -*-
'''
@File    :   p02_6-1-0_read_write_txt.py
@Time    :   2023/06/27 15:51:27
@Author  :   Feelins Shao 
@Version :   1.0
@Contact :   feipengshao@163.com
@License :   (C)Copyright 2022-2023, Feelins Shao
@Desc    :   6.1 文本格式数据的读写
'''

import pandas as pd
import numpy as np

def read_write_txt():
    '''
    6.1 文本格式数据的读写
    '''
    # 6.1.1 读取文本格式数据
    # 首先使用read_csv读取文本格式数据
    df = pd.read_csv(r'Part-02\P02_007_Python_for_Data_Analysis\Chap06\ex1.csv')
    print(df)
    # 然后使用read_table读取文本格式数据
    df2 = pd.read_table(r'Part-02\P02_007_Python_for_Data_Analysis\Chap06\ex1.csv', sep=',')
    print(df2)
    # 有的文件并不包括表头，在读取时允许自动分配表头
    df3 = pd.read_table(r'Part-02\P02_007_Python_for_Data_Analysis\Chap06\ex2.csv', sep=',', header=None)
    print(df3)
    # 也可以自己指定表头
    df4 = pd.read_table(r'Part-02\P02_007_Python_for_Data_Analysis\Chap06\ex2.csv', sep=',', names=['A', 'B', 'C', 'D', 'E', 'MESSAGE'])
    print(df4)
    # 指定位置4的列为索引
    df5 = pd.read_table(r'Part-02\P02_007_Python_for_Data_Analysis\Chap06\ex2.csv', sep=',', names=['A', 'B', 'C', 'D', 'E', 'MESSAGE'], index_col='MESSAGE')
    print(df5)
    # 从多个列中形成一个分层索引
    df6 = pd.read_csv(r'Part-02\P02_007_Python_for_Data_Analysis\Chap06\csv_mindex.csv', index_col=['key1', 'key2'])
    print(df6)
    #            value1  value2
    # key1 key2
    # one  a          1       2
    #     b          3       4
    #     c          5       6
    #     d          7       8
    # two  a          9      10
    #     b         11      12
    #     c         13      14
    #     d         15      16
    # 有一些数据，会有一些附加信息，这些是不想读取的，这时候可以用skiprow
    df7 = pd.read_csv(r'Part-02\P02_007_Python_for_Data_Analysis\Chap06\ex4.csv', skiprows=[2])
    print(df7)
    # 6.1.2 写入文本格式数据

read_write_txt()