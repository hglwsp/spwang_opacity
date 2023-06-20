def guessNumber(n,k):
    left = 1
    right = n
    res = k
    while (left < right):
        mid = (left + right)//2
        if mid > res:
            left = mid + 1
        elif mid < res:
            right = mid
        else:
            return left
n = 10
k = 6
print(guessNumber(n,k))

