#!/usr/bin/env python
# -*-coding:utf-8 -*-
'''
@File    :   p02_007_4-0-0_numpy_more_fast.py
@Time    :   2023/12/26 19:58:21
@Author  :   Feelins Shao 
@Version :   1.0
@Contact :   feipengshao@163.com
@License :   (C)Copyright 2022-2023, Feelins Shao
@Desc    :   4. numpy更高效
'''


import logging, time
import numpy as np

if __name__ == '__main__':

    # 记录开始运行时间
    start_time = time.time()
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
    logging.info('开始: ')
    
    # my_arr = np.arange(10000000)
    # my_arr2 = my_arr * 2
    # 总共用时: 0.04秒

    my_list = list(range(10000000))
    my_list2 = [x * 2 for x in my_list]
    # 总共用时: 0.98秒
    
    # 记录结束时间，计算运行时间
    end_time = time.time()
    total_time = end_time - start_time
    logging.info('结束：')
    logging.info(f'总共用时: {total_time:.2f}秒')
    logging.info('Done!')