#!/usr/bin/env python
# -*-coding:utf-8 -*-
'''
@File    :   p02_007_7-1-2_complete_null_values.py
@Time    :   2023/12/19 09:45:37
@Author  :   Feelins Shao 
@Version :   1.0
@Contact :   feipengshao@163.com
@License :   (C)Copyright 2022-2023, Feelins Shao
@Desc    :   None
'''


import logging, time
import pandas as pd
from numpy import nan as NA
import numpy as np

if __name__ == '__main__':

    # 记录开始运行时间
    start_time = time.time()
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
    logging.info('开始: ')
    

    df = pd.DataFrame(np.random.randn(8, 4))
    df.iloc[2:4, 3] = NA
    df.iloc[5:7, 0] = NA
    df.iloc[:4, 1] = NA
    print(df)
    # 1. 赋值一个常数
    print(df.fillna(8.888))
    # 2. 可以分别对不同的列赋值不同的常数
    print(df.fillna({1: 8.888, 3: 9.999}))
    # 3. fillna是生成一个新的对象，但是也可以通过inplace=True修改本身，同样适用于Series
    data = pd.Series([1., NA, 3.5, NA, 7.])
    print(data.fillna(data.mean()))
    print(data)
    _ = data.fillna(data.mean(), inplace=True)
    print(data)
    print(df.fillna({1: 8.888, 3: 9.999}, inplace=True))
    print(df)
    # 4. 也可以使用一些插值方法
    df = pd.DataFrame(np.random.randn(8, 4))
    df.iloc[2:4, 3] = NA
    df.iloc[5:7, 0] = NA
    df.iloc[:4, 1] = NA
    print(df)
    print(df.fillna(method='ffill'))
    # 4.1 也可以限定插值，几个数值
    print(df.fillna(method='ffill', limit=1))
    # 4.2 如果设定axis=1呢
    print(df.fillna(method='ffill', limit=1, axis=1)) # 横着填充


    # 记录结束时间，计算运行时间
    end_time = time.time()
    total_time = end_time - start_time
    logging.info('结束：')
    logging.info(f'总共用时: {total_time:.2f}秒')
    logging.info('Done!')