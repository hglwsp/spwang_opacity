def preorderTraversal(root):
    # 先序， print -> left -> right
    # res = []
    # def xs(root):
    #     if not root:
    #         return []
    #     res.append(root.val)
    #     xs(root.left)
    #     xs(root.right)
    # xs(root)
    # return res


    # stack
    if not root:
        return []
    stack = []
    res = []
    cur = root
    while stack or cur:
        while cur:
            res.append(cur.val)
            stack.pop()
            cur = cur.left
        cur = stack.pop()
        cur = cur.right
    return res