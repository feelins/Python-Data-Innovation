#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   split_files_to_dir.py
@Time    :   2024/06/09 星期天 20:08:32
@Author  :   feelins, shao
@Version :   1.0
@Contact :   feipengshao@163.com
@License :   (C)Copyright 2022-2023, 极地语音工作室
@Desc    :   
'''

# here put the import lib
import os
import shutil

input_dir = r'E:\Data_ArcticPhonetics\20240530_wangjiaqi\experimentdata\final_TG_add'
input_wav_dir = r'E:\Data_ArcticPhonetics\20240530_wangjiaqi\experimentdata\wang_data'
output_dir = r'E:\Data_ArcticPhonetics\20240530_wangjiaqi\experimentdata\final_TG_dir'
if not os.path.exists(output_dir):
    os.mkdir(output_dir)

for file_name in os.listdir(input_dir):
    print(file_name)
    pre_file_name = file_name[:4]
    pre_pre_dir_name = file_name[:2]
    output_next_dir = os.path.join(output_dir, pre_pre_dir_name)
    if not os.path.exists(output_next_dir):
        os.mkdir(output_next_dir)
    output_small_dir = os.path.join(output_next_dir, pre_file_name)
    if not os.path.exists(output_small_dir):
        os.mkdir(output_small_dir)
    source_file = os.path.join(input_dir, file_name)
    target_file = os.path.join(output_small_dir, file_name)
    shutil.copyfile(source_file, target_file)
    source_file = os.path.join(input_wav_dir, file_name.replace('.TextGrid', '.wav'))
    target_file = os.path.join(output_small_dir, file_name.replace('.TextGrid', '.wav'))
    shutil.copyfile(source_file, target_file)




