#!/usr/bin/env python
# -*-coding:utf-8 -*-
'''
@File    :   p05_008_002_get_pitch.py
@Time    :   2025/04/08 09:12:06
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
    # 提取基频（Pitch）
    # pitch = parselmouth.praat.call(sound, "To Pitch", 0.0, 75, 600)  # 设置基频分析参数
    pitch = sound.to_pitch()

    start_time = 0.4
    end_time = 0.5
    
    cur_pitch = parselmouth.praat.call(pitch, "Get value at time", 0.45, "Hertz", "linear")
    min_pitch = parselmouth.praat.call(pitch, "Get minimum", start_time, end_time, "Hertz", "Parabolic")
    max_pitch = parselmouth.praat.call(pitch, "Get maximum", start_time, end_time, "Hertz", "Parabolic")
    mean_pitch = parselmouth.praat.call(pitch, "Get mean", start_time, end_time, "Hertz")
    std_pitch = parselmouth.praat.call(pitch, "Get standard deviation", start_time, end_time, "Hertz")
    print('基频：' + str(cur_pitch))
    print('最小基频：' + str(min_pitch))
    print('最大基频：' + str(max_pitch))
    print('平均基频：' + str(mean_pitch))
    print('基频标准差：' + str(std_pitch))

    pitch_values = pitch.selected_array['frequency']
    print(len(pitch_values))
    
    # 记录结束时间，计算运行时间
    end_time = time.time()
    total_time = end_time - start_time
    logger.info('结束：')
    logger.info(f'总共用时: {total_time:.2f}秒')
    logger.info('Done!')