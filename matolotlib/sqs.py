# -*-coding:utf-8-*-
import cv2
import numpy as np
from cv2 import *
from matplotlib import pyplot as plt
x=np.linspace(-10,10,100)
y1=5*x+1*4
y2=5*x+2*4
y3=5*x+3*4
y4=5*x+4*4
y5=5*x+5*4


plt.plot(x,y1,label='$tanh$',color="red",lw=2,linestyle="-",)
plt.plot(x,y2,label='$tanh$',color="red",lw=2,linestyle="-",)
plt.plot(x,y3,label='$tanh$',color="red",lw=2,linestyle="-",)
plt.plot(x,y4,label='$tanh$',color="red",lw=2,linestyle="-",)
plt.plot(x,y5,label='$tanh$',color="red",lw=2,linestyle="-",)
# plt.plot(x,y2,label='$sigmoid$',color="green",lw=2,linestyle="-",)

# plt.plot(x,y3,label='$Relu$',color="blue",lw=2,linestyle="-",)



plt.show()