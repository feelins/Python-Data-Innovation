#!/usr/bin/env python
# -*-coding:utf-8 -*-
'''
@File    :   p02_007_4-1-4_basic_index_and_slice.py
@Time    :   2023/12/27 19:16:57
@Author  :   Feelins Shao 
@Version :   1.0
@Contact :   feipengshao@163.com
@License :   (C)Copyright 2022-2023, Feelins Shao
@Desc    :   4.1.4 基础索引与切片
'''


import logging, time
import numpy as np

if __name__ == '__main__':

    # 记录开始运行时间
    start_time = time.time()
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
    logging.info('开始: ')
    
    arr = np.random.randn(10)
    print('输出原数组')
    print(arr)
    print('输出原数组，第6个元素')
    print(arr[5])
    print('输出原数组，第6-7个元素')
    print(arr[5:7])
    print('切片也可以传递值')
    arr[5:7] = 0.888
    print(arr)
    print('切片的内容并不是复制')
    arr_slice = arr[3:7]
    arr_slice[0] = 0.9999
    print(arr)
    print('不写切片值将会输出所有值[:]')
    print(arr[:])
    print('如何想要拷贝，需要用copy()')
    arr_slice_copy = arr[3:7].copy()
    arr_slice_copy[0] = 0.000
    print(arr)

    print('二维数组')
    arr2d = np.array([[1, 2, 3], [3, 4, 5]])
    print('二维数组，第一维')
    print(arr2d[0])
    print('二维数组，索引单个元素，可通过以下两种方式')
    print(arr2d[0][2])
    print(arr2d[0, 2])

    print('三维数组')
    arr3d = np.array([[[1, 1, 1], [2, 2, 2]], [[3, 3, 3], [4, 4, 4]]])
    print(arr3d)
    print('索引0，是一个2*3的数组')
    print(arr3d[0])
    print('标量，数组都可以传递给arr3d[0]')
    tmp_values = np.array([[6, 6, 6], [7, 7, 7]])
    arr3d[0] = 88
    print(arr3d)
    arr3d[0] = tmp_values
    print(arr3d)

    print('两个索引，返回的是一个一维数组')
    print(arr3d[1, 0])

    logging.info('4.1.4.1 数组的切片索引')
    arr2d = np.array([[1, 2, 3], [3, 4, 5]])
    print(arr2d)
    print('选择前两行')
    print(arr2d[:2])
    print('进行多组切片，选择前2行，每一行的第2个元素往后')
    print(arr2d[:2, 1:])
    print('选择第2行，只选择前两列')
    print(arr2d[1, :2])
    print('选择第2列，只选择前一行')
    print(arr2d[:1, 1])


    

    # 记录结束时间，计算运行时间
    end_time = time.time()
    total_time = end_time - start_time
    logging.info('结束：')
    logging.info(f'总共用时: {total_time:.2f}秒')
    logging.info('Done!')