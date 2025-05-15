#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   p02_001_004_progress_bar_iterations.py
@Time    :   2022/03/12 20:14:58
@Author  :   feelins, shao 
@Version :   1.0
@Contact :   feipengshao@163.com
@License :   (C)Copyright 2022-2023, 极地语音工作室 
@Desc    :   用于定义迭代次数的进度条
'''

# here put the import lib
import time
from progress.bar import IncrementalBar

mylist = [1, 2, 3, 4, 5, 6, 7, 8]
bar = IncrementalBar('Countdown', max=len(mylist))
for item in mylist:
    bar.next()
    time.sleep(1)
    bar.finish()