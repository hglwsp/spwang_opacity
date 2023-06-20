def isValid(s):
    dic = {')': '(', ']': '[', '}': '{'}
    stack = []
    for i in s:
        if stack and i in dic:
            if stack[-1] == dic[i]:
                stack.pop()
            else:
                return False
        else:
            stack.append(i)
    return not stack


s = "{[]}"
print(isValid(s))