import numpy as np
import matplotlib.pyplot as plt

# x = np.random.rand(10,2)
# print(x)
# print("\n")
# print(x[2]) #输出索引2的行
# print(x[[1,2,3]]) #输出索引1,2,3的行
# print(x[:,0]) #输出所有行的第0列

# data = 2*np.random.rand(10000,2)-1 #-1到1的范围
# print(data)
# x = data[:,0] 
# y = data[:,1]
# idx = x**2 + y**2 < 1 #判断点是否在圆内
# hole = x**2 + y**2 < 0.25
# idx = np.logical_and(idx,~hole)
# plt.plot(x[idx],y[idx],'go',markersize=1)
# plt.show()

p = np.random.rand(10000)
np.set_printoptions(edgeitems=5000,suppress=True) #设置打印时的边缘项数
# print(p.shape)
plt.hist(p,bins=20,color='g',edgecolor='k') #等分为20个区间，颜色为绿色，边缘颜色为黑色
# plt.hist(p,bins=20,color='g') #直方图,等分为20个区间，颜色为绿色，不设边缘颜色会是怎样的

plt.show()
