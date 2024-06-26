#!/usr/bin/env python
# -*-coding:utf-8 -*-
'''
@File    :   p02_007_4-1-0_ndarray.py
@Time    :   2023/12/26 20:08:26
@Author  :   Feelins Shao 
@Version :   1.0
@Contact :   feipengshao@163.com
@License :   (C)Copyright 2022-2023, Feelins Shao
@Desc    :   4.1 Numpy ndarray: 多维数组对象
'''


import logging, time
import numpy as np

if __name__ == '__main__':

    # 记录开始运行时间
    start_time = time.time()
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
    logging.info('开始: ')
    
    data = np.random.randn(2, 3)
    print(data)

    print(data * 10)
    print(data.shape)
    print(data.dtype)


    # 记录结束时间，计算运行时间
    end_time = time.time()
    total_time = end_time - start_time
    logging.info('结束：')
    logging.info(f'总共用时: {total_time:.2f}秒')
    logging.info('Done!')