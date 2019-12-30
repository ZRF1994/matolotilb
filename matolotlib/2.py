# -*-coding:utf-8-*-
import cv2
import numpy as np
from cv2 import *
from matplotlib import pyplot as plt
x=np.linspace(1,46,46)
y=2*x+1
y1=x+1
# plt.figure(num=2,figsize=(8,5))
# plt.plot(x,y,color="red",linewidth=2,linestyle=":",marker='v')#线型选择方式有...marker为折点
#坐标轴
plt.figure(num=2,figsize=(8,5))
plt.plot(x,y,label='$up$',color="red",lw=2,linestyle=":",marker='v')#线型选择方式有...marker为折点
plt.plot(x,y1,color="orange",linewidth=2,linestyle="-.",marker='o')#线型选择方式有...marker为折点
# l1,=plt.plot(x,y1,color="orange",linewidth=2,linestyle="-.",marker='o')
plt.xlim(-10,10)
plt.ylim(-2,10)#y轴取值范围
plt.xlabel("$xx$")
plt.ylabel('yy')#y轴标签
new_ticks=np.linspace(-10,10,5)
plt.xticks(new_ticks)
plt.yticks([-20,-10,0,10,20],["$q$",'$w$','$e$','$r$','$t$'])#标签替换
#获取当前的坐标轴
ax=plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')#取消边框颜色
ax.xaxis.set_ticks_position('bottom')#xx轴用bottom代替
ax.yaxis.set_ticks_position('left')
ax.spines['bottom'].set_position(('data',0))#将bottom放在0处
ax.spines['left'].set_position(('data',0))
plt.legend()#show  plot label
#plt.lenged(handles=[l1],labels=[qqq],loc='best')
x0=1
y0=2*x0+1
plt.scatter(x0,y0,color='g',lw=21,s=50)#点的大小和颜色
plt.plot([x0,x0],[y0,-10],'k--',lw=2.5)#（x0,y0）----(x0,0)
plt.annotate(r'$2x+1=%s$' % y0, xy=(x0, y0), xycoords='data', xytext=(+30, -30),
             textcoords='offset points', fontsize=16,
             arrowprops=dict(arrowstyle='->', connectionstyle="arc3,rad=.2"))
plt.text(-3.7, 3, r'$This\ is\ the\ some\ text. \mu\ \sigma_i\ \alpha_t$',
         fontdict={'size': 16, 'color': 'r'})
plt.show()