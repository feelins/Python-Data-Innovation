#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   p03_001_read_wavform.py
@Time    :   2022/03/13 10:51:06
@Author  :   feelins, shao 
@Version :   1.0
@Contact :   feipengshao@163.com
@License :   (C)Copyright 2022-2023, 极地语音工作室 
@Desc    :   读取wav
'''

# here put the import lib
import wave
#import numpy as np
#import pylab as pl

# ============ test the algorithm =============
# read wave file and get parameters.
fw = wave.open(r'000001.wav','rb')
params = fw.getparams()
print(params)
nchannels, sampwidth, framerate, nframes = params[:4]
strData = fw.readframes(nframes)
waveData = np.fromstring(strData, dtype=np.int16)
waveData = waveData*1.0/max(abs(waveData))  # normalization
fw.close()

# plot the wave
time = np.arange(0, len(waveData)) * (1.0 / framerate)

index1 = 15000.0 / framerate
index2 = 15512.0 / framerate
index3 = 16000.0 / framerate
index4 = 16512.0 / framerate

pl.subplot(311)
pl.plot(time, waveData)
pl.plot([index1,index1],[-1,1],'r')
pl.plot([index2,index2],[-1,1],'r')
pl.plot([index3,index3],[-1,1],'g')
pl.plot([index4,index4],[-1,1],'g')
pl.xlabel("time (seconds)")
pl.ylabel("Amplitude")

pl.subplot(312)
pl.plot(np.arange(512),waveData[15000:15512],'r')
pl.plot([59,59],[-1,1],'b')
pl.plot([169,169],[-1,1],'b')
print(1/( (169-59)*1.0/framerate ))
pl.xlabel("index in 1 frame")
pl.ylabel("Amplitude")

pl.subplot(313)
pl.plot(np.arange(512),waveData[16000:16512],'g')
pl.xlabel("index in 1 frame")
pl.ylabel("Amplitude")
pl.show()
