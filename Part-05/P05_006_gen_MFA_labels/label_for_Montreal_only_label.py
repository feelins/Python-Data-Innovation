#!usr/bin/env python
# -*- coding:utf-8 _*-
""" 
@author:shaopf
@file: label_for_Montreal.py
@version:
@time: 2019/04/24 20:20:45
@email:feipengshao@163.com
@function： prepare labels and dict for Montreal Alignment, need input pinyin file
"""

import os
import shutil

# def gen_single_file(_input_txt_file, )



def genDictLabWord(pinyin_file, out_lab_path, check_wav_dir):
    """gen data"""
    if not os.path.exists(out_lab_path):
        os.mkdir(out_lab_path)
    tmp_dict_list = {}
    with open(pinyin_file, encoding='utf-8') as fid:
        pinyin_lines = [x.strip() for x in fid.readlines()]
    for line in pinyin_lines:
        file_name, all_pinyin = line.split('|', 1)
        simple_file_name = file_name.replace('.wav', '').replace('.txt', '')
        new_file_name = simple_file_name + '.txt'
        save_lab_file = os.path.join(out_lab_path, new_file_name)
        print('gen label for align file ' + file_name)
        out_lab_list = []

        # old_pinyins = all_pinyin.split('/')
        # new_pinyins = [item for item in filter(lambda x: x.strip() not in _PUNCS and x.strip() != '', old_pinyins)]

        # output the labels
        # lab_pinyins = [item for item in map(lambda x: x.replace(' ', ''), new_pinyins)]
        out_lab_list.append(all_pinyin + '\n')
        wav_file_name = os.path.join(check_wav_dir, simple_file_name + '.wav')
        target_wav_file = os.path.join(out_lab_path, simple_file_name + '.wav')
        if os.path.exists(wav_file_name):
            with open(save_lab_file, 'w') as wid:
                wid.writelines(out_lab_list)
            shutil.copyfile(wav_file_name, target_wav_file)


if __name__ == '__main__':
    """supported languages:
    mandarin
    cantonese
    shanghai
    """
    input_pinyin_file = r'list_pinyin.txt'
    input_wav_dir = r'ftc_wavs'

    output_lab_align_path = r'gen_labels_20240610'
    genDictLabWord(input_pinyin_file, output_lab_align_path, input_wav_dir)
    print('Done!')
