#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   p01_010_how_to_use_at.py
@Time    :   2022/03/13 11:00:03
@Author  :   feelins, shao 
@Version :   1.0
@Contact :   feipengshao@163.com
@License :   (C)Copyright 2022-2023, 极地语音工作室 
@Desc    :   python修饰符@的使用
'''

# here put the import lib
# python函数修饰符@的作用是为现有函数增加额外的功能，常用于插入日志、性能测试、事务处理等等。

# 创建函数修饰符的规则：
# （1）修饰符是一个函数
# （2）修饰符取被修饰函数为参数
# （3）修饰符返回一个新函数
# （4）修饰符维护被维护函数的签名


# 例子1：被修饰符不带参数
def test01():
    def log(func):
        def wrapper():
            print('log开始 ...')
            func()
            print('log结束 ...')
        return wrapper
        
    @log
    def test():
        print('test ..')

    test()

# 例子2：使用functools模块提供的修改函数属性的方法wraps
def test02():
    def log(func):
        def wrapper():
            print('log开始 ...')
            func()
            print('log结束 ...')
        return wrapper
        
    @log
    def test1():
        print('test1 ..')

    def test2():
        print('test2 ..')

    print(test1.__name__) # 可见test1的函数名称变了，如果某些代码用到就会出问题
    print(test2.__name__)
    # wrapper
    # test2

# 例子3：可以使用functools模块提供的修改函数属性的方法wraps

from functools import wraps
def test03():
    def log(func):
        @wraps(func)
        def wrapper():
            print('log开始 ...')
            func()
            print('log结束 ...')
        return wrapper
        
    @log
    def test1():
        print('test1 ..')

    def test2():
        print('test2 ..')

    print(test1.__name__)
    print(test2.__name__)

test01()
test02()
test03()