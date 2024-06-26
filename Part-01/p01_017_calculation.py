#!/usr/bin/env python
# -*-coding:utf-8 -*-
'''
@File    :   p01_017_calculation.py
@Time    :   2024/02/29 09:14:39
@Author  :   Feelins Shao 
@Version :   1.0
@Contact :   feipengshao@163.com
@License :   (C)Copyright 2022-2024, Feelins Shao
@Desc    :   017: 基本的计算
'''


import logging, time

if __name__ == '__main__':

    # 记录开始运行时间
    start_time = time.time()
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
    logging.info('开始: ')
    
    a = 10
    b = 20
    a += b        # 相当于：a = a + b
    a *= a + 50   # 相当于：a = a * (a + 50)
    print(a)      # 这里会输出？

    # A. 60
    # B. 2400
    # C. 100
    # D. 600


    # 记录结束时间，计算运行时间
    end_time = time.time()
    total_time = end_time - start_time
    logging.info('结束：')
    logging.info(f'总共用时: {total_time:.6f}秒')
    logging.info('Done!')