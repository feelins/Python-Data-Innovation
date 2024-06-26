#!/usr/bin/env python
# -*-coding:utf-8 -*-
'''
@File    :   p02_007_4-1-5_bool_index.py
@Time    :   2024/01/10 09:29:24
@Author  :   Feelins Shao 
@Version :   1.0
@Contact :   feipengshao@163.com
@License :   (C)Copyright 2022-2023, Feelins Shao
@Desc    :   4.1.5 布尔索引
'''


import logging, time
import numpy as np

if __name__ == '__main__':
    # 记录开始运行时间
    start_time = time.time()
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
    logging.info('开始: ')

    # 假设我们有这样一个数组
    names =  np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe'])

    # 我们使用numpy.random生成随机正态分布的数据
    data =  np.random.randn(7, 4)
    print(names)
    print(data)
    # 使用布尔索引来选择Bob的数据，根据索引索引，是选择第0，3行的数据输出
    logging.info('Bob的数据：根据索引索引，是选择第0，3行的数据输出')
    logging.info(data[names == 'Bob'])

    # 当布尔值长度不正确时，并不会报错，要注意
    names =  np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe'])
    data =  np.random.randn(7, 4)

    logging.info('当布尔值长度不正确时，并不会报错，要注意')
    # 这个地方没有看懂！！！！！！！！！！！！！！！！！！=================
    print(names == 'Bob', names == 'Joe')
    try:
        logging.info(data[names == 'Bob', names == 'Joe'])
    except IndexError as e:
        logging.error(f'发生错误：{e}')
    # =============================
    
    print(data)
    print(data[names == 'Bob', 2:])

    print('也可以取反')
    print(data[~(names == 'Bob')])

    print('也可以用逻辑运算，下面这个符号用or不行？，书上说的是必须要用& | 不能用and or')
    mask = (names == 'Bob') | (names == 'Will')
    print(data[mask])

    print('也可以通过布尔值，设置数组')
    data[data < 0] = 0
    print(data)

    data[names != 'Joe'] = 7
    print(data)


    # 记录结束时间，计算运行时间
    end_time = time.time()
    total_time = end_time - start_time
    logging.info('结束：')
    logging.info(f'总共用时: {total_time:.2f}秒')
    logging.info('Done!')