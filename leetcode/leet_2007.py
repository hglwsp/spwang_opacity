import collections

def findOriginalArray(changed):
    to_remove = collections.Counter()   #计数器
    ans = []
    changed.sort()
    for num in changed:
        #print(to_remove[num])
        if to_remove[num] == 0:  #1 计数为0,
            ans.append(num)
            to_remove[num*2] += 1    #1*2=2，计数+1
        else:
            to_remove[num] -= 1
    if len(ans) * 2 == len(changed):
        return ans
    else:
        return []

m = [1,2,3,4,6,8]
print(findOriginalArray(m))