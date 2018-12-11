'''爬取糗事百科的段子 参考https://www.jianshu.com/p/9c266216957b
网页有下一页，网址page=数字，属于静态网页的爬取
网址的界面直接有内容，比较简单，有些是网址只是分类，再点进去才能看到 比如小说网址
'''
import pandas as pd
import requests
from bs4 import BeautifulSoup

import time
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36'}


base_url = 'https://www.qiushibaike.com/text/page/'  # 设定一个网址不变的部分，然后我们只要每次在这个后面加数字就可以了


for num in range(1, 15): # 设置循环，让num分别等于1-10

    # print('第{}页'.format(num))
    r = requests.get(base_url + str(num), headers=headers) #这里对网址进行一个修改
    #剩下的部分都是和原来的代码一样
    # print(r.text)
    content = r.text
    soup = BeautifulSoup(r.text, 'lxml')

    divs = soup.find_all(class_='article block untagged mb15 typs_hot')

    for div in divs:
        # if div.find_all(class_='thumb'):
        #     continue
        joke = div.span.get_text()#获取所有文字内容
        # time.sleep(1)  # （休停1s 防止被认出来是代码访问）

        # print(joke)
        # print('------')
        #创建并写入txt，追加格式，若没有文件则创建
        with open('qiushi_joke.txt', 'a+', encoding='utf-8') as f:
            f.write(joke+"\n")
