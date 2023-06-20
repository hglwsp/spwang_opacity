def searchMatrix(matrix ,target):
    m = len(matrix)
    n = len(matrix[0])      #行列长度
    for i in range(0,m):
        for j in range(0,n):
            if matrix[i][j] == target:
                return True
    return False


test = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
target = 20
print(searchMatrix(test,target))