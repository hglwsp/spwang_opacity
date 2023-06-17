import matplotlib.pyplot as plt
import xlrd

x1_data = []
y1_data = []
x2_data = []
y2_data = []


#find bound
y3_data = []
y4_data = []

#data
data1 = xlrd.open_workbook(r'D:\pythonProject\opacity_loss1u\plot_traj\data_x1.xlsx')
data2 = xlrd.open_workbook(r'D:\pythonProject\opacity_loss1u\plot_traj\data_x2.xlsx')

table1 = data1.sheets()[0]
x1_data = list(range(99))
table2 = data2.sheets()[0]
x2_data = list(range(99))

cap_0 = table1.row_values(3)
cap_1 = table2.row_values(3)

for j in range(0, 99):
    y1_data.append(cap_0[j])
    y2_data.append(cap_1[j])
#cap_0 is original data,we need to use it to find bound
# print(y1_data)
l_x = len(y1_data)
#find lower bound
for k in range(0,l_x):
    if y1_data[k] - 1 <= 0:
        y3_data.append(0)
    else:
        y3_data.append(y1_data[k]-1)

#find upper bound
for m in range(0,l_x):
    if y1_data[m] + 1 >= 10:
        y4_data.append(10)
    else:
        y4_data.append(y1_data[m]+1)

#plot
plt.plot(x1_data, y1_data, '-', linestyle="-", linewidth=0.5,label="traj_x1")
plt.plot(x2_data, y2_data, '-', linestyle="-", linewidth=0.5,label="traj_x2")
plt.plot(x1_data, y3_data, '-', linestyle="-", linewidth=0.5,label="lowerbound")
plt.plot(x1_data, y4_data, '-', linestyle="-", linewidth=0.5,label="upperbound")

#lower bound -> upper bound
# facecolor：覆盖区域的颜色
# alpha：覆盖区域的透明度[0,1],其值越大，表示越不透明
plt.fill_between(x1_data,y3_data,y4_data,where=y3_data<=y4_data,facecolor='grey',interpolate=True,alpha=0.1)

plt.title('h')
plt.legend(loc='upper right', fontsize=8) # 标签位置
plt.xlabel('x')
plt.ylabel('y')
plt.xlim(0,100)
plt.ylim(0,10)
plt.show()