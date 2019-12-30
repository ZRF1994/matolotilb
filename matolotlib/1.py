# -*-coding:utf-8-*-
import cv2
import numpy as np
from cv2 import *
from matplotlib import pyplot as plt
x=[0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1]
y=[0.85,0.84,0.83,0.79,0.75,0.73,0.69,0.65,0.6,0.5]
y1=[0.62,0.650,0.7,0.73,0.78,0.783,0.8,0.82,0.85,0.851]
y2=[0.7,0.733,0.75,0.76,0.766,0.764,0.74,0.725,0.7,0.65]
y3=[0.55,0.59,0.64,0.67,0.73,0.72,0.73,0.74,0.78,0.76]
print(y2)
# plt.figure(num=2,figsize=(8,5))
# plt.plot(x,y,color="red",linewidth=2,linestyle=":",marker='v')#线型选择方式有...marker为折点
#坐标轴
plt.figure(num=2,figsize=(8,5))
l1,=plt.plot(x,y,label='$up$',color="blue",linewidth=1,linestyle=":",marker='v')#线型选择方式有...marker为折点
l2,=plt.plot(x,y1,color="orange",linewidth=1,linestyle="-.",marker='s')#线型选择方式有...marker为折点
l3,=plt.plot(x,y2,color="red",linewidth=1,linestyle="--",marker='+')#线型选择方式有...marker为折点
l4,=plt.plot(x,y3,color="green",linewidth=1,linestyle="-",marker='o')
# l1,=plt.plot(x,y1,color="orange",linewidth=2,linestyle="-.",marker='o')
plt.xlim(0,1)
plt.ylim(0,1)#y轴取值范围
plt.xlabel("threshold")
plt.ylabel('value')#y轴标签
new_ticks=np.linspace(0,1,11)
plt.xticks(new_ticks)
# plt.yticks([-20,-10,0,10,20],["$q$",'$w$','$e$','$r$','$t$'])#标签替换
#获取当前的坐标轴
ax=plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')#取消边框颜色
# ax.xaxis.set_ticks_position('bottom')#xx轴用bottom代替
ax.yaxis.set_ticks_position('left')
ax.spines['bottom'].set_position(('data',0))#将bottom放在0处
ax.spines['left'].set_position(('data',0))
plt.legend()#show  plot label
plt.legend(handles = [l1,l2,l3,l4], labels = ['recall','precision',"F", 'IOU'], loc = 'best',fontsize=16)
plt.savefig("F:\TIM文件\\zzzz")
# 代码中的“...”代表省略的其他参数
# 设置刻度字体大小
plt.xticks(fontsize=16)
plt.yticks(fontsize=16)
# 设置坐标标签字体大小
plt.show()