#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   p02_001_002_progress_bar_with_time.py
@Time    :   2022/03/12 20:01:45
@Author  :   feelins, shao 
@Version :   1.0
@Contact :   feipengshao@163.com
@License :   (C)Copyright 2022-2023, 极地语音工作室 
@Desc    :   带时间进度条
'''

# here put the import lib

import time
scale = 50
print('执行开始'.center(scale // 2, '-'))
start = time.perf_counter()
for i in range(scale + 1):
    a = '*' * i
    b = '.' * (scale - i)
    c = (i / scale) * 100
    dur = time.perf_counter() - start
    print('\r{:^3.0f}%[{}->{}]{:.2f}s'.format(c, a, b, dur), end='')
    time.sleep(0.1)
print('\n' + '执行结束.'.center(scale // 2, '-'))