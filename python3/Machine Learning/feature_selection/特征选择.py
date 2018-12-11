import pandas as pd
import numpy as np
from pandas import DataFrame, Series
from sklearn.feature_selection import RFE
from sklearn.linear_model import LogisticRegressionCV

data = pd.read_excel('正常测试数据.xlsx')
data = data.ix[:, [15,16,17,18,19,21,24,25,26,27,28,29,30,42]]
data.insert(0, '交互项', 0)
data['交互项'] = data['脑混沌'] * data['内外和']
print(data)

from sklearn import preprocessing
x, y = np.split(data, (-1,), axis=1)
names = data.columns.values.ravel()
x = preprocessing.StandardScaler().fit_transform(x)#标准化

lr = LogisticRegressionCV()
rfe = RFE(lr, n_features_to_select=1)
rfe.fit(x,y.values.ravel())
print(sorted(zip(map(lambda x: round(x, 4), rfe.ranking_), names)))
