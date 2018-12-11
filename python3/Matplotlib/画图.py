import matplotlib  .pyplot  as plt
import pandas as pd
import numpy as np
from pandas import DataFrame ,Series
from numpy.random  import randn
from numpy  import nan as NA
from mpl_toolkits.mplot3d import Axes3D
# squares=[1,4,9,16,25];
# x=[1,2,3,4,5]
# plt.title('SQUARES OF VALUE')
# plt.xlabel('value',fontsize=24)
# plt.ylabel('squares of value',fontsize=24)
# plt.tick_params (axis= 'both',labelsize=15)
# plt.plot (x,squares,linewidth=5,kind='barh');
# plt.show()
# df= DataFrame (np.random.randn(10,4).cumsum(0),
#                index= np.arange(0,100,10),columns= ['A','B','C','D'])
# df.plot(kind='barh')
# df.plot (kind='barh',stacked= True )
# plt.show()
'''四个图放在一起 方法一'''
# fig,axes=plt.subplots(2,2)
# axes[0,0].plot(randn(50).cumsum(),'b--',label='one')
# axes[0,1].plot(randn(50).cumsum(),'r--',label='two')
# axes[1,0].plot(randn(50).cumsum(),'k--',label='three')
# axes[1,1].plot(randn(50).cumsum(),'o--',label='four')
# axes[0,0].legend (loc='best')
# axes[0,1].legend (loc='best')
# axes[1,0].legend (loc='best')
# axes[1,1].legend (loc='best')
# plt.show ()
'''四个图在一起 方法二'''
# fig=plt.figure()
# ax1=fig.add_subplot(2,2,1)
# ax2=fig.add_subplot(2,2,2)
# ax3=fig.add_subplot(2,2,3)
# ax4=fig.add_subplot(2,2,4)
# ax1.plot(randn(50).cumsum(),'b--',label='one')
# ax2.plot(randn(50).cumsum(),'r--',label='two')
# ax3.plot(randn(50).cumsum(),'k--',label='three')
# ax4.plot(randn(50).cumsum(),'o--',label='four')
# ax1.legend (loc='best')
# ax2.legend (loc='best')
# ax3.legend (loc='best')
# ax4.legend (loc='best')
# plt.show ()

# plt.subplot(1,1,1)
df= pd.DataFrame ({'A':['A','B','C','D'],
                  'B': [8,7,5,4],
                   'C': [6,6,4,3]})
print(df)
fig=plt.figure()
ax1=fig.add_subplot(111)
# plt.plot(df.index,df.B,kind='barh')
ax1.plot(df['A'], df.ix[:,['B','C']])#x,y分别设置x轴，y轴的列标签或列的位置
plt.show()

'''3D图'''

# from mpl_toolkits.mplot3d import Axes3D
# import numpy as np
# import matplotlib.pyplot as plt
#
# fig = plt.figure()
# ax = fig.gca(projection='3d')
#
# # Prepare arrays x, y, z
# theta = np.linspace(-4 * np.pi, 4 * np.pi, 100)
# z = np.linspace(-2, 2, 100)
# r = z**2 + 1
# x = r * np.sin(theta)
# y = r * np.cos(theta)
#
# ax.plot(x, y, z, label='parametric curve')  #这里传入x, y, z的值
# ax.legend()
#
# plt.show()

# 载入模块
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# 创建 3D 图形对象
# fig = plt.figure()
# ax = Axes3D(fig)
#
# # 生成数据
# X = np.arange(-2, 2, 0.1)
# Y = np.arange(-2, 2, 0.1)
# X, Y = np.meshgrid(X, Y)
# Z = np.sqrt(X ** 2 + Y ** 2)
#
# # 绘制曲面图，并使用 cmap 着色
# ax.plot_surface(X, Y, Z, cmap='winter')
#
# plt.show()

# fig = plt.figure()
# # ax = fig.gca(projection='3d')
# ax = Axes3D(fig)
# X = np.arange(-4, 4, 0.25)
# Y = np.arange(-4, -4, 0.25)
# X, Y = np.meshgrid(X, Y)
# # R = np.sqrt(X**2+Y**2)
# Z = np.sin(np.sqrt(X**2+Y**2))
# ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='rainbow')
# # ax.contourf(X, Y, Z, zdir='z', offset=-2, cmap='rainbow')
# # ax.set_zlim(-2,2)
# plt.show()