def myPow(x, n):
    res = 1
    if n < 0 :
        x, n = 1/x, -n
    while n:
        if n%2 == 0:
            x*=x
            n/=2
        else:
            res*=x
            n-=1
    return res


x = 2.00000
n = 10
print(myPow(x,n))