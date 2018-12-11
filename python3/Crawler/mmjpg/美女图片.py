import pandas as pd
import requests
from bs4 import BeautifulSoup
import re
from urllib.request import  urlretrieve
import os
import time

# 设置图片存储路径
PICTURES_PATH = os.path.join(os.getcwd(), 'pictures_self/')
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36',
    'Referer': "http://www.mmjpg.com"
}
# header = {
#     "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
#     "Accept-Encoding": "gzip, deflate",
#     "Accept-Language": "zh-CN,zh;q=0.9",
#     "Cache-Control": "max-age=0",
#     "Connection": "keep-alive",
#     "Host": "www.mmjpg.com",
#     "Referer": "http://www.mmjpg.com/tag/xinggan",
#     "Upgrade-Insecure-Requests": "1",
#     "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36"
# }

class Spider(object):
    def __init__(self, page_num):
        self.page_num = page_num
        self.page_urls = ['http://www.mmjpg.com/']
        self.girl_urls = []
        self.girl_name = ''
        self.pic_urls = []
        self.header = header
        self.each_page_num = 20

    # 获取页面url的方法
    def get_page_urls(self):
        if int(page_num) > 1:
            for n in range(2, int(page_num) + 1):
                page_url = 'http://www.mmjpg.com/home/' + str(n)
                self.page_urls.append(page_url)
        elif int(page_num) == 1:
            pass

    # 获取妹子的url的方法
    def get_girl_urls(self):
        for page_url in self.page_urls:
            html = requests.get(page_url, headers=self.header).content
            soup = BeautifulSoup(html, 'lxml')
            divs = soup.find_all(class_='title')
            soup = BeautifulSoup(str(divs), 'lxml')
            for link in soup.find_all('a'):
                link = link.get('href')
                self.girl_urls.append(link)

#获取图片地址
    def get_pic_urls(self):
        for girl_url in self.girl_urls:
            html = requests.get(girl_url, headers=self.header).content
            soup = BeautifulSoup(html, 'lxml')
            divs = soup.find_all('div', class_='article')
            for div in divs:
                self.girl_name = div.h2.get_text()
            for n in range(1, self.each_page_num + 1):
                girl_pic_url = girl_url + '/' + str(n)
                html = requests.get(girl_pic_url, headers=self.header).content
                soup_page = BeautifulSoup(html, 'lxml')
                divs_page = soup_page.find_all('div', class_='content')
                soup_page = BeautifulSoup(str(divs_page), 'lxml')
                divs_page = soup_page.find_all('img')
                for i in divs_page:
                    pic_url = i.get('src')
                    self.pic_urls.append(pic_url)
            try:
                self.download_pic()
            except Exception as e:
                print("{}保存图片失败".format(self.girl_name) + str(e))

    # 下载图片的方法
    def download_pic(self):
        try:
            os.mkdir(PICTURES_PATH)
        except:
            pass
        girl_path = PICTURES_PATH + self.girl_name
        try:
            os.mkdir(girl_path)
        except Exception as e:
            print("{}已存在".format(self.girl_name))
        img_name = 0
        for pic_url in self.pic_urls:
            img_name += 1
            img_content = requests.get(pic_url, headers=self.header).content
            pic_path = girl_path + '/' + str(img_name) + '.jpg'
            if os.path.isfile(pic_path):
                print("{}第{}已存在".format(self.girl_name, img_name))
                pass
            else:
                with open(pic_path, 'wb') as f:
                    f.write(img_content)
                    print("正在保存{}第{}张图片".format(self.girl_name, img_name))
        return
# 爬虫的启动方法，按照爬虫逻辑依次调用方法
    def start(self):
        self.get_page_urls()
        self.get_girl_urls()
        self.get_pic_urls()

if __name__ == '__main__':
    page_num = input("请输入页码:")
    mmjpg_spider = Spider(page_num)
    mmjpg_spider.start()
