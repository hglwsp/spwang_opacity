# 判断子序列
# 给定字符串 s 和 t ，判断 s 是否为 t 的子序列。
# 输入：s = "abc", t = "ahbgdc"
# 输出：true

def isSubsequence( s, t):
    # 双指针
    # l1 = len(s)
    # l2 = len(t)
    # i = 0
    # j = 0
    # while i < l1 and j < l2:
    #     if s[i] == t[j]:
    #         i+=1
    #     j+=1
    # return i == l1

    # dp
    l1 = len(s)
    l2 = len(t)

s = "abc"
t = "ahbgdc"
print(isSubsequence(s,t))