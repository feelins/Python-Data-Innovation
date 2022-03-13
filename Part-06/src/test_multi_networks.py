#!usr/bin/env python
# -*- coding:utf-8 _*-
""" 
@author: shaopf
@file: test_multi_networks.py 
@version: 1.0
@time: 2019/06/13 16:02:55
@email: feipengshao@163.com
@function： 
"""

import numpy as np
import matplotlib.pylab as plt

def step_function(x):
    """支持NumPy数组的阶跃函数"""
    # y = x > 0
    # return y.astype(np.int)
    return np.array(x > 0, dtype=np.int)


def sigmoid(x):
    """sigmoid函数"""
    return 1 / (1 + np.exp(-x))


def relu(x):
    """ReLU函数"""
    return np.maximum(0, x)  # 输出较大的那个值


x = np.arange(-5.0, 5.0, 0.1)
y1 = step_function(x)
y = sigmoid(x)
plt.plot(x, y1, "--")
plt.plot(x, y)
plt.ylim(-0.1, 1.1)  # 指定y轴范围
plt.show()
