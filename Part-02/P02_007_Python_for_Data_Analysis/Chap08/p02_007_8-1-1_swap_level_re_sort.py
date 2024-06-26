#!/usr/bin/env python
# -*-coding:utf-8 -*-
'''
@File    :   p02_007_8-1-1_swap_level_re_sort.py
@Time    :   2023/12/25 19:35:31
@Author  :   Feelins Shao 
@Version :   1.0
@Contact :   feipengshao@163.com
@License :   (C)Copyright 2022-2023, Feelins Shao
@Desc    :   8.1.1 重排序和层级排序
'''


import logging, time
import pandas as pd
import numpy as np

if __name__ == '__main__':

    # 记录开始运行时间
    start_time = time.time()
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
    logging.info('开始: ')
    
    frame = pd.DataFrame(np.arange(12).reshape((4, 3)), index=[['ab', 'ac', 'bc', 'bd'], [1, 2, 1, 2]], columns=[['Ohio', 'Ohio', 'Colorado'], ['Green', 'Red', 'Green']])
    print(frame)
    frame.index.names = ['key1', 'key2']
    frame.columns.names = ['state', 'color']
    logging.info('swaplevel接收两个层级的序号，或者层级名称，顺序变化了之后，数据不变')
    print(frame.swaplevel('key1', 'key2'))
    print(frame.swaplevel(0, 1))
    logging.info('sort_index在单一层级上对数据！！！进行排序')
    print(frame.sort_index(level=1))


    # 记录结束时间，计算运行时间
    end_time = time.time()
    total_time = end_time - start_time
    logging.info('结束：')
    logging.info(f'总共用时: {total_time:.2f}秒')
    logging.info('Done!')