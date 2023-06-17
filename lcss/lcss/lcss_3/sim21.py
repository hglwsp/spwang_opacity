import numpy as np
import matplotlib.pyplot as plt
import math
import random
#import tensorflow as tf
from sympy import *
import sympy as sp

x1 = symbols("x1")  # 符号x，自变量
x2 = symbols("x2")
x3 = symbols("x3")
z = symbols("tanh")
# y = 0.792*pow(x1-1,2)#公式
# apart(y,x1)



w1=[[0.5557,-0.1396,1.6683,-0.7194,-0.7428],
      [-0.4361,-0.5516,-0.0882,-0.0426,0.0540],
         [-0.3962,-0.1922,-1.3668,0.4441,0.6488]]
b1=[-0.7916, -0.1209, -0.7710, -0.6779,  0.3071]

expr1=z*(np.matmul([[x1,x2,x3]],w1)+b1)



w2 =[ [0.5037],
      [0.3255],
      [0.9507],
      [0.7603],
      [-0.0535]]
b2=[-0.5602]

expr2=np.matmul(expr1,w2)+b2
#print(expr2)
expr3 = simplify(expr2)
print(expr3)