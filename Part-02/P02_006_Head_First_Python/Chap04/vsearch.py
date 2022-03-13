#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   Chap4_01.py
@Time    :   2021/05/26 08:50:08
@Author  :   shaopengfei 
@Version :   1.0
@Contact :   feipengshao@163.com
@License :   (C)Copyright 2020-2021 
@Desc    :   the use of function
'''

# here put the import lib
def search4vowels(word):
    """Return any vowels found in a supplied word.(docstring)"""
    vowels = set('aeiou')
    return vowels.intersection(set(word))


# The function with only one line is not means unnecessary, because others can read clearly from the function Name!
def search4letters(phrase:str, letters:str="aeiou") -> set:
    """Return a set of the letters found in phrase"""
    return set(letters).intersection(set(phrase))

print(search4vowels('hello'))
# {'o', 'e'}

print(search4vowels('sky'))
# set()  # 

print(search4letters("many", "ma"))
# {'a', 'm'}

print(search4letters("many people here"))
# {'e', 'o', 'a'}