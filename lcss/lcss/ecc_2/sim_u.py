import numpy as np
import matplotlib.pyplot as plt
import math
import random
#import tensorflow as tf
from sympy import *
import sympy as sp
import torch
import torch.nn as nn

x1 = symbols("x1")  # 符号x，自变量




z = symbols("relu")
z1 = symbols("hardtanh")
z2 = symbols("sigmoid")

# y = 0.792*pow(x1-1,2)#公式
# apart(y,x1)



w1=np.array([
[0.9946468636179848],[ 0.44674031450935286],[ 0.10894351281284403],[ 0.46817811061816217],[ 1.5852445104105957],[ -0.2945158563287541],[ 1.4063942699465268],[ -0.28401321462165313]
]).T

b1= \
[-0.6411184403633341, -0.7963825018582469, -0.1106259201568242, -0.42443234410763775, -0.3218651118042591, 1.5333102043740907, -1.321109693262751, -1.239687112457733]
expr1 =  np.matmul([[x1]],w1)+b1
#expr1 = -0.0001711589065517019 *pow(expr1,4)+ -0.01447711943585072 *pow(expr1,3)+ 0.002849795794085815 *pow(expr1,2)+ 0.5071116596907747 *expr1+ -0.00508383030596129
# expr1_1 = 0.25 * expr1 * expr1 + 0.001
# expr1 = 0.5 * expr1 + pow(expr1_1,0.5)

w2 =np.array(
[0.3352476217442264, -0.1336877865564933, 1.3340164077516297, 0.447447840111403, -0.2548119395879631, 2.867443767486909, 0.6981169973804853, -1.1196246309042654]
).T

b2=   [0.008442196081411994]

expr2 =  np.matmul(expr1,w2)+b2
print(expr2)
# expr3 = simplify(expr2)
# print(expr3)