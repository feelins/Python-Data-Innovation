#!/usr/bin/env python
# -*-coding:utf-8 -*-
'''
@File    :   p02_007_4-1-1_create_ndarray.py
@Time    :   2023/12/26 20:24:11
@Author  :   Feelins Shao 
@Version :   1.0
@Contact :   feipengshao@163.com
@License :   (C)Copyright 2022-2023, Feelins Shao
@Desc    :   4.1.1 生成ndarray
'''


import logging, time
import numpy as np

if __name__ == '__main__':

    # 记录开始运行时间
    start_time = time.time()
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
    logging.info('开始: ')
    
    data1 = [6, 7.5, 8, 0, 1.]
    arr1 = np.array(data1)
    print(arr1)

    data2 = [[1, 2, 3, 4], [5, 6, 7, 8]]
    arr2 = np.array(data2)
    print(arr2)
    print(arr2.ndim)
    print(arr2.shape)

    # 使用zeros创建全0数组
    arr3 = np.zeros(10)
    print(arr3)
    arr4 = np.zeros((3, 5))
    print(arr4)

    # 使用ones可以创建全1的数组
    arr5 = np.ones((5, 2))
    print(arr5)

    # 使用empty创建没有初始化的数组
    arr6 = np.empty((2, 3, 2))
    print(arr6)



    # 记录结束时间，计算运行时间
    end_time = time.time()
    total_time = end_time - start_time
    logging.info('结束：')
    logging.info(f'总共用时: {total_time:.2f}秒')
    logging.info('Done!')