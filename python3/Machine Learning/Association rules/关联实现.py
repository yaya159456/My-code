'''
    1.apriori算法是一种寻找关联规则的算法，啤酒与尿布是典型的例子。
        官方没有apriori.py文件  所以需要自己编写并保存到目录下供调用
    2.用apriori前将dataframe转换成矩阵！df = df.values
'''
import apriori
import pandas as pd
from pandas import DataFrame, Series
import numpy as np
data = pd.read_excel('正常测试数据.xlsx')
data = data.ix[:, [16, 18, 21, 25,30,33,35,37,39,51]]
data.loc[data['真实值2'] == 0, '真实值2'] = 'J1'
data.loc[data['真实值2'] == 1, '真实值2'] = 'J2'

# print(data)
data = data.values#Dataframe转换成矩阵 apriori算法的数据导入格式是矩阵 这个必须要转

L, suppData = apriori.apriori(data, 0.2)
rules = apriori.generateRules(L, suppData, 0.75)#函数里面自动输出了  所以不用再写print()
print('\n')
for item in L[1]:
    if item.intersection('J2'): print('如下：', item)
for item in L[2]:
    if item.intersection('J2'): print('如下：', item)
# print(rules)
for item in L[3]:
    if item.intersection('J2'): print('如下：', item)
for item in L[4]:
    if item.intersection('J2'): print('如下：', item)
