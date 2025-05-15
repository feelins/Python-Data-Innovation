# coding=utf-8
#!/usr/bin/python
# Created on 2018-03-22 15:49
# @author: Administrator
# @name: Chapter2Marvin.py
# @info: 

paranoid_android = "Marvin, the Paranoid Android"
letters = list(paranoid_android)
for char in letters[:6]:
    print('\t', char)
print()
for char in letters[-7:]:
    print('\t'*2, char)
for char in letters[12:20]:
    print('\t'*3, char)