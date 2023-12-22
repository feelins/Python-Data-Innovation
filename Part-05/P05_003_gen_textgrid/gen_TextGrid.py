#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   gen_TextGrid.py
@Time    :   2022/04/10 17:58:16
@Author  :   feelins, shao 
@Version :   1.0
@Contact :   feipengshao@163.com
@License :   (C)Copyright 2022-2023, 极地语音工作室
@Desc    :   读生成TextGrid
'''

# here put the import lib
import textgrid as tg
import os
import wave

input_label_dir = r'D:\003_PythonCode\20230318-luchen\潮州话字音标注to鹏飞20230630\labels'
input_wav_dir = r'D:\003_PythonCode\20230318-luchen\潮州话字音标注to鹏飞20230630\未能正常处理的wav'

output_data_dir = r'D:\003_PythonCode\20230318-luchen\潮州话字音标注to鹏飞20230630\data_out'
if not os.path.exists(output_data_dir):
    os.mkdir(output_data_dir)
error_file = r'D:\003_PythonCode\20230318-luchen\潮州话字音标注to鹏飞20230630\data_out_error.txt'

phon_dict_file = r'D:\003_PythonCode\20230318-luchen\潮州话字音标注to鹏飞20230630\dict\zi2ShengYun.txt'
with open(phon_dict_file, encoding='utf-8') as fid:
    phon_dict_list = [x.strip() for x in fid.readlines()]
phon_dicts = {}
for line in phon_dict_list[1:]:
    word, phon = line.split('\t')
    phon_dicts[word] = phon
tone_dict_file = r'D:\003_PythonCode\20230318-luchen\潮州话字音标注to鹏飞20230630\dict\zi2Tone.txt'
with open(tone_dict_file, encoding='utf-8') as fid:
    tone_dict_list = [x.strip() for x in fid.readlines()]
tone_dicts = {}
for line in tone_dict_list[1:]:
    word, tone = line.split('\t')
    tone_dicts[word] = tone

errors = []
for file_name in os.listdir(input_label_dir):
    wav_file = os.path.join(input_wav_dir, file_name.replace('.txt', '.wav'))
    if file_name.find('.txt') != -1 and os.path.exists(wav_file):
        print(file_name)
        
        label_file = os.path.join(input_label_dir, file_name)
        with open(label_file, encoding='utf-8') as fid:
            labels = [x.strip() for x in fid.readlines()]
        
        char_words = labels[1].split()
        char_words = [item for item in filter(lambda x: x.strip() != '', char_words)]
        _N = len(char_words)
        wavefile = wave.open(wav_file, 'r')
        #swavefile.readframes
        framerate = wavefile.getframerate()
        numframes = wavefile.getnframes()
        #wavefile
        duration = float(numframes) / float(framerate)
        old_begin = 0
        old_end = duration
        new_begin = old_begin + 0.1
        new_end = old_end - 0.1

        _real_N = _N + _N - 1
        step_time = (new_end - new_begin) / _real_N

        output_grid_file = os.path.join(output_data_dir, file_name.replace('.txt', '.TextGrid'))
        result_list = []
        word_tiers = []
        tone_tiers = []
        phons_tiers = []
        null_tiers = []
        tmp_begin = new_begin
        has_error = []
        word_tiers.append(tg.Entry(old_begin, new_begin, '', '字'))
        tone_tiers.append(tg.Entry(old_begin, new_begin, '', '声调'))
        phons_tiers.append(tg.Entry(old_begin, new_begin, '', '声韵'))
        word_index = 0
        for j in range(_real_N):
            
            tmp_time = tmp_begin + step_time
            tone_info = ''
            phon_info = ''
            if char_words[word_index] not in tone_dicts:
                has_error.append(char_words[word_index] + ', 无声调')
                tone_info = '无声调'
            else:
                tone_info = tone_dicts[char_words[word_index]]
            if char_words[word_index] not in phon_dicts:
                has_error.append(char_words[word_index] + ', 无拼音')
                phon_info = '无拼音'
            else:
                phon_info = phon_dicts[char_words[word_index]]
            if j % 2 == 0:
                word_tiers.append(tg.Entry(tmp_begin, tmp_time, char_words[word_index], '字'))
                tone_tiers.append(tg.Entry(tmp_begin, tmp_time, tone_info, '声调'))
                # phon_tier = phon_dicts[char_words[j]]
                phons = phon_info.split()
                phons = [item for item in filter(lambda x: x.strip() != '', phons)]
                inside_duration = tmp_time - tmp_begin
                inside_step = inside_duration / len(phons)
                inside_tmp_begin = tmp_begin
                for k in range(len(phons)):
                    inside_tmp_time = inside_tmp_begin + inside_step
                    if k == len(phons) - 1:
                        inside_tmp_time = tmp_time
                    phons_tiers.append(tg.Entry(inside_tmp_begin, inside_tmp_time, phons[k], '声韵'))
                    inside_tmp_begin =  inside_tmp_time
                word_index += 1
            else:
                if j != _real_N - 1:
                    word_tiers.append(tg.Entry(tmp_begin, tmp_time, '', '字'))
                    tone_tiers.append(tg.Entry(tmp_begin, tmp_time, '', '声调'))
                    phons_tiers.append(tg.Entry(tmp_begin, tmp_time, '', '声韵'))
            tmp_begin = tmp_time
        
        if has_error:
            errors.append(file_name + '有错误！！！;'.join(has_error))
        else:
            word_tiers.append(tg.Entry(new_end, old_end, '', '字'))
            tone_tiers.append(tg.Entry(new_end, old_end, '', '声调'))
            phons_tiers.append(tg.Entry(new_end, old_end, '', '声韵'))
            null_tiers.append(tg.Entry(0, duration, '', '复元音'))
            result_list.append(word_tiers)
            result_list.append(phons_tiers)
            result_list.append(tone_tiers)
            result_list.append(null_tiers)
            tg.write_textgrid(output_grid_file, result_list)
with open(error_file, 'w', encoding='utf-8') as wid:
    wid.writelines([x + '\n' for x in errors])
print('Done!')
