#!/usr/bin/env python
# -*-coding:utf-8 -*-
'''
@File    :   p02_007_8-1-2_sumup_by_levels.py
@Time    :   2023/12/25 19:41:41
@Author  :   Feelins Shao 
@Version :   1.0
@Contact :   feipengshao@163.com
@License :   (C)Copyright 2022-2023, Feelins Shao
@Desc    :   8.1.2 按层级进行汇总统计
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
    
    frame.index.names = ['key1', 'key2']
    frame.columns.names = ['state', 'color']
    print(frame)
    
    # print(frame.sum(level='key2', axis=0)) #??????????????????????????
# Out[27]: 
# state  Ohio     Colorado
# color Green Red    Green
# key2                    
# 1         6   8       10
# 2        12  14       16

# In [28]: frame.sum(level='color', axis=1)
# Out[28]: 
# color      Green  Red
# key1 key2            
# a    1         2    1
#      2         8    4
# b    1        14    7
#      2        20   10


    # 记录结束时间，计算运行时间
    end_time = time.time()
    total_time = end_time - start_time
    logging.info('结束：')
    logging.info(f'总共用时: {total_time:.2f}秒')
    logging.info('Done!')