# result = []
# def backtrack(选择列表, 路径):
#     if 满足结束条件:
#         result.add(路径)
#         return
#     for 选择 in 选择列表:
#         # 做选择
#         路径.add(选择)
#         将该选择从选择列表移除
#         backtrack(选择列表, 路径) # 核心 递归调用之前【做选择】，调用之后【撤销选择】
#         # 撤销选择
#         路径.remove(选择)
#         将该选择再加入选择列表


def permute(nums):
    # 回溯法模板
    # 选择，递归，撤销选择
    n = len(nums)
    res = []
    path = []
    used = [False]*n
    def backtrack(nums,path,used):
        # 判断是否触发结束条件
        if len(path) == n:
            res.append(path[:])
            return
        else:
            for i in range(n):
                if used[i]:   # nums[i]选过，跳过
                    continue
                # 选择回溯递归
                path.append(nums[i])
                used[i] = True
                backtrack(nums,path,used)
                # 撤销选择
                path.pop()
                used[i] = False
    backtrack(nums,path,used)
    return res




nums = [1,2,3]
print(permute(nums))