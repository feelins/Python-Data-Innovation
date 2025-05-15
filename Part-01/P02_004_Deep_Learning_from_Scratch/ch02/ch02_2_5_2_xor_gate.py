#!usr/bin/env python
# -*- coding:utf-8 _*-
"""
@file: Deep_Learning_from_Scratch/ch02/ch02_2_5_2_xor_gate.py
@version: 1.0
@time: 2019/06/21 16:43:32
@function： 异或门
(0, 0) -> 0
(1, 0) -> 1
(0, 1) -> 1
(1, 1) -> 1
"""
import numpy as np

from ch02_2_3_3_and_gate import AND
from ch02_2_3_3_nand_gate import NAND
from ch02_2_3_3_or_gate import OR


def XOR(x1, x2):
    s1 = NAND(x1, x2)
    s2 = OR(x1, x2)
    y = AND(s1, s2)
    return y


if __name__ == '__main__':
    for xs in [(0, 0), (1, 0), (0, 1), (1, 1)]:
        y = XOR(xs[0], xs[1])
        print(str(xs) + " -> " + str(y))
