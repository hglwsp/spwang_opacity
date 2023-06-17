from z3 import *

a = Real('a')#定义一个整形 a
b = Real('b')#定义一个整形 b
s = Solver()#生成一个约束求解器

s.add((a + b)**0.5<10)#添加约束条件 a+b<2
s.add(a>=0)#添加约束条件 a>=0
s.add(b>=0)#添加约束条件 b>=0

print(s.check())#检查约束求解器是否有解，如果有,返回sat; 如果不满足,返回unsat
print(s.model())#输出结果

