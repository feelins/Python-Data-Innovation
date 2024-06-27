#!/usr/bin/env python
# -*-coding:utf-8 -*-
'''
@File    :   p02_002_001_unzip_rar.py
@Time    :   2024/01/08 11:00:50
@Author  :   Feelins Shao 
@Version :   1.0
@Contact :   feipengshao@163.com
@License :   (C)Copyright 2022-2023, Feelins Shao
@Desc    :   解压及压缩rar文件
'''


import logging, time
import rarfile

def unrar_file(file_path, output_path):
    with rarfile.RarFile(file_path) as rf:
        rf.extractall(output_path)

if __name__ == '__main__':

    # 记录开始运行时间
    start_time = time.time()
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
    logging.info('开始: ')
    


    file_path = 'abc.rar'
    output_path = './'
    unrar_file(file_path, output_path)



    # 记录结束时间，计算运行时间
    end_time = time.time()
    total_time = end_time - start_time
    logging.info('结束：')
    logging.info(f'总共用时: {total_time:.2f}秒')
    logging.info('Done!')