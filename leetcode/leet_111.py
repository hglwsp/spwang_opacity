def minDepth(self,root):
    # dfs
    # if root == None: return 0
    # if root.left == None and root.right == None: return 1
    # minleft = self.minDepth(root.left)
    # minright = self.minDepth(root.right)
    # if root.left != None and root.right == None:
    #     return minleft + 1
    # if root.left == None and root.right != None
    #     return minright + 1
    # return min(minleft, minright) + 1

    # bfs
    if root == None: return 0
    queue1 = [root]
    depth = 1
    res = []
    while queue1:
        # res.append(node.val for node in queue1)
        queue2 = []
        for node in queue1:
            if not node.left and not node.right:
                return depth
            if node.left:
                queue2.append(node.left)
            if node.right:
                queue2.append(node.right)
        queue1 = queue2
        depth += 1
    return depth





