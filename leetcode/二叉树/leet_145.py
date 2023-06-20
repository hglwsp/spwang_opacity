def postorderTraversal(root):
    # res = []
    # def hs(root):
    #     if not root:
    #         return []
    #     hs(root.left)
    #     hs(root.right)
    #     res.append(root)
    # hs(root)
    # return res
    # 中序‘ 反转
    if not root:
        return []
    res = []
    stack = []
    cur = root
    while stack or cur:
        # 右孩子一直进栈
        while cur:
            res.append(cur.val)
            stack.append(cur)
            cur = cur.right
        cur = stack.pop()
        cur = cur.left
    return res[::-1]