import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import re

def GetBookList(link, _heads):
    res = requests.get(link, headers=_heads)
    res.encoding = 'utf-8'
    page_content = res.text
    soup = BeautifulSoup(page_content, features='lxml')
    dates = []
    for date in soup.select('span[class="date"]'):
         dates.append(str(date.text).replace('\n','').replace('读过',''))
    tags=[]
    for tag in soup.select('p[class="comment"]'):
         tags.append(str(tag.text))
    pubs=[]
    for pub in soup.select('div[class="pub"]'):
         pubs.append(str(pub.text))
    books=[]
    for book in soup.select('a[title]'):
        books.append(str(book.text).replace('\n','').replace(' ',''))
    for i in range(len(books) - len(dates)):
        books.pop()
    results = {}
    results['book'] = books
    results['date'] = dates
    results['tag'] = tags
    results['pub'] = pubs
    return results

def GetMovieList(link, _heads):
    res = requests.get(link, headers=_heads)
    res.encoding = 'utf-8'
    page_content = res.text
    res.close()
    time.sleep(2)
    soup = BeautifulSoup(page_content, features='lxml')
    tmp_items = soup.select('div[class="item"]')
    dates = []
    tags=[]
    pubs=[]
    books=[]
    imgs = []
    rates = []
    for item in tmp_items:
        img = item.find('img').get('src')
        date = item.find('span', class_='date').text.strip().replace('\n','')
        tmp = item.find('span', class_='comment')
        if tmp:
            comment = item.find('span', class_='comment').text.strip().replace('\n','')
        else:
            comment = 'NULL'
        intro = item.find('li', class_='intro').text.strip().replace('\n','')
        title = item.find('li', class_='title').text.strip().replace('\n','').replace('[可播放]', '').strip()
        title = re.sub(' +', ' ', title)
        # <span class="rating2-t"></span>
        tmp_span_rates = item.find_all('span')
        rate = ''
        for j in tmp_span_rates:
            ttmp = j.get('class')[0]
            if ttmp.find('rating') != -1:
                rate = ttmp
        dates.append(date)
        tags.append(comment)
        pubs.append(intro)
        books.append(title)
        imgs.append(img)
        rates.append(rate)
    results = {}
    results['book'] = books
    results['date'] = dates
    results['tag'] = tags
    results['pub'] = pubs
    results['img'] = imgs
    results['rate'] = rates
    
    return results

def SaveBook_list():
    start_link = '---'#自行修改你的域名

    #在Referer里修改你的域名
    heads = {
        "Host": "book.douban.com",
        "Referer":"---",
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
    }
    depth = 3 #你的页数
    lists= {'BOOK':[], 'DATE':[], 'TAG':[], 'PUB':[]}
    for i in range(depth):
        link= start_link + str(15 * i)
        list = GetBookList(link, heads)
        lists['BOOK'].extend(list['book'])
        lists['DATE'].extend(list['date'])
        lists['TAG'].extend(list['tag'])
        lists['PUB'].extend(list['pub'])

    pd.set_option('display.max_rows', None)
    df_book = pd.DataFrame(lists)
    df_book.to_excel('result_douban_book_self.xlsx')
    print(df_book)

def SaveMovie_list():
    start_link = '---'#自行修改你的域名

    #在Referer里修改你的域名
    heades = {
    "Host": "movie.douban.com",
    "Referer":"---",
    'Cookie':'---'
    }
    depth = 52 #你的页数
    lists= {'BOOK':[], 'DATE':[], 'TAG':[], 'PUB':[], 'IMG':[], 'RATE':[]}
    for i in range(depth):
        link= start_link + str(15 * i)
        print(i)
        list = GetMovieList(link, heades)
        lists['BOOK'].extend(list['book'])
        lists['DATE'].extend(list['date'])
        lists['TAG'].extend(list['tag'])
        lists['PUB'].extend(list['pub'])
        lists['IMG'].extend(list['img'])
        lists['RATE'].extend(list['rate'])

    pd.set_option('display.max_rows', None)
    df_book = pd.DataFrame(lists)
    df_book.to_csv(r'result_douban_movie_self.csv')
    print(df_book)

# 保存书的列表
# SaveBook_list()


# 保存电影列表
SaveMovie_list()