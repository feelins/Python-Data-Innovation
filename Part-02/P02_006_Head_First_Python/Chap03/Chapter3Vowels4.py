# coding=utf-8
#!/usr/bin/python
# Created on 2018-03-23 10:22
# @author: Administrator
# @name: Chapter3Vowels4.py
# @info: 

vowels = ['a', 'e', 'i', 'o', 'u']

word = "life, the universe, what is up"
found = {}
#for vow in vowels:
#    found[vow] = 0
for letter in word:
    if letter in vowels:
        found.setdefault(letter, 0) #可以有效避免，不存在的键值问题
        found[letter] += 1
for k, v in sorted(found.items()):
    print(k, 'was found', v, 'time(s).')