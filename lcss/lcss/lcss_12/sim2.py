import numpy as np
from sympy import *


x1 = symbols("x1")  # 符号x，自变量
x2 = symbols("x2")
x3 = symbols("x3")
x4 = symbols("x4")


z = symbols("relu")

# y = 0.792*pow(x1-1,2)#公式
# apart(y,x1)



w1=np.array([
    [0.6005637727876951, -0.5358484882167984, -1.4394264982831684, 0.5108267348412788],[ 0.1324893966401164, -0.6240488628617473, -0.9549134733644905, 0.2669204350098638],[ -0.29217584386815376, -0.3783611149065176, -0.0045102286739366355, 0.10927513074283736],[ 0.28945965580420085, 1.3211107248480114, 1.235017555453641, -0.7492424282113965],[ 1.642262278480177, -1.5940216794773063, 2.0917717044353203, -1.9585421942541512],[ 1.160550609660752, -1.1154599185826897, 1.1195175138689213, 1.0489371981515314],[ 0.4543357365004019, 0.08984278733630828, -0.9830611994724119, -1.0699431336335141],[ -0.8498640668029128, -0.4284785212030548, -0.13520986402523338, -0.7155514236873811],[ -0.04145716309741289, -1.582724169856361, -1.014810596798369, 1.8667450691549599],[ 0.5050061695599972, 0.3604190134083436, -2.1543480811635543, 0.36764965552043255],[ -1.0948480250129886, 0.7745389392668738, 1.5968050092634876, -0.3089537127333798],[ 0.08682592596590691, -1.2936519054127453, -0.09751089857203867, 1.1747898804949495],[ 0.8580178754274119, -0.7902901415051404, 0.8091485431960054, -1.1092961657354645],[ 1.0181415700962575, -2.3349303886083823, 0.41162529954834004, 0.9584458906491704],[ -0.4095637932487307, 0.3280300168509243, -0.8730832207834258, -2.156048884197225],[ -1.520286905562377, 1.5913691494168336, -0.5383544938460167, 1.1876627429212467]
]).T
b1= \
    [-1.1028608423684458, 0.9795871821618028, -0.9670593937277123, 0.35702105144041035, -0.39206770018274484,
     0.5067862726020285, 0.8086410590634434, 0.06687831117360701, 0.6029565996394344, 1.263316566044935,
     2.3614913697559805, -0.07788876239534596, -0.49749220601462874, 1.5194204358646088, 0.8960741637454085,
     -0.7442509284270634]

expr1 = z * (np.matmul([[x1,x2,x3,x4]],w1)+b1)
#expr1 = -0.0001711589065517019 *pow(expr1,4)+ -0.01447711943585072 *pow(expr1,3)+ 0.002849795794085815 *pow(expr1,2)+ 0.5071116596907747 *expr1+ -0.00508383030596129
# expr1_1 = 0.25 * expr1 * expr1 + 0.001
# expr1 = 0.5 * expr1 + pow(expr1_1,0.5)


w2 =np.array(
    [-0.4456238059520372, -0.04313062719289106, 0.25731484478305033, -0.21107544582616874, 1.3947900359799126,
     -0.8373456406654303, 0.08695930713413144, 1.0193291505673208, -0.16011892902149397, 0.250477844518647,
     0.20541960920224497, 0.21163876238317633, 0.9445742125434423, -0.0014157537672593802, -1.079005155279257,
     1.3531227415898015]
).T
b2=  [0.2853233217913641]

expr2=np.matmul(expr1,w2)+b2
print(expr2)
# expr3 = simplify(expr2)
# print(expr3)