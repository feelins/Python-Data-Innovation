#!/usr/bin/env python
# -*-coding:utf-8 -*-
'''
@File    :   p01_018_know_list.py
@Time    :   2024/03/01 11:05:30
@Author  :   Feelins Shao 
@Version :   1.0
@Contact :   feipengshao@163.com
@License :   (C)Copyright 2022-2024, Feelins Shao
@Desc    :   018. 认识列表，列表的基本操作
'''


import logging, time

if __name__ == '__main__':

    # 记录开始运行时间
    start_time = time.time()
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
    logging.info('开始: ')
    
    list01 = [1, 8, 15, 20, 33]
    print(len(list01)) # 列表的长度，即个数
    list01.apend(40) # 列表增加一个元素，位置在最后
    list01.insert(2, 15)
    list02 = [99, 88]
    list01.extend(list02)
    list01.pop(6)
    if 33 in list01:
        list01.remove(33)
    print(len(list01))
    print(list01[7])


    # 记录结束时间，计算运行时间
    end_time = time.time()
    total_time = end_time - start_time
    logging.info('结束：')
    logging.info(f'总共用时: {total_time:.2f}秒')
    logging.info('Done!')