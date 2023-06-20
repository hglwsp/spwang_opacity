def myPow(x,n) :
    res = 1
    if n == 0:
        return 1
    if n < 0:
        x = 1/x
        n = -n
    while n > 0:
        if n % 2 == 0:
            x*=x
            n/=2
        else:
            res*=x
            n-=1
    return res

