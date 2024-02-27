#!/usr/bin/env python
# -*-coding:utf-8 -*-
'''
@File    :   p01_016_bool.py
@Time    :   2024/02/27 18:40:04
@Author  :   Feelins Shao 
@Version :   1.0
@Contact :   feipengshao@163.com
@License :   (C)Copyright 2022-2024, Feelins Shao
@Desc    :   None
'''


import logging, time

if __name__ == '__main__':

    # 记录开始运行时间
    start_time = time.time()
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
    logging.info('开始: ')
    
    bi8bo = '佳'
    if bi8bo is '斯佳':
        print('YES')
    else:
        print('NO')

    bi8bo = '男生'
    judge = not ( bi8bo is '女生' )
    if judge:
        print('YES')
    else:
        print('NO')

    # A. YES YES
    # B. YES NO
    # C. NO YES
    # D. NO NO


    # 记录结束时间，计算运行时间
    end_time = time.time()
    total_time = end_time - start_time
    logging.info('结束：')
    logging.info(f'总共用时: {total_time:.2f}秒')
    logging.info('Done!')