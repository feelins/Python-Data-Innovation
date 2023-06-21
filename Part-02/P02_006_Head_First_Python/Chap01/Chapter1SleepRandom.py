# coding=utf-8
#!/usr/bin/python
# Created on 2018-03-22 13:47
# @author: Administrator
# @name: Chapter1SleepRandom.py
# @info: 

from datetime import datetime
import random
import time

odds = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 57]

for i in range(5):
    right_this_minute = datetime.today().minute
    if right_this_minute in odds:
        print('This minute seems a little odd.')
    else:
        print("Not an odd minute")
    wait_time = random.randint(1, 60)
    time.sleep(wait_time)
    