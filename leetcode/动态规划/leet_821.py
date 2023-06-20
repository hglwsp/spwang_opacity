def shortestToChar(s, c):
    n = len(s)
    # 字母向左和向右，是c字符的距离为0
    res = [0 if C == c else n for C in s]

    # 向右
    for i in range(1, n):
        res[i] = min(res[i], res[i - 1] + 1)
    # 向左
    for i in range(n - 2, -1, -1):
        res[i] = min(res[i], res[i + 1] + 1)
    return res

s = "loveleetcode"
c = "e"
print(shortestToChar(s,c))

