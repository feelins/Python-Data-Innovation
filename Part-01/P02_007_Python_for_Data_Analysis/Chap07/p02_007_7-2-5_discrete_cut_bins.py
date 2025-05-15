#!/usr/bin/env python
# -*-coding:utf-8 -*-
'''
@File    :   p02_007_7-2-5_discrete_cut_bins.py
@Time    :   2023/12/20 15:58:32
@Author  :   Feelins Shao 
@Version :   1.0
@Contact :   feipengshao@163.com
@License :   (C)Copyright 2022-2023, Feelins Shao
@Desc    :   7.2.5 离散化和分箱
'''


import logging, time
import pandas as pd

if __name__ == '__main__':

    # 记录开始运行时间
    start_time = time.time()
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
    logging.info('开始: ')
    
    ages = [20, 22, 25, 27, 21, 23, 37, 31, 61, 45, 41, 32]
    bins = [18, 25, 35, 60, 100]
    # 通过right=False，决定这个分箱的区间，是左开右闭，还是左闭右开，貌似没有全封闭，和全开？？
    cats = pd.cut(ages, bins, right=False)
    print(cats)
    print(cats.codes)
    print(pd.value_counts(cats))
    # 增加一个labels来自定义箱名
    group_names = ['Youth', 'YoungAdult', 'MiddleAges', 'Senior']
    print('----- 增加一个labels来自定义箱名 -----')
    print(pd.cut(ages, bins, right=False, labels=group_names))

    print('----- 可以根据最大值，最小值，计算出平均出来的箱区间 -----')
    df = pd.read_csv(r'result_duration_pitch.txt', sep='\t')
    df = df.iloc[:, 2:3]
    dd = pd.Series(df['duration'].values)
    print(dd)
    cats = pd.cut(dd, 4, precision=3)
    print(cats)
    print(pd.value_counts(cats))
    print('----- 使用qcut 分位数的形式 -----')
    cats = pd.qcut(dd, 4)
    print(cats)
    print(pd.value_counts(cats))
    print('----- 使用qcut 分位数，也可以自定义一个区间 -----')
    cats = pd.qcut(dd, [0, 0.7, 1.])
    print(cats)
    print(pd.value_counts(cats))


    # 记录结束时间，计算运行时间
    end_time = time.time()
    total_time = end_time - start_time
    logging.info('结束：')
    logging.info(f'总共用时: {total_time:.2f}秒')
    logging.info('Done!')