#!/usr/bin/env python
# -*-coding:utf-8 -*-
'''
@File    :   p02_007_7-2-3_replace_values.py
@Time    :   2023/12/20 13:42:18
@Author  :   Feelins Shao 
@Version :   1.0
@Contact :   feipengshao@163.com
@License :   (C)Copyright 2022-2023, Feelins Shao
@Desc    :   7.2.3 替代值
'''


import logging, time
import pandas as pd
import numpy as np

if __name__ == '__main__':

    # 记录开始运行时间
    start_time = time.time()
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
    logging.info('开始: ')
    
    # 前面的fillna填充缺失值，是通用值替换的一个特殊案例
    df = pd.read_csv(r'result_duration_pitch.txt', sep='\t')
    df = df.iloc[:, 1:3]
    print(df)   

    # 我们准备把name里的sil换成SP
    print(df['name'].replace('sil', 'SP'))
    cv_dict = {'h': 'C', 'a': 'V', 'er': 'V', 'p': 'C', 'u': 'V', 'ei': 'V', 'uai': 'V', 's': 'C', 'uen': 'V', 'h': 'C', 'ua': 'V', 't': 'C', 'i': 'V', 'sil': 'C'}
    # 映射表
    df['CV'] = df['name'].replace(cv_dict)
    print(df)

    # 也可以通过替代值的列表
    data = pd.Series([1., -999, 2., -999, 3.5, -999, 4.2, -1000])
    print(data)
    new_data = data.replace([-999, -1000], [np.nan, 0])
    print(new_data)


    # 记录结束时间，计算运行时间
    end_time = time.time()
    total_time = end_time - start_time
    logging.info('结束：')
    logging.info(f'总共用时: {total_time:.2f}秒')
    logging.info('Done!')