#!usr/bin/env python
# -*- coding:utf-8 _*-
""" 
@author: shaopf
@file: test_Perceptron.py 
@version: 1.0
@time: 2019/05/29 22:29:30
@email: feipengshao@163.com
@function： 感知机
"""

import numpy as np

def AND(x1, x2):
    """与门"""
    w1, w2, theta = 0.5, 0.5, 0.7
    tmp = x1 * w1 + x2 * w2
    if tmp <= theta:
        return 0
    else:
        return 1


def AND_2(x1, x2):
    """与门"""
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.7
    tmp = np.sum(w * x) + b
    if tmp <= 0:
        return 0
    else:
        return 1


def NAND(x1, x2):
    """与非门"""
    x = np.array([x1, x2])
    w = np.array([-0.5, -0.5])
    b = 0.7
    tmp = np.sum(w * x) + b
    if tmp <= 0:
        return 0
    else:
        return 1


def OR(x1, x2):
    """或门"""
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.2
    tmp = np.sum(w * x) + b
    if tmp <= 0:
        return 0
    else:
        return 1


def XOR(x1, x2):
    """异或门"""
    s1 = NAND(x1, x2)
    s2 = OR(x1, x2)
    y = AND(s1, s2)
    return y

result = AND(1, 1)
print(result)
result = AND_2(1, 1)
print(result)
result = NAND(1, 1)
print(result)
result = OR(0, 1)
print(result)

# x = np.array([0, 1])
# w = np.array([0.5, 0.5])
# b = -0.7
# print(w * x)
# print(np.sum(w * x) + b)
