'''
LOOK! LOOK!! LOOK!!!
看一下，简单介绍一下内容，如果和你的工程不一样，也不耽误你时间了，去寻找别的方法吧；如果能帮到你，This is my honor
1.导入的数据格式为Dataframe，并进行了简单的处理，这个每个任务不同，结合实际情况，也是一次人工选取特征的过程
2.将训练集拆分成训练集和测试集 函数：train_test_split
3.训练模型 DecisionTreeClassifier  fit
4.持久化模型  joblib.dump
5.cm_plot  混淆矩阵可视化函数 这个可以自己写下来保存到自己电脑上 就能每次调用了
6.计算kappa一致性值 kappa>0.6时，认为模型和原始金方案高度一致（如果你的分类target是一种描述方法，可以用来看看是否一致）
7.graphviz 可视化，设置一些参数能让你的图更漂亮~
            多说一下，我这的中文乱码问题没解决，直接输出的还是框框，如果你想问这个问题，就不用看了，不会- -！
            不过你可以选择这样一个方式：先导出dot文件格式，再用cmd窗口将dot转成pdf或png
'''
import pandas as pd
import numpy as np
data = pd.read_excel('text.xlsx')
#提取excel中用到的若干列，删除冗余信息,也是一次人工选取特征的过程
data = data.ix[:, [2, 4, 15, 7, 6, 14, 16, 17, 13, 10, 28]]
#对初始数据进行预处理，这里将受教育程度改成数值
data['受教育年限'] = data['受教育年限'].replace({'小学': 1, '初中': 2, '高中': 3, '大学': 4})
#对受教育年限 <=12 年（高中及以下）的，总分+1分
data.loc[data['受教育年限'] <= 3, '总分1'] = data['总分1'] + 1
#标记target，总分 >= 26有认知障碍，不合格定为0， < 26的合格定为1
data.insert(11, '是否有问题', 0)#定义标签 定初始值=0，表示不合格
data.loc[data['总分1'] < 26, '是否有问题'] = 1#若满足总分 < 26 则合格 定为1
data.drop(['总分1'], axis=1, inplace=True)
data.drop(['受教育年限'], axis=1, inplace=True)

'''需要将训练集拆分成训练集和测试集'''
from sklearn.model_selection import train_test_split
#划分数据集
x, y = np.split(data, (-1,), axis=1)
x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=0, train_size=0.7)

#sklearn导入决策树
from sklearn.tree import DecisionTreeClassifier

treefile = 'tree.pkl'
#设置max_depth min_samples_split min_samples_leaf参数来进行修剪
clf = DecisionTreeClassifier(criterion='gini', max_depth=4, min_samples_split=2, min_samples_leaf=1)
clf = clf.fit(x_train, y_train)
#持久化模型
from sklearn.externals import joblib
joblib.dump(clf, treefile)

# cm_plot.py 文件,包括了混淆矩阵可视化函数,
# 放置在python的site-packages 目录,供调用
# 例如:~/anaconda2/lib/python2.7/site-packages
#-*- coding: utf-8 -*-
def cm_plot(y, yp):

    from sklearn.metrics import confusion_matrix #导入混淆矩阵函数
    cm = confusion_matrix(y, yp) #混淆矩阵
    import matplotlib.pyplot as plt #导入作图库
    plt.matshow(cm, cmap=plt.cm.Greens) #画混淆矩阵图，配色风格使用cm.Greens，更多风格请参考官网。
    plt.colorbar() #颜色标签
    for x in range(len(cm)): #数据标签
        for y in range(len(cm)):
            plt.annotate(cm[x, y], xy=(x, y), horizontalalignment='center', verticalalignment='center')
    plt.xlabel('True label') #坐标轴标签
    plt.ylabel('Predicted label') #坐标轴标签
    return plt
#函数调用
cm_plot(y_test, clf.predict(x_test)).show()

'''graphviz可视化'''
import graphviz
from graphviz import Digraph
from sklearn import tree
from sklearn.tree import export_graphviz
from sklearn.externals.six import StringIO
import pydotplus
#graphviz 经常搞事情 就是报错，goole了一下，都认为它不稳定，比较傻设置路径还是走错路，
# 所以给他定义了路径，强行把它掰直了~ 用OS设置路径，后面根据自己graphviz的安装路径可调
import os
os.environ["PATH"] += os.pathsep + 'F:\\Graphviz\\bin\\'

#可以用数据的列名称作为特征名称feature_name, 也可以自定义列名称，这里用自定义方式，自定义的时候一定保证是一个str
# data_feature_name = x_train.columns
# data_target_name = y_train.columns
feature_names = ['nhd', 'jyjg', 'nn', 'jjd', 'nyz', 'nwd', 'npk', 'nnl', 'kj']
class_names = ['0', '1']

# ,  feature_names=data.feature_names, class_names=data.target_names
dot_data = StringIO()
tree.export_graphviz(clf, out_file=dot_data, feature_names=feature_names, class_names=class_names,
                     filled=True, rounded=True, special_characters=True)
'''
 .replace('helvetica', "Microsoft YaHei") 
本来准备解决输出中文乱码问题，感觉我电脑奇葩，goole所有方法用了都没效果，
所以这次结果也是英文的（所以我自定义了特征名称- -！）
'''
#输出 会生成两个文件一个dot 一个png 文件格式可调（eg:pdf....）
graph = pydotplus.graph_from_dot_data(dot_data.getvalue())
graph.write_dot('tree_nine.dot')
# graph.write_png('tree.png')
graph.write_png("Tree_nine.png")
#输出一下测试集的预测结果
print(clf.predict(x_test))
