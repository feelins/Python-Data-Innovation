#!usr/bin/env python
# -*- coding:utf-8 _*-
"""
@file: Deep_Learning_from_Scratch/ch01/ch01_1-6-2_sin_cos_graph.py
@version: 1.0
@time: 2019/06/21 16:12:24
@function：numpy使用，sin函数图像
"""

import numpy as np
import matplotlib.pyplot as plt

# 生成数据
x = np.arange(0, 6, 0.1)  # 以0.1为单位，生成0到6的数据
y1 = np.sin(x)
y2 = np.cos(x)

# 绘制图形
plt.plot(x, y1, label="sin")
plt.plot(x, y2, linestyle="--", label="cos")
plt.xlabel("x")  # x轴的标签
plt.ylabel("y")  # y轴的标签
plt.title('sin & cos')
plt.legend()
plt.show()
