# 输入: a = "aba", b = "cdc"
# 输出: 3
def findLUSlength(a,b):
    la = len(a)
    lb = len(b)
    if a != b:
        return max(la,lb)
    else:
        return -1
a = "aba"
b = "cdc"
print(findLUSlength(a,b))
