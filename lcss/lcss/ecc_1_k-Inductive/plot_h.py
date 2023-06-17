import matplotlib.pyplot as plt
import xlrd

x_data = []
y_data = []
y1_data = []
y2_data = []
y3_data = []
y4_data = []


data = xlrd.open_workbook(r'D:\pythonProject\opacity_loss1u\plot_traj\data_x1x2.xlsx')
table = data.sheets()[0]
x_data = list(range(99))

cap_0 = table.row_values(0)
cap_1 = table.row_values(1)
cap_2 = table.row_values(2)
cap_3 = table.row_values(3)
cap_4 = table.row_values(4)


# print(cap)  #打印出来检验是否正确读取

for j in range(0, 99):
    y_data.append(cap_0[j])
    y1_data.append(cap_1[j])
    y2_data.append(cap_2[j])
    y3_data.append(cap_3[j])
    y4_data.append(cap_4[j])


plt.plot(x_data, y_data, '.-', linestyle="-", color = 'blue',linewidth=0.5,label="traj_1")
plt.plot(x_data, y1_data, '.-', linestyle="-", linewidth=0.5,label="traj_2")
plt.plot(x_data, y2_data, '.-', linestyle="-", linewidth=0.5,label="traj_3")
plt.plot(x_data, y3_data, '.-', linestyle="-", linewidth=0.5,label="traj_4")
plt.plot(x_data, y4_data, '.-', linestyle="-", linewidth=0.5,label="traj_5")

plt.axhline(y=1,ls=":",c="red",linestyle="solid", linewidth=5,label="h = 1")#添加水平直线,h=1
plt.title('h')
plt.legend(loc='upper right', fontsize=8) # 标签位置
plt.xlabel('x')
plt.ylabel('y')
plt.xlim(0,100)
plt.ylim(0,1.6)
plt.show()
