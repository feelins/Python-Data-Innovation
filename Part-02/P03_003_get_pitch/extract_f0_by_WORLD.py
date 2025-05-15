#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   ExtrFeaturesWORLD.py
@Time    :   2022/03/20 20:56:02
@Author  :   feelins, shao 
@Version :   1.0
@Contact :   feipengshao@163.com
@License :   (C)Copyright 2022-2023, 极地语音工作室 
@Desc    :   使用WORLD提取基频
'''

# here put the import lib
import pyworld as pw
import os
import soundfile as sf

def createDir(new_path):
    if not os.path.exists(new_path):
        os.makedirs(new_path)

def write(_save_path, _save_list):
    output_file = open(_save_path, 'w')
    results = []
    for line in _save_list:
        results.append(str(line) + '\n')
    output_file.writelines(results)
    output_file.close()



base_dir = "sample_data"
f0_dir = "f0"
ap_dir = "ap"
sp_dir = "sp"
createDir(f0_dir)
createDir(ap_dir)
createDir(sp_dir)
for file_names in os.listdir(base_dir):
    print(file_names)
    # 读取文件
    WAV_FILE = os.path.join(base_dir, file_names)

    # 提取语音特征
    x, fs = sf.read(WAV_FILE)
    f0, sp, ap = pw.wav2world(x, fs)    # use default options

    f0_path = os.path.join(f0_dir, file_names.split('.')[0] + '.f0')
    write(f0_path, f0)
    sp_path = os.path.join(sp_dir, file_names.split('.')[0] + '.sp')
    write(sp_path, sp)
    ap_path = os.path.join(ap_dir, file_names.split('.')[0] + '.ap')
    write(ap_path, ap)
