#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   p01_008_vscode_path_problem.py
@Time    :   2022/03/13 10:09:09
@Author  :   feelins, shao 
@Version :   1.0
@Contact :   feipengshao@163.com
@License :   (C)Copyright 2022-2023, 极地语音工作室 
@Desc    :   VS Code中使用Python相对路径问题
'''

# here put the import lib
# 方法一，如果没有修改Python插件的设置
import os, sys

input_dir = r'../samples'
print(os.getcwd())
print(os.listdir(os.path.join(sys.path[0], input_dir)))

# 方法二，修改了Python插件之后
import os, sys

input_dir = r'../samples'
print(os.getcwd())
print(os.listdir(input_dir))