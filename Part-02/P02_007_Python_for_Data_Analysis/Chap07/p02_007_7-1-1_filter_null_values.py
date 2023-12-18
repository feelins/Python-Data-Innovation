#!/usr/bin/env python
# -*-coding:utf-8 -*-
'''
@File    :   p02_007_7-1-1_filter_null_values.py
@Time    :   2023/12/18 15:28:38
@Author  :   Feelins Shao 
@Version :   1.0
@Contact :   feipengshao@163.com
@License :   (C)Copyright 2022-2023, Feelins Shao
@Desc    :   7.1.1 过滤缺失值
'''


import logging, time
from numpy import nan as NA
import numpy as np
import pandas as pd

if __name__ == '__main__':

    # 记录开始运行时间
    start_time = time.time()
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
    logging.info('开始: ')

    # 可以通过pandas.isnull判断索引后，手工过滤
    # dropna是非常有用的
    # 在Series上使用dropna会返回非空的数据和索引值
    data = pd.Series([1, NA, 3.5, NA, 7.9])
    print(data)
    print('----- dropna之后 -----')
    print(data.dropna())
    
    # 在DataFrame上复杂一些，默认是删除所有包括NA的行
    data = pd.DataFrame([[1., 6.5, 3.], [5., NA, NA],
                         [NA, NA, NA], [NA, 6.9, 9.]])
    print(data)
    print('----- dropna之后 -----')
    print(data.dropna())

    # 引入how='all'参数， 将会只删除这一行里的元素全部为NA的行
    print(data)
    print('----- dropna how=''all'' 之后 -----')
    print(data.dropna(how='all'))

    # 以上两个操作删除列，则加一个axis=1
    data[4] = NA
    print(data)
    print('----- dropna-列 之后 -----')
    print(data.dropna(axis=1)) # 全部删除

    print(data)
    print('----- dropna-列 how=''all'' 之后 -----')
    print(data.dropna(axis=1, how='all')) # 只删除第4列

    # 实际应用中，通过thresh能够更灵活的控制对于空值数值的过滤
    
    df = pd.DataFrame(np.random.randn(8, 4))
    df.iloc[2:4, 3] = NA
    df.iloc[5:7, 0] = NA
    df.iloc[:4, 1] = NA
    print(df)
    # 例一：过滤每一行中，至少有3个非空值，不满足的过滤掉；
    print('----- 过滤每一行中，至少有3个非空值，不满足的过滤掉 -----')
    print(df.dropna(thresh=3)) # 只保留了0，1，4，6，7行
    # 例二：过滤每一行中，至少有70%的非空值的部分；
    print('----- 过滤每一行中，至少有80%的非空值的部分 -----')
    print(df.dropna(thresh=0.8 * len(df.columns))) # 只保留了4，7行
    # 例三：过滤每一列中，至少有5个非空值，不满足的过滤掉；
    print('----- 过滤每一列中，至少有5个非空值，不满足的过滤掉 -----')
    print(df.dropna(thresh=5, axis=1)) # 只保留了0，2, 3列
    # 例三：过滤每一列中，至少有80%非空值，不满足的过滤掉；
    print('----- 过滤每一列中，至少有80%非空值，不满足的过滤掉 -----')
    print(df.dropna(thresh=0.8 * len(df), axis=1)) # 只保留了2列



    # 记录结束时间，计算运行时间
    end_time = time.time()
    total_time = end_time - start_time
    logging.info('结束：')
    logging.info(f'总共用时: {total_time:.2f}秒')
    logging.info('Done!')