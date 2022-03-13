#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   p01_011_better_code_style.py
@Time    :   2022/03/13 11:21:18
@Author  :   feelins, shao 
@Version :   1.0
@Contact :   feipengshao@163.com
@License :   (C)Copyright 2022-2023, 极地语音工作室 
@Desc    :   几个例子，代码的一些更好的形式
'''

# here put the import lib
# good
lst = [1, 2, 3, -2]
for i in range(len(lst)):
    print(lst[i])

# better
for i in lst:
    print(i)
for i, elem in enumerate(lst):
    print(i, elem)
dict1 = {1: 'a', 2: 'b'}
for key, value in dict1.items():
    print(key, value)

# good
f = open('samples/file1')
text = f.read()
print(text)
f.close()

# better, the advantage of 'with' is it finally will close your file even if you make mistakes
with open('samples/file1') as f:
    for line in f:
        print(line)

# good
new_lst = []
for i in lst:
    if i > 0:
        new_lst.append(i)
print(new_lst)

# better, List comprehension
new_lst = [i for i in lst if i > 0]
print(new_lst)

# even better, if you don't need the list object, use generator here, which will save the resources
new_lst = (i for i in lst if i > 0)
for i in new_lst:
    print(i)

# NOT good
x = True
y = []
z = None
if x == True:
    pass
if len(y) == 0:
    pass
if z == None:
    pass

# better
if x:
    pass
if not y:
    pass
if z is None:
    pass


# good, the problem is if key not exist, call exception
value = dict1[2]

# better
value = dict1.get(2, 0)