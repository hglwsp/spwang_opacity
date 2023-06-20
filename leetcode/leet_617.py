def mergeTrees(self, root1, root2):
    # 二叉树优先考虑递归思路求解
    if not root1: return root2
    if not root2: return root1
    # 合并，根左右
    merged = TreeNode(root1.val+root2.val)
    merged.left = self.mergeTrees(root1.left,root2.left)
    merged.right = self.mergeTrees(root1.right,root2.right)
    return merged