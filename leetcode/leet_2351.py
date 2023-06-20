def repeatedCharacter(s):
    n = len(s)
    hash = dict()
    for i in range(n):
        if s[i] not in hash:
            hash[s[i]] = 1
        else:
            return s[i]