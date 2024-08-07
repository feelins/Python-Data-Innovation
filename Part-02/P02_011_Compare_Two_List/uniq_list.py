#!/usr/bin/env python
# -*-coding:utf-8 -*-
'''
@File    :   uniq_list.py
@Time    :   2024/07/08 16:01:17
@Author  :   Feelins Shao 
@Version :   1.0
@Contact :   feipengshao@163.com
@License :   (C)Copyright 2022-2024, Feelins Shao
@Desc    :   None
'''


import logging, time
import json
import os
import re

def extract_five_digit_numbers(input_string):
    pattern = r'\d{5,}'
    result = re.findall(pattern, input_string)
    return result


def uniq_download_list():
    input_file = r'D:\007_LLM\20240603-duxiu-not\大学堂原始文件信息_need_download.json'
    output_file = r'D:\007_LLM\20240603-duxiu-not\大学堂原始文件信息_need_download_uniq_id.json'
    output_download_file = r'D:\007_LLM\20240603-duxiu-not\大学堂原始文件信息_need_download_uniq_id_download.json'

    # ？？？
    input_dxt_file = r'D:\007_LLM\20240603-duxiu-not\dxt\dxt.json'

    uniq_ids = {}
    errors = []
    with open(input_file, encoding='utf-8') as fid:
        for _line in fid:
            _line = _line.strip()
            tmp_json = json.loads(_line)
            tmp_path = tmp_json['path']
            tmp_book_name = os.path.basename(tmp_path)
            tmp_ids = extract_five_digit_numbers(tmp_book_name)
            
            
            if len(tmp_ids) != 1:
                errors.append(tmp_json)
            else:
                if tmp_ids[0] in uniq_ids:
                    uniq_ids[tmp_ids[0]].append(tmp_path)
                else:
                    uniq_ids[tmp_ids[0]] = [tmp_path]


    with open(input_dxt_file, encoding='utf-8') as fid:
        for _line in fid:
            _line = _line.strip()
            tmp_json = json.loads(_line)
            tmp_path = tmp_json['path']
            tmp_book_name = os.path.basename(tmp_path)
            tmp_ids = extract_five_digit_numbers(tmp_book_name)
            
            
            if len(tmp_ids) != 1:
                errors.append(tmp_json)
            else:
                if tmp_ids[0] in uniq_ids:
                    uniq_ids[tmp_ids[0]].append(tmp_path)
                else:
                    uniq_ids[tmp_ids[0]] = [tmp_path]
            # print('hello')
    print(len(uniq_ids))
    results = []
    for k, v in uniq_ids.items():
        result_json = {}
        result_json['id'] = k
        result_json['paths'] = v
        exts = {}
        for item in v:
            tmp_book_name = os.path.basename(item)
            ext = os.path.splitext(tmp_book_name)[-1].lower()
            if ext not in exts:
                exts[ext] = [item]
            else:
                exts[ext].append(item)
        result_json['exts'] = '|'.join(exts.keys())
        uniq_path = ''
        if '.pdf' in exts:
            find_path = ''
            for j in exts['.pdf']:
                if j.find('无密码') != -1:
                    find_path = j
            if not find_path:
                find_path = exts['.pdf'][0]
        elif '.zip' in exts:
            find_path = ''
            for j in exts['.zip']:
                if j.find('无密码') != -1:
                    find_path = j
            if not find_path:
                find_path = exts['.zip'][0]
        else:
            find_path = v[0]
        result_json['uniq_path'] = find_path
        results.append(result_json)

    with open(output_file, 'w', encoding='utf-8') as wid:
        wid.writelines([json.dumps(x, ensure_ascii=False, separators=(',', ':')) + '\n' for x in results])

    with open(output_file.replace('.json', '_error.txt'), 'w', encoding='utf-8') as wid:
        wid.writelines([json.dumps(x, ensure_ascii=False, separators=(',', ':')) + '\n' for x in errors])


def uniq_error_list():
    """将出现错误的error，唯一处理"""
    input_error_file01 = r'D:\007_LLM\20240603-duxiu-not\大学堂原始文件信息_need_download_error.json'
    input_error_file02 = r'D:\007_LLM\20240603-duxiu-not\大学堂原始文件信息_need_download_uniq_id_error.txt'

    output_error_file = r'D:\007_LLM\20240603-duxiu-not\大学堂原始文件信息_need_download_ERROR_ids.txt'

    uniq_lines = []
    results = []
    with open(input_error_file01, encoding='utf-8') as fid:
        for _line in fid:
            _line = _line.strip()
            if _line not in uniq_lines:
                uniq_lines.append(_line)
                tmp_json = json.loads(_line)
                results.append(tmp_json)

    with open(input_error_file02, encoding='utf-8') as fid:
        for _line in fid:
            _line = _line.strip()
            if _line not in uniq_lines:
                uniq_lines.append(_line)
                tmp_json = json.loads(_line)
                results.append(tmp_json)

    with open(output_error_file, 'w', encoding='utf-8') as wid:
        wid.writelines([json.dumps(x, ensure_ascii=False, separators=(',', ':')) + '\n' for x in results])




if __name__ == '__main__':

    # 记录开始运行时间
    start_time = time.time()
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
    logging.info('开始: ')

    uniq_error_list()
    


    # 记录结束时间，计算运行时间
    end_time = time.time()
    total_time = end_time - start_time
    logging.info('结束：')
    logging.info(f'总共用时: {total_time:.2f}秒')
    logging.info('Done!')