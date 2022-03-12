#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   p01_003_internal_function_of_dict.py
@Time    :   2022/03/01 09:31:16
@Author  :   feelins, shao 
@Version :   1.0
@Contact :   feipengshao@163.com
@License :   (C)Copyright 2022-2023, 极地语音工作室
@Desc    :   字典的内置函数
'''

# 清除字典
cur_dict = {'tom' : 16, 'jerry' : 18, 'mary' : 20}
print(cur_dict)  # {'tom': 16, 'jerry': 18, 'mary': 20}
cur_dict.clear()  # 清除字典内容，输出为空 {}
print(cur_dict)

# dict.get()搜索字典，如果发现返回关联的值。如果未找到，则返回None。
cur_dict = {'tom' : 16, 'jerry' : 18, 'mary' : 20}
print(cur_dict.get('tom'))
print(cur_dict.get('Lisa')) # 输出为None

# dict.items(), 返回字典中的键值对列表
d = {'a': 10, 'b': 20, 'c': 30}
print(d) # {'a': 10, 'b': 20, 'c': 30}
print(list(d.items()))  #  [('a', 10), ('b', 20), ('c', 30)]
print(list(d.items())[1][0]) # b, 输出第二个元素('b', 20)的第一个值
# 遍历也可以用到
for k, v in d.items():
    print(k + ', ' + str(v))
# a, 10
# b, 20
# c, 30

# dict.keys(), dict.values(), 返回字典的键和值的列表
d = {'a': 10, 'b': 20, 'c': 30}
print(list(d.values()))  # [10, 20, 30]
print(list(d.keys())) # ['a', 'b', 'c']

# dict.pop(), 从字典中删除一个键，如果它存在，删除成功，并返回它的值；如果不存在，则报异常
d = {'a': 10, 'b': 20, 'c': 30}
print(d) # {'a': 10, 'b': 20, 'c': 30}
d.pop('b')
print(d) # {'a': 10, 'c': 30}
# d.pop('z') # KeyError: 'z'


# dict.popitem(), 从字典删除键值对，删除最后一个，直到字典被清空，最后报异常
d = {'a': 10, 'b': 20, 'c': 30}
print(d) # {'a': 10, 'b': 20, 'c': 30}
d.popitem()
print(d) # {'a': 10, 'b': 20}
d = {}
# d.popitem() # KeyError: 'popitem(): dictionary is empty'

# dict.update(), 将字典与另一个字典或可迭代的键值对合并
d1 = {'a': 10, 'b': 20, 'c': 30}
d2 = {'b': 200, 'd': 400}
d1.update(d2)
print(d1) # {'a': 10, 'b': 200, 'c': 30, 'd': 400}