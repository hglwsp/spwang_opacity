from z3 import *

a,b,c,d = Reals('a b c d')

# points {0, 1}, {0.2, 1.1}, {0.4, 1.2}, {0.6, 1.3}, {1, 1.8}
# points {21,21.7},{21.25,21.6},{21.75,21.42},{22,21.2}
# points {4,4.82},{4.3,4.95},{4.6,5.35},{4.8,5.55}
# points {1,1.2},{1.03,1.3},{1.06,1.42},{1.1,1.5}
# points {0,0.9},{0.2,0.95},{0.6,1.2}{0.8,1.4}
# equation form
# ax^3 + bx^2 + cx + d = y

f_x =  a + b + c + d

print("start verify")
s = Solver()
s.add(And(  d == 0.9,
           0.2*0.2*0.2*a + 0.2*0.2*b + 0.2*c + d == 0.95,
           0.6*0.6*0.6*a +  0.6*0.6*b + 0.6*c + d == 1.2,
           0.8*0.8*0.8*a + 0.8*0.8*b+0.8*c+d ==1.5))
# print(s.check())
if s.check() == sat: #check()方法用来判断是否有解，sat(satisify)表示满足有解
    ans = s.model() #model()方法得到解
    print(s.check())
    print(ans)
    #也可以用变量名作为下标得到解
else:
    print("no ans!")
