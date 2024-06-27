#!/usr/bin/env python
# -*-coding:utf-8 -*-
'''
@File    :   p02_009_001_merge_websites.py
@Time    :   2024/01/29 15:51:18
@Author  :   Feelins Shao 
@Version :   1.0
@Contact :   feipengshao@163.com
@License :   (C)Copyright 2022-2023, Feelins Shao
@Desc    :   合并所有域名
'''


import logging, time

if __name__ == '__main__':

    # 记录开始运行时间
    start_time = time.time()
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
    logging.info('开始: ')
    
    input_file = r'2000w.txt_cut1v2.offline_freq.txt'
    old_websites = {}
    new_websites = {}
    uniq_websites = {}
    with open(input_file, encoding='utf-8') as fid:
        for x in fid:
            x = x.strip()
            sarray = x.split('\t')
            tmp_webs = sarray[0].split('.')
            new_web_tag = ''
            if len(tmp_webs) >= 2:
                # new_websites[sarray[0]] = int(sarray[1])
                tmp_website = '.'.join([tmp_webs[-2], tmp_webs[-1]])
                new_web_tag = tmp_website
                # uniq_websites[tmp_website] = 0
            else:
                new_web_tag = sarray[0]
                # uniq_websites[sarray[0]0] = 0
            if new_web_tag in new_websites:
                new_websites[new_web_tag] += int(sarray[1])
            else:
                new_websites[new_web_tag] = int(sarray[1])
            old_websites[sarray[0]] = int(sarray[1])
    # tmp_index = 0
    # for website, t in uniq_websites.items():
    #     # logging.info(website)
    #     num_count = 0
    #     for k, v in old_websites.items():
    #         sarray = k.split('.')
    #         if len(sarray) >= 2:
    #             tmp_website = '.'.join([sarray[-2], sarray[-1]])
    #             if website == tmp_website:
    #                 num_count += v
    #         else:
    #             if website == sarray[0]:
    #                 num_count += v
    #     if tmp_index % 10000 == 0:
    #         logging.info(tmp_index)
    #     tmp_index += 1
    #     uniq_websites[website] = num_count

    output_file = r'D:\007_LLM\20240129-websites\20240129-compare-websites\CC_all_domain.txt'
    sorted_new_websites = sorted(new_websites.items(), key=lambda x:x[1], reverse=True)
    with open(output_file, 'w', encoding='utf-8') as wid:
        wid.writelines([x[0] + '\t' + str(x[1]) + '\n' for x in sorted_new_websites])

    # 记录结束时间，计算运行时间
    end_time = time.time()
    total_time = end_time - start_time
    logging.info('结束：')
    logging.info(f'总共用时: {total_time:.2f}秒')
    logging.info('Done!')