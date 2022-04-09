#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   p01_014_join_string.py
@Time    :   2022/04/09 11:40:24
@Author  :   feelins, shao 
@Version :   1.0
@Contact :   feipengshao@163.com
@License :   (C)Copyright 2022-2023, 极地语音工作室
@Desc    :   字符串连接
'''

# here put the import lib
# 我们有两种连接字符串的方式，一种是用+号，一种是用join

str1 = ' '.join(['hello', 'world'])
str2 = 'hello' + ' ' + 'world'

print(str1) # hello world
print(str2) # hello world

# 两者的结果是一样的，问题是，两者的性能有区别吗？
import timeit
def test1(strlist):
    return "".join(strlist)

def test2(strlist):
    result = ""
    for v in strlist:
        result = result+v
    return result

if __name__ == "__main__":
    strlist = ["a very very very very very very very long string" for n in range(100000)]
    timer1 = timeit.Timer("test1(strlist)", "from __main__ import strlist, test1")
    timer2 = timeit.Timer("test2(strlist)", "from __main__ import strlist, test2")
    time1 = timer1.timeit(number=100)
    time2 = timer2.timeit(number=100)
    print("join: %f, plus: %f" % (time1, time2)) # join: 0.497081, plus: 153.290512
    
# 当用操作符+连接字符串的时候，每执行一次+都会申请一块新的内存，然后复制上一个+操作的结果和本次操作的右操作符到这块内存空间，因此用+连接字符串的时候会涉及好几次内存申请和复制。
# 而join在连接字符串的时候，会先计算需要多大的内存存放结果，然后一次性申请所需内存并将字符串复制过去
# 这是为什么join的性能优于+的原因。所以在连接字符串数组的时候，我们应考虑优先使用join。