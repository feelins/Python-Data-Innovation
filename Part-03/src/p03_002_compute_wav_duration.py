#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   p03_002_compute_wav_duration.py
@Time    :   2022/03/16 17:37:19
@Author  :   feelins, shao 
@Version :   1.0
@Contact :   feipengshao@163.com
@License :   (C)Copyright 2022-2023, 极地语音工作室
@Desc    :   计算一个目录里的音频的时长
'''

# here put the import lib
from unittest import result
import wave
import os

input_dir = r'Part-03\sample_data\p03_002_wavs' # 也可以用E:\Wave的目录形式
wav_duration_result = input_dir + '_duration_result.txt' # 结果文件是直接在上面的目录上增加，相当于在音频的同级目录生成一个结果文件

total_durtion = 0.0
results = []
for file_name in os.listdir(input_dir):
	print("Processing " + file_name)
	wav_file = os.path.join(input_dir, file_name)
	
	wavefile = wave.open(wav_file, 'r')
	framerate = wavefile.getframerate()
	numframes = wavefile.getnframes()
	duration = float(numframes) / float(framerate)
	results.append(file_name + "\t" + str(duration))
	total_durtion = total_durtion + duration

results.insert(0, 'Total duration: ' + str(total_durtion) + '秒, 约为: ' + str(total_durtion / 3600) + '小时。')
results.insert(1, '')
with open(wav_duration_result, 'w', encoding='utf-8') as wid:
    wid.writelines([x + '\n' for x in results])
print('Done!')