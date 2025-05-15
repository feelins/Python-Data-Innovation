#!/usr/bin/env python
# -*-coding:utf-8 -*-
'''
@File    :   p02_007_6-2-2_read_excel.py
@Time    :   2023/07/07 14:09:36
@Author  :   Feelins Shao 
@Version :   1.0
@Contact :   feipengshao@163.com
@License :   (C)Copyright 2022-2023, Feelins Shao
@Desc    :   6.2.2 读取Excel文件
'''

import pandas as pd
import os


total_logs = []
pd.options.mode.chained_assignment = None # 会有一个warning
_input_excel_file = r'Part-02/P02_007_Python_for_Data_Analysis/Chap06/test.xlsx'
xlsx = pd.ExcelFile(_input_excel_file)
# 这里sheet_name可以用名字，也可以用索引
df = pd.read_excel(xlsx, sheet_name=0)
# 处理缺失值，否则在按行，形成split数组时，缺失值的地方会造成数据乱列
df.fillna('NULL', inplace=True)
# df.assign(PDF是否存在='0', TXT是否存在='0')
# 增加两列
df['PDF是否存在'] = '0'
df['TXT是否存在'] = '0'

# 和这个遍历表格信息
for i in range(len(df)):
    title_name = str(df['书名'][i])
    
    # 还是要注意"这种符号，从txt拷贝到excel的时候，会将后面几行的内容全部变成一个单元格
    # write_Excel = pd.ExcelWriter(_output_file)
    # 给新列赋值
    df['PDF是否存在'][i] = True
    df['PDF是否存在'][i] = True
    

for file_name in pdf_real_list:
    if file_name not in df.loc[:, 'damsCode'].values:
        total_logs.append(file_name + 'PDF不存在')
df.to_excel(_output_file)
with open(_output_file, 'w', encoding='utf-8') as w:
    w.writelines([str(x) + '\t' + str(y) + '\t' + str(z) + '\n' for x, y, z in zip(df['文件编号'].values, df['文件格式'].values, df['书名'].values)])
