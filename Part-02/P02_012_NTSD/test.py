
# import pandas as pd
# import os

# input_dir = r'D:\007_LLM\000-无监督数据工作二期\00_寻源下载\004_外购\mt-book_transfer'
# results = []
# for file_name in os.listdir(input_dir):
    
#     input_file = os.path.join(input_dir, file_name)
#     with open(input_file, encoding='utf-8') as fid:
#         for _line in fid:
#             _line = _line.strip()
#             sarray = _line.split(',')
#             if len(sarray) > 1:
#                 print(sarray[0])
#                 results.append(sarray[1])

# output_file = r'D:\007_LLM\000-无监督数据工作二期\00_寻源下载\004_外购\mt-book_.txt'
# with open(output_file, 'w', encoding='utf-8') as wid:
#     wid.writelines([x + '\n' for x in results])
            
    # df = pd.read_csv(input_file, skipinitialspace=True, quotechar='"', encoding='utf-8')
    # print('hello')
import pyworld as pw
import librosa
import soundfile as sf

audio_file = r'D:\003_PythonCode\Python-Data-Innovation\Part-02\P02_012_NTSD\00000073.wav'
# y, sr = librosa.load(audio_file, sr=16000)

x, fs = sf.read(audio_file)
f0, sp, ap = pw.wav2world(x, fs)
for f00 in f0:
    print(f00)

