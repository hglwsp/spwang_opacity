def sumNums(n):
    return n and n + sumNums(n-1)


test = 5
print(sumNums(test))