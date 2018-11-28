'''skleran中集成了许多算法，其导入包的方式如下所示，

　　逻辑回归：from sklearn.linear_model import LogisticRegression

      朴素贝叶斯：from sklearn.naive_bayes import GaussianNB

 　　K-近邻：from sklearn.neighbors import KNeighborsClassifier

 　　决策树：from sklearn.tree import DecisionTreeClassifier

 　　支持向量机：from sklearn import svm'''
'''
m = np.arange(8.0)
n = np.split(m, (3,))
print(n)
 
#结果：[array([0., 1., 2.]), array([3., 4., 5., 6., 7.])]
 
#机器学习中的用法解释：
#axis=1,代表列，是要把data数据集中的所有数据按第四、五列之间分割为X集和Y集。
x, y = np.split(data, (4,), axis=1)
'''

import pandas as pd
import numpy as np
from sklearn import svm
data = pd.read_excel('text1.xlsx')
#提取excel中用到的若干列，删除冗余信息
data = data.ix[:, [13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 36]]
data.insert(17, 'mark', -1)#定义标签 定初始值=-1，表示不合格
data.loc[data['总分(30)'] < 26, 'mark'] = 1#若满足总分 < 26 则合格 定为1
data.drop(['总分(30)'], axis=1, inplace=True)
'''需要将训练集拆分成训练集和测试集'''
from sklearn.model_selection import train_test_split
#划分数据集
x, y = np.split(data, (16,), axis=1)
x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=1, train_size=0.8)
x_train = 1.0*(x_train-x_train.mean())/x_train.std()
x_test = 1.0*(x_test-x_test.mean())/x_test.std()
# print(y_train)
from sklearn import model_selection
#训练
#方法1、设置固定参数值C,g
# clf = svm.SVC(C=1, kernel='rbf', gamma=0.001, decision_function_shape='ovr')
# cv=5 5折交叉验证
# scores = cross_val_score(clf, iris.data, iris.target, cv=5)
#方法2、寻找最优超参数
#网格搜索 寻找最优参数
parameters = [{'kernel': ['rbf'], 'gamma': [1e-4, 1e-3, 1e-2, 1e-1, 1, 10, 100, 1000, 10000],
                                    'C': [1, 10, 100, 1000, 10000]},
                {'kernel': ['poly'], 'C': [1], 'degree': [2, 3]},
                {'kernel': ['linear'], 'C': [1, 10, 100, 1000]}]

clf = model_selection.GridSearchCV(svm.SVC(), parameters, cv=10, return_train_score=True)
clf.fit(x_train, y_train.values.ravel())

print(clf.best_params_) #查看最优参数
print(clf.best_score_)

from sklearn.metrics import accuracy_score
# 准确率
print(clf.score(x_train, y_train))  # 精度

print('训练集准确率：', accuracy_score(y_train, clf.predict(x_train)))

print(clf.score(x_test, y_test))

print('测试集准确率：', accuracy_score(y_test, clf.predict(x_test)))


# decision_function   计算样本点到分割超平面的函数距离
# print('decision_function:\n', clf.decision_function(x_train))

print('\npredict:\n', clf.predict(x_test))

#计算Kappa值
from sklearn.metrics import confusion_matrix #导入混淆矩阵函数
result = confusion_matrix(y_test, clf.predict(x_test)) #混淆矩阵
def kappa_coefficient(confusion_matrix):
    """
    descibe:compute kappa coefficient
    param confusion_matrix:matrix
    return kappa coefficient
    """
    import numpy as np

    P_0 = 0
    for i in range(len(confusion_matrix)):
        P_0 = P_0 + confusion_matrix[i, i]

    a = []
    b = []
    for i in range(len(confusion_matrix)):
        a.append(sum(confusion_matrix[i]))
        b.append(sum(confusion_matrix[:, i]))

    P_e = sum(np.array(a) * np.array(b)) / (sum(a) * sum(a))
    kappa = (P_0 / sum(a) - P_e) / (1 - P_e)

    return kappa

kappa = kappa_coefficient(confusion_matrix=result)
print(kappa)


