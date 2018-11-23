
import requests
import re
import pandas as pd
import time

page = 2#定义页数
def get_data(page):

    url = 'http://hotel.elong.com/ajax/tmapilist/asyncsearch'

    data = {
        'code': ' 7163838',
        'listRequest.areaID': '',
        'listRequest.bedLargeTypes': '',
        'listRequest.bookingChannel': '1',
        'listRequest.breakfasts': '0',
        'listRequest.cancelFree': 'false',
        'listRequest.cardNo': '192928',
        'listRequest.checkInDate': '2018-11-16 00:00:00',
        'listRequest.checkOutDate': '2018-11-17 00:00:00',
        'listRequest.cityID': '0101',
        'listRequest.cityName': '北京市',
        'listRequest.customLevel': '11',
        'listRequest.distance': '20',
        'listRequest.endLat': '0',
        'listRequest.endLng': '0',
        'listRequest.facilityIds': '',
        'listRequest.highPrice': '0',
        'listRequest.hotelBrandIDs': '',
        'listRequest.isAdvanceSave': 'false',
        'listRequest.isAfterCouponPrice': 'true',
        'listRequest.isCoupon': 'false',
        'listRequest.isDebug': 'false',
        'listRequest.isLimitTime': 'false',
        'listRequest.isLogin': 'false',
        'listRequest.isMobileOnly': 'true',
        'listRequest.isNeed5Discount': 'true',
        'listRequest.isNeedNotContractedHotel': 'false',
        'listRequest.isNeedSimilarPrice': 'false',
        'listRequest.isReturnNoRoomHotel': 'true',
        'listRequest.isStaySave': 'false',
        'listRequest.isTrace': 'false',
        'listRequest.isUnionSite': 'false',
        'listRequest.isnstantConfirm': 'false',
        'listRequest.keywords': '',
        'listRequest.keywordsType': '0',
        'listRequest.language': 'cn',
        'listRequest.listType': '0',
        'listRequest.lowPrice': '0',
        'listRequest.orderFromID': '50793',
        'listRequest.pageIndex':page,
        'listRequest.pageSize': '20',
        'listRequest.payMethod': '0',
        'listRequest.personOfRoom': '0',
        'listRequest.poiId': '0',
        'listRequest.promotionChannelCode': '0000',
        'listRequest.promotionSwitch': '-1',
        'listRequest.proxyID': 'ZD',
        'listRequest.rankType': '0',
        'listRequest.returnFilterItem': 'true',
        'listRequest.sectionId': '',
        'listRequest.sellChannel': '1',
        'listRequest.seoHotelStar': '0',
        'listRequest.sortDirection': '1',
        'listRequest.sortMethod': '1',
        'listRequest.standBack': '-1',
        'listRequest.starLevels': '',
        'listRequest.startLat': '0',
        'listRequest.startLng': '0',
        'listRequest.taRecommend': 'false',
        'listRequest.themeIds': '',
        'listRequest.traceId': '2f2a49bb-7648-421d-8a59-91b7c1498375',
        'listRequest.wordId': '',
        'listRequest.wordType': '0',
        'listRequest.elongToken': ' 0b0efdbf-e1cb-4a84-8396-d7564f8dd526'
    }

    header = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'keep-alive',
        'Content-Length': '1836',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Cookie': 'CookieGuid=0b0efdbf-e1cb-4a84-8396-d7564f8dd526; SessionGuid=8312cc9d-9def-4f3d-81fb-049973001b06; Esid=674b6761-5c05-483d-8d28-6ed89c13a1e5; semid=ppzqbaidu; outerFrom=ppzqbaidu; com.eLong.CommonService.OrderFromCookieInfo=Status=1&Orderfromtype=5&Isusefparam=0&Pkid=50793&Parentid=3150&Coefficient=0.0&Makecomefrom=0&Cookiesdays=0&Savecookies=0&Priority=9001; fv=pcweb; ext_param=bns%3D4%26ct%3D3; s_cc=true; s_eVar44=ppzqbaidu; _fid=0b0efdbf-e1cb-4a84-8396-d7564f8dd526; newjava1=7130cc3d9d22a2dcd3765ca837d60121; anti_token=43452C53-8DD1-4B68-814C-A3A99D09B459; __jsluid=8f62fa4fb7e7943d5839f6d19a538cfa; __tctmb=0.3147442083043156.1542346322360.1542346322360.1; s_visit=1; __tccgd=0.0; newjava2=47b51959fbd1eb528ebb6d50036790d5; CitySearchHistory=401%23%E9%87%8D%E5%BA%86%23chongqing%23%40101%23%E5%8C%97%E4%BA%AC%23beijing%23; JSESSIONID=033AE32B5DDAAA031092E823CEE6FD0E; ShHotel=CityID=0101&CityNameCN=%E5%8C%97%E4%BA%AC%E5%B8%82&CityName=%E5%8C%97%E4%BA%AC%E5%B8%82&OutDate=2018-11-17&CityNameEN=beijing&InDate=2018-11-16; s_sq=elongcom%3D%2526pid%253Dhotel.elong.com%25252Fbeijing%2526pidt%253D1%2526oid%253Djavascript%25253Avoid(0)%2526ot%253DA; __tctmc=0.215881358; __tctmd=0.187661553',
        'Host': 'hotel.elong.com',
        'Origin': 'http://hotel.elong.com',
        'Referer': 'http://hotel.elong.com/beijing/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest'
    }
    response = requests.post(url, data=data, headers=header)#网页上是post方法所以用的post ，根据网页来
    html = response.json()
    print(html)
    hotel_name = re.findall('target="_blank" title="(.*?)"><span class="icon_nmb">', html['value']['hotelListHtml'])
    hotel_price = re.findall('<span class="h_pri_num ">(.*?)</span>', html['value']['hotelListHtml'])
    hotel_address = re.findall('data-hoteladdress="(.*?)" >', html['value']['hotelListHtml'])
    #返回酒店名称，酒店价格，酒店地址
    return hotel_name, hotel_price, hotel_address


if __name__ == '__main__':
    hotel_name = []#定义空文件 用来存储
    hotel_price = []
    hotel_address = []
    for i in range(10):
        hotel_name_, hotel_price_, hotel_address_ = get_data(i)
        hotel_name.extend(hotel_name_)#extend（）用来添加 和append不一样
        hotel_price.extend(hotel_price_)
        hotel_address.extend(hotel_address_)
        time.sleep(1)#（休停1s 防止被认出来是代码访问（hahaha。。））
        print("已完成第" + str(i) + "页爬取")
    dataframe = pd.DataFrame({'酒店名称': hotel_name, '酒店价格': hotel_price, '酒店地址': hotel_address})
    '''
    数据改成Dataframe格式
    保存成csv文件，注意：经常保存后的csv用excel打不开 所以后面加上encoding=“utf_8_sig”就行了
    '''
    # dataframe.to_csv("hotel.csv", index=False, sep=',', encoding="utf_8_sig")

