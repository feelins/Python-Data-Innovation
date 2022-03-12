#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   p02_001_normal_progress_bar.py
@Time    :   2022/03/12 19:57:03
@Author  :   feelins, shao 
@Version :   1.0
@Contact :   feipengshao@163.com
@License :   (C)Copyright 2022-2023, 极地语音工作室 
@Desc    :   普通进度条
'''

# here put the import lib
import sys
import time

def progress_bar():
    for i in range(1, 101):
        print('\r', end='')
        print('Progress: {}%:'.format(i), '|' * (i // 2), end='')
        sys.stdout.flush()
        time.sleep(0.05)
    print('\n')

progress_bar()