def deepestLeavesSum(root):
    # res = []
    # def level(root,depth):
    #     if not root:
    #         return []
    #     if len(res) < depth:
    #         res.append([])
    #     res[depth-1].append(root.val)
    #     if root.left:
    #         level(root.left,depth+1)
    #     if root.right:
    #         level(root.right,depth+1)
    # level(root,1)
    # return res[-1]

    # queue
    if not root:
        return []
    res = []
    queue1 = [root]
    while queue1:
        res.append(node.val for node in queue1)
        queue2 = []
        for node in queue1:
            if node.left:
                queue2.append(node.left)
            if node.right:
                queue2.append(node.right)
        queue1 = queue2
    return sum(res[-1])
