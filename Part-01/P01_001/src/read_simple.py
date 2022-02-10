from email import header
#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   read_simple.py
@Time    :   2022/02/11 01:24:30
@Author  :   feelins, shao 
@Version :   1.0
@Contact :   feipengshao@163.com
@License :   (C)Copyright 2022-2023, 极地语音工作室
@Desc    :   读文本文件内容，打印出来
'''

# here put the import lib
my_file = r'Part-01\P01_001\data\my_txt.txt'
with open(my_file, encoding='utf-8') as fid:
    file_content = [x.strip() for x in fid.readlines()]

for line in file_content:
    print(line)
print('Done!')