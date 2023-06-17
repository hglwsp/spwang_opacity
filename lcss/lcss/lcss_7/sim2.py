import numpy as np
from sympy import *


# x1 = symbols("x1")  # 符号x，自变量
# x2 = symbols("x2")
# x3 = symbols("x3")
# x4 = symbols("x4")

x1 = symbols("f_x1")  # 符号x，自变量
x2 = symbols("f_x2")
x3 = symbols("f_x3")
x4 = symbols("f_x4")


z = symbols("relu")

# y = 0.792*pow(x1-1,2)#公式
# apart(y,x1)



w1=np.array([
[0.10903903941728209, 0.5058296433973086, 0.5119074293492736, -0.3423524663127079],[ 0.0713668390633883, 1.268263860300487, 0.12539703539017474, 1.5574697215082625],[ -0.6755798564202986, -1.040747081461227, 0.641608263204786, 0.5395856390920678],[ 1.232556340937075, 0.7330373209526571, -1.3643258471826016, -1.8831823885807755],[ -0.04822574979490374, -1.7371339688419571, -0.647605665144212, -0.3693916258774071],[ 0.5574868811607956, -0.4636351772230615, 1.1288059871781795, -0.4133345453333781],[ -0.3692116037615234, -0.26049021513217574, 0.46389021477607817, -0.7349675566084827],[ 0.19077105893706092, 1.9328562769082391, 1.240495671995555, -0.22248975109796112],[ -0.05372158583708602, -1.1287094673249507, -0.6960773407083688, -2.0490065033026905],[ -2.0203422206610946, 0.6112478169199232, 1.263995854041885, 0.20684361846125665],[ -1.5917329949133037, 0.1445771045129832, -0.15892482027195248, 0.2720946350965579],[ -1.7124947900888936, -1.1900187200663879, -1.0619933024130035, -0.33294720317913135],[ -0.008396277769531717, -0.130651909033963, 0.42906505126062805, -1.0718478999167835],[ -1.4968935110499137, 1.4561383926388318, 0.4607321612189646, -0.001169418972205813],[ 0.03912482558329311, 0.00990344925698502, -0.07557840190978371, 1.4112575593858692],[ -0.5721767235993657, 0.5342688746226021, -0.9672971201691266, 2.181154090208142]
    ]).T
b1=\
[-1.1203114883484553, -0.9011156876243939, 0.7251839796938934, -0.533376768163647, 0.9667701319435611, -1.111050189690258, -0.4791881571478601, -1.5746066888625878, 0.09362227468458209, 0.5302439586781946, -1.7716552270240449, -0.3770183387705624, -0.07979649238200909, -0.0993213784119466, -0.15013774221993592, 0.40266742902080677]
expr1 = z * (np.matmul([[x1,x2,x3,x4]],w1)+b1)
#expr1 = -0.0001711589065517019 *pow(expr1,4)+ -0.01447711943585072 *pow(expr1,3)+ 0.002849795794085815 *pow(expr1,2)+ 0.5071116596907747 *expr1+ -0.00508383030596129
# expr1_1 = 0.25 * expr1 * expr1 + 0.001
# expr1 = 0.5 * expr1 + pow(expr1_1,0.5)


w2 =np.array(
[-1.0506410760290767, -0.5781859535689464, 0.6678645960343518, 0.9151386297843713, 1.9729153325245168, -0.21257038570192519, -0.8835560825582329, 0.0507500189161057, -0.4107481978583476, 0.7714039822490634, -1.3691049046515031, -0.12977921381477447, -1.1599918113614318, 0.8314450099877065, -0.8053402189160616, -0.3229399729423081]
).T
b2=[-0.3000382110603256]

expr2=np.matmul(expr1,w2)+b2
print(expr2)
# expr3 = simplify(expr2)
# print(expr3)