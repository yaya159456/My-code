# import pyocr
# import importlib
# import sys
# import time
#
# importlib.reload(sys)
# time1 = time.time()
# # print("初始时间为：",time1)
#
# import os.path
# from pdfminer.pdfparser import PDFParser, PDFDocument
# from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
# from pdfminer.converter import PDFPageAggregator
# from pdfminer.layout import LTTextBoxHorizontal, LAParams
# from pdfminer.pdfinterp import PDFTextExtractionNotAllowed
#
# text_path = r'words-words.pdf'
#
#
# # text_path = r'photo-words.pdf'
#
# def parse():
#     '''解析PDF文本，并保存到TXT文件中'''
#     fp = open(text_path, 'rb')
#     # 用文件对象创建一个PDF文档分析器
#     parser = PDFParser(fp)
#     # 创建一个PDF文档
#     doc = PDFDocument()
#     # 连接分析器，与文档对象
#     parser.set_document(doc)
#     doc.set_parser(parser)
#
#     # 提供初始化密码，如果没有密码，就创建一个空的字符串
#     doc.initialize()
#
#     # 检测文档是否提供txt转换，不提供就忽略
#     if not doc.is_extractable:
#         raise PDFTextExtractionNotAllowed
#     else:
#         # 创建PDF，资源管理器，来共享资源
#         rsrcmgr = PDFResourceManager()
#         # 创建一个PDF设备对象
#         laparams = LAParams()
#         device = PDFPageAggregator(rsrcmgr, laparams=laparams)
#         # 创建一个PDF解释其对象
#         interpreter = PDFPageInterpreter(rsrcmgr, device)
#
#         # 循环遍历列表，每次处理一个page内容
#         # doc.get_pages() 获取page列表
#         for page in doc.get_pages():
#             interpreter.process_page(page)
#             # 接受该页面的LTPage对象
#             layout = device.get_result()
#             # 这里layout是一个LTPage对象 里面存放着 这个page解析出的各种对象
#             # 一般包括LTTextBox, LTFigure, LTImage, LTTextBoxHorizontal 等等
#             # 想要获取文本就获得对象的text属性，
#             for x in layout:
#                 if (isinstance(x, LTTextBoxHorizontal)):
#                     with open(r'2.txt', 'a') as f:
#                         results = x.get_text()
#                         print(results)
#                         f.write(results + "\n")
#
#
# if __name__ == '__main__':
#     parse()
#     time2 = time.time()
#     print("总共消耗时间为:", time2 - time1)

from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfpage import PDFTextExtractionNotAllowed
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.pdfdevice import PDFDevice
from pdfminer.layout import *
from pdfminer.converter import PDFPageAggregator


def Pdf2Txt(Path, Save_name):
    # 来创建一个pdf文档分析器
    parser = PDFParser(Path)
    # 创建一个PDF文档对象存储文档结构
    document = PDFDocument(parser)
    # 检查文件是否允许文本提取
    if not document.is_extractable:
        raise PDFTextExtractionNotAllowed
    else:
        # 创建一个PDF资源管理器对象来存储共赏资源
        rsrcmgr = PDFResourceManager()
        # 设定参数进行分析
        laparams = LAParams()
        # 创建一个PDF设备对象
        # device=PDFDevice(rsrcmgr)
        device = PDFPageAggregator(rsrcmgr, laparams=laparams)
        # 创建一个PDF解释器对象
        interpreter = PDFPageInterpreter(rsrcmgr, device)
        # 处理每一页
        for page in PDFPage.create_pages(document):
            interpreter.process_page(page)
            # 接受该页面的LTPage对象
            layout = device.get_result()
            for x in layout:
                if (isinstance(x, LTTextBoxHorizontal)):
                    with open('%s' % (Save_name), 'a',encoding= 'utf-8') as f:
                        print(x.get_text() )
                        f.write(x.get_text()+ '\n')


Path = open(r'F:\Pycharm\yaya\杨宇-20180803-单1-5_IMG\ceshi2.pdf', 'rb')
Pdf2Txt(Path, 'b.txt')
