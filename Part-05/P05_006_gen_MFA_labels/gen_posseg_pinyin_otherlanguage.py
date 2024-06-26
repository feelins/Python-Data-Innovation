#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" 
@author: shaopf
@file: gen_posseg_pinyin_otherlanguage.py 
@version: 1.0
@time: 2019/07/15 10:54:02
@email: feipengshao@163.com
@function： 其它无前端语言，根据发音词典生成，分词仍然利用jieba
"""
from jieba import posseg
from seperate_pinyin import pinyinformat
from language_util import _PUNCS
import os
import re


def init_dict(_dict_file):
    """initialize the dict file"""
    with open(_dict_file, encoding='utf-8') as fid:
        dict_list = [x.strip() for x in fid.readlines()]
    dicts = {}
    for line in dict_list:
        k, v = re.split('\,|\t|\|| ', line, 1)
        dicts[k] = v

    return dicts


def gen_phons(_dicts, _word, lang):
    """Return the phone of a given word"""
    phon_result = []
    if _word in _dicts:
        phon_result.append(pinyinformat(_dicts[_word], lang))
    else:
        for i in range(len(_word)):
            if _word[i] in _dicts:
                phon_result.append(pinyinformat(_dicts[_word[i]], lang))
            else:
                phon_result.append('NULL')

    return phon_result


def txt2result(_txt, _dicts, lang):
    """Return a list of words, segs and pinyins of txt.
    _txt: input sentence
    """
    # clean punctuations
    clean_txt = _txt
    for pu in _PUNCS:
        clean_txt = clean_txt.replace(pu, '')
    words = []
    poses = []
    pinyins = []
    result_jieba = iter(posseg.cut(clean_txt))
    for word, pos in result_jieba:
        words.append(word)
        poses.append(pos[0])
        result_pypinyin = gen_phons(_dicts, word, lang)
        pinyins.append(' '.join([item for item in result_pypinyin]))

    return words, poses, pinyins


def save_result(_results, _save_dir, _save_filename, _str):
    """Save result"""
    save_file = os.path.join(_save_dir, _save_filename + '_' + _str + '.txt')
    with open(save_file, 'w') as wid:
        wid.writelines(_results)


def gen_result(_in_file, _dict_file, lang):
    """Return all results for a txt file.
    _in_file: input txt file
    """
    gen_dicts = init_dict(_dict_file)
    cur_dir = os.path.dirname(_in_file)
    cur_filename = os.path.basename(_in_file)
    cur_filename = cur_filename[:cur_filename.find('.')]
    print(_in_file)
    with open(_in_file, encoding='utf-8') as fid:
        txt_lines = [x.strip() for x in fid.readlines()]
    results_words = []
    results_poses = []
    results_pinyins = []
    for line in txt_lines:
        print('processing: ', line)
        file_name, txt = re.split(' |\||\t', line, 1)
        tmp_words, tmp_poses, tmp_pinyins = txt2result(txt, gen_dicts, lang)
        results_words.append(file_name + '|' + '/'.join(tmp_words) + '\n')
        results_poses.append(file_name + '|' + '/'.join(tmp_poses) + '\n')
        results_pinyins.append(file_name + '|' + '/'.join(tmp_pinyins) + '\n')
    # save
    save_result(results_poses, cur_dir, cur_filename, 'pos')
    save_result(results_words, cur_dir, cur_filename, 'seg')
    save_result(results_pinyins, cur_dir, cur_filename, 'pinyin')


if __name__ == '__main__':
    """supported languages:
        mandarin
        cantonese
        shanghai
        """
    input_txt_file = r'/home/shaopf/study/mTTS_frontend/example_file/cantonese_script.txt'
    dict_file = r'/home/shaopf/study/mTTS_frontend/misc/cantonese_dict.txt'
    gen_result(input_txt_file, dict_file, 'cantonese')
    print('Done!')

