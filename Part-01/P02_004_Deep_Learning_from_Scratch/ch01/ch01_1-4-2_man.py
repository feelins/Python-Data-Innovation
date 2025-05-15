#!usr/bin/env python
# -*- coding:utf-8 _*-
"""
@file: Deep_Learning_from_Scratch/ch01/ch01_1-4-2_man.py
@version: 1.0
@time: 2019/06/21 15:59:14
@function：类
"""


class Man:
    """示例类"""

    def __init__(self, name):
        """构造函数"""
        self.name = name
        print("Initilized!")

    def hello(self):
        print("Hello " + self.name + "!")

    def goodbye(self):
        print("Good-bye " + self.name + "!")


m = Man("Tom")
m.hello()
m.goodbye()
