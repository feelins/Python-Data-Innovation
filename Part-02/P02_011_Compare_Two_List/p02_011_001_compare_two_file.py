#!/usr/bin/env python
# -*-coding:utf-8 -*-
'''
@File    :   p02_011_001_compare_two_file.py
@Time    :   2024/07/01 16:10:21
@Author  :   Feelins Shao 
@Version :   1.0
@Contact :   feipengshao@163.com
@License :   (C)Copyright 2022-2024, Feelins Shao
@Desc    :   比较duxiu两个书单情况
'''


import logging, time
import json
import os
import re

def extract_five_digit_numbers(input_string):
    pattern = r'\d{5,}'
    result = re.findall(pattern, input_string)
    return result


def uniq_list():
    """检查1100W不重复情况"""
    input_book_list_file = r''
    output_error_file = r''
    output_id_stats_file = r''
    errors = []
    total_ids = {}
    tmp_index = 0
    with open(input_book_list_file, encoding='utf-8') as fid:
        for _line in fid:
            tmp_json = json.loads(_line)
            cur_path = tmp_json['path']
            cur_size = tmp_json['size']
            tmp_book_name = os.path.basename(cur_path)
            tmp_ids = extract_five_digit_numbers(tmp_book_name)
            
            
            if len(tmp_ids) != 1:
                errors.append(_line)
            else:
                if tmp_ids[0] not in total_ids:
                    total_ids[tmp_ids[0]] = [tmp_json]
                else:
                    total_ids[tmp_ids[0]].append(tmp_json)
            if tmp_index % 500000 == 0:
                logging.info('检查路径  ' + tmp_book_name)
            tmp_index += 1
            # if tmp_index > 20000:
            #     break

    uniq_ids = []
    tmp_index = 0
    for k, v in total_ids.items():
        if tmp_index % 500000 == 0:
            logging.info('保存结果  ' + k)
        
        result_json = {}
        result_json['id'] = str(k)
        exts = []
        for item in v:
            tmp_book_name = os.path.basename(item['path'])
            ext = os.path.splitext(tmp_book_name)[-1].lower()
            exts.append(ext)
        result_json['exts'] = '|'.join(exts)
        result_json['paths'] = v
        uniq_ids.append(result_json)
        tmp_index += 1
        # if tmp_index > 20000:
        #     break

    with open(output_error_file, 'w', encoding='utf-8') as wid:
        wid.writelines([x + '\n' for x in errors])
    with open(output_id_stats_file, 'w', encoding='utf-8') as wid:
        wid.writelines([json.dumps(x, ensure_ascii=False, separators=(',', ':')) + '\n' for x in uniq_ids])
    print(len(total_ids))



def compare_two_list():
    input_not_found_file = r''
    input_ref_check_file = r''

    output_check_file = r''

    # {"file_name": "13000067", "book_name": "精编和谐家居  隔断与哑口"}
    # {"mtime":1694956248,"path":"/橘子微课/大学堂读秀书库/读秀1.0/资料000/22/12404897_常见眼病知识问答 汪湘琳编 重庆出版社 1986.05 P51.pdf","size":2028835}

    not_found_books = {}
    tmp_index = 0
    with open(input_not_found_file, encoding='utf-8') as fid:
        for _line in fid:
            _line = _line.strip()
            tmp_json = json.loads(_line)
            cur_book_id = tmp_json['file_name']
            
            not_found_books[cur_book_id] = tmp_json
            tmp_index += 1
            if tmp_index % 500000 == 0:
                logging.info('创建未下载字典  ' + cur_book_id)
    
    results = []
    errors = []
    tmp_index = 0
    total_ids = {}
    with open(input_ref_check_file, encoding='utf-8') as fid:
        for _line in fid:
            _line = _line.strip()
            tmp_json = json.loads(_line)
            tmp_path = tmp_json['path']
            tmp_book_name = os.path.basename(tmp_path)
            tmp_ids = extract_five_digit_numbers(tmp_book_name)
            
            
            if len(tmp_ids) != 1:
                errors.append(tmp_json)
            else:
                total_ids[tmp_ids[0]] = ''
                
                if tmp_ids[0] in not_found_books:
                    # logging.info('检查路径  ' + tmp_ids[0])
                    results.append(tmp_json)
            tmp_index += 1
            if tmp_index % 500000 == 0:
                logging.info('检查路径  ' + tmp_book_name)

    # errors2 = []
    # with open(input_not_found_file, encoding='utf-8') as fid:
    #     for _line in fid:
    #         _line = _line.strip()
    #         tmp_json = json.loads(_line)
    #         cur_book_id = tmp_json['file_name']
    #         logging.info('创建未下载字典  ' + cur_book_id)
    #         if cur_book_id not in total_ids:
    #             errors2.append(_line)
            # not_found_books[cur_book_id] = tmp_json

    with open(output_check_file, 'w', encoding='utf-8') as wid:
        wid.writelines([json.dumps(x, ensure_ascii=False, separators=(',', ':')) + '\n' for x in results])
    with open(output_check_file.replace('.json', '_error.json'), 'w', encoding='utf-8') as wid:
        wid.writelines([json.dumps(x, ensure_ascii=False, separators=(',', ':')) + '\n' for x in errors])

    # with open(output_check_file, 'w', encoding='utf-8') as wid:
    #     wid.writelines([json.dumps(x, ensure_ascii=False, separators=(',', ':')) + '\n' for x in results])
    # with open(output_check_file.replace('.json', '_error_2nd.json'), 'w', encoding='utf-8') as wid:
    #     wid.writelines([json.dumps(x, ensure_ascii=False, separators=(',', ':')) + '\n' for x in errors2])

if __name__ == '__main__':

    # 记录开始运行时间
    start_time = time.time()
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
    logging.info('开始: ')

    # uniq_list()
    compare_two_list()
    
    



    # 记录结束时间，计算运行时间
    end_time = time.time()
    total_time = end_time - start_time
    logging.info('结束：')
    logging.info(f'总共用时: {total_time:.2f}秒')
    logging.info('Done!')