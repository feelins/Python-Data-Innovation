#!/usr/bin/env python
# -*-coding:utf-8 -*-
'''
@File    :   p02_007_8-2-1_merge_concat_dataset_style.py
@Time    :   2023/12/26 17:13:17
@Author  :   Feelins Shao 
@Version :   1.0
@Contact :   feipengshao@163.com
@License :   (C)Copyright 2022-2023, Feelins Shao
@Desc    :   8.2.1 数据库风格的DataFrame连接
'''


import logging, time
import pandas as pd


if __name__ == '__main__':

    # 记录开始运行时间
    start_time = time.time()
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
    logging.info('开始: ')
    
    df1 = pd.DataFrame({'key' : ['b', 'b', 'a', 'c', 'a', 'a', 'b'], 'data1' : range(7)})
    df2 = pd.DataFrame({'key' : ['a', 'b', 'd'], 'data2' : range(3)})

    print(df1)
    print(df2)

    print(pd.merge(df1, df2))

    # 为什么缺少c, d？merge默认情况下做的是inner，内连接，按交集
    logging.info('how = left')
    print(pd.merge(df1, df2, how='left'))
    logging.info('how = right')
    print(pd.merge(df1, df2, how='right'))
    logging.info('how = outer')
    print(pd.merge(df1, df2, how='outer'))

    # 书上讲的让我头晕，看一个其它例子
    d1 = {'Name': ['Pankaj', 'Meghna', 'Lisa'], 'Country': ['India', 'India', 'USA'], 'Role': ['CEO', 'CTO', 'CTO']}
    df1 = pd.DataFrame(d1)
    print('DataFrame 1:\n', df1)
    df2 = pd.DataFrame({'ID': [1, 2, 3], 'Name': ['Pankaj', 'Anupam', 'Amit']})
    print('DataFrame 2:\n', df2)
    df_merged = pd.merge(df1, df2)
    print('Result:\n', df_merged)
    df_merged_outer = pd.merge(df1, df2, how='outer')
    print('Result outer:\n', df_merged_outer)

    d1 = {'Name': ['Pankaj', 'Meghna', 'Lisa'], 'ID': [1, 2, 3], 'Country': ['India', 'India', 'USA'], 'Role': ['CEO', 'CTO', 'CTO']}
    df1 = pd.DataFrame(d1)
    print('DataFrame 1:\n', df1)
    df2 = pd.DataFrame({'ID': [1, 2, 3], 'Name': ['Pankaj', 'Anupam', 'Amit']})
    print('DataFrame 2:\n', df2)

    # 指定一个key合并，这时候如果两个有不同的项，会用Name_x, Name_y表示
    print(df1.merge(df2, on='ID'))
    print(df1.merge(df2, on='Name'))





    # 记录结束时间，计算运行时间
    end_time = time.time()
    total_time = end_time - start_time
    logging.info('结束：')
    logging.info(f'总共用时: {total_time:.2f}秒')
    logging.info('Done!')