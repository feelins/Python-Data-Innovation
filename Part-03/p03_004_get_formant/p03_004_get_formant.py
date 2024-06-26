#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   p03_004_get_formant.py
@Time    :   2024/04/05 星期五 15:30:09
@Author  :   feelins, shao
@Version :   1.0
@Contact :   feipengshao@163.com
@License :   (C)Copyright 2022-2023, 极地语音工作室
@Desc    :   
'''

# here put the import lib

import librosa
import numpy as np

# 加载音频文件
audio_file = r'UM101_018_chinese.wav'
y, sr = librosa.load(audio_file)

# 计算音频的短时傅里叶变换（STFT）
stft = librosa.stft(y)

# 计算音频的功率谱密度（PSD）
psd = np.abs(stft) ** 2

# 计算音频的梅尔频谱
mel_spectrogram = librosa.feature.melspectrogram(S=psd, sr=sr)

# 计算音频的梅尔频率倒谱系数（MFCC）
mfcc = librosa.feature.mfcc(S=librosa.power_to_db(mel_spectrogram), sr=sr)

# 提取共振峰
resonance_peaks = librosa.util.peak_pick(mfcc, 3, 3, 3, 5, 0.5, 10)

print("共振峰：", resonance_peaks)
