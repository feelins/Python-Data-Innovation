#!/usr/bin/env python
# -*-coding:utf-8 -*-
'''
@File    :   p02_012_001_split_ntsd_websites.py
@Time    :   2024/07/19 15:59:04
@Author  :   Feelins Shao 
@Version :   1.0
@Contact :   feipengshao@163.com
@License :   (C)Copyright 2022-2024, Feelins Shao
@Desc    :   None
'''


import logging, time
import json
from urllib.parse import urlparse
import os

def extract_main_site(url):
    try:
        # 使用 urlparse 解析 URL
        parsed_url = urlparse(url)
        
        # 从解析后的 URL 中获取主站点部分（方案和主机）
        main_site = f"{parsed_url.scheme}://{parsed_url.netloc}"
        
        return main_site
    except Exception as e:
        print(f"Error occurred: {e}")
        return None

if __name__ == '__main__':

    # 记录开始运行时间
    start_time = time.time()
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
    logging.info('开始: ')

    in_str = "-- 98714\nnet/2047/d20016418"
    if in_str.find('2047/d20016418') != -1:
        print('hello')
    
    input_ntsd_file = r'D:\007_LLM\20240305-元数据sciEngine-汉斯\论文下载_NDLTD-源信息.json'

    output_ntsds = r'D:\007_LLM\20240305-元数据sciEngine-汉斯\NDLTD'

    diff_urls = {}
    tmp_index = 0
    with open(input_ntsd_file, encoding='utf-8') as fid:
        for _line in fid:
            _line = _line.strip()
            if _line.find('2047/d20016418') != -1 or _line.find('http://s://eidr') != -1 or _line.find('www.oregonpdf.org>') != -1:
                continue
            tmp_json = json.loads(_line)
            cur_url = tmp_json['pdf_page_url']
            cur_url = extract_main_site(cur_url)
            pre_mark = ''
            if cur_url.find('http://') != -1:
                pre_mark = 'http://'
                cur_url = cur_url.replace(pre_mark, '')
            if cur_url.find('https://') != -1:
                pre_mark = 'https://'
                cur_url = cur_url.replace(pre_mark, '')
            cur_url = cur_url.split(':')[0]
            cur_url = pre_mark + cur_url


            if cur_url not in diff_urls:
                diff_urls[cur_url] = [tmp_json]
            else:
                diff_urls[cur_url].append(tmp_json)

            if tmp_index % 1000000 == 0:
                logging.info('读取 ' + str(tmp_index))
            tmp_index += 1
    with open(r'D:\003_PythonCode\Python-Data-Innovation\Part-02\P02_012_NTSD\url.txt', 'w', encoding='utf-8') as wid:
        wid.writelines([x + '\n' for x in diff_urls.keys()])
    for k, v in diff_urls.items():
        logging.info('生成 ' + k)
        tmp_results = []
        cur_mark_name = k.split('/')[-1].replace('.', '_')
        output_file = os.path.join(output_ntsds, cur_mark_name + '.json')
        with open(output_file, 'w', encoding='utf-8') as wid:
            wid.writelines([json.dumps(x, ensure_ascii=False, separators=(',', ':')) + '\n' for x in v])
            



    # 记录结束时间，计算运行时间
    end_time = time.time()
    total_time = end_time - start_time
    logging.info('结束：')
    logging.info(f'总共用时: {total_time:.2f}秒')
    logging.info('Done!')