#!usr/bin/env python
# -*- coding:utf-8 _*-
"""
@file: Deep_Learning_from_Scratch/ch03/ch03_3_2_7_relu.py
@version: 1.0
@time: 2019/06/24 18:42:22
@function：relu函数
"""
import numpy as np
import matplotlib.pylab as plt


def relu(x):
    return np.maximum(0, x)


x = np.arange(-5.0, 5.0, 0.1)
y = relu(x)
plt.plot(x, y)
plt.ylim(-1.0, 5.5)
plt.show()
