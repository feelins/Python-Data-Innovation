import time
import threading
import sys
import pyworld as pw
import soundfile as sf
import numpy as np

import nls

def read_numbers_from_file(file_path):
    numbers = []
    with open(file_path, 'r') as file:
        for line in file:
            # 假设文件中的每一行都是一个数字或包含多个用空格分隔的数字
            line_numbers = map(float, line.split())
            numbers.extend(line_numbers)
    return np.array(numbers, dtype=np.float64)

# Convert speech into features (using default arguments)
WAV_FILE = r'tests\test_tts_阿里-知小夏.wav'
x, fs = sf.read(WAV_FILE)
f0, sp, ap = pw.wav2world(x, fs)
f0_FILE = r'tests\test_tts_阿里-知小夏.f0'
with open(f0_FILE, 'w') as wid:
    wid.writelines([str(x) + '\n' for x in f0])
f0_FILE = r'tests\test_tts_阿里-知小夏.new.f0'
f0_ = read_numbers_from_file(f0_FILE)
y = pw.synthesize(np.array(f0_), sp, ap, fs)
OUT_WAV_FILE = r'tests\test_tts_阿里-知小夏_out.wav'
sf.write(OUT_WAV_FILE, y, fs)

URL="wss://nls-gateway-cn-shanghai.aliyuncs.com/ws/v1"
TOKEN="d2ecff27a2814f6da888763ed17ca915"  #参考https://help.aliyun.com/document_detail/450255.html获取token
APPKEY="CKHXq4tUs26fQq6t"       #获取Appkey请前往控制台：https://nls-portal.console.aliyun.com/applist



TEXT='你看一下这些图标中还有其它的交通工具吗?'

#以下代码会根据上述TEXT文本反复进行语音合成
class TestTts:
    def __init__(self, tid, test_file):
        self.__th = threading.Thread(target=self.__test_run)
        self.__id = tid
        self.__test_file = test_file
   
    def start(self, text):
        self.__text = text
        self.__f = open(self.__test_file, "wb")
        self.__th.start()
    
    def test_on_metainfo(self, message, *args):
        print("on_metainfo message=>{}".format(message))  

    def test_on_error(self, message, *args):
        print("on_error args=>{}".format(args))

    def test_on_close(self, *args):
        print("on_close: args=>{}".format(args))
        try:
            self.__f.close()
        except Exception as e:
            print("close file failed since:", e)

    def test_on_data(self, data, *args):
        try:
            self.__f.write(data)
        except Exception as e:
            print("write data failed:", e)

    def test_on_completed(self, message, *args):
        print("on_completed:args=>{} message=>{}".format(args, message))


    def __test_run(self):
      	print("thread:{} start..".format(self.__id))
      	tts = nls.NlsSpeechSynthesizer(url=URL,
      	      	      	      	       token=TOKEN,
      	      	      	      	       appkey=APPKEY,
      	      	      	      	       on_metainfo=self.test_on_metainfo,
      	      	      	      	       on_data=self.test_on_data,
      	      	      	      	       on_completed=self.test_on_completed,
      	      	      	      	       on_error=self.test_on_error,
      	      	      	      	       on_close=self.test_on_close,
      	      	      	      	       callback_args=[self.__id])
      	print("{}: session start".format(self.__id))
      	r = tts.start(self.__text, voice="xiaogang")
      	print("{}: tts done with result:{}".format(self.__id, r))

def multiruntest(num=500):
    for i in range(0, num):
        name = "thread" + str(i)
        t = TestTts(name, "tests/test_tts_zhishuo99.pcm")
        t.start(TEXT)

nls.enableTrace(True)
multiruntest(1)