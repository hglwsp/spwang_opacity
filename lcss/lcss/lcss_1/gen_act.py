import numpy as np
import matplotlib.pyplot as plt
import math
import random


#x2=np.arange(-4,0,0.1)
#y2=x2*0

#x3=np.arange(0,4,0.1)
#y3=x3
#x2=np.append(x2,x3,axis=0)
#y2=np.append(y2,y3,axis=0)
#plt.plot(x2,y2)
pi = 3.14
x2=np.arange(-pi,pi,0.1)
y2=np.sin(x2)

plt.plot(x2,y2)


a=np.polyfit(x2,y2,2) #多项式次数
print(a)
print(a[0],'*pow(x,2)+',a[1],'*x+',a[2])
# print(a[0],'*pow(x,2)+',a[1],'*x+',a[2],)
#print(a[0],'*pow(x,3)+',a[1],'*pow(x,2)+',a[2],'*x+',a[3],)
# print(a[0],'*pow(x,4)+',a[1],'*pow(x,3)+',a[2],'*pow(x,2)+',a[3],'*x+',a[4],)
#print(a[0],'*pow(x,5)+',a[1],'*pow(x,4)+',a[2],'*pow(x,3)+',a[3],'*pow(x,2)+',a[4],'*x+',a[5])
#print(a[0],'*pow(x,6)+',a[1],'*pow(x,5)+',a[2],'*pow(x,4)+',a[3],'*pow(x,3)+',a[4],'*pow(x,2)+',a[5],'*x+',a[6])

b=np.poly1d(a)
c=b(x2)#生成多项式对象之后，就是获取x在这个多项式处的值
plt.scatter(x2,y2,marker='.',label='original datas')#对原始数据画散点图
plt.plot(x2,c,ls='--',c='red',label='fitting with second-degree polynomial')#对拟合之后的数据，也就是x，c数组画图
# plt.plot(x,y)
plt.show()
