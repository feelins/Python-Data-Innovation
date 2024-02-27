#!/usr/bin/env python
# -*-coding:utf-8 -*-
'''
@File    :   p01_015_count_words.py
@Time    :   2024/02/23 13:22:20
@Author  :   Feelins Shao 
@Version :   1.0
@Contact :   feipengshao@163.com
@License :   (C)Copyright 2022-2023, Feelins Shao
@Desc    :   None
'''


# tmp_str = "In recent years scientists in many parts of the world have pooled their money"

# sarray = tmp_str.split(" ")
# print(sarray)

# shuxiang = "狗"
# if shuxiang == "狗":
#     print("你是 Bi8bo")
# else:
#     print("你是憨憨")

shuxiangs = ["狗", "虎", "虎", "狗", "猴", "狗", "狗", "猪"]
shuxiang_types = []
for shuxiang in shuxiangs:
    if shuxiang not in shuxiang_types:
        shuxiang_types.append(shuxiang)


for shuxiang_type in shuxiang_types:
    shuxiang_number = 0
    for shuxiang in shuxiangs:
        if shuxiang == shuxiang_type:
            shuxiang_number += 1
    print("属相" + shuxiang_type + "共有：" + str(shuxiang_number))