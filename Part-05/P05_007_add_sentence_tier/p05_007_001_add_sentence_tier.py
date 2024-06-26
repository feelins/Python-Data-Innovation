#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   p05_007_001_add_sentence_tier.py
@Time    :   2024/06/11 星期二 10:18:00
@Author  :   feelins, shao
@Version :   1.0
@Contact :   feipengshao@163.com
@License :   (C)Copyright 2022-2023, 极地语音工作室
@Desc    :   增加一层句子层
'''

# here put the import lib
import os
import textgrid as tg

input_tg_dir = r'final_TG'
input_txt_dir = r'wang_data_txt'
txt_list = {}
for file_name in os.listdir(input_txt_dir):
    input_txt_file = os.path.join(input_txt_dir, file_name)
    with open(input_txt_file, encoding='utf-8') as fid:
        input_list = [x.strip() for x in fid.readlines()]
    txt_list[file_name] = input_list[0]
output_tg_dir = r'final_TG_add'
if not os.path.exists(output_tg_dir):
    os.mkdir(output_tg_dir)

for file_name in os.listdir(input_tg_dir):
    print(file_name)
    input_tg_file = os.path.join(input_tg_dir, file_name)
    tgrid = tg.read_textgrid(input_tg_file)
    tmp_begin = tgrid[0][0].stop
    tmp_end = tgrid[0][-1].start
    input_txt = ''
    tmp_key = file_name.replace('.TextGrid', '.txt')
    if tmp_key in txt_list:
        input_txt = txt_list[tmp_key]
    new_sentence_tier = []
    new_sentence_tier.append(tg.Entry(0, tmp_begin, '', 'sentence'))
    new_sentence_tier.append(tg.Entry(tmp_begin, tmp_end, input_txt, 'sentence'))
    new_sentence_tier.append(tg.Entry(tmp_end, tgrid[0][-1].stop, '', 'sentence'))
    results = []
    results.append(new_sentence_tier)
    results.append(tgrid[0])
    results.append(tgrid[2])
    results.append(tgrid[1])
    output_tg_file = os.path.join(output_tg_dir, file_name)
    tg.write_textgrid(output_tg_file, results)
print('Done!')