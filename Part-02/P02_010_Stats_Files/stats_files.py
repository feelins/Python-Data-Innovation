#!/usr/bin/env python
# -*-coding:utf-8 -*-

import logging, time
import os, sys
import zipfile
from datetime import datetime
import json


def getFileSize(_file_path):
    """获取文件大小"""
    try:
        return os.path.getsize(_file_path)
    except (FileNotFoundError, OSError) as e:
        return 0
    
def support_gbk(zip_file):
    name_to_info = zip_file.NameToInfo
    for name, info in name_to_info.copy().items():
        real_name = name.encode('cp437').decode('gbk')
        if real_name != name:
            info.filename = real_name
            del name_to_info[name]
            name_to_info[real_name] = info
    return zip_file
    

def statsFile(_input_path, _input_data_name, _input_data_batch, _target_dir, _out_meta_file, _json_mark):
    """统计目录"""
    all_files = readFiles(_input_path)
    result_json = {}
    result_json['数据集'] = _input_data_name
    result_json['批次'] = _input_data_batch
    result_json['目标路径'] = _target_dir
    total_size = 0
    valid_no_pdf_exts = 'epub|mobi|azw|txt|doc|fb2|rtf|lit|lrf|tex'.split('|')
    uniq_paths = []
    exts = {}
    total_json_lines = 0
    valid_pdf = 0
    valid_no_pdf = 0
    for cur_file in all_files:
        cur_file_name = os.path.basename(cur_file)
        cur_file_path = os.path.dirname(cur_file)
        cur_file_ext = os.path.splitext(cur_file)[-1].lower()
        if cur_file_ext in ['.doc', '.docx']:
            cur_file_ext = '.doc'
        if cur_file_ext in ['.azw2', '.azw2']:
            cur_file_ext = '.azw'
        cur_file_simple_name = os.path.splitext(cur_file)[0]
        target_file = cur_file.replace(_input_path, _target_dir)
        if _json_mark and cur_file_ext in ['.json', '.jsonl']:
            with open(cur_file, 'r', encoding='utf-8') as fid:
                cur_jsons = [x.strip() for x in fid.readlines()]
            total_json_lines += len(cur_jsons)
        if cur_file_ext in ['.zip']:
            zip_file = support_gbk(zipfile.ZipFile(cur_file, 'r'))
            for file_name in zip_file.namelist():
                if file_name.endswith('.json') or file_name.endswith('jsonl'):
                    with zip_file.open(file_name) as json_file:
                        for line in json_file:
                            total_json_lines += 1
            cur_zip_files = zip_file.infolist()
            for item in cur_zip_files:
                item_file_name = item.filename
                item_ext = os.path.splitext(item_file_name)[-1].lower()
                item_simple_name = os.path.splitext(item_file_name)[0].lower()
                item_path = cur_file
                item_size = item.file_size
                total_size += item_size
                if item_ext not in exts:
                    exts[item_ext] = 1
                else:
                    exts[item_ext] += 1
                if item_ext in ['.pdf']:
                    valid_pdf += 1
                if item_ext in valid_no_pdf_exts:
                    valid_no_pdf += 1
                # uniq_paths[target_file + '[' + item_file_name + ']'] = []
                cur_path = {}
                cur_path['scp'] = target_file + '[' + item_file_name + ']'
                cur_path['title'] = ''
                cur_path['url'] = ''
                uniq_paths.append(cur_path)
        else:
            if cur_file_ext in ['.pdf']:
                valid_pdf += 1
            if cur_file_ext in valid_no_pdf_exts:
                valid_no_pdf += 1
            if cur_file_ext not in exts:
                exts[cur_file_ext] = 1
            else:
                exts[cur_file_ext] += 1
            cur_file_size = getFileSize(cur_file)
            total_size += cur_file_size
            cur_path = {}
            cur_path['scp'] = target_file
            cur_path['title'] = ''
            cur_path['url'] = ''
            uniq_paths.append(cur_path)
        

    result_json['总个数'] = len(all_files)
    result_json['总大小'] = str(round(total_size / (1024 * 1024 * 1024), 2)) + 'G'
    result_json['有效总数'] = valid_pdf + valid_no_pdf
    result_json['PDF'] = valid_pdf
    result_json['非PDF可处理'] = valid_no_pdf
    result_json['json行数'] = total_json_lines
    result_json['other_ext'] = exts
    result_json['metas'] = uniq_paths
    

    # with open(_out_meta_file, 'w', encoding='utf-8') as wid:
    #     wid.writelines([json.dumps(x, ensure_ascii=False, separators=(',', ':')) + '\n' for x in [result_json]])
    fw_data = json.dumps(result_json, ensure_ascii=False, indent=4)
    with open(_out_meta_file, 'w', newline='\n', encoding='utf-8') as fwd:
        fwd.write(fw_data)


def readFiles(_input_path):
    """读取所有文件"""
    all_files = []
    for roots, dirs, files in os.walk(_input_path):
        if files:
            for file in files:
                cur_file = os.path.join(roots, file)
                all_files.append(cur_file)
    logging.info('获取所有文件：' + str(len(all_files)))
    return list(set(all_files))




if __name__ == '__main__':

    # 记录开始运行时间
    start_time = time.time()
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
    logging.info('开始: ')
    
    # 传输的输入路径
    input_path = sys.argv[1]

    # 传输的数据集名称
    input_data_name = sys.argv[2]

    # 传输的数据批次名称
    input_data_batch = sys.argv[3]

    # 传输到大模型网的路径
    input_target_dir = sys.argv[4]

    # 暂定的下载的元数据文件，默认为数据路径下的meta.json
    input_ref_json_file = sys.argv[5]

    # 输出的meta文件，根据群里讨论，默认为数据路径下的statistics.meta
    output_meta_file = sys.argv[6]

    # 是否读取输入数据里的json行数，默认为false
    json_mark = sys.argv[7]

    # statistics.meta

    statsFile(input_path, input_data_name, input_data_batch, input_target_dir, output_meta_file, json_mark)
    

    # 记录结束时间，计算运行时间
    end_time = time.time()
    total_time = end_time - start_time
    logging.info('结束：')
    logging.info(f'总共用时: {total_time:.2f}秒')
    logging.info('Done!')