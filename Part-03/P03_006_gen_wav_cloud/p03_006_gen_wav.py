import time
import threading
import sys
import nls



SPEAKER = ['zhifeng_emo', 'siyue']
select_index = 1
SPEAKER_RATE = 100
URL="wss://nls-gateway-cn-shanghai.aliyuncs.com/ws/v1"
TOKEN="e05a6425f4994af5958f18d8955f8f3c"  #参考https://help.aliyun.com/document_detail/450255.html获取token
APPKEY="CKHXq4tUs26fQq6t"       #获取Appkey请前往控制台：https://nls-portal.console.aliyun.com/applist

inpt_text_file = r''
with open(inpt_text_file, encoding='utf-8') as fid:
    TEXT = fid.read()
# TEXT='你看一下这些图标中还有其它的交通工具吗?'

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
      	r = tts.start(self.__text, voice=SPEAKER[select_index], speech_rate=SPEAKER_RATE)
      	print("{}: tts done with result:{}".format(self.__id, r))

def multiruntest(num=500):
    for i in range(0, num):
        name = "thread" + str(i)
        t = TestTts(name, "tests/test_tts_" + SPEAKER[select_index] + "_" + str(SPEAKER_RATE) + ".pcm")
        t.start(TEXT)

nls.enableTrace(True)
multiruntest(1)