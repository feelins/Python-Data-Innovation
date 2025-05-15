#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" 
@author: shaopf
@file: seperate_pinyin.py
@version: 1.0
@time: 2019/07/15 13:44:43
@email: feipengshao@163.com
@function： 拼音分成声母，韵母，以及有必要的话，进行拼音转换
"""

from language_util import _TRANSFORM_DICT, _CONSONANT, _VOWEL

def pinyinformat(syllable, language='mandarin'):
    '''format pinyin to mtts's format'''
    if not syllable[-1].isdigit():
        syllable = syllable + '5'
    assert syllable[-1].isdigit()
    syl_no_tone = syllable[:-1]
    if syl_no_tone in _TRANSFORM_DICT[language]:
        syllable = syllable.replace(syl_no_tone, _TRANSFORM_DICT[language][syl_no_tone])
    return syllable


def seperate_syllable(syllable, language='mandarin'):
    """pinyin combos"""
    assert syllable[-1].isdigit(), 'Tone Error' + str(syllable)
    consonants = _CONSONANT[language]
    vowels = _VOWEL[language]
    all_pinyins = {}
    for vv in vowels:
        all_pinyins[vv] = vv
        for cc in consonants:
            all_pinyins[cc + vv] = cc + '+' + vv
    tmp_sys = all_pinyins[syllable[:-1]].split('+')
    if len(tmp_sys) == 1:
        return (tmp_sys[0] + syllable[-1], )
    else:
        return (tmp_sys[0], tmp_sys[1] + syllable[-1])


if __name__ == '__main__':
    print(seperate_syllable('bao2'))
    print(pinyinformat('yang4'))
