#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   p02_001_003_tqdm_progress_bar.py
@Time    :   2022/03/12 20:08:16
@Author  :   feelins, shao 
@Version :   1.0
@Contact :   feipengshao@163.com
@License :   (C)Copyright 2022-2023, 极地语音工作室 
@Desc    :   tqdm进度条
'''

# here put the import lib
from time import sleep
from tqdm import tqdm

for i in tqdm(range(1, 500)):
    sleep(0.01)
sleep(0.5)