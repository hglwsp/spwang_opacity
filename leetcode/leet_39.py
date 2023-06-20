# result = []
# def backtrack(选择列表, 路径):
#     if 满足结束条件:
#         result.add(路径)
#         return
#
#     for 选择 in 选择列表:
#         # 做选择
#         路径.add(选择)
#         将该选择从选择列表移除
#         backtrack(选择列表, 路径) # 核心 递归调用之前【做选择】，调用之后【撤销选择】
#         # 撤销选择
#         路径.remove(选择)
#         将该选择再加入选择列表

def combinationSum(candidates, target):
    res = []
    def backtrack(candidates,path,target,start):
        if sum(path) == target:
            res.append(path[:])
            return
        if sum(path) > target:
            return
        for i in range(start,len(candidates)):
            path.append(candidates[i])
            backtrack(candidates,path,target,i)
            path.pop()
    backtrack(candidates,[],target,0)
    return res

