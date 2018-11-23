import tensorflow as tf
from numpy.random import RandomState
import numpy as np


batch_size = 8 #定义batch的大小

#定义神经网络参数
w1 = tf.Variable(tf.random_normal(shape=[2, 3], stddev=1, seed=1), name='w1')
w2 = tf.Variable(tf.random_normal(shape=[3, 1], stddev=1), name='w2')

#定义x-input y-input
x = tf.placeholder(tf.float32, shape=(None, 2), name='x-input')
y_ = tf.placeholder(tf.float32, shape=(None, 1), name='y-input')


#定义网络传播过程
a = tf.matmul(x, w1)
y = tf.matmul(a, w2)

global_step = tf.Variable(0)
#通过exponential_decay函数生成学习率
learning_rate = tf.train.exponential_decay(0.1, global_step, 100, 0.96, staircase=True)

#定义损失函数和反向传播的算法

cross_entropy = -tf.reduce_mean(y_*tf.log(tf.clip_by_value(y, 1e-10, 1.0)))
# learning_rate = 0.001
train_step = tf.train.AdamOptimizer(learning_rate).minimize(cross_entropy, global_step=global_step)

#通过随机数生成一个模拟数据集
#randomState 函数中数字1,相当于一个seed种子，每次产生的随机数都是相同的
rdm = RandomState(1)
dataset_size = 128
#产生一个128行×2列的随机矩阵
X = rdm.rand(dataset_size, 2)

#产生一个布尔型结果矩阵128×1
Y = [[int(x1 + x2 < 1)] for (x1, x2) in X]

#创建会话 输出
with tf.Session() as sess:
    #初始化变量
    init_op = tf.global_variables_initializer()
    sess.run(init_op)
    print(sess.run(w1))
    print(sess.run(w2))

    #设置训练次数
    steps = 5000
    for i in range(steps):

        #每次选取batch_size个样本进行训练
        start = (i * batch_size) % dataset_size
        end = min(start + batch_size, dataset_size)

        #通过选取的样本 训练神经网络并更新参数
        sess.run(train_step, feed_dict={x: X[start: end], y_: Y[start: end]})
        if i % 1000 == 0:
            #每隔一段时间，计算所有数据上的 交叉熵 并输出
            total_cross_entropy = sess.run(cross_entropy, feed_dict={x: X, y_: Y})
            print("After %s training step(s), cross entropy on all data is %g" % (i, total_cross_entropy))

    #输出最终的权重参数
    print(sess.run(w1))
    print(sess.run(w2))

