#!/usr/bin/env python
# -*-coding:utf-8 -*-
'''
@File    :   p05_008_001_read_write_wav.py
@Time    :   2025/04/07 14:05:25
@Author  :   feelins
@Version :   1.0
@Contact :   feipengshao@163.com
@License :   (C)Copyright 2025-2026, 极地语音工作室
@Desc    :   None
'''

import logging, time
from logging import handlers
import os
import parselmouth


if __name__ == '__main__':
    cur_root = os.path.split(os.path.realpath(__file__))[0]
    level = logging.INFO
    stamp = int(time.time())
    log_filename = 'log_' + time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(stamp)) + '.log'
    # datefmt='%Y-%m-%d-%H-%M-%S'
    # 创建一个日志器。提供了应用程序接口
    logger = logging.getLogger(log_filename)
    # 设置日志输出的最低等级,低于当前等级则会被忽略
    logger.setLevel(level)
    # 创建日志输出路径
    log_path = os.path.join(cur_root, 'logs')
    if not os.path.exists(log_path):
        os.mkdir(log_path)
    log_file_path = os.path.join(log_path, log_filename)
    # 创建格式器
    formatter = logging.Formatter('%(asctime)s - %(filename)s - %(levelname)s: %(message)s')
    # 创建处理器：ch为控制台处理器，fh为文件处理器
    ch = logging.StreamHandler()
    ch.setLevel(level)
    # 输出到文件
    fh = logging.handlers.TimedRotatingFileHandler(filename=log_file_path, when='D', backupCount=0, encoding='utf-8')
    fh.setLevel(level)
    # 设置日志输出格式
    fh.setFormatter(formatter)
    ch.setFormatter(formatter)
    # 将处理器，添加至日志器中
    logger.addHandler(fh)
    logger.addHandler(ch)
    # 记录开始运行时间
    start_time = time.time()
    logger.info('开始: ')
    
    

    # 加载音频文件
    sound = parselmouth.Sound(r'input_data\000001.wav')
    print("采样率:", sound.sampling_frequency)
    print("时长:", sound.duration)
    print("声道数:", sound.n_channels)

    # 保存为新的WAV文件
    output_path = r"output_data\output_000001.wav"
    sound.save(output_path, parselmouth.SoundFileFormat.WAV)  # 明确指定WAV格式
    
    # 记录结束时间，计算运行时间
    end_time = time.time()
    total_time = end_time - start_time
    logger.info('结束：')
    logger.info(f'总共用时: {total_time:.2f}秒')
    logger.info('Done!')