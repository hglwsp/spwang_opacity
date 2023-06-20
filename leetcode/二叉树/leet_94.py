def inorderTraversal(root):
    if not root:
        return []
    res = []
    stack = []
    cur = root
    while stack or cur:
        # 左孩子一直进栈
        while cur:
            stack.append(cur)
            cur = cur.left
        cur = stack.pop(cur)
        res.append(cur.val)
        cur = cur.right
    return res


# 递归
# return self.inorderTraversal(root.left) + root.val + self.inorderTraversal(root.right)
# return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)


# res = []
# def dfs(root):
#     if not root:
#         return []
#     dfs(root.left)
#     res.append(root.val)    # left -> print -> right
#     dfs(root.right)
# dfs(root)
# return res



