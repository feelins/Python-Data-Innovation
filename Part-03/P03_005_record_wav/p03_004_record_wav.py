#!/usr/bin/env python
# -*-coding:utf-8 -*-
'''
@File    :   p03_004_record_wav.py
@Time    :   2024/08/08 10:10:02
@Author  :   Feelins Shao 
@Version :   1.0
@Contact :   feipengshao@163.com
@License :   (C)Copyright 2022-2024, Feelins Shao
@Desc    :   利用Python录音脚本，随后显示频谱图
'''


import logging, time
import pyaudio
import wave
import librosa.display
import matplotlib.pyplot as plt
import librosa

if __name__ == '__main__':

    # 记录开始运行时间
    start_time = time.time()
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
    logging.info('开始: ')
    
    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 2
    RATE = 16000
    RECORD_SECONDS = 10
    WAVE_OUTPUT_FILENAME = "test.wav"

    p = pyaudio.PyAudio()

    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

    print("开始录音......")

    frames = []

    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)

    print("录音结束!")

    stream.stop_stream()
    stream.close()
    p.terminate()

    wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()

    data1, sample_rate = librosa.load("test.wav", sr=RATE)
    plt.plot(data1)
    plt.show()
    plt.figure(figsize=(14, 5))
    
    librosa.display.waveplot(data1, sample_rate)
    plt.show()


    # 记录结束时间，计算运行时间
    end_time = time.time()
    total_time = end_time - start_time
    logging.info('结束：')
    logging.info(f'总共用时: {total_time:.2f}秒')
    logging.info('Done!')
