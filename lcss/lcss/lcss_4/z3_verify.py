import torch
import ann
import time
import superp
from z3.z3 import *
import numpy as np

def ReLU(x):
    res = [[If(ele > 0, ele, 0) for ele in row] for row in x]
    return np.array(res)

def barrier(x1,x2,x3,x4,netof_barr):
    params=netof_barr.state_dict() #获得模型的原始状态以及参数。
    hidden = []
    for k,v in params.items():
        hidden.append(v.detach().numpy())
    hidden1 = ReLU(np.dot(hidden[0], np.array([x1, x2,x3,x4]).reshape(-1, 1))+ (hidden[1].reshape(-1,1)))
    # hidden2 = ReLU(np.dot(hidden[2], hidden1) + (hidden[3].reshape(-1,1)))
    hidden2 = np.dot(hidden[2], hidden1) + (hidden[3].reshape(-1,1))
    return hidden2

def controller(x1,x2,netof_u):
    params=netof_u.state_dict() #获得模型的原始状态以及参数。
    hidden = []
    for k,v in params.items():
        hidden.append(v.detach().numpy())
    hidden1_u = ReLU(np.dot(hidden[0], np.array([x1, x2]).reshape(-1, 1)) + (hidden[1].reshape(-1,1)))
    # hidden2_u = ReLU(np.dot(hidden[2], hidden1_u) + (hidden[3].reshape(-1,1)))
    hidden2_u = np.dot(hidden[2], hidden1_u) +(hidden[3].reshape(-1,1))
    return hidden2_u

x1 = Real("x1")
x2 = Real("x2")
x3 = Real("x3")
x4 = Real("x4")         #要传入的变量
barr_nn = ann.gen_nn(superp.N_H_B, superp.D_H_B, superp.DIM_S, 1, superp.BARR_ACT, superp.BARR_OUT_BOUND) #要传入的网络
ctrl_nn = ann.gen_nn(superp.N_H_C, superp.D_H_C, superp.DIM_S-2, superp.DIM_C, superp.CTRL_ACT, superp.CTRL_OUT_BOUND)
barr_nn.load_state_dict(torch.load('pre_trained_barr.pt'), strict=True)
ctrl_nn.load_state_dict(torch.load('pre_trained_ctrl.pt'), strict=True)
B = sum(barrier(x1,x2,x3,x4,barr_nn))[0]
u1 = sum(controller(x1,x3,ctrl_nn))[0]
u2 = sum(controller(x2,x4,ctrl_nn))[0]

# 运动系统
f_x1 = x1 + x3 + 0.5 * u1
f_x2 = x2 + x4 + 0.5 * u2
f_x3 = x3 + u1
f_x4 = x4 + u2
B_f = sum(barrier(f_x1,f_x2,f_x3,f_x4,barr_nn))[0]




# z3验证
time_start_verify = time.time()
print("start verify init")
s = Solver()
s.add(And(0 <= x1, x1 <= 0.8, 0.8 <= x2, x2 < 1.8,
          x3 == 0, x4 == 0,
          x2 - x1 <= 0.8,
          0 <= u1, u1 <= 0.05,0 <= u2, u2 <= 0.05,
          B > 0))
# print(s.check())
if s.check() == sat: #check()方法用来判断是否有解，sat(satisify)表示满足有解
    ans = s.model() #model()方法得到解
    print(s.check())
    print(ans)
    #也可以用变量名作为下标得到解
else:
    print("no ans!")

print("start verify unsafe1")
#unsafe condition
s = Solver()
s.add(And(0 <= x1, x1 <= 7, 0 <= x2, x2 <= 7,
          0 <= x3, x3 <= 0.1, 0 <= x4, x4 <= 0.1,
          0 <= u1 ,u1 <= 0.05,0 <= u2 ,u2 <= 0.05,
          x2 - x1 > 1,
             B < 0)
         )
# print(s.check())
if s.check() == sat: #check()方法用来判断是否有解，sat(satisify)表示满足有解
    ans = s.model() #model()方法得到解
    print(s.check())
    print(ans)
else:
    print("no ans!")


print("start verify unsafe2")
#unsafe condition
s = Solver()
s.add(And(0 <= x1, x1 <= 7, 0 <= x2, x2 <= 7,
          0 <= x3, x3 <= 0.1, 0 <= x4, x4 <= 0.1,
          0 <= u1 ,u1 <= 0.05,0 <= u2 ,u2 <= 0.05,
          x1 - x2 > 1,
             B < 0),
         )
# print(s.check())
if s.check() == sat: #check()方法用来判断是否有解，sat(satisify)表示满足有解
    ans = s.model() #model()方法得到解
    print(s.check())
    print(ans)
else:
    print("no ans!")

print("start verify diff")
#diff condition
s = Solver()
s.add(And(0 <= x1, x1 <= 7, 0 <= x2, x2 <= 7,
          0 <= x3, x3 <= 0.1, 0 <= x4, x4 <= 0.1,
          0 <= u1, u1 <= 0.05,0 <= u2, u2 <= 0.05,
          0 <= f_x1, f_x1 <= 7, 0 <= f_x2, f_x2 <= 7,
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

time_end_verify = time.time()

print("Verifying totally costs:", time_end_verify - time_start_verify)
print("-------------------------------------------------------------------------")
print("success")






