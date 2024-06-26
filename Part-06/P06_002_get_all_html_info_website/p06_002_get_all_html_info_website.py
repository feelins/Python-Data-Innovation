#!/usr/bin/env python
# -*-coding:utf-8 -*-
'''
@File    :   p06_002_get_all_html_info_website.py
@Time    :   2023/06/19 17:16:04
@Author  :   Feelins Shao 
@Version :   1.0
@Contact :   feipengshao@163.com
@License :   (C)Copyright 2022-2023, Feelins Shao
@Desc    :   None
'''

import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin
import os

import time
import socket
 
socket.setdefaulttimeout(20)  # 设置socket层的超时时间为20秒


# 发起 HTTP GET 请求获取网页内容
def get_page_content(url):
    try:
        response = requests.get(url)
        tmp_content = response.content
        response.close()
        
        return tmp_content
    except requests.exceptions.RequestException as e:
        print("请求出错:", e)
        return None

# 提取页面中的所有链接
def extract_links(page_content, base_url):
    soup = BeautifulSoup(page_content, 'html.parser')
    links = []
    for link in soup.find_all('a'):
        href = link.get('href')
        absolute_url = urljoin(base_url, href)
        links.append(absolute_url)
    return links

# 保存网页内容到本地文件
def save_page_content(url, page_content):
    # filename = urlparse(url).path
    # if filename == '/':
    #     filename = 'index.html'
    # else:
    #     filename = filename[1:] + '.html'
    filename = url
    if len(filename) < 5 or (len(filename) >= 5 and filename[-5:] != '.html'):
        filename += '.html'
    filename = filename.replace('https://', '').replace('/', '_')
    save_filename = r'\dl_data\\' + filename
    # if os.path.exists(save_filename):
    #     return
    with open(save_filename, 'wb') as file:
        file.write(page_content)

# 爬取网站的所有网页
def crawl_website(url, max_depth):
    visited = set()

    def helper(url, depth):
        # if url in visited or url in ['javascript:;', 'javascript:void(0);'] or url.find('xueshu.com') == -1 or depth > max_depth:
        #     return
        if url in visited or depth > max_depth:
            return
        visited.add(url)
        print(url)

        page_content = get_page_content(url)
        save_page_content(url, page_content)
        time.sleep(1)

        links = extract_links(page_content, url)
        for link in links:
            helper(link, depth + 1)

    helper(url, 0)

# 设置初始的 URL
initial_url = 'https://www.researchgate.net/topics'
max_depth = 3

# 开始爬取网站
crawl_website(initial_url, max_depth)
