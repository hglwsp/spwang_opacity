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
x2 = symbols("x2")


z = symbols("relu")
z1 = symbols("hardtanh")

# y = 0.792*pow(x1-1,2)#公式
# apart(y,x1)



w1=np.array([[-0.06801227804566226, 0.9651790335085192],
[0.26439412729656625, 1.178410065995593],
[-2.17606326540943, -1.8112869855607325],
[0.8459128306926029, -0.3107374199851089],
[0.5528253090968612, -0.2663270999972738]
    ]).T
b1=[0.4725925904144397, 0.09841312835479193, -0.00011611432687108514, 0.035303995414540414, 0.3362794843471059]

expr1 = z * (np.matmul([[x1,x2]],w1)+b1)
#expr1 = -0.0001711589065517019 *pow(expr1,4)+ -0.01447711943585072 *pow(expr1,3)+ 0.002849795794085815 *pow(expr1,2)+ 0.5071116596907747 *expr1+ -0.00508383030596129
# expr1_1 = 0.25 * expr1 * expr1 + 0.001
# expr1 = 0.5 * expr1 + pow(expr1_1,0.5)

w2 =np.array([-2.4671391238944764, 1.8604633860353461, -0.04251425987261815, -1.3547370969841415, 0.8793268005455553]).T
b2=[0.7839539994407394]

expr2=np.matmul(expr1,w2)+b2
print(expr2)
# expr3 = simplify(expr2)
# print(expr3)