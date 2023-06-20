def trap(height):
    ans,n = 0,len(height)
    l_max = [0]*n
    r_max = [0]*n
    l_max[0] = height[0]
    r_max[n-1] = height[-1]
    for i in range(1,n):
        l_max[i] = max(height[i],l_max[i-1])
    for j in range(n-2,-1,-1):
        r_max[j] = max(height[j],r_max[j+1])
    for k in range(1,n-1):
        ans += min(l_max[k],r_max[k]) - height[k]
    return ans

height = [0,1,0,2,1,0,1,3,2,1,2,1]
print(trap(height))
