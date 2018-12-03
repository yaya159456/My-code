'''
对数据进行一些预处理：（apriori算法前对输出预处理），将连续性数据根据指定范围离散化，其他方法还有聚类，等宽，等频等。。。
    1.data.loc[(判断条件), '列名'] = int/str 选取对应位置赋值
    2.data.loc[(data.ix[:, feature] >= b), 'class'] = list_class[2]判断条件中的列名称可以替换，不过feature必须是list[i]
    3.pop方法让列换位置
    4.if __name__ == "__main__"：.py文件可以当做运行文件也可以当做一个库文件（可以在其他.py文件中import），
                    有了这个if __name__ == "__main__"：当被其他调用的时候，是不运行这个下面的程序的，
                    如果没有，将运行这个.py中的所有行。
    5.如果是为了实现apriori算法，别忘了将dataframe转换成矩阵 df = df.values
'''
import apriori
import pandas as pd
from pandas import DataFrame, Series
import numpy as np
#导入数据，并选取需要的列
data = pd.read_excel('正常测试数据.xlsx')
data = data.ix[:, [15, 16, 18, 21, 25, 27, 28, 29, 30, 42]]
print(data)

#自定义一个可以转换的函数，然后调用函数就可以节省大量的代码量
def change_class(feature, a, b, list_class, j):
    #此处只能用data.ix[:, :]的方式提取对应位置的数
    #data.loc[(判断条件), '列名'] = int/str 选取对应位置赋值
    data.loc[(data.ix[:, feature] >= 0) & (data.ix[:, feature] < a), 'class'] = list_class[0]
    data.loc[(data.ix[:, feature] >= a) & (data.ix[:, feature] < b), 'class'] = list_class[1]
    data.loc[(data.ix[:, feature] >= b), 'class'] = list_class[2]
    #以下三行 是对列的换位置，也可以不删除原列，这里直接删除了
    data.drop(columns=feature, inplace=True)#删除一列
    col = data.pop('class')#pop的方法换列的位置，先将需要换的列挑出来
    data.insert(j, feature, col)#将挑出来的列插入dataframe中
    return data
if __name__ == '__main__':#调用函数

    li = data.columns.values.tolist()
    #这里很遗憾，用循环更麻烦，因为每一列的范围都不一样，所以就迭代写入了，否则可以考虑用for循环写就方便了
    data = change_class(feature=li[0], a=10, b=20, list_class=list(['A1', 'A2', 'A3']), j=0)
    data = change_class(feature=li[1], a=130, b=250, list_class=list(['B1', 'B2', 'B3']), j=1)
    data = change_class(feature=li[2], a=20, b=40, list_class=list(['C1', 'C2', 'C3']), j=2)
    print(data)


