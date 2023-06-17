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
[3.578663988466958],[ -5.470403002156279],[ 3.7501764936933757],[ 9.163381478723782],[ -16.335446580893958],[ 19.857042943084494],[ 10.2106857552514],[ -4.064613711936462]
]).T

b1= \
[-129.20352046115954, 77.98602014334462, -108.37325141450788, -112.47830209719977, 95.5733696477746, -123.51325538354291, -41.796662232408394, -12.013390402972824]

expr1 =  np.matmul([[x1]],w1)+b1
#expr1 = -0.0001711589065517019 *pow(expr1,4)+ -0.01447711943585072 *pow(expr1,3)+ 0.002849795794085815 *pow(expr1,2)+ 0.5071116596907747 *expr1+ -0.00508383030596129
# expr1_1 = 0.25 * expr1 * expr1 + 0.001
# expr1 = 0.5 * expr1 + pow(expr1_1,0.5)

w2 =np.array(
[6.275857400119805, -2.3471985198503784, -10.290103789616536, -4.081379418905428, -12.26321873527407, -11.559609260038375, 8.163055407170319, 4.3933683026450545]
).T

b2=  [151.23734877580748]

expr2 =  np.matmul(expr1,w2)+b2
print(expr2)
# expr3 = simplify(expr2)
# print(expr3)