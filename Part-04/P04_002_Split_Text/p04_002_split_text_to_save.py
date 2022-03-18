#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   p04_002_split_text_to_save.py
@Time    :   2022/03/18 09:59:52
@Author  :   feelins, shao 
@Version :   1.0
@Contact :   feipengshao@163.com
@License :   (C)Copyright 2022-2023, 极地语音工作室 
@Desc    :   对一个有几列的文本，通过某种分割符分别保存
'''

# here put the import lib
input_txt_file = r'input_text.txt'

# 读文件
with open(input_txt_file, encoding='utf-8') as fid:
	input_txt_list = [x.strip() for x in fid.readlines()]

results = {}
for i, line in enumerate(input_txt_list):
	print(line)
	results[i] = line.split('\t')

for i in range(3):
	save_file = input_txt_file[:input_txt_file.find('.')] + str(i + 1) + '.txt'
	with open(save_file, 'w', encoding='utf-8') as wid:
		wid.writelines([v[i] + '\n' for k, v in results.items()])
print('Done!')