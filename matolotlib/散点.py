# -*- coding: utf-8 -*-
# @Time    : 2019/10/14 16:09
# @Author  : 张茹飞
# @Email   : 1106815482@qq.com
# @File    : 散点.py
# @Software: PyCharm
import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import KMeans
from sklearn import datasets
import numpy as np
import matplotlib.pyplot as plt

#圆
r=25.0
a,b=0.0,0.0
theta = np.arange(0, 2*np.pi, 0.01)
x = a + r * np.cos(theta)
y = b + r * np.sin(theta)
fig = plt.figure()
axes = fig.add_subplot(111)
axes.plot(x, y)
axes.axis('equal')
# 点

x = [12.0,  -13.8,  5,  6.6,  -16.8,  12.3,14.8,8.5,14.5 ,
7.6,9.8, -16.3,8.5,9.3,13.6,5.5, 8.9,-10.5 ,
10.9,9.2, -6.8,2.4,-8.8,7.3, -11.5,10.3,9.5 ,
9.7,-10.8, -9.2,7.3,8.9,8.1, -3.6,6.8,-13.3 ,
15.6,-14.2,9.5,-11.2,9.7 , -14.5,-16.5,-13.9, -15.8 ,
9.7,-13.2, 7.1,8.8,7.3]
a=len(x)
x1=0
y1=0
y = np.random.uniform(-20,20,a)
plt.scatter(x,y,c='r',marker='s')
plt.scatter(x1,y1,c='g',marker='x')
plt.show()

for i in range(1,51):
    list2.append(i)
plt.scatter(list2,list1)


plt.xlim(0,50)
plt.ylim(0,25)#y轴取值范围
plt.xlabel("$xx$")
plt.ylabel('yy')#y轴标签
new_ticks=np.linspace(0,50,5)
plt.xticks(new_ticks)


plt.show()



# plt.figure(num=2,figsize=(8,5))
# plt.plot(x,y,color="red",linewidth=2,linestyle=":",marker='v')#线型选择方式有...marker为折点
#坐标轴

# plt.plot(x,y,label='$up$',color="red",lw=2,linestyle=":",marker='v')#线型选择方式有...marker为折点
# plt.plot(x,y1,color="orange",linewidth=2,linestyle="-.",marker='o')#线型选择方式有...marker为折点
# l1,=plt.plot(x,y1,color="orange",linewidth=2,linestyle="-.",marker='o')
