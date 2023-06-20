def subsets(nums):
    # res = [[]]     # 返回结果，至少包含空集
    # for i in nums:
    #     res = res + [[i] + num for num in res]
    # return res

    # 回溯
    res = []
    n = len(nums)

    def helper(i, tmp):
        res.append(tmp)
        for j in range(i, n):
            helper(j + 1, tmp + [nums[j]])

    helper(0, [])
    return res


nums = [1,2,3]
print(subsets(nums))