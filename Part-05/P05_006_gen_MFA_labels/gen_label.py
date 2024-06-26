#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: shaopf
@file: gen_label.py
@version: 1.0
@time: 2019/07/16 09:24:36
@email: feipengshao@163.com
@function： 生成fulllab
"""

import os
import re
import textgrid as tg
from language_util import _VOWEL, _CONSONANT
from labcnp import LabGenerator
from labformat import tree
from seperate_pinyin import seperate_syllable


def txt2label(language, txt, pinyin_txt, monofile=None):
    """Return a generator of HTS format label of txt.
    Args:
        txt: like raw txt "0001|向#1香港#1特别行政区#1同胞#3澳门台湾#1同胞"
             punctuation is allow in txt
        pinyin_txt: like raw txt " 0001|xiang4 xiang1 gang3 te4 bie2..."
            it has to have the same list order and number with word txt.
        monofile: absolute path of monolab file (alignment file). A monolab file
            example(measure time by 10e-7 second, 12345678 means 1.2345678
            second)
            --------
            0 4000000 sil
            4000000 4900000 j
            4900000 6400000 ing1
            6400000 6899999 g
            6899999 9500000 uo4
            9500000 11100000 sh
            ---------
    Return:
        A generator of phone label for the txt, convenient to save as a label file
    """
    lang_vowels = _VOWEL[language]
    lang_consonants = _CONSONANT[language]
    words = re.split('#\d', txt)
    words = [item for item in filter(lambda x: x.strip() != '', words)]
    rhythms = re.findall('#\d', txt)

    syllables = []
    pinyin_list = re.split('\/| ', pinyin_txt)
    for item in pinyin_list:
        syllables.append(seperate_syllable(item))

    phone_list = []
    for syllable in syllables:
        phone_list.extend(list(syllable))

    if monofile:
        phs_type = []
        times = ['0']
        with open(monofile) as fid:
            monos = [x.strip() for x in fid.readlines()]
        for line in monos:
            line = line.strip()
            assert len(line.split(' ')) == 3, 'check format of monolab file'
            start, stop, ph = line.split(' ')
            times.append(int(float(stop)))
            if ph in lang_vowels:
                phs_type.append('b')
            elif ph in lang_consonants:
                phs_type.append('a')
            elif ph == 'sil':
                phs_type.append('s')
            elif ph == 'sp':
                phs_type.append('sp')
            else:
                print('Error phones' + ph)
                exit(0)
    else:
        phs_type = ['a'] * len(phone_list)
        phs_type.insert(0, 's')
        phs_type.append('s')
        times = [0] * (len(phs_type) + 1)
    '''
    for item in words:
        print(item)

    print ('words: ', words)
    print ('rhythms: ',rhythms)
    print ('syllables: ', syllables)
    print ('poses: ', poses)
    print ('phs_type: ', phs_type)
    print ('times: ', times)
    '''
    poses = words
    poses = [item for item in map(lambda x: 'n', poses)]
    phone = tree(words, rhythms, syllables, poses, phs_type)
    return LabGenerator(phone, rhythms, times)

def textgrid2mono(textgrid_path, csv_path, monolab_path):
    """textgrid change to monolab file which contains time boundary and label"""
    for file_name in os.listdir(textgrid_path):
        file_name = file_name.split('.')[0]
        textgrid_file = os.path.join(textgrid_path, file_name + '.TextGrid')
        csv_file = os.path.join(csv_path, file_name + '.csv')
        monolab_file = os.path.join(monolab_path, file_name + '.lab')

        print('textgrid2mono processing file %s' % (file_name))
        # textgrid to csv
        tgrid = tg.read_textgrid(textgrid_file)
        tg.write_csv(tgrid, csv_file, sep=' ', header=False, meta=False)

        # csv to monolab
        total_list = []
        with open(csv_file) as fid:
            for line in fid.readlines():
                start, end, name, label = line.strip().split(' ')
                if label == 'phones':
                    start = str(int(float(start) * 10e6))
                    end = str(int(float(end) * 10e6))
                    if name[-1].isdigit():
                        name = name[:-1]
                    total_list.append(start + ' ' + end + ' ' + name + '\n')
        with open(monolab_file, 'w') as wid:
            wid.writelines(total_list)


def txt2full(language, txt_file, pinyin_file, output_label_path, mono_path=None):
    """gen full label"""
    txt_lines = {}
    with open(txt_file) as fid:
        all_txt_lines = [x.strip() for x in fid.readlines()]
        for line in all_txt_lines:
            file_name, txt = line.split('|')
            txt_lines[file_name] = txt
    pinyin_lines = {}
    with open(pinyin_file) as fid:
        all_pinyin_lines = [x.strip() for x in fid.readlines()]
        for line in all_pinyin_lines:
            file_name, txt = line.split('|')
            pinyin_lines[file_name] = txt

    if mono_path:
        for file_name in os.listdir(mono_path):
            file_name = file_name.replace('.lab', '')
            try:
                in_label_file = os.path.join(mono_path, file_name + '.lab')
                out_label_file = os.path.join(output_label_path, file_name + '.lab')
                label_line = txt2label(language, txt_lines[file_name], pinyin_lines[file_name], in_label_file)
                print('txt2fulllabel processing file %s' % (file_name))
            except Exception as e:
                print('Error at %s, please check your txt, with error %s' % (file_name, str(e)))
                exit(0)
            else:
                with open(out_label_file, 'w') as oid:
                    for item in label_line:
                        oid.write(item + '\n')
    else:
        for k, v in txt_lines.items():
            file_name = str(k)
            try:
                out_label_file = os.path.join(output_label_path, file_name + '.lab')
                label_line = txt2label(language, txt_lines[file_name], pinyin_lines[file_name])
                print('txt2fulllabel processing file %s' % (file_name))
            except Exception as e:
                print(
                    'Error at %s, please check your txt, with error %s' % (file_name, str(e)))
                exit(0)
            else:
                with open(out_label_file, 'w') as oid:
                    for item in label_line:
                        oid.write(item + '\n')


def generate_label(lang, txtfile, pinyinfile, output_labels_path, textgrid_path=None):
    """gen labels from sfs_file, txt_file, pos_file, pinyin_file"""
    os.system('mkdir -p %s' % output_labels_path)
    if textgrid_path:
        output_path = os.path.dirname(textgrid_path)
        mono_path = os.path.join(output_path, 'mono')
        csv_path = os.path.join(output_path, 'csv')
        os.system('mkdir -p %s' % mono_path)
        os.system('mkdir -p %s' % csv_path)
        textgrid2mono(textgrid_path, csv_path, mono_path)
        txt2full(lang, txtfile, pinyinfile, output_labels_path, mono_path)
    else:
        txt2full(lang, txtfile, pinyinfile, output_labels_path)


if __name__ == '__main__':
    """supported languages:
            mandarin
            cantonese
            shanghai
            """
    tmp_lang = 'mandarin'
    ########## gen label with alignment results ##########
    textgrid_path = r'/home/shaopf/study/mTTS_frontend/dddd/thchs30_250_demo/TextGrid'
    input_pinyin_file = r'/home/shaopf/study/mTTS_frontend/dddd/thchs30_250_demo/A11_pinyin.txt'
    input_txt_file = r'/home/shaopf/study/mTTS_frontend/dddd/thchs30_250_demo/A11_seg.txt'
    label_path = r'/home/shaopf/study/mTTS_frontend/dddd/thchs30_250_demo/labels'
    generate_label(tmp_lang, input_txt_file, input_pinyin_file, label_path, textgrid_path)
    ########## gen label for testlabel ##########
    # input_pinyin_file = r'/home/shaopf/study/mTTS_frontend/dddd/thchs30_250_demo/A11_pinyin.txt'
    # input_txt_file = r'/home/shaopf/study/mTTS_frontend/dddd/thchs30_250_demo/A11_seg.txt'
    # label_path = r'/home/shaopf/study/mTTS_frontend/dddd/thchs30_250_demo/labels'
    # generate_label(tmp_lang, input_txt_file, input_pinyin_file, label_path)

