#!/usr/bin/env python
# -*-coding:utf-8 -*-
'''
@File    :   p03_006_gen_wav.py
@Time    :   2024/11/05 09:13:12
@Author  :   feelins
@Version :   1.0
@Contact :   feipengshao@163.com
@License :   (C)Copyright 2024-2025, shao
@Desc    :   None
'''

import logging, time
from logging import handlers
import os
import threading
import sys
import nls
import os

SPEAKER = ['zhifeng_emo', 'siyue']
select_index = 0
SPEAKER_RATE = 0
URL="wss://nls-gateway-cn-shanghai.aliyuncs.com/ws/v1"
TOKEN="fb1f970aff034177b85c0876af4dad55"  #参考https://help.aliyun.com/document_detail/450255.html获取token
APPKEY="CKHXq4tUs26fQq6t"       #获取Appkey请前往控制台：https://nls-portal.console.aliyun.com/applist

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
        t = TestTts(name, os.path.join(output_pcm_dir, SPEAKER[select_index] + "_" + str(SPEAKER_RATE).zfill(2) + "_" + sarray[0].strip() + "_" + sarray[1].strip() + ".pcm"))
        t.start(TEXT)


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
    formatter = logging.Formatter('%(asctime)s - %(pathname)s - %(levelname)s: %(message)s')
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
    
    

    input_text_file = r'input_txt.txt'
    output_pcm_dir = r'tests_1107'
    if not os.path.exists(output_pcm_dir):
        os.mkdir(output_pcm_dir)
    with open(input_text_file, encoding='utf-8') as fid:
        input_texts = [x.strip() for x in fid.readlines()]
    step_num = len(input_texts) // 10
    begin = 0
    end = 0
    for _line in input_texts:
        # end = patch * step_num
        # this_patch = input_texts[begin:end]
        # TEXT = ''.join(this_patch)
        # begin = end
        TEXT = _line
        sarray = TEXT.split('。')
        logger.info(sarray[0] + ', ' + sarray[1])
        time.sleep(5)
        
        
        # with open(input_text_file, encoding='utf-8') as fid:
        #     TEXT = fid.read()
        # TEXT='你看一下这些图标中还有其它的交通工具吗?'
        # https://sourceforge.net/projects/sox/

        

        nls.enableTrace(True)
        multiruntest(1)
        time.sleep(10)
    
    # 记录结束时间，计算运行时间
    end_time = time.time()
    total_time = end_time - start_time
    logger.info('结束：')
    logger.info(f'总共用时: {total_time:.2f}秒')
    logger.info('Done!')