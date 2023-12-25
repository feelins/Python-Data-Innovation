#!/usr/bin/env python
# -*-coding:utf-8 -*-
'''
@File    :   p02_007_7-3-3_vectorized_string_function.py
@Time    :   2023/12/25 16:45:42
@Author  :   Feelins Shao 
@Version :   1.0
@Contact :   feipengshao@163.com
@License :   (C)Copyright 2022-2023, Feelins Shao
@Desc    :   7.3.3 pandas中的向量化字符串函数
'''


import logging, time
import pandas as pd
import numpy as np
import re

if __name__ == '__main__':

    # 记录开始运行时间
    start_time = time.time()
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
    logging.info('开始: ')

    data = {'Dave' : 'dave@gmail.com', 'Steve' : 'steve@hotmail.com', 'Rob' : 'rob@gmail.com', 'Wes' : np.nan}
    data = pd.Series(data)
    print(data.isnull())
    print(data.str.contains('gmail'))

    pattern = '([A-Z0-9._%+-]+)@([A-Z0-9.-]+)\\.([A-Z]{2,4})'
    print(data.str.findall(pattern, flags=re.IGNORECASE))
    print(data.str.match(pattern, flags=re.IGNORECASE))


    # 记录结束时间，计算运行时间
    end_time = time.time()
    total_time = end_time - start_time
    logging.info('结束：')
    logging.info(f'总共用时: {total_time:.2f}秒')
    logging.info('Done!')