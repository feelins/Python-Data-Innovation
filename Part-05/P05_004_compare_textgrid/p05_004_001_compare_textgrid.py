#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   p05_004_001_compare_textgrid.py
@Time    :   2024/05/26 星期天 20:09:46
@Author  :   feelins, shao
@Version :   1.0
@Contact :   feipengshao@163.com
@License :   (C)Copyright 2022-2023, 极地语音工作室
@Desc    :   比较textgrid
'''

# here put the import lib
import os
import textgrid as tg

input_tg_main_dir = r'E:\003_ProgramLanguage\Python-Data-Innovation\Part-05\P05_004_compare_textgrid\oldTextGrid1'
input_tg_secdonary_dir = r'E:\003_ProgramLanguage\Python-Data-Innovation\Part-05\P05_004_compare_textgrid\oldTextGrid2'

output_check_tg_dir = r'E:\003_ProgramLanguage\Python-Data-Innovation\Part-05\P05_004_compare_textgrid\check_textgrid'
if not os.path.exists(output_check_tg_dir):
    os.mkdir(output_check_tg_dir)

# 要比较几层？怎么比较？限定两层。
# 比较两个文件的相似度。

# 第一种情况，两两比较，一个是基准，另外一个只是修改了一些内容，想比较这个人标注的得分；只出一个得分；同时比较内容，边界，以及可能不相同的interval
# 

errors = []
total = 0
for file_name in os.listdir(input_tg_main_dir):
    print(file_name)
    input_tg_main = os.path.join(input_tg_main_dir, file_name)
    tgrid_main = tg.read_textgrid(input_tg_main)
    input_tg_secdonary = os.path.join(input_tg_secdonary_dir, file_name)
    tgrid_secdonary = tg.read_textgrid(input_tg_secdonary)
    interval_main = tgrid_main[0]
    interval_secdonary = tgrid_secdonary[0]
    interval_check = [item for item in interval_main]
    interval_check2 = [item._replace(name='') for item in interval_secdonary]
    if len(interval_main) == len(interval_secdonary):
        for k in range(len(interval_main)):
            cur_interval_name_main = interval_main[k].name
            cur_interval_name_secdonary = interval_secdonary[k].name
            if cur_interval_name_main != cur_interval_name_secdonary:
                interval_check2[k] = interval_check2[k]._replace(name=cur_interval_name_secdonary)
                errors.append(','.join(['内容不同', file_name, cur_interval_name_main, cur_interval_name_secdonary]))
            cur_interval_begin_main = interval_main[k].start
            cur_interval_begin_secdonary = interval_secdonary[k].start
            if cur_interval_begin_main != cur_interval_begin_secdonary:
                interval_check2[k] = interval_check2[k]._replace(name='检查左边界')
                errors.append(','.join(['边界不同', file_name, str(cur_interval_begin_main), str(cur_interval_begin_secdonary)]))
            total += 1
    else:
        # 不同的Intervals
        pass
    result_list = []
    result_list.append(interval_check)
    result_list.append(interval_check2)
    output_tg = os.path.join(output_check_tg_dir, file_name)
    tg.write_textgrid(output_tg, result_list)

# 第二种情况，在第一种情况的基础上，增加生成新的判断TG，这些判断TG，在原来主TG的基础上，增加一层，用来判断校对。判断完了之后，删除这一层校对TG。脚本也写好。

print('Done!')

print((1 - len(errors) / total))
print(errors)
