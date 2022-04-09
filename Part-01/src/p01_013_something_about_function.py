#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   p01_013_something_about_function.py
@Time    :   2022/04/09 10:52:58
@Author  :   feelins, shao 
@Version :   1.0
@Contact :   feipengshao@163.com
@License :   (C)Copyright 2022-2023, 极地语音工作室
@Desc    :   理解一些关于函数的概念
'''

# here put the import lib
def func():
    '''这是一个函数'''
    print('Hi, I\'m here.')
 
# 1. 调用这个函数，相当于可以批量的运行函数内的语句   
for i in range(5):
    func()
# Hi, I'm here.
# Hi, I'm here.
# Hi, I'm here.
# Hi, I'm here.
# Hi, I'm here.

# 2. 函数的对象特性，Python中的所有对象都有3个特征：身份（每个对象都可以通过id获取），类型和值
print(type(func)) # <class 'function'>  类型，class类型
print(func) # <function func at 0x000001431482A200>  值，内存地址
print(id(func)) # 1387618542080  身份，id

# 3. 函数可以赋值
func2 = func # 我们将func作为一个值，赋值给func2, func2也可以作为一个函数使用了。
print(func) # <function func at 0x000001882D66A200>
print(func2) # <function func at 0x000001882D66A200>
for i in range(5):
    func2()

# 4. 函数可以当参数传递， another_fun函数有一个参数是func，fun函数当参数一样直接传递给了func；接着我们在another_fun()里面可以可以直接调用了
def another_func(f):
    print('Hello, I am another func')
    f()
    
another_func(func) 
# Hello, I am another func
# Hi, I'm here.

# 5. 返回值也可以是函数, 经常使用的闭包，装饰器就是这么玩的
def show_name(name):
    def inner(age):
        print('My name is: ', name)
        print('My age is: ', age)
    return inner

# 我们定义一个函数叫show_name，这个函数的返回值是一个函数。也就是说变量f就是返回的inner函数。所以我们可以用f('20')来执行函数
f = show_name('Tome')
f('20')
# My name is:  Tome
# My age is:  20


# 6. 函数可以在字典里面使用: 函数可以容器中使用，比如列表，字典里面象参数一样使用
def show_apple(price):
    print('This is apple\'s price: ', price)

def show_orange(price):
    print('This is orange\'s price: ', price)
    
shops = {'apple': show_apple, 'orange': show_orange} # 函数作为一个参数在字典里使用

def choose(your_choice, price):
    shops[your_choice](price)
    
choose('apple', 8.8) # This is apple's price:  8.8
choose('orange', 15) # This is orange's price:  15

# 我们把函数show_apple()和show_orange()当作变量一样放在字典里面，外边设计一个函数可以根据类别来动态的调用函数。这样的设计实战是太巧妙了
