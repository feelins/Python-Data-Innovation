#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   p02_001_alive_progress_bar.py
@Time    :   2022/03/12 20:23:27
@Author  :   feelins, shao 
@Version :   1.0
@Contact :   feipengshao@163.com
@License :   (C)Copyright 2022-2023, 极地语音工作室 
@Desc    :   有一些动画效果的进度条
'''

# here put the import lib
import time
from alive_progress import alive_bar
items = range(100)
with alive_bar(len(items)) as bar:
    for item in items:
        bar()
        time.sleep(0.1)