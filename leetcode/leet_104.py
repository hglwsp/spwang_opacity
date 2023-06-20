def maxDepth(root):
    # 宽度遍历
    if not root:
        return 0
    # 两个队列
    queue1 = [root]
    queue2 = []
    res = []
    level = 1
    while queue1:
        # res.append(node.val for node in root)
        level += 1
        for node in queue1:
            if node.left:
                queue2.append(node.left)
            if node.right:
                queue2.append(node.right)
        queue1 = queue2
        queue2 = []
    return level
