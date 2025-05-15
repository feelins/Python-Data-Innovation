#!/usr/bin/env python
# -*-coding:utf-8 -*-
'''
@File    :   p02_007_7-2-2_trans_data_with_map_dict_or_function.py
@Time    :   2023/12/19 13:55:16
@Author  :   Feelins Shao 
@Version :   1.0
@Contact :   feipengshao@163.com
@License :   (C)Copyright 2022-2023, Feelins Shao
@Desc    :   None
'''


import logging, time
import pandas as pd

if __name__ == '__main__':

    # 记录开始运行时间
    start_time = time.time()
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
    logging.info('开始: ')

    df = pd.read_csv(r'result_duration_pitch.txt', sep='\t')
    df = df.iloc[:, 1:3]
    print(df)   

    cv_dict = {'h': 'C', 'a': 'V', 'er': 'V', 'p': 'C', 'u': 'V', 'ei': 'V', 'uai': 'V', 's': 'C', 'uen': 'V', 'h': 'C', 'ua': 'V', 't': 'C', 'i': 'V', 'sil': 'C'}
    # 映射表
    df['CV'] = df['name'].map(cv_dict)
    print(df)

    # 也可以通过映射函数实现
    df['CVCV'] = df['name'].map(lambda x: cv_dict[x.lower()])
    print(df)


    # 记录结束时间，计算运行时间
    end_time = time.time()
    total_time = end_time - start_time
    logging.info('结束：')
    logging.info(f'总共用时: {total_time:.2f}秒')
    logging.info('Done!')