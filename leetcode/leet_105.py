def buildTree(self, preorder, inorder):
    if not preorder or not inorder:
        return None

    rootval = preorder[0]
    root = TreeNode(rootval)
    # 找中序下标
    midindex = inorder.index(rootval)
    inorderleft = inorder[:midindex]
    inorderright = inorder[midindex+1:]
    # 前序节点
    preorderleft = preorder[1:len(inorderleft) + 1]
    preorderright = preorder[len(inorderleft) + 1:]
    root.left = self.buildTree(preorderleft,inorderleft)
    root.right = self.buildTree(preorderright,inorderright)
    return root


