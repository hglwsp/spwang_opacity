def levelOrder(self,root):
    # 两个队列
    # if not root:
    #     return []
    # queue1 = [root]
    # res = []
    # while queue1:
    #     res.append([node.val for node in queue1])
    #     queue2 = []
    #     for node in queue1:
    #         if node.left:
    #             queue2.append(node.left)
    #         if node.right:
    #             queue2.append(node.right)
    #     queue1 = queue2
    # return res

    # 递归
    res = []
    self.level(root,1,res)
    return res

def level(self,root,depth,res):
    if not root:
        return []
    if len(res) < depth:
        res.append([])
    res[depth-1].append(root.val)    # 添加
    if root.left:
        self.level(root.left,depth+1,res)
    if root.right:
        self.level(root.right,depth+1,res)



