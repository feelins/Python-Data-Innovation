#!usr/bin/env python
# -*- coding:utf-8 _*-
"""
@file: Deep_Learning_from_Scratch/ch01/ch01_1-6-1_sin_graph.py
@version: 1.0
@time: 2019/06/21 16:09:20
@function：numpy使用，sin函数图像
"""

import numpy as np
import matplotlib.pyplot as plt

# 生成数据
x = np.arange(0, 6, 0.1) # [0.  0.1 0.2 0.3 ... 5.9]
# print(x)
y = np.sin(x)

# 绘制图形
plt.plot(x, y)
plt.show()
