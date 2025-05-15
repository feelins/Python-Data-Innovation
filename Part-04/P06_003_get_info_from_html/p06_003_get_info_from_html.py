#!/usr/bin/env python
# -*-coding:utf-8 -*-
'''
@File    :   p06_003_get_info_from_html.py
@Time    :   2023/06/19 15:36:32
@Author  :   Feelins Shao 
@Version :   1.0
@Contact :   feipengshao@163.com
@License :   (C)Copyright 2022-2023, Feelins Shao
@Desc    :   从已有html中获取需要的一些信息
'''

from bs4 import BeautifulSoup
import os
import json
import re
import js2py

def read_param_of_js(file):
    with open(file, mode='r', encoding='utf-8') as f:
        data = f.read()
        res = re.findall(rf'option[ ]*=[ []]*([\s\S]*?);', data)
        # res = re.findall(rf'var {param}[ ]*=[ ]*([\s\S]*?);', data)
        return res[0] if res else None

results = []
input_dir = r'D:\003_PythonCode\download\dl_data1'
for file_name in os.listdir(input_dir):
    print(file_name)
    cur_file = os.path.join(input_dir, file_name)
    with open(cur_file, 'r', encoding='UTF-8') as wb_data:
        Soup = BeautifulSoup(wb_data,'lxml')

        cur_title = Soup.select_one('div.w850.r.info-box').select('div[class="box-title"]')[0].select('h3')[0].contents[0]
        cur_intros = Soup.select_one('div[class="content-box"]').select('div[class="box-con plr20"]')[0].select('p')
        cur_intro = ' '.join([item.contents[0] for item in cur_intros])
        pattern = re.compile(r'option = {')
        scripts = Soup.find("script",text=pattern)
        # xml = js2xml.parse(script,encoding='utf-8',debug=False)
        for scri in scripts:
            scri = scri.strip()
            scri = scri.strip('$').strip('(').strip(';').strip(')')
            context = js2py.EvalJs()
            js = context.execute(scri)
            
            print(js)
            #     - 拷贝使用到js文件的内容到本项目中
            #     - 读取js文件的内容,使用context来执行它们
            with open("BigInt.js", 'r', encoding='utf8') as f:
                context.execute(f.read())
            js2py.eval_js(scri.strip().replace('$(', '').strip(';').strip(')'))
            
        data_line = ''
        # for j, line in enumerate(tmps):
        #     context = js2py.EvalJs()
        #     context.execute(line)
        #     if line.text.find("name:'发文量'") != -1:
        #         tmp_index = line.text.find("name:'发文量'")
        #         print(line)
        results.append(cur_title + '\t' + cur_intro)
    # tmp_result = read_param_of_js(cur_file).replace('\n', '').replace('\t', '')
    # json_result = json.loads(read_param_of_js(cur_file))
    # print(file_name)
output_file = r'dl_data_stat.txt'
with open(output_file, 'w', encoding='utf-8') as wid:
    wid.writelines([x + '\n' for x in results])

print('Done!')