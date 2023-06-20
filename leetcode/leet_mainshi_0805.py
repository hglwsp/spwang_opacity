def multiply(A, B):
    flag = 0
    res = 0
    if A == 0 or B == 0:
        return 0
    if A > 0 & B < 0 or A < 0 & B > 0:
        flag = 1
    if A < 0:
        A = -A
    if B < 0:
        B = -B
    for i in range(0,B):
        res+=A
    if flag == 1:
        return -res
    else:
        return res


A = 1
B = 10
print(multiply(A,B))