def minCostToMoveChips(position):
    # n = len(position)
    # res = 99999999
    # for i in range(0,n):
    #     flag = 0
    #     for j in range(0,n):
    #         if (position[j]-position[i])%2==1:
    #             flag+=1
    #     res = min(res,flag)
    # return res
    n = len(position)
    ji = 0
    ou = 0
    for i in range(0,n):
        if position[i]%2 == 0:
            ji+=1
        else:
            ou+=1
    return min(ji,ou)



position = [2,2,2,3,3]
print(minCostToMoveChips(position))