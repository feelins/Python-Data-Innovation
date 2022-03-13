#!usr/bin/env python
# -*- coding:utf-8 _*-
""" 
@file: Deep_Learning_from_Scratch/ch03/ch03_3_2_3_step_function.py
@version: 1.0
@time: 2019/07/03 21:07:24
@function：损失函数－均方误差
"""

import numpy as np


def mean_squared_error(y, t):
    return 0.5 * np.sum((y - t) ** 2)


y = [0.1, 0.05, 0.6, 0.0, 0.05, 0.1, 0.0, 0.1, 0.0, 0.0]
t = [0, 0, 1, 0, 0, 0, 0, 0, 0, 0]
error = mean_squared_error(np.array(y), np.array(t))
print(error)  # 0.09750000000000003
y = [0.1, 0.05, 0.1, 0.0, 0.05, 0.1, 0.0, 0.6, 0.0, 0.0]
t = [0, 0, 1, 0, 0, 0, 0, 0, 0, 0]
error = mean_squared_error(np.array(y), np.array(t))
print(error)  # 0.5975
