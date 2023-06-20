def diameterOfBinaryTree(self, root) -> int:
    # 二叉树优先考虑递归思路求解
    self.res = 1
    def depth(node):
        if not node:return 0
        l = depth(node.left)
        r = depth(node.right)
        self.res = max(self.res, l+r+1)
        # 返回该节点为根的子树的最深的深度
        return max(l, r) + 1

    depth(root)
    return self.res - 1