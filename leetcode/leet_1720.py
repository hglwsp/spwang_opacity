def decode(encoded, first):
    res = []
    l = len(encoded)
    res.append(first)
    for i in range(0,l):
        res.append(res[-1] ^ encoded[i])
    return res

encoded = [1,2,3]
first = 1
print(decode(encoded,first))