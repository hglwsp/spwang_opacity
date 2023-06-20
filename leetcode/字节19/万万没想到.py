m = int(input())
while m > 0:
    examples = input()
    res = []  # 返回结果
    for s in examples: # m is number of examples
        if len(res)<2:
            res.append(s)
            continue
        if len(res)>=2:
            if res[-1] == s and res[-2] == s:
                continue
        if len(res)>=3:
            if res[-1] == s and res[-2] == res[-3]:
                continue
        res.append(s)
    print("".join(res))
    m -= 1

