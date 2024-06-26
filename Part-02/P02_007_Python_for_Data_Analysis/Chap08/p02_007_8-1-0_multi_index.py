#!/usr/bin/env python
# -*-coding:utf-8 -*-
'''
@File    :   p02_007_8-1-0_multi_index.py
@Time    :   2023/12/25 17:39:03
@Author  :   Feelins Shao 
@Version :   1.0
@Contact :   feipengshao@163.com
@License :   (C)Copyright 2022-2023, Feelins Shao
@Desc    :   8.1 分层索引
'''


import logging, time
import pandas as pd
import numpy as np

if __name__ == '__main__':

    # 记录开始运行时间
    start_time = time.time()
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
    logging.info('开始: ')
    
    data = pd.Series(np.random.randn(9), index=[['a', 'a', 'a', 'b', 'b', 'c', 'c', 'd', 'd'], [1, 2, 3, 1, 3, 1, 2, 2, 3]])
    logging.info('在一个轴向上拥有多个索引层级')
    print(data)
    logging.info('使用MultiIndex作为索引的美化视图')
    print(data.index)
    print(data['b'])
    print(data['b' : 'c'])
    print(data.loc[['b', 'd']])
    print(data.loc[:, 2]) # 这个代表是a, b, c，第一层的所有行，这里面所有第二层索引为2的值
    print(data.unstack())

    # 每个轴都可以拥有分层索引
    frame = pd.DataFrame(np.arange(12).reshape((4, 3)), index=[['ab', 'ac', 'bc', 'bd'], [1, 2, 1, 2]], columns=[['Ohio', 'Ohio', 'Colorado'], ['Green', 'Red', 'Green']])
    print(frame)
    logging.info('分层的层级可以有名称')
    frame.index.names = ['key1', 'key2']
    frame.columns.names = ['state', 'color']
    print(frame)
    print(frame['Ohio'])



    # 记录结束时间，计算运行时间
    end_time = time.time()
    total_time = end_time - start_time
    logging.info('结束：')
    logging.info(f'总共用时: {total_time:.2f}秒')
    logging.info('Done!')