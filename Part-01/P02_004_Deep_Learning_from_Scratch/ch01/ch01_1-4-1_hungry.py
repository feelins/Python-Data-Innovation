#!usr/bin/env python
# -*- coding:utf-8 _*-
"""
@file: Deep_Learning_from_Scratch/ch01/ch01_1-4-1_hungry.py
@version: 1.0
@time: 2019/06/21 15:49:13
@function：if语句，以及for语句，函数
"""


def sleep():
    print("I'm sleepy.")


hungry = False
if hungry:
    for i in [1, 2, 3]:
        print("I'm hungry!")
else:
    for i in range(5):
        print("I'm not hungry!")
        sleep()
