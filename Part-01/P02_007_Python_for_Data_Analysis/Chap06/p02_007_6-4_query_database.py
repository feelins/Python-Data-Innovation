#!/usr/bin/env python
# -*-coding:utf-8 -*-
'''
@File    :   p02_007_6-4_query_database.py
@Time    :   2023/07/06 19:48:19
@Author  :   Feelins Shao 
@Version :   1.0
@Contact :   feipengshao@163.com
@License :   (C)Copyright 2022-2023, Feelins Shao
@Desc    :   6.4 与数据库交互
'''

import sqlite3

def create_table():

    query = """create TABLE test (id INTEGER PRIMARY KEY, name TEXT);"""
    conn = sqlite3.connect('p02_007_6-4_query_database.db')
    conn.execute(query)
    conn.commit()
    conn.close()

def insert_data():
    conn = sqlite3.connect('p02_007_6-4_query_database.db')
    in_data = [(i, 'name' + str(i)) for i in range(10)]
    stmt = "INSERT INTO test VALUES (?,?);"
    conn.executemany(stmt, in_data)
    conn.commit()
    conn.close()

def query_data():
    conn = sqlite3.connect('p02_007_6-4_query_database.db')
    cursor = conn.execute('SELECT * FROM test;')
    rows = cursor.fetchall()
    print(rows)

    conn.close()

def db_query_database():
    # 引入sqlalchemy 不需要每次重复很多步骤去执行游标
    import sqlalchemy as sqla
    import pandas as pd
    engine = sqla.create_engine('sqlite:///p02_007_6-4_query_database.db')
    conn = engine.connect()
    # cursor = conn.execute('SELECT * FROM test;')
    print(pd.read_sql('select * from test', engine))
    
    conn.close()



if __name__ == '__main__':
    # select one option below:
    # 1. Create
    # create_table()
    # 2. Insert
    # insert_data()
    # 3. Query
    # query_data()

    # 4. Query database
    db_query_database()