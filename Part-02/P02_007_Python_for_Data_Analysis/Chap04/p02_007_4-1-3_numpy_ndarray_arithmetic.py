#!/usr/bin/env python
# -*-coding:utf-8 -*-
'''
@File    :   p02_007_4-1-3_numpy_ndarray_arithmetic.py
@Time    :   2023/12/27 15:08:02
@Author  :   Feelins Shao 
@Version :   1.0
@Contact :   feipengshao@163.com
@License :   (C)Copyright 2022-2023, Feelins Shao
@Desc    :   4.1.3 NumPy数组算术
'''


import logging, time
import numpy as np

if __name__ == '__main__':

    # 记录开始运行时间
    start_time = time.time()
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
    logging.info('开始: ')
    
    arr = np.array([[1., 2., 3.], [4., 5., 6.]])
    print(arr)
    print(arr + arr)
    print(arr * arr)

    arr2 = np.array([[0., 4., 1.], [7., 2.,16.]])
    print(arr > arr2)



    # 记录结束时间，计算运行时间
    end_time = time.time()
    total_time = end_time - start_time
    logging.info('结束：')
    logging.info(f'总共用时: {total_time:.2f}秒')
    logging.info('Done!')