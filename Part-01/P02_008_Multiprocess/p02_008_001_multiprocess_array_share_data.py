#!/usr/bin/env python
# -*-coding:utf-8 -*-
'''
@File    :   p02_008_001_multiprocess_array_share_data.py
@Time    :   2023/08/10 17:12:28
@Author  :   Feelins Shao 
@Version :   1.0
@Contact :   feipengshao@163.com
@License :   (C)Copyright 2022-2023, Feelins Shao
@Desc    :   多进程脚本，使用Array共享数据
'''


from multiprocessing import Process
from multiprocessing import Array

def func(i,temp):
    temp[0] += 100
    print("进程%s " % i, ' 修改数组第一个元素后----->', temp[0])

if __name__ == '__main__':
    temp = Array('i', [1, 2, 3, 4])
    for i in range(10):
        p = Process(target=func, args=(i, temp))
        p.start()