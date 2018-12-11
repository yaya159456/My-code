'''
clf是训练模型 例如：clf = LogisticRegression()
                    clf = clf.fit(x_train, y_train)
            clf.predict(x_test)用来预测测试集结果
加到模型.py的后面就可以，仅仅用来展示函数的使用
matplotlib画图过程中，需要加的图例，线的方式和颜色，坐标轴标签等信息，自行加上就行
'''

'''ROC曲线&AUC'''
from sklearn.metrics import roc_curve, roc_auc_score
test_predict = clf.predict(x_test)

#计算AUC
auc_test = roc_auc_score(y_test, test_predict)
print('Auc_test:{}'.format(auc_test))

#计算ROC曲线
roc_test = roc_curve(y_test, test_predict)

import matplotlib.pyplot as plt
#画图
fig = plt.figure()
ax1 = fig.add_subplot(111)
ax1.plot(roc_test[0], roc_test[1])
# plt.xlabel('XXX')
# plt.ylabel('XXX')#坐标轴标签
# plt.xlim(a, b)#横坐标范围
# plt.title('XXX')#题目 
# ax1.plot(x, y, 'r-', labels='XXXX')
# ax.legend()
# 自行加吧 不写了 需要啥自己加
plt.show()