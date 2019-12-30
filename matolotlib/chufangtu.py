# -*- coding: utf-8 -*-
# @Time    : 2019/12/14 17:47
# @Author  : 张茹飞
# @Email   : 1106815482@qq.com
# @File    : chufangtu.py
# @Software: PyCharm
import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import KMeans
from sklearn import datasets
import matolotlib as mpl
'''
处方图绘制
'''
#定义函数画线
def draw_line():
    pass
x=np.linspace(0,30,31)
y=np.linspace(0,10,11)


plt.figure(facecolor="white",figsize=(30, 10))

for i in range(10):
    plt.hlines(i,0,30,"#000000")
for i in range(30):
        plt.vlines(i, 0, 10,colors="#000000")
for j in range(30):
    for i in range(10):
        plt.plot([j,j+1],[i,i+1])


frame = plt.gca()
# y 轴不可见
frame.axes.get_yaxis().set_visible(False)
# x 轴不可见
frame.axes.get_xaxis().set_visible(False)
plt.show()
