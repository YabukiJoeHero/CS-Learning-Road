import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# #下：numpy的随机数范围
# d = np.random.rand(10)
# print(d)
# print(d<0.5) #输出小于0.5的布尔值
# print(d[d<0.5]) #布尔索引，输出小于0.5的数值

# d[d<0.5] = 0.5 #将小于0.5的数值赋值为0.5

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

# p = np.random.rand(10000)
# np.set_printoptions(edgeitems=5000,suppress=True) #设置打印时的边缘项数
# # print(p.shape)
# plt.hist(p,bins=20,color='g',edgecolor='k') #等分为20个区间，颜色为绿色，边缘颜色为黑色
# # plt.hist(p,bins=20,color='g') #直方图,等分为20个区间，颜色为绿色，不设边缘颜色会是怎样的
# plt.show()

# # 下：中心极限定理
# N = 10000
# times = 100
# z = np.zeros(N)  #准备长度为10000的账本
# for i in range(times):
#     z += np.random.rand(N)
# z /= times
# plt.hist(z,bins=20,color='m',edgecolor='k')
# plt.show()

d = np.random.rand(3,4)
print(d)
print(type(d)) #<class 'numpy.ndarray'>dimensional array多维数组
data = pd.DataFrame(data = d,columns = list('abcd'))
print('=' *50)
print(data)
print(type(data)) #<class 'pandas.core.frame.DataFrame'>DataFrame数据框
print(data['a']) #输出a列

