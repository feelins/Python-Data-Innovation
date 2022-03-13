#!usr/bin/env python
# -*- coding:utf-8 _*-
""" 
@author: shaopf
@file: test_forward_networks.py
@version: 1.0
@time: 2019/06/13 17:02:55
@email: feipengshao@163.com
@function： 
"""

import numpy as np


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


def identity_function(x):
    """输出函数：恒等函数"""
    return x


def init_network():
    """初始化"""
    network = {}
    network['W1'] = np.array([[0.1, 0.3, 0.5], [0.2, 0.4, 0.5]])
    network['b1'] = np.array([0.1, 0.2, 0.3])
    network['W2'] = np.array([[0.1, 0.4], [0.2, 0.5], [0.3, 0.6]])
    network['b2'] = np.array([0.1, 0.2])
    network['W3'] = np.array([[0.1, 0.3], [0.2, 0.4]])
    network['b3'] = np.array([0.1, 0.2])

    return network


def forward(network, x):
    """前向"""
    W1, W2, W3 = network['W1'], network['W2'], network['W3']
    b1, b2, b3 = network['b1'], network['b2'], network['b3']

    a1 = np.dot(x, W1) + b1
    z1 = sigmoid(a1)
    a2 = np.dot(z1, W2) + b2
    z2 = sigmoid(a2)
    a3 = np.dot(z2, W3) + b3
    y = identity_function(a3)

    return y


network = init_network()
x = np.array([1.0, 0.5])
y = forward(network, x)
print(y)  # [0.31655918 0.69567667]
