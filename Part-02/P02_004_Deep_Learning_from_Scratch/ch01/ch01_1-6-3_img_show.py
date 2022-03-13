#!usr/bin/env python
# -*- coding:utf-8 _*-
"""
@file: Deep_Learning_from_Scratch/ch01/ch01_1-6-3_img_show.py
@version: 1.0
@time: 2019/06/21 16:14:09
@function：显示图像
"""

import matplotlib.pyplot as plt
from matplotlib.image import imread

img = imread('../dataset/lena.png')  # 读入图像
plt.imshow(img)

plt.show()
