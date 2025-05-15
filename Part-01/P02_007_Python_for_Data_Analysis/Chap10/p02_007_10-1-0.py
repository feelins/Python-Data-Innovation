#!/usr/bin/env python
# -*-coding:utf-8 -*-
'''
@File    :   p02_007_10-1-0.py
@Time    :   2024/03/07 18:57:04
@Author  :   Feelins Shao 
@Version :   1.0
@Contact :   feipengshao@163.com
@License :   (C)Copyright 2022-2024, Feelins Shao
@Desc    :   10.1 GroupBy机制
'''


import logging, time
import pandas as pd
import numpy as np

if __name__ == '__main__':

    # 记录开始运行时间
    start_time = time.time()
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
    logging.info('开始: ')
    

    df = pd.DataFrame({'gender' : ['男', '女', '女', '女', '男'],
                       'age' : ['16', '16', '17', '16', '18'],
                       'height' : [170, 162, 165, 172, 175],
                       'score' : [95, 98, 92, 99, 89]})
    
    grouped = df['height'].groupby(df['gender'])
    print(grouped)
    print(grouped.mean())

    # 记录结束时间，计算运行时间
    end_time = time.time()
    total_time = end_time - start_time
    logging.info('结束：')
    logging.info(f'总共用时: {total_time:.2f}秒')
    logging.info('Done!')