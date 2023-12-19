#!/usr/bin/env python
# -*-coding:utf-8 -*-
'''
@File    :   p02_007_7-2-1_drop_duplicate_values.py
@Time    :   2023/12/19 10:47:41
@Author  :   Feelins Shao 
@Version :   1.0
@Contact :   feipengshao@163.com
@License :   (C)Copyright 2022-2023, Feelins Shao
@Desc    :   7.2.1 删除重复值
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
    # 1. 返回一个布尔值，Series，每一行是否存在重复值（与之前出现的行重复）
    print(df.duplicated())
    # 2. 返回的是DataFrame，将上面为False的部分保留下来
    print(df.drop_duplicates())
    # 3. 根据name这一列去除重复的部分
    print(df.drop_duplicates(['name']))
    # 4. 根据name这一列，去除重复，而且是保留最后一个出现的
    print(df.drop_duplicates(['name'], keep='last'))

    # 记录结束时间，计算运行时间
    end_time = time.time()
    total_time = end_time - start_time
    logging.info('结束：')
    logging.info(f'总共用时: {total_time:.2f}秒')
    logging.info('Done!')