def myAtoi(s):
    res = '0'
    while len(s) > 0:
        if s[0] == ' ' and res == '0':
            s = s[1:]
        elif s[0] == '-' and res == '0':
            res = '-'
            s = s[1:]
        elif s[0] == '+' and res == '0':
            res = '+'
            s = s[1:]
        elif 48 <= ord(s[0]) <= 57:
            res = res + s[0]
            s = s[1:]
        else:
            s = ''
    print(res)
    # result
    if res == '-' or res == "+":
        res = 0
    res = int(res)
    if res >= 2 ** 31 - 1:
        return 2 ** 31 - 1
    elif res <= -2 ** 31:
        return -2 ** 31
    else:
        return res

s = "42 word"
print(myAtoi(s))
