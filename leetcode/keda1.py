def SDPCheck(str):
    n = len(str)
    if not str[0].islower(): return False
    if str[1] != '=': return False  # 没有value
    if (str[2] == ' '): return False # value 第一个空格
    for i in range(2,n):
        if not (str[i].isdigit() or str[i].islower() or str[i] == ' '):
            return False
    return True

str = "v=0"
print(SDPCheck(str))