#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File       :   p04_003_gen_ipa_english.py
@Time     :   2022/09/16 15:47:18
@Author  :   feelins, shao 
@Version :   1.0
@Contact :   feipengshao@163.com
@License :   (C)Copyright 2022-2023, 极地语音工作室
@Desc    :    英语句子生成IPA音标
'''

# here put the import lib
vowels = []


def is_vowel(_cur_phon):
    if _cur_phon in vowels:
        return True
    else:
        return False


def count_vowels_number(_phons):
    _vowel_num = 0
    for j in range(len(_phons)):
        no_tone_phon = _phons[j]
        if _phons[j][-1].isdigit():
            no_tone_phon = _phons[j][:-1]
        if is_vowel(no_tone_phon):
            _vowel_num += 1
    return _vowel_num


def gen_syllable(phons):
    result_str = ''
    i = len(phons) - 1
    if count_vowels_number(phons) > 1:
        while i >= 0:
            if result_str != '' and result_str[0] == '-':
                result_str = phons[i] + result_str.strip()
            else:
                result_str = phons[i] + '' + result_str.strip()
            no_tone_phon = phons[i]
            no_tone_phon_prev = phons[i - 1]
            if phons[i][-1].isdigit():
                no_tone_phon = phons[i][:-1]
            if phons[i - 1][-1].isdigit():
                no_tone_phon_prev = phons[i - 1][:-1]
            if is_vowel(no_tone_phon):
                if is_vowel(no_tone_phon_prev):
                    if i != 0:
                        result_str = '-' + result_str.strip()
                    i = i - 1
                else:
                    if count_vowels_number(phons[0:i]) > 0:
                        result_str = '-' + phons[i - 1] + '' + result_str.strip()
                        i = i - 2
                    else:
                        result_str = ''.join(phons[0:i]) + '' + result_str.strip()
                        break
            else:
                i = i - 1
    else:
        # i = i - 1
        result_str = ''.join(phons)
    return result_str.strip().strip()


sentence_file = r'E:\Data_ArcticPhonetics\20220916-English\sentence.txt'
with open(sentence_file, encoding='utf-8') as fid:
    input_list = [x.strip() for x in fid.readlines()]

english_dict_file = r'E:\Data_ArcticPhonetics\20220916-English\english.dict'
with open(english_dict_file, encoding='utf-8') as fid:
    english_dict_list = [x.strip() for x in fid.readlines()]

english_dicts = {}
for line in english_dict_list:
    sarray = line.split(' ', 1)
    english_dicts[sarray[0].lower()] = sarray[1]

vowel_path = r"E:\Data_ArcticPhonetics\20220916-English\vowel.txt"
with open(vowel_path, encoding='utf-8') as fid:
    vowels = [x.strip() for x in fid.readlines()]

phon_map_file = r'E:\Data_ArcticPhonetics\20220916-English\english_phoneme.txt'
with open(phon_map_file, encoding='utf-8') as fid:
    phon_map_list = [x.strip() for x in fid.readlines()]
phon_map = {}
for line in phon_map_list:
    sarray = line.split(',')
    phon_map[sarray[0]] = sarray[1]

output_sentence_file = r'E:\Data_ArcticPhonetics\20220916-English\sentence_out.txt'
results = []
for line in input_list:
    print(line)
    sarray = line.split()
    new_words = []
    for word in sarray:
        init_phons = english_dicts[word.lower()].split()
        init_phons = [item for item in filter(lambda x: x.strip() != '', init_phons)]
        map_phons = []
        for ph in init_phons:
            tone = ''
            if ph[-1].isdigit():
                tone = ph[-1]
                ph = ph[:-1]

            map_phons.append(phon_map[ph] + tone)
        # map_phons = [item for item in map(lambda x: phon_map[x])]
        new_words.append(gen_syllable(map_phons))
        save_words_results = [word, gen_syllable(map_phons), '', word.capitalize()]
        results.append(str(save_words_results))
    # results.append(' '.join(new_words))
with open(output_sentence_file, 'w', encoding='utf-8') as wid:
    wid.writelines([x + '\n' for x in results])
print('Done!')
