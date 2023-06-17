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
x3 = symbols("x3")
x4 = symbols("x4")
x5 = symbols("x5")



z = symbols("relu")
z1 = symbols("hardtanh")

# y = 0.792*pow(x1-1,2)#公式
# apart(y,x1)



w1=np.array([
    [-30.35962905296206, -24.197380084372213], [-4.321009573484131, -8.923751214752992],
    [22.688562890728356, -9.045005879362664], [1.81451809118713, -88.83705167714311],
    [1.4968767223786812, -1.9543465364579027]
]).T
b1= \
    [0,0,0,0,0]
expr1 =  (np.matmul([[x1,x2]],w1)+b1)
#expr1 = -0.0001711589065517019 *pow(expr1,4)+ -0.01447711943585072 *pow(expr1,3)+ 0.002849795794085815 *pow(expr1,2)+ 0.5071116596907747 *expr1+ -0.00508383030596129
# expr1_1 = 0.25 * expr1 * expr1 + 0.001
# expr1 = 0.5 * expr1 + pow(expr1_1,0.5)

w2 =np.array(
[-0.022615027086791577, -0.01928722876707544, 0.006249846551438877, 0.012708929330755736, 0.0025484229550819058]
).T
b2=   [0]

expr2 =  np.matmul(expr1,w2)+b2
print(expr2)
# expr3 = simplify(expr2)
# print(expr3)