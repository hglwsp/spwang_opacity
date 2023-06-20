def rob(root):
    def dfs(root):
        if not root:
            return [0,0]  # 偷， 不偷
        left = dfs(root.left)
        right = dfs(root.right)
        # 偷root, left,right不偷
        max1 = root.val + left[1] + right[1]
        # 不偷, 偷左右子树最大值
        max2 = max(left[0],left[1]) + max(right[0],right[1])
        return [max1,max2]
    res = dfs(root)
    return max(res)



