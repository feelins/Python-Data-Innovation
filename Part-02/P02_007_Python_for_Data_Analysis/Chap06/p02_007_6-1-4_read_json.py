#!/usr/bin/env python
# -*-coding:utf-8 -*-
'''
@File    :   p02_007_6-1-4_read_json.py
@Time    :   2023/07/06 19:09:11
@Author  :   Feelins Shao 
@Version :   1.0
@Contact :   feipengshao@163.com
@License :   (C)Copyright 2022-2023, Feelins Shao
@Desc    :   6.1.4 JSON数据
'''
import json
option = """
{
    'tooltip': {
        'trigger': 'axis',
        'axisPointer': {
            'type': 'cross'
        }
    },
    'legend': {
        'left': 90,
        'bottom':-10,
        'data':['发文量','期刊他引率']
    },
    'xAxis': [
        {
            'type': 'category',
            'axisTick': {'show': false,},
            'data': [
                "2010年","2011年","2012年","2013年","2014年","2015年","2016年","2017年","2018年","2019年","2020年",
            ]	
        }
    ],
    'yAxis': [
        {
            'type': 'value',
            'name': '发文量',
            'splitLine':{'show': false},
            'axisTick': {'show': false,},
            'axisLine': {'show': false},
            'axisLabel': {'formatter': '{value}'}
        },
        {
            'type': 'value',
            'name': '期刊他引率',
            'axisTick': {'show': false,},
            'axisLine': {'show': false},
            'axisLabel': {'formatter': '{value}'}
        }
    ],
    'series': [
        {
            'name':'发文量',
            'type':'line', 
            'color': '#3a3a3a',
            'data':[
                3371,1088,990,0,2716,2844,3034,2371,1881,1696,1659,
            ]
        },
        {
            'name':'期刊他引率',
            'type':'line',
            'yAxisIndex': 1,
            'color': '#00a2ca',
            'data':[
                0.643,0.84,0.853,1,0.997,0.995,0.991,0.991,0.99,0.988,0.988,
            ]
        }
    ]
}
"""
result = json.loads(option)
print(result)