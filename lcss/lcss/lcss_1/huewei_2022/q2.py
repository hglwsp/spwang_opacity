from z3 import *
c,phy1,phy2,phy3 = Reals('c phy1 phy2 phy3')
solver = Solver()

qs = [1.05*phy3+1.58*phy2+7.0*phy1+c==10.75,0.33*phy3+0.63*phy2+2.6*phy1+c==10.51,
      0.74*phy3+0.33*phy2+1.19*phy1+c==4.82,0.42*phy3+0.46*phy2+1.15*phy1+c==12.3]
for q in qs:
    solver.add(q)
if solver.check() == sat:
    result = solver.model()
print(result)
# print("x =", result[x], ", y =", result[y])
