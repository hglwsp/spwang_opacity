def rob(nums):
    N = len(nums)
    if len(nums) == 0:
        return 0
    if N == 1:
        return nums[0]
    else:
        return max(rob1(nums[1:N]) ,rob1(nums[0:N-1]))

def rob1(nums):
    N = len(nums)
    if N == 0:
        return 0
    if N == 1:
        return nums[0]
    dp = [0] * N
    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])
    for i in range(2,N):
        dp[i] = max(dp[i-1], dp[i-2]+nums[i])
    return dp[-1]

nums = [2,3,2]
print(rob(nums))