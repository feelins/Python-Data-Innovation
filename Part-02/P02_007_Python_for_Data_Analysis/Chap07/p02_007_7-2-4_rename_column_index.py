#!/usr/bin/env python
# -*-coding:utf-8 -*-
'''
@File    :   p02_007_7-2-4_rename_column_index.py
@Time    :   2023/12/20 13:56:38
@Author  :   Feelins Shao 
@Version :   1.0
@Contact :   feipengshao@163.com
@License :   (C)Copyright 2022-2023, Feelins Shao
@Desc    :   7.2.4 重命名轴索引
'''


import logging, time
import pandas as pd
import numpy as np

if __name__ == '__main__':

    # 记录开始运行时间
    start_time = time.time()
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
    logging.info('开始: ')
    
    data = pd.DataFrame(np.arange(12).reshape((3, 4)), index=['Ohio', 'Colorado', 'New York'], columns=['one', 'two', 'three', 'four'])
    print(data)
    # 轴索引，也可以有一个map方法
    transform = lambda x: x[:4].upper() # [:4]的意思是格式化为不超过4个字符
    print(data.index.map(transform))
    print(data.columns.map(transform))

    # 这样赋值后，可个性dataframe
    data.columns = data.columns.map(transform)
    print(data)
    print('----- 不修改原有数据集 -----')
    data = pd.DataFrame(np.arange(12).reshape((3, 4)), index=['Ohio', 'Colorado', 'New York'], columns=['one', 'two', 'three', 'four'])
    data_new = data.rename(index=str.title, columns=str.upper)
    print(data_new)
    print('----- rename可以结合字典对象使用 -----')
    data_new = data.rename(index={'Ohio': 'INDIANA'}, columns={'three': 'ZERO'})
    print(data_new)

    # 实际用法
    sale_data = pd.DataFrame([['四川A', '门店1', 0.756, 0.617], 
                              ['四川A', '门店2', 0.143, 0.71], 
                              ['四川B', '门店3', 0.852, 0.45]], index=list('012'), columns=['区域', '门店', '销售', '人员数量'])
    print(sale_data)
    # 现在想要把'销售'改成’10月销售', '人员数量'改成‘10月人员数量'
    sale_data_october  = sale_data.rename(columns={'销售': '10月销售', '人员数量': '10月人员数量'})
    print(sale_data_october)
    # 1、 columns代表要对列名进行修改。在Python3 的pandas库里面，跟列名有关的一般都是用 columns,而不是用names。
    # 2、在columns后面是一个字典形式，键代表原列名，值代表新列名。不需要修改的列名不需要列出来，她们不会被修改。

    # 记录结束时间，计算运行时间
    end_time = time.time()
    total_time = end_time - start_time
    logging.info('结束：')
    logging.info(f'总共用时: {total_time:.2f}秒')
    logging.info('Done!')