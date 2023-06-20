def integerReplacement(n):
    if n == 1:
        return 0
    elif n % 2 == 0:
        return 1 + integerReplacement(n/2)
    else:
        return 1 + min(integerReplacement(n + 1),integerReplacement(n - 1))


test = 7
print(integerReplacement(test))
