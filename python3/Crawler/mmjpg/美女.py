# -*- coding: utf-8 -*-
import re
import os
import requests
from lxml import etree
import time

# 设置图片存储路径
PICTURES_PATH = os.path.join(os.getcwd(), 'pictures/')

# 设置headers
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36',
    'Referer': "http://www.mmjpg.com"
}


class Spider(object):
    def __init__(self, page_num):
        self.page_num = page_num
        self.page_urls = ['http://www.mmjpg.com/']
        self.girl_urls = []
        self.girl_name = ''
        self.pic_urls = []

# 获取页面url的方法
    def get_page_urls(self):
        if int(page_num) > 1:
            for n in range(2, int(page_num)+1):
                page_url = 'http://www.mmjpg.com/home/' + str(n)
                self.page_urls.append(page_url)
        elif int(page_num) == 1:
            pass

# 获取妹子的url的方法
    def get_girl_urls(self):
        for page_url in self.page_urls:
            html = requests.get(page_url).content
            selector = etree.HTML(html)
            self.girl_urls += (selector.xpath('//span[@class="title"]/a/@href'))

# 获取图片的url的方法
    def get_pic_urls(self):
        for girl_url in self.girl_urls:
            html = requests.get(girl_url).content
            selector = etree.HTML(html)
            page_num = int(selector.xpath('//*[@id="page"]/a[last()-1]/text()')[0])
            self.girl_name = selector.xpath('//div[@class="article"]/h2/text()')[0]
            self.pic_urls = []
            for i in range(1, page_num+1):
                girl_pic_url = ''.join([girl_url, '/' + str(i)])
                html = requests.get(girl_pic_url).content
                selector = etree.HTML(html)
                pic_url = selector.xpath('//div[@id="content"]/a/img/@src')[0]
                self.pic_urls.append(pic_url)
            try:
                self.download_pic()
            except Exception as e:
                print("{}保存失败".format(self.girl_name) + str(e))

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
            img_data = requests.get(pic_url, headers=headers)
            pic_path = girl_path + '/' + str(img_name)+'.jpg'
            if os.path.isfile(pic_path):
                print("{}第{}张已存在".format(self.girl_name, img_name))
                pass
            else:
                with open(pic_path, 'wb')as f:
                    f.write(img_data.content)
                    print("正在保存{}第{}张".format(self.girl_name, img_name))
                    f.close()
        return

# 爬虫的启动方法，按照爬虫逻辑依次调用方法
    def start(self):
        self.get_page_urls()
        self.get_girl_urls()
        self.get_pic_urls()


# main函数
if __name__ == '__main__':
    page_num = input("请输入页码:")
    mmjpg_spider = Spider(page_num)
    mmjpg_spider.start()