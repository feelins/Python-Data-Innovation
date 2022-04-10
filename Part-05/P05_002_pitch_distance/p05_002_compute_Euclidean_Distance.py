#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   p05_002_compute_Euclidean_Distance.py
@Time    :   2022/03/21 12:52:56
@Author  :   feelins, shao 
@Version :   1.0
@Contact :   feipengshao@163.com
@License :   (C)Copyright 2022-2023, 极地语音工作室
@Desc    :   计算两个向量的欧氏距离
'''

# here put the import lib
import math
# 计算两点之间的距离
def eucliDist(A,B):
    return math.sqrt(sum([(a - b)**2 for (a,b) in zip(A,B)]))


def method01():
    input_average_pitch_file = r'result_duration_pitch_average.txt'
    input_compare_pitch_file = r'result_duration_pitch_test.txt'
    result_file = r'result_pitch_method_01.txt'
    
    average_pitches = {}

    with open(input_average_pitch_file, encoding='utf-8') as fid:
        for line in fid.readlines()[1:]:
            line = line.strip()
            sarray = line.split()
            average_pitches[sarray[0]] = [float(item) for item in sarray[1:]]
    
    with open(input_compare_pitch_file, encoding='utf-8') as fid:
        input_compare_list = [x.strip() for x in fid.readlines()]

    tones = ['1', '2', '3', '4', '5']
    results = []
    for line in input_compare_list[1:]:
        print(line)
        sarray = line.split('\t')
        cur_tone = sarray[1][-1]
        if cur_tone in average_pitches:
            cur_pitch = [float(item) for item in sarray[3:]]
            result_distance = []
            min_value = 9999
            min_value_index = '0'
            for tone in tones:
                euc_distance = eucliDist(average_pitches[tone], cur_pitch)
                if euc_distance < min_value:
                    min_value = euc_distance
                    min_value_index = tone
                result_distance.append(euc_distance)
            #result = min(result_distance)
            if min_value_index == cur_tone:
                results.append(line + '\t' + '\t'.join([str(item) for item in result_distance]) + '\t' + str(min_value) + '\t' + min_value_index + '\t' + 'YES')
            else:
                results.append(line + '\t' + '\t'.join([str(item) for item in result_distance]) + '\t' + str(min_value) + '\t' + min_value_index + '\t' + 'NO')
    
    with open(result_file, 'w', encoding='utf-8') as wid:
        wid.writelines([x + '\n' for x in results])
        
def method02():
    input_pitch_file = r'result_duration_pitch.txt'
    input_compare_pitch_file = r'result_duration_pitch_test.txt'
    result_file = r'result_pitch_method_02.txt'
    
    pitches = {}

    with open(input_pitch_file, encoding='utf-8') as fid:
        for line in fid.readlines()[1:]:
            line = line.strip()
            sarray = line.split()
            pitches[sarray[1][-1]] = [float(item) for item in sarray[3:]]
    
    with open(input_compare_pitch_file, encoding='utf-8') as fid:
        input_compare_list = [x.strip() for x in fid.readlines()]

    tones = ['1', '2', '3', '4', '5']
    results = []
    for line in input_compare_list[1:]:
        print(line)
        sarray = line.split('\t')
        cur_tone = sarray[1][-1]
        if cur_tone in pitches:
            cur_pitch = [float(item) for item in sarray[3:]]
            result_distance = []
            min_value = 9999
            min_value_index = '0'
            for tone in tones:
                euc_distance = eucliDist(pitches[tone], cur_pitch)
                if euc_distance < min_value:
                    min_value = euc_distance
                    min_value_index = tone
                result_distance.append(euc_distance)
            #result = min(result_distance)
            if min_value_index == cur_tone:
                results.append(line + '\t' + '\t'.join([str(item) for item in result_distance]) + '\t' + str(min_value) + '\t' + min_value_index + '\t' + 'YES')
            else:
                results.append(line + '\t' + '\t'.join([str(item) for item in result_distance]) + '\t' + str(min_value) + '\t' + min_value_index + '\t' + 'NO')
    with open(result_file, 'w', encoding='utf-8') as wid:
        wid.writelines([x + '\n' for x in results])
        
# 方案一
# method01()

# 方案二
method02()
print('done!')