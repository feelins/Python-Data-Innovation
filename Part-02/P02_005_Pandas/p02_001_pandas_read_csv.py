#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   p02_001_pandas_read_csv.py
@Time    :   2022/03/13 11:13:33
@Author  :   feelins, shao 
@Version :   1.0
@Contact :   feipengshao@163.com
@License :   (C)Copyright 2022-2023, 极地语音工作室 
@Desc    :   None
'''

# here put the import lib
import pandas
import matplotlib.pyplot as plt

dataset = pandas.read_csv(r'./sample_data/airline-passengers.csv', usecols=[1], engine='python')
plt.plot(dataset)
plt.show()