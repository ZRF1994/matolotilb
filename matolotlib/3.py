# -*-coding:utf-8-*-
import cv2
import numpy as np
from cv2 import *
from matplotlib import pyplot as plt
import  math
#
#
#
#
#
# r=20.0
# a,b=0.0,0.0
# theta = np.arange(0, 2*np.pi, 0.01)
# x = a + r * np.cos(theta)
# y = b + r * np.sin(theta)
# fig = plt.figure()
# axes = fig.add_subplot(111)
# axes.plot(x, y)
# axes.axis('equal')
#
#
# x = [12.0,  13.8,  5,  6.6,  16.8,  12.3,14.8,8.5,14.5 ,
# 7.6,9.8, 16.3,8.5,9.3,13.6,5.5, 8.9,10.5 ,
# 10.9,9.2, 6.8,2.4,8.8,7.3, 11.5,10.3,9.5 ,
# 9.7,10.8, 9.2,7.3,8.9,8.1, 3.6,6.8,13.3 ,
# 15.6,14.2,9.5,11.2,9.7 , 14.5,16.5,13.9, 15.8 ,
# 9.7,13.2, 7.1,8.8,7.3]
# theat=0
# print(math.sin(30/180*math.pi))
# for i in  x:
#     plt.scatter(math.cos(theat/180*math.pi)*i,math.sin(theat/180*math.pi)*i)
#     theat=theat+7.2
#
# ax=plt.gca()
# ax.spines['right'].set_color('none')
# ax.spines['top'].set_color('none')#取消边框颜色
# ax.xaxis.set_ticks_position('bottom')#xx轴用bottom代替
# ax.yaxis.set_ticks_position('left')
# ax.spines['bottom'].set_position(('data',0))#将bottom放在0处
# ax.spines['left'].set_position(('data',0))
# plt.legend()#show  plot label
# plt.show()



import numpy as np
import matplotlib.pyplot as plt
import  math
#圆

# 点

xq = [12.0,  13.8,  5,  6.6,  16.8,  12.3,14.8,8.5,14.5 ,
7.6,9.8, 16.3,8.5,9.3,13.6,5.5, 8.9,10.5 ]
a=len(xq)
x2= xq
y2= xq
print(x2)
print(y2)
i=0
for i in range(a):
        h = 2.1
        c = 1.4
        x2[i]=h*xq[i]
        print(x2[i])
        y2[i]=c*xq[i]
        print(x2[i])
plt.scatter(x2,y2,c='r',marker='s')
plt.show()