#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   p05_001_check_file_numbers.py
@Time    :   2022/03/17 09:54:09
@Author  :   feelins, shao 
@Version :   1.0
@Contact :   feipengshao@163.com
@License :   (C)Copyright 2022-2023, 极地语音工作室 
@Desc    :   检查标注文件和音频文件个数
'''

# here put the import lib
import os
import shutil

input_check_dir1 = r'sample_textgrid'
check_dir1_ext = '.TextGrid'

input_check_dir2 = r'sample_wav'
check_dir2_ext = '.wav'

check_result_file = input_check_dir1 + '_checked_result.txt'

check_list1 = [ls[:ls.find('.')] for ls in os.listdir(input_check_dir1) if ls[ls.find('.'):] == check_dir1_ext]
check_list2 = [ls[:ls.find('.')] for ls in os.listdir(input_check_dir2) if ls[ls.find('.'):] == check_dir2_ext]

check_all_list = set(check_list1).intersection(check_list2)
check_only_list1 = list(set(check_list1).difference(set(check_list2)))
check_only_list2 = list(set(check_list2).difference(set(check_list1)))

# 保存两个目录都有的文件
save_dir_all = input_check_dir1 + '_save_all'
if not os.path.exists(save_dir_all):
    os.mkdir(save_dir_all)
for file_name in check_all_list:
    init_file1 = os.path.join(input_check_dir1, file_name + check_dir1_ext)
    target_file1 = os.path.join(save_dir_all, file_name + check_dir1_ext)
    shutil.copyfile(init_file1, target_file1)
    init_file2 = os.path.join(input_check_dir2, file_name + check_dir2_ext)
    target_file2 = os.path.join(save_dir_all, file_name + check_dir2_ext)
    shutil.copyfile(init_file2, target_file2)
print('保存两个目录都存在的文件在: ' + save_dir_all)

# 保存目录1里多余的文件
save_only_dir1 = input_check_dir1 + '_only'
if not os.path.exists(save_only_dir1):
    os.mkdir(save_only_dir1)
for file_name in check_only_list1:
    init_file1 = os.path.join(input_check_dir1, file_name + check_dir1_ext)
    target_file1 = os.path.join(save_only_dir1, file_name + check_dir1_ext)
    shutil.copyfile(init_file1, target_file1)
print('保存只在第一个目录存在的文件: ' + save_only_dir1)

# 保存目录2里多余的文件
save_only_dir2 = input_check_dir2 + '_only'
if not os.path.exists(save_only_dir2):
    os.mkdir(save_only_dir2)
for file_name in check_only_list2:
    init_file2 = os.path.join(input_check_dir2, file_name + check_dir2_ext)
    target_file2 = os.path.join(save_only_dir2, file_name + check_dir2_ext)
    shutil.copyfile(init_file2, target_file2)
print('保存只在第一个目录存在的文件: ' + save_only_dir2)

results = []
results.append('两个目录都存在的文件有: ' + str(len(check_all_list)))
results.append('')
results.append('只在第一个目录存在的文件: ')
results.extend(check_only_list1)
results.append('')
results.append('只在第二个目录存在的文件: ')
results.extend(check_only_list2)
results.append('')

with open(check_result_file, 'w', encoding='utf-8') as wid:
    wid.writelines([x + '\n' for x in results])
print('Done!')

