#!usr/bin/env python
# -*- coding:utf-8 _*-
"""
@file: Deep_Learning_from_Scratch/ch03/ch03_3_2_4_sigmoid.py
@version: 1.0
@time: 2019/06/24 18:39:29
@function：sigmoid函数
"""
import numpy as np
import matplotlib.pylab as plt


def sigmoid(x):
    return 1 / (1 + np.exp(-x))    


X = np.arange(-5.0, 5.0, 0.1)
Y = sigmoid(X)
plt.plot(X, Y)
plt.ylim(-0.1, 1.1)
plt.show()
