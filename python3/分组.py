import pandas as pd
import numpy as np
from pandas import DataFrame,Series
pd.set_option('display.max_columns', None) #显示所有列
data = pd.read_csv('cleanfirst_20181024.csv')
data = data.ix[:, [6, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23]]#选取原文档中的xxx列，剔除其余列冗余信息
#分组 共有9组
data_1 = data[data.年龄.isin([0, 1, 2])]
data_2 = data[data.年龄.isin([3, 4])]
data_3 = data[data.年龄.isin([5, 6])]
data_4 = data[data.年龄.isin([7, 8, 9])]
data_5 = data[data.年龄.isin([10, 11, 12, 13])]
data_6 = data[(data['年龄'] >= 14) & (data['年龄'] <= 24)]
data_7 = data[(data['年龄'] >= 25) & (data['年龄'] <= 39)]
data_8 = data[(data['年龄'] >= 40) & (data['年龄'] <= 65)]
data_9 = data[data['年龄'] > 65]

def data_quantile(data_i, i, j):#自定义函数，计算三种百分位数（90,50,10分位）
    #round（）函数 将数值四舍五入 quantile()计算百分位
    df = DataFrame(
        data=[round(data_i.ix[:, j].quantile(0.9)), round(data_i.ix[:, j].quantile(0.5)),
              round(data_i.ix[:, j].quantile(0.1))],
        index=pd.Index(['90percent', 'median', '10percent'], name=data_1.columns.values.tolist()[j]),
        columns=[i]).T
    return df
if __name__ == '__main__':
    '''先是内循环，取每个指标的三种百分位函数，利用定义好的函数
       然后是外循环，取16个指标'''
    #16个指标 从1-16循环range(1, 17)
    for j in range(1, 17):
        data_n = DataFrame()

        for i in range(1, 10):
            if i == 1:
                data_i = data_1
            if i == 2:
                data_i = data_2
            if i == 3:
                data_i = data_3
            if i == 4:
                data_i = data_4
            if i == 5:
                data_i = data_5
            if i == 6:
                data_i = data_6
            if i == 7:
                data_i = data_7
            if i == 8:
                data_i = data_8
            if i == 9:
                data_i = data_9
            data_quan_i = data_quantile(data_i=data_i, i=i, j=j)
            data_n = pd.concat([data_n, data_quan_i], sort=False, ignore_index=False)
        data_n['年龄'] = 0
        data_n.ix[1, 3] = ['0-2']
        data_n.ix[2, 3] = ['3-4']
        data_n.ix[3, 3] = ['5-6']
        data_n.ix[4, 3] = ['7-9']
        data_n.ix[5, 3] = ['10-13']
        data_n.ix[6, 3] = ['14-24']
        data_n.ix[7, 3] = ['25-39']
        data_n.ix[8, 3] = ['40-65']
        data_n.ix[9, 3] = ['> 65']
        data_n.set_index(['年龄'], drop=True, inplace=True)
        print(data_n)

        # 将数据保存成excel，并以指标名定义成excel文件名 %s 格式化输出
        # data_n.to_excel('%s.xlsx' %data_1.columns.values.tolist()[j])
        increase = (data_n.ix[8, 1] - data_n.ix[7, 1]) / data_n.ix[7, 1]
        print(increase)

        import matplotlib.pyplot as plt
        '''输出可视化，调用matplotlib 画出图形'''
        plt.rcParams['font.sans-serif'] = ['SimHei']#图形显示中文

        plt.figure()
        plt.ylabel(data_1.columns.values.tolist()[j])
        plt.xlabel('年龄')

        x = data_n.index
        y1 = data_n.ix[:, 0]
        plt.plot(x, y1, 'r-', label='90percent')
        for a, b in zip(x, y1):#plt.txt() 在图形中的每个点 标出坐标 ha='' va=''定义标记的位置 fontsize定义字号大小
            plt.text(a, b, b, ha='center', va='bottom', fontsize=10)
        y2 = data_n.ix[:, 1]
        plt.plot(x, y2, 'b-', label='50percent')
        for a, b in zip(x, y2):
            plt.text(a, b, b, ha='center', va='bottom', fontsize=10)
        y3 = data_n.ix[:, 2]
        plt.plot(x, y3, 'k-', label='10percent')
        for a, b in zip(x, y3):
            plt.text(a, b, b, ha='center', va='bottom', fontsize=10)
        plt.legend()        #显示图例
        # plt.savefig('%s.jpg' %data_1.columns.values.tolist()[j])#保存图片，可自定义格式（pdf，jgp...ect）
        # plt.show()

