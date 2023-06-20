# 斐波那契数列
# F(0) = 0，F(1) = 1
# F(n) = F(n - 1) + F(n - 2)，其中 n > 1
# 0 1 1 2 3 5
def fib(n):
    if n==0:
        return 0
    if n==1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

test = 5
print(fib(test))