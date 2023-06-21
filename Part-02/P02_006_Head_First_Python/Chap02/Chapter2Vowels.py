# coding=utf-8
#!/usr/bin/python
# Created on 2018-03-22 14:35
# @author: Administrator
# @name: Chapter2Vowels.py
# @info: 

vowels = ['a', 'e', 'i', 'o', 'u']
word = "milliways"
for letter in word:
    if letter in vowels:
        print(letter)
print(vowels)
vowels.pop(2)
print(vowels)
print(vowels[3:])