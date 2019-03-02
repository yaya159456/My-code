import pandas as pd
import numpy as np
from pandas import DataFrame, Series
import matplotlib.pyplot as plt
data_zhongke = pd.read_excel('中科数据.xlsx')
data_yifei = pd.read_excel('cleanafirst_20190221.xlsx')
data_yifei = data_yifei.ix[:, [4,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21]]
data_yifei.insert(17, '100-脑排空', 100-data_yifei['脑排空'])
def insert_data(data):
    data.insert(0, '分组', 0)
    data.loc[(data['年龄'] >= 6) & (data['年龄'] <= 9), '分组'] = 1
    data.loc[(data['年龄'] >= 10) & (data['年龄'] <= 11), '分组'] = 2
    data.loc[(data['年龄'] >= 12) & (data['年龄'] <= 14), '分组'] = 3
    data.loc[(data['年龄'] >= 15) & (data['年龄'] <= 17), '分组'] = 4
    data = data[~data['分组'].isin([0])]
    data = data.drop('年龄', axis=1)
    return data

def plot_data(data, name, data_columns_name):
    for column in data_columns_name.columns.tolist()[2:]:
        # print(column)
        plt.rcParams['font.sans-serif'] = ['SimHei']
        plt.figure()
        plt.title('{}趋势图'.format(column), fontsize=18)
        # x = [1, 2, 3, 4]
        x = data['分组']['mean']
        y1 = data[column].ix[:, 4]
        y2 = data[column].ix[:, 5]
        y3 = data[column].ix[:, 6]
        plt.ylim(0, max(data[column].ix[:, 6] + 20))
        plt.xticks([1, 2, 3, 4], ['6-9', '10-11', '12-14', '15-17'], fontsize=18)
        plt.xlabel('年龄段', fontsize=16)
        plt.ylabel('{}'.format(column), fontsize=16)
        plt.plot(x, y3, color='y', linewidth=3.0, label='第三分位数')
        plt.plot(x, y2, color='b', linewidth=3.0, label='第二分位数')
        plt.plot(x, y1, color='r', linewidth=3.0, label='第一分位数')
        plt.legend()
        for a, b in zip(x, y1):
            plt.text(a, b, round(b), ha='center', va='bottom', fontsize=16)
        for c, d in zip(x, y2):
            plt.text(c, d, round(d), ha='center', va='bottom', fontsize=16)
        for e, f in zip(x, y3):
            plt.text(e, f, round(f), ha='center', va='bottom', fontsize=16)
        # plt.savefig(name + '{}.jpg'.format(column))
        plt.show()
def run(data, name):
    df = insert_data(data=data)
    df_groupby_describe = df.groupby('分组', as_index=False).describe()
    print(df_groupby_describe.columns)
    plot_data(df_groupby_describe, name=name, data_columns_name=data)

if __name__ == '__main__':
    pd.set_option('display.max_columns', None)
    run(data=data_yifei, name='易飞')
    run(data=data_zhongke, name='中科')
    # print(data_yifei)