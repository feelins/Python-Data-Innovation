#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" 
@author: shaopf
@file: gen_posseg_pinyin_mandarin.py 
@version: 1.0
@time: 2019/07/10 09:24:36
@email: feipengshao@163.com
@function： 利用pypinyin，jieba生成汉字普通话拼音，分词，词性文件
"""
from pypinyin import pinyin, Style
# from seperate_pinyin import pinyinformat
from jieba import posseg
# from language_util import _PUNCS
import os
import re

_PUNCS = ['，', '。', '、', '？', '！', '；']


def arabic_to_chinese(num):
    chinese_nums = '零一二三四五六七八九'
    chinese_units = ' 十百千万亿'
    chinese_num = ''
    num_str = str(num)
    for i in range(len(num_str)):
        num_digit = int(num_str[i])
        if num_digit == 0:
            continue
        chinese_num += chinese_nums[num_digit]
        chinese_num += chinese_units[len(num_str) - i - 1]

    return chinese_num


def arabic_to_chinese_simple(num):
    chinese_nums = '零一二三四五六七八九'
    # chinese_units = ' 十百千万亿'
    chinese_num = ''
    num_str = str(num)
    for i in range(len(num_str)):
        num_digit = int(num_str[i])
        # if num_digit == 0:
        #     continue
        chinese_num += chinese_nums[num_digit]
        # chinese_num += chinese_units[len(num_str) - i - 1]

    return chinese_num
        

def txt2result(_txt):
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
        # words.extend(list(word))
        
        words.append(word)
        poses.append(pos[0])

    fix_words = []
    for i, word in enumerate(words):
        next_word = ''
        if i < len(words) - 1:
            next_word = words[i + 1]
        if word == '87':
            print('hello')
        if word.isdigit():
            if next_word in ['年']:
                word = arabic_to_chinese_simple(word).strip()
            else:
                word = arabic_to_chinese(word).strip()
        fix_words.append(word)

    
    for word in fix_words:
        result_pypinyin = pinyin(word, style=Style.TONE3)
        # pinyins.append(' '.join(result_pypinyin))
        new_result_pypinyins = []
        for item in result_pypinyin:
            cur_py = item[0]
            if not cur_py[-1].isdigit():
                cur_py += '5'
            new_result_pypinyins.append(cur_py)
        pinyins.append(' '.join(new_result_pypinyins))

    return fix_words, poses, pinyins


def save_result(_results, _save_dir, _save_filename, _str):
    """Save result seperately"""
    save_file = os.path.join(_save_dir, _save_filename + '_' + _str + '.txt')
    with open(save_file, 'w', encoding='utf-8') as wid:
        wid.writelines(_results)


def gen_result(_in_file):
    """Return all results for a txt file.
    _in_file: input txt file
    """
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
        tmp_words, tmp_poses, tmp_pinyins = txt2result(txt)
        new_words = tmp_words
        # for www in tmp_words:
        #     # for chw in www:
        #     if u'\u4e00' <= www <= u'\u9fff':
        #         new_words.append(www)
        assert len(tmp_words) == len(tmp_pinyins)
        # if len(new_words) > 8 or len(new_words) < 3:
        #     continue
        results_words.append(file_name + '|' + '/'.join(new_words) + '\n')
        results_poses.append(file_name + '|' + '/'.join(tmp_poses) + '\n')
        results_pinyins.append(file_name + '|' + ' '.join(tmp_pinyins) + '\n')
    # save
    save_result(results_poses, cur_dir, cur_filename, 'pos')
    save_result(results_words, cur_dir, cur_filename, 'seg')
    save_result(results_pinyins, cur_dir, cur_filename, 'pinyin')


def gen_result_list(_input_files):
    cur_dir = os.path.dirname(_input_files)
    cur_filename = os.path.basename(_input_files)
    cur_filename = cur_filename[:cur_filename.find('.')]
    results_words = []
    results_poses = []
    results_pinyins = []
    for file_name in os.listdir(_input_files):
        input_file_name = os.path.join(_input_files, file_name)
        with open(input_file_name, encoding='utf-8') as fid:
            input_list = [x.strip() for x in fid.readlines()]
        tmp_words, tmp_poses, tmp_pinyins = txt2result(input_list[0])
        new_words = tmp_words
        # for www in tmp_words:
        #     # for chw in www:
        #     if u'\u4e00' <= www <= u'\u9fff':
        #         new_words.append(www)
        assert len(tmp_words) == len(tmp_pinyins)
        results_words.append(file_name + '|' + '/'.join(new_words) + '\n')
        results_poses.append(file_name + '|' + '/'.join(tmp_poses) + '\n')
        results_pinyins.append(file_name + '|' + ' '.join(tmp_pinyins) + '\n')
    # save
    save_result(results_poses, cur_dir, cur_filename, 'pos')
    save_result(results_words, cur_dir, cur_filename, 'seg')
    save_result(results_pinyins, cur_dir, cur_filename, 'pinyin')


if __name__ == '__main__':
    # import argparse
    # parser = argparse.ArgumentParser(
    #     description="gen pos, seg, pinyin for mandarin_txt.")
    # parser.add_argument(
    #     "txtfile",
    #     help=
    #     "Full path to txtfile which each line contain file_name and txt (seperated by | or [blank] or tab) "
    # )
    # args = parser.parse_args()
    #
    # gen_result(args.txtfile)
    ##################################################################################
    input_txt_file = r'E:\Data_ArcticPhonetics\20240410-fatiaozhang\list.list'
    gen_result(input_txt_file)
    # input_txt_files = r'E:\Data_ArcticPhonetics\20240530_wangjiaqi\experimentdata\addition_files\init_txt'
    # gen_result_list(input_txt_files)
    print('Done!')