#!usr/bin/env python
# -*- coding:utf-8 _*-
"""
@file: Deep_Learning_from_Scratch/ch03/ch03_3_2_5_sig_step_compare.py
@version: 1.0
@time: 2019/06/24 18:40:02
@function：阶跃函数和sigmoid函数比较
"""
import numpy as np
import matplotlib.pylab as plt


def sigmoid(x):
    return 1 / (1 + np.exp(-x))    


def step_function(x):
    return np.array(x > 0, dtype=np.int)


x = np.arange(-5.0, 5.0, 0.1)
y1 = sigmoid(x)
y2 = step_function(x)

plt.plot(x, y1)
plt.plot(x, y2, 'r--')
plt.ylim(-0.1, 1.1)  # 指定图中绘制的y轴的范围
plt.show()
