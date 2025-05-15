#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   p04_001_001_wordSeg.py
@Time    :   2022/03/14 20:46:02
@Author  :   feelins, shao 
@Version :   1.0
@Contact :   feipengshao@163.com
@License :   (C)Copyright 2022-2023, 极地语音工作室 
@Desc    :   前后项分词
'''

# here put the import lib

import sys
import re
#StopWordtmp = ['。', '，', '！', '？', '：', '“', '”', '‘', '’', '（', '）', '【', '】', '｛', '｝', '-', '－', '～', '［', '］', '〔', '〕', '．', '＠', '￥', '•', '.']
StopWordtmp = [' ', u'\u3000', u'\x30fb', u'\u3002', u'\uff0c', u'\uff01', u'\uff1f', u'\uff1a', u'\u201c', u'\u201d', u'\u2018', u'\u2019', u'\uff08', u'\uff09', u'\u3010', u'\u3011', u'\uff5b', u'\uff5d', u'-', u'\uff0d', u'\uff5e', u'\uff3b', u'\uff3d', u'\u3014', u'\u3015', u'\uff0e', u'\uff20', u'\uffe5', u'\u2022', u'.']

WordDic = {}
StopWord = []
span = 16

def InitStopword():
    for key in StopWordtmp:
        StopWord.append(key)

def InitDic(Dicfile):
    f = open(Dicfile, 'r', encoding = 'utf-8')
    for line in f:
        curWords = line.strip().split(':')
        WordDic[curWords[0]] = 1;
    f.close()
    print(str(len(WordDic)))
    print("Dictionary has built down!")

def WordSeg(Inputfile, Outputfile, outputfile2):
    f = open(Inputfile, 'r', encoding = 'utf-8')
    w = open(Outputfile, 'w', encoding = 'utf-8')
    w2 = open(Outputfile2, 'w', encoding = 'utf-8')
    prewritelinelist = []
    postwritelinelist = []
    for line in f:
        line = line.strip()
        senList = []
        newsenList = []
        tmpword = ''
        for i in range(len(line)):
            if line[i] in StopWord:
                senList.append(tmpword)
                senList.append(line[i])
                tmpword = ''
            else:
                tmpword += line[i]
                if i == len(line) - 1:
                    senList.append(tmpword)
        #Pre
        for key in senList:
            if key in StopWord:
                newsenList.append(key)
            else:
                tmplist = PreSenSeg(key, span)
                for keyseg in tmplist:
                    newsenList.append(keyseg)
        Prewriteline = ''
        for key in newsenList:
            Prewriteline = Prewriteline + key + '/'
        prewritelinelist.append(Prewriteline.strip('/') + "\n")
        #Post
        newsenList = []
        for key in senList:
            if key in StopWord:
                newsenList.append(key)
            else:
                tmplist = PostSenSeg(key, span)
                for keyseg in tmplist:
                    newsenList.append(keyseg)
        Postwriteline = ''
        for key in newsenList:
            Postwriteline = Postwriteline + key + '/'
        Postwriteline = Postwriteline.strip('/') + "\n"
        postwritelinelist.append(Postwriteline)

    w.writelines(prewritelinelist)
    w2.writelines(postwritelinelist)
    f.close()
    w.close()
    w2.close()
    
def WordSegLine(line):
    line = line.strip()
    senList = []
    newsenList = []
    tmpword = ''
    for i in range(len(line)):
        if line[i] in StopWord:
            senList.append(tmpword)
            senList.append(line[i])
            tmpword = ''
        else:
            tmpword += line[i]
            if i == len(line) - 1:
                senList.append(tmpword)
    #Pre
    for key in senList:
        if key in StopWord:
            newsenList.append(key)
        else:
            tmplist = PreSenSeg(key, span)
            for keyseg in tmplist:
                newsenList.append(keyseg)
    Prewriteline = ''
    for key in newsenList:
        Prewriteline = Prewriteline + key + ' '
    return Prewriteline

def PreSenSeg(sen, span):
    post = span
    if len(sen) < span:
        post = len(sen)
    cur = 0
    revlist = []
    while 1:
        if cur >= len(sen):
            break
        s = re.search(u"^[0|1|2|3|4|5|6|7|8|9|\uff11|\uff12|\uff13|\uff14|\uff15|\uff16|\uff17|\uff18|\uff19|\uff10|\u4e00|\u4e8c|\u4e09|\u56db|\u4e94|\u516d|\u4e03|\u516b|\u4e5d|\u96f6|\u5341|\u767e|\u5343|\u4e07|\u4ebf|\u5146|\uff2f]+", sen[cur:])
        if s:
            if s.group() != '':
                revlist.append(s.group())
            cur = cur + len(s.group()) 
            post = cur + span
            if post > len(sen):
                post = len(sen)
        s = re.search(u"^[a|b|c|d|e|f|g|h|i|j|k|l|m|n|o|p|q|r|s|t|u|v|w|x|y|z|A|B|C|D|E|F|G|H|I|J|K|L|M|N|O|P|Q|R|S|T|U|V|W|X|Y|Z|\uff41|\uff42|\uff43|\uff44|\uff45|\uff46|\uff47|\uff48|\uff49|\uff47|\uff4b|\uff4c|\uff4d|\uff4e|\uff4f|\uff50|\uff51|\uff52|\uff53|\uff54|\uff55|\uff56|\uff57|\uff58|\uff59|\uff5a|\uff21|\uff22|\uff23|\uff24|\uff25|\uff26|\uff27|\uff28|\uff29|\uff2a|\uff2b|\uff2c|\uff2d|\uff2e|\uff2f|\uff30|\uff31|\uff32|\uff33|\uff35|\uff36|\uff37|\uff38|\uff39|\uff3a]+", sen[cur:])
        if s:
            if s.group() != '':
                revlist.append(s.group())
            cur = cur + len(s.group()) 
            post = cur + span
            if post > len(sen):
                post = len(sen)
        if (WordDic.__contains__(sen[cur:post])) or (cur + 1 == post):
            if sen[cur:post] != '':
                revlist.append(sen[cur:post])
            cur = post
            post = post + span
            if post > len(sen):
                post = len(sen)
        else:
            post -= 1    
    return revlist 

def PostSenSeg(sen, span):
    cur = len(sen)
    pre = cur -  span 
    if pre < 0:
        pre = 0
    revlist = []
    while 1:
        if cur <= 0:
            break
        s = re.search(u"[0|1|2|3|4|5|6|7|8|9|\uff11|\uff12|\uff13|\uff14|\uff15|\uff16|\uff17|\uff18|\uff19|\uff10|\u4e00|\u4e8c|\u4e09|\u56db|\u4e94|\u516d|\u4e03|\u516b|\u4e5d|\u96f6|\u5341|\u767e|\u5343|\u4e07|\u4ebf|\u5146|\uff2f]+$", sen[pre:cur])
        if s:
            if s.group() != '':
                revlist.append(s.group())
            cur = cur - len(s.group()) 
            pre = cur - span
            if pre < 0:
                pre = 0
        s = re.search(u"^[a|b|c|d|e|f|g|h|i|j|k|l|m|n|o|p|q|r|s|t|u|v|w|x|y|z|A|B|C|D|E|F|G|H|I|J|K|L|M|N|O|P|Q|R|S|T|U|V|W|X|Y|Z|\uff41|\uff42|\uff43|\uff44|\uff45|\uff46|\uff47|\uff48|\uff49|\uff47|\uff4b|\uff4c|\uff4d|\uff4e|\uff4f|\uff50|\uff51|\uff52|\uff53|\uff54|\uff55|\uff56|\uff57|\uff58|\uff59|\uff5a|\uff21|\uff22|\uff23|\uff24|\uff25|\uff26|\uff27|\uff28|\uff29|\uff2a|\uff2b|\uff2c|\uff2d|\uff2e|\uff2f|\uff30|\uff31|\uff32|\uff33|\uff35|\uff36|\uff37|\uff38|\uff39|\uff3a]+", sen[pre:cur])
        if s:
            if s.group() != '':
                revlist.append(s.group())
            cur = cur - len(s.group()) 
            pre = cur - span
            if pre < 0:
                pre = 0

        if (WordDic.__contains__(sen[pre:cur])) or (cur - 1 == pre):
            if sen[pre:cur] != '':
                revlist.append(sen[pre:cur])
            cur = pre
            pre = pre - span
            if pre < 0:
                pre = 0
        else:
            pre += 1    
    return revlist[::-1] 

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: python wordseg.py Dicfile Inputfile Outfile")
    Dicfile = r'E:\008_Mongo\Process_20180210\Models\TextGridOver_20180409_CiganCizhui_FinalResult_20180412_seg_dict.txt'
    Inputfile = r'E:\008_Mongo\Process_20180210\Models\TextGridOver_20180409_CiganCizhui_FinalResult_20180412_ToSeg.txt'
    Outputfile = r'E:\008_Mongo\Process_20180210\Models\TextGridOver_20180409_CiganCizhui_FinalResult_20180412_ToSeg_result1.txt'
    Outputfile2 = r'E:\008_Mongo\Process_20180210\Models\TextGridOver_20180409_CiganCizhui_FinalResult_20180412_ToSeg_result1.txt'
    InitDic(Dicfile)
    InitStopword()
    WordSeg(Inputfile, Outputfile, Outputfile2)
