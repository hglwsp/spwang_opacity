def checkTree(root):
    if root.val == root.left.val + root.right.val:
        return True
    else:
        return False