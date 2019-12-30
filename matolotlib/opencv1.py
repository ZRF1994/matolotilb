# -*- coding: utf-8 -*-
# @Time    : 2019/12/14 20:03
# @Author  : 张茹飞
# @Email   : 1106815482@qq.com
# @File    : opencv1.py
# @Software: PyCharm
import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import KMeans
from sklearn import datasets
import cv2
import random
font=cv2.FONT_HERSHEY_SIMPLEX
colorA=[(243,196,11),(213,177,39),(188,162,60),(164,146,73),(143,130,80),(114,107,78)]
colorB=[(84,243,13),(96,215,43),(100,188,60),(102,161,75),(97,138,78),(88,112,77)]
img=cv2.imread("xx.jpg")
#竖线
xx=np.linspace(50,1850,31)
yy=np.linspace(50,650,11)
for i in xx:
    cv2.line(img,(0+int(i),50),(0+int(i),650),(255,0,0))
for i in yy:
    cv2.line(img,(50,0+int(i)),(1850,0+int(i)),(255,0,0))

#图例
cv2.line(img,(1900,50),(1900,650),(0,255,0))
cv2.line(img,(1950,50),(1950,650),(0,255,0))

for i  in range(7):
    cv2.line(img,(1900,50+i*100),(1950,i*100+50),(0,255,0))
for i  in range(7):
    cv2.line(img,(1970,50+i*100),(2020,i*100+50),(0,255,0))

cv2.line(img,(1970,50),(1970,650),(0,255,0))
cv2.line(img,(2020,50),(2020,650),(0,255,0))
#颜色矩形框
for i in range(6):
    pts = np.array([[1900,50+i*100], [1950,50+i*100],[1950,50+100+i*100], [1900,50+100+i*100],[1900,50+i*100]], dtype=np.int32)
    pts = pts.reshape((-1, 1, 2))
    cv2.fillPoly(img, [pts], colorA[-i-1])
for i in range(6):
    pts = np.array([[1970,50+i*100], [2020,50+i*100],[2020,50+100+i*100], [1970,50+100+i*100],[1970,50+i*100]], dtype=np.int32)
    pts = pts.reshape((-1, 1, 2))
    cv2.fillPoly(img, [pts], colorB[-i-1])
for i in range(6):
    cv2.putText(img,str(i+1)+"level",(2020,30+100*(6-i)),font,1,(255,255,0),2)
#绘制斜线
xxx=0
yyy=0
for j in range(10):
    xxx=0
    for i in range(30):

        cv2.line(img, (50+xxx+60, 50+yyy), (xxx-10+60, 110+yyy), (255, 0, 0))
        xxx+=60
    yyy+=60
#上三角
def draw_top(mm,nn,*args):
    pts = np.array([[(nn-1)*60+50, (mm-1)*60+50], [nn*60+50,(mm-1)*60+50], [(nn-1)*60+50, mm*60+50]], dtype=np.int32)
    pts = pts.reshape((-1, 1, 2))

    cv2.fillPoly(img, [pts], *args)
#下三角
def draw_low(mm,nn,*args):
    pts = np.array([[(nn-1)*60+50+60, (mm-1)*60+50+60], [nn*60+50,(mm-1)*60+50], [(nn-1)*60+50, mm*60+50]], dtype=np.int32)
    pts = pts.reshape((-1, 1, 2))
    cv2.fillPoly(img, [pts], *args)
a=[0]*210+[1]*20+[2]*20+[3]*20+[4]*20+[5]*10
random.shuffle(a)
print(a)
m=0
for j in range(1,11):
    for i in range(1,31):
        if a[m]==0:
            draw_low(j,i,colorA[0])
        elif a[m]==1:
            draw_low(j, i, colorA[1])
        elif a[m] == 2:
            draw_low(j, i, colorA[2])
        elif a[m] == 3:
            draw_low(j, i, colorA[3])
        elif a[m] == 4:
            draw_low(j, i, colorA[4])
        else:
            draw_low(j, i, colorA[5])
        m+=1
b=[0]*210+[1]*20+[2]*20+[3]*20+[4]*20+[5]*10
random.shuffle(b)
n=0
for j in range(1, 11):
    for i in range(1, 31):
        if a[n]==0:
            draw_top(j,i,colorB[0])
        elif a[n]==1:
            draw_top(j, i, colorB[1])
        elif a[n] == 2:
            draw_top(j, i, colorB[2])
        elif a[n] == 3:
            draw_top(j, i, colorB[3])
        elif a[n] == 4:
            draw_top(j, i, colorB[4])
        else:
            draw_top(j, i, colorB[5])
        n+=1




img = img[40:670, 40:2150]
cv2.imshow("ww",img)
cv2.imwrite('C:\\Users\\Administrator\\Desktop\\xxx.jpg', img)
cv2.waitKey(0)


