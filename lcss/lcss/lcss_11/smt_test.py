from z3 import *
import torch.nn as nn

x1,x2,x3,x4,x5 = Reals('x1 x2 x3 x4 x5')
h = (x1 - x2) * (x1 - x2)

#relu
def relu(x):
    res = If(x>0,x,0)
    return res




#controller
u = 0.8*x1 - 0.8*x3 + 1.5*x2 - 1.5*x4 + x5


#system
f_x1 = x1 + x3 + 0.5 * x5
f_x2 = x2 + x4 + 0.5 * u
f_x3 = x3 + x5
f_x4 = x4 + u

#barrier
B = 0.9227*x1*x1 + 0.2348*x3*x3+ 0.9227*x2*x2 + 0.2348*x4*x4
+ 0.006*x1*x3 - 0.006*x2*x3 - 0.006*x1*x4 - 0.006*x2*x4 - 0.4696*x2*x4 - 1.845*x1 * x2- 0.0002*x2 + 0.0728

B_f =  0.9227*f_x1*f_x1 + 0.2348*f_x3*f_x3+ 0.9227*f_x2*f_x2 + 0.2348*f_x4*f_x4
+ 0.006*f_x1*f_x3 - 0.006*f_x2*f_x3 - 0.006*f_x1*f_x4 - 0.006*f_x2*f_x4 - 0.4696*f_x2*f_x4 - 1.845*f_x1 * f_x2- 0.0002*f_x2 + 0.0728

print("start verify")
s = Solver()
s.add(And(0 <= x1, x1 <= 1, 1 <= x2, x2 <= 10,
          x2 - x1 <= 1,
          x3 == 0, x4 == 0,
          B > 1))
# print(s.check())
if s.check() == sat: #check()方法用来判断是否有解，sat(satisify)表示满足有解
    ans = s.model() #model()方法得到解
    print(s.check())
    print(ans)
    #也可以用变量名作为下标得到解
else:
    print("no ans!")

print("start verify")
#unsafe condition
s = Solver()
s.add(And(0 <= x1, x1 <= 10, 0 <= x2, x2 <= 10,
          0 <= x3, x3 <= 0.1, 0 <= x4, x4 <= 0.1,
          (x2 - x1) * (x2 - x1) > 1.001*1.001,
             B < 1),
         )
# print(s.check())
if s.check() == sat: #check()方法用来判断是否有解，sat(satisify)表示满足有解
    ans = s.model() #model()方法得到解
    print(s.check())
    print(ans)
else:
    print("no ans!")


print("start verify")
#diff condition
s = Solver()
s.add(And(0 <= x1, x1 <= 10, 0 <= x2, x2 <= 10,
          0 <= x3, x3 <= 0.1, 0 <= x4, x4 <= 0.1,
          -0.05 <= x5, x5 <= 0.05,-0.05 <= u, u <= 0.05,
          0 <= f_x1, f_x1 <= 10, 0 <= f_x2, f_x2 <= 10,
          0 <= f_x3, f_x3 <= 0.1, 0 <= f_x4, f_x4 <= 0.1,
          B_f - B > 0 ))
# print(s.check())
if s.check() == sat: #check()方法用来判断是否有解，sat(satisify)表示满足有解
    ans = s.model() #model()方法得到解
    print(s.check())
    print(ans)
    #也可以用变量名作为下标得到解
else:
    print("no ans!")


print("success")