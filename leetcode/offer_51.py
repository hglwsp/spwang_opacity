def maxPathSum(self,root: TreeNode):
    def hx(root):
        if not root: return 0
        left = hx(root.left)
        right = hx(root.right)
        self.ans = max(self.ans,root.val + left + right)
        return max(0,root.val,root.val+left,root.val+right)

    self.ans = root.val
    hx(root)
    return self.ans
