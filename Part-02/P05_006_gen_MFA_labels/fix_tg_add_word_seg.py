
#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   fix_tg_add_word_seg.py
@Time    :   2024/06/01 星期六 14:30:17
@Author  :   feelins, shao
@Version :   1.0
@Contact :   feipengshao@163.com
@License :   (C)Copyright 2022-2023, 极地语音工作室
@Desc    :   给TG增加分词边界
'''

# here put the import lib

import textgrid as tg
import os

input_tg_dir = r'E:\Data_ArcticPhonetics\20240530_wangjiaqi\experimentdata\addition_files\out05\out05'
input_seg_files = r'E:\Data_ArcticPhonetics\20240530_wangjiaqi\experimentdata\addition_files\init_tx_seg.txt'
with open(input_seg_files, encoding='utf-8') as fid:
    input_segs = [x.strip() for x in fid.readlines()]
input_seg_words = {}
for _line in input_segs:
    file_name, word_line = _line.split('|')
    input_seg_words[file_name] = word_line
output_tg_dir = r'E:\Data_ArcticPhonetics\20240530_wangjiaqi\experimentdata\addition_files\add_TG'
if not os.path.exists(output_tg_dir):
    os.mkdir(output_tg_dir)
for file_name in os.listdir(input_tg_dir):
    if file_name.find('.TextGrid') == -1:
        continue
    print(file_name)
    input_tg_file = os.path.join(input_tg_dir, file_name)
    tgrid = tg.read_textgrid(input_tg_file)
    # input_word_seg_txt_file = os.path.join(input_seg_files, file_name.replace('.TextGrid', '.txt'))
    # with open(input_word_seg_txt_file, encoding='utf-8') as fid:
    #     input_word_seg_str = fid.readline()
    # word_segs = input_word_seg_str.split()
    word_segs = input_seg_words[file_name.replace('.TextGrid', '.txt')].split('/')

    # check if equal
    word_num = 0
    for word in word_segs:
        word_num += len(word)
    tg_word_len = len([item for item in tgrid[2] if item.name.strip() != 'sil' and item.name.strip() != ''])
    if tg_word_len != word_num:
        print('Need to check word-num and tgrid-word-num')
        exit(0)
    i = 0
    j = 0
    tg_words = []
    tmp_word_begin = 0
    tmp_word_end = 0
    for word in word_segs:
        print(word)
        while tgrid[2][i].name == '':
        # if tgrid[2][i].name == '':
            tmp_word_end = tgrid[2][i].stop
            tg_words.append(tg.Entry(tmp_word_begin, tmp_word_end, '', 'CHs'))
            tmp_word_begin = tmp_word_end
            i += 1
        for k in range(len(word)):
            tmp_word_end = tgrid[2][i].stop
            i += 1
        
        tg_words.append(tg.Entry(tmp_word_begin, tmp_word_end, word, 'CHs'))
        tmp_word_begin = tmp_word_end
        # i += 1
    tg_words.append(tg.Entry(tmp_word_begin, tgrid[2][-1].stop, '', 'CHs'))
        

    results = []
    results.append(tgrid[0])
    results.append(tgrid[2])
    results.append(tg_words)
    output_tg_file = os.path.join(output_tg_dir, file_name)
    tg.write_textgrid(output_tg_file, results)
