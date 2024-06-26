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
from seperate_pinyin import seperate_syllable
from language_util import _PUNCS


def genDictLabWord(pinyin_file, out_lab_path, out_dict_file, lang='mandarin'):
    """gen data"""
    if not os.path.exists(out_lab_path):
        os.mkdir(out_lab_path)
    tmp_dict_list = {}
    with open(pinyin_file) as fid:
        pinyin_lines = [x.strip() for x in fid.readlines()]
    for line in pinyin_lines:
        file_name, all_pinyin = line.split('|', 1)
        save_lab_file = os.path.join(out_lab_path, file_name + '.lab')
        print('gen label for align file ' + file_name)
        out_lab_list = []

        old_pinyins = all_pinyin.split('/')
        new_pinyins = [item for item in filter(lambda x: x.strip() not in _PUNCS and x.strip() != '', old_pinyins)]

        # output the labels
        lab_pinyins = [item for item in map(lambda x: x.replace(' ', ''), new_pinyins)]
        out_lab_list.append(' '.join(lab_pinyins) + '\n')
        with open(save_lab_file, 'w') as wid:
            wid.writelines(out_lab_list)

        # gen dict
        for word_py in new_pinyins:
            dict_word_pinyins = []
            syllable_pinyins = word_py.split()
            syllable_pinyins = [item for item in filter(lambda x: x.strip() != '', syllable_pinyins)]
            for pinyin in syllable_pinyins:
                sheng_yuns = seperate_syllable(pinyin, lang)
                dict_word_pinyins.append(' '.join(list(sheng_yuns)))
            word_py = word_py.replace(' ', '')
            if word_py not in tmp_dict_list:
                tmp_dict_list[word_py] = ' '.join(dict_word_pinyins)
    with open(out_dict_file, 'w') as oid:
        for k, v in tmp_dict_list.items():
            oid.write(str(k) + '\t' + str(v) + '\n')


if __name__ == '__main__':
    """supported languages:
    mandarin
    cantonese
    shanghai
    """
    input_pinyin_file = r'/home/shaopf/study/mTTS_frontend/example_file/cantonese_script_pinyin.txt'
    output_dict_file = r'/home/shaopf/study/mTTS_frontend/example_file/montreal_align_dict_cantonese.txt'
    output_lab_align_path = r'/home/shaopf/study/mTTS_frontend/example_file/lab_align'
    genDictLabWord(input_pinyin_file, output_lab_align_path, output_dict_file, 'cantonese')
    print('Done!')
