import torch
import ann
import time
import superp
from z3.z3 import *
import numpy as np

# y = ax + b
x = Real("x")
a = Real("a")
b = Real("b")


f = -0.0822 * x  + 3.6904

print("start verify")
s = Solver()

# s.add(And(x<=40, f < 0))
# s.add(And(x>49.61, f > 0))
s.add(And(-0.0822 * x  + 3.6904 >=0,
          -0.0822*  (x + 0.0005*(1000-0.5418*x*x))  + 3.6904 <0))


# print(s.check())
if s.check() == sat: #check()方法用来判断是否有解，sat(satisify)表示满足有解
    ans = s.model() #model()方法得到解
    print(s.check())
    print(ans)
    #也可以用变量名作为下标得到解
else:
    print("no ans!")