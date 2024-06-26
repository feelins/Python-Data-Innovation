#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   p05_005_001_delete_one_tier.py
@Time    :   2024/05/26 星期天 21:07:11
@Author  :   feelins, shao
@Version :   1.0
@Contact :   feipengshao@163.com
@License :   (C)Copyright 2022-2023, 极地语音工作室
@Desc    :   删除一层
'''

# here put the import lib
import os
import textgrid as tg

input_tg_dir = r'oldTextGrid1'
output_tg_dir = r'newtg'
if not os.path.exists(output_tg_dir):
    os.mkdir(output_tg_dir)

for file_name in os.listdir(input_tg_dir):
    print(file_name)
    input_tg = os.path.join(input_tg_dir, file_name)
    tgrid = tg.read_textgrid(input_tg)
    result_list = []
    result_list.append(tgrid[0])
    output_tg = os.path.join(output_tg_dir, file_name)
    tg.write_textgrid(output_tg, result_list)
print('Done!')