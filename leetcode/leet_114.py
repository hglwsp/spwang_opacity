def flatten(root):
    pre = list()
    def xs(root):
        if root:
            pre.append(root)
            xs(root.left)
            xs(root.right)
    xs(root)
    n = len(pre)
    for i in range(1,n):
        prev,cur = pre[i-1],pre[i]
        prev.left = None
        prev.right = cur