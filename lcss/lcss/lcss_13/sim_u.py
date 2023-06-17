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
    [-0.2777678556967114, -2.228728113622503], [-0.1771691855184613, -0.1870589682562671],
    [-0.35312543551945863, 1.0746790095678305], [-0.2520932084937407, 0.6419722183062249],
    [-0.03867305720666885, 2.5569490081571224]
]).T
b1= \
    [0,0,0,0,0]
expr1 =  (np.matmul([[x1,x2]],w1)+b1)
#expr1 = -0.0001711589065517019 *pow(expr1,4)+ -0.01447711943585072 *pow(expr1,3)+ 0.002849795794085815 *pow(expr1,2)+ 0.5071116596907747 *expr1+ -0.00508383030596129
# expr1_1 = 0.25 * expr1 * expr1 + 0.001
# expr1 = 0.5 * expr1 + pow(expr1_1,0.5)

w2 =np.array(
[0.28461198162192664, 0.17768261661089965, 0.3496321253688998, 0.24999012306148138, 0.030679324995581153]
).T
b2=   [0]

expr2 =  np.matmul(expr1,w2)+b2
print(expr2)
# expr3 = simplify(expr2)
# print(expr3)