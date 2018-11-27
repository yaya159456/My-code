import pandas as pd
data = pd.read_excel(open('20181016.xlsx', 'rb'))
data.drop(columns=['脑健康评价总分', '脑能力总分', '左右脑偏侧化', '警觉度', '内源性焦虑', '脑耗能',
                   '脑惰性', '外专注', '反应速度', '脑稳定', '记忆加工'], axis=1, inplace=True)
k = 5
iteration = 500
data_zs = 1.0*(data-data.mean())/data.std()#归一化
# pd.set_option('display.max_columns', None)#输出所有的列，不谢的话，若有多列，系统默认只显示前后几列
# print(data.describe())

import sklearn
from sklearn.cluster import KMeans
#训练模型
model = KMeans(n_clusters=k, max_iter=iteration)
model.fit(data_zs)
#计算轮廓系数
silhouette_score = sklearn.metrics.silhouette_score(data_zs, model.labels_, metric='euclidean')
print(silhouette_score)
#输出一个dataframe，各个聚类中心及每个类别所包含的数量
r1 = pd.Series(model.labels_).value_counts()
r2 = pd.DataFrame(model.cluster_centers_)
r = pd.concat([r2, r1], axis=1)
r.columns = list(data.columns) + [u'类别数目']
print(r)
#输出一个dataframe 原始数据，最后一列加上所在的聚类类别
r = pd.concat([data, pd.Series(model.labels_, index=data.index)], axis=1)
r.columns = list(data.columns) + [u'聚类类别']
print(r)

#tsne 进行可视化
from sklearn.manifold import TSNE
tsne = TSNE()
tsne.fit_transform(data_zs) #进行数据降维
tsne = pd.DataFrame(tsne.embedding_, index=data_zs.index) #转换数据格式

import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False #用来正常显示负号
#不同类别用不同颜色和样式绘图
d = tsne[r[u'聚类类别'] == 0]
plt.plot(d[0], d[1], 'r.')
d = tsne[r[u'聚类类别'] == 1]
plt.plot(d[0], d[1], 'go')
d = tsne[r[u'聚类类别'] == 2]
plt.plot(d[0], d[1], 'b*')
d = tsne[r[u'聚类类别'] == 3]
plt.plot(d[0], d[1], 'k-')
d = tsne[r[u'聚类类别'] == 4]
plt.plot(d[0], d[1], 'p*')
plt.show()
