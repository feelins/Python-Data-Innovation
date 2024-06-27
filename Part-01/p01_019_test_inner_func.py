#!/usr/bin/env python
# -*-coding:utf-8 -*-
'''
@File    :   p01_019_test_inner_func.py
@Time    :   2024/03/22 18:39:43
@Author  :   Feelins Shao 
@Version :   1.0
@Contact :   feipengshao@163.com
@License :   (C)Copyright 2022-2024, Feelins Shao
@Desc    :   测试内置函数
'''


import logging, time

if __name__ == '__main__':

    # 记录开始运行时间
    start_time = time.time()
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
    logging.info('开始: ')
    

    a = 10
    def myfunc():
        def inner_func(b):
            return a + b
        return inner_func
    
    func1 = myfunc()
    a = 20
    func2 = myfunc()
    print(func1(10), func2(10))
    

    # 记录结束时间，计算运行时间
    end_time = time.time()
    total_time = end_time - start_time
    logging.info('结束：')
    logging.info(f'总共用时: {total_time:.2f}秒')
    logging.info('Done!')