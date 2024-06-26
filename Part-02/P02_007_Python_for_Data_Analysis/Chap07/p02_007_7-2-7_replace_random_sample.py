#!/usr/bin/env python
# -*-coding:utf-8 -*-
'''
@File    :   p02_007_7-2-7_replace_random_sample.py
@Time    :   2023/12/22 13:38:53
@Author  :   Feelins Shao 
@Version :   1.0
@Contact :   feipengshao@163.com
@License :   (C)Copyright 2022-2023, Feelins Shao
@Desc    :   7.2.7 转换和随机抽样
'''


import logging, time
import pandas as pd
import numpy as np

if __name__ == '__main__':

    # 记录开始运行时间
    start_time = time.time()
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
    logging.info('开始: ')
    

    df = pd.DataFrame(np.arange(5 * 4).reshape((5, 4)))
    print(df)
    sampler = np.random.permutation(5)
    print(sampler)
    print('----- 使用take函数获取转换后的结果 -----')
    print(df.take(sampler))

    # 选出一个不含有替代值的随机子集
    # 生成一个带有替代值的样本????

    # 记录结束时间，计算运行时间
    end_time = time.time()
    total_time = end_time - start_time
    logging.info('结束：')
    logging.info(f'总共用时: {total_time:.2f}秒')
    logging.info('Done!')