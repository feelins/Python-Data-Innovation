# import ttkbootstrap as ttk
# from ttkbootstrap.constants import *


# def click1():
#     print('click once')

# root = ttk.Window()
# ttk.Button(root, text="Button 1", bootstyle=SUCCESS, command=click1).pack(side=LEFT, padx=5, pady=10)
# ttk.Button(root, text="Button 2", bootstyle=(INFO, OUTLINE)).pack(side=LEFT, padx=5, pady=10)
# ttk.Button(root, text="Button 3", bootstyle=(PRIMARY, "outline-toolbutton")).pack(side=LEFT, padx=5, pady=10)
# ttk.Button(root, text="Button 4", bootstyle="link").pack(side=LEFT, padx=5, pady=10)
# ttk.Button(root, text="Button 5", bootstyle="success-link").pack(side=LEFT, padx=5, pady=10)
# ttk.Button(root, text="Button 6", state="disabled").pack(side=LEFT, padx=5, pady=10) #在禁用状态下创建按钮
# # ttk.Entry(root, show=None).pack('0', '默认插入内容')
# root.mainloop()



import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
from ttkbootstrap import Style

import wave
import numpy as np
import pylab as pl

root = tk.Tk()
style = Style()
root.style = style

def select_file():
    file_path = filedialog.askopenfilename()
    file_entry.delete(0, tk.END)
    file_entry.insert(0, file_path)

def play_wave():
    # ============ test the algorithm =============
    # read wave file and get parameters.
    fw = wave.open(file_entry.get(),'rb')
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


file_label = ttk.Label(root, text='Select a file:')
file_label.pack(pady=10)

file_entry = ttk.Entry(root, width=50)
file_entry.pack(pady=10)

file_button = ttk.Button(root, text='Choose File', command=select_file, style='primary.TButton')
file_button.pack(pady=10)

play_button = ttk.Button(root, text='Play', command=play_wave, style='primary.TButton')
play_button.pack(pady=10)

root.mainloop()