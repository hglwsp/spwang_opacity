def arrayNesting(nums):
    # 图，原地标记
    ans = 0
    n = len(nums)
    for i in range(1,n):
        cnt = 0
        while nums[i] < n:
            num = nums[i]
            nums[i] = n
            i = num
            cnt+=1
        ans = max(ans,cnt)
    return ans