def findNumberIn2DArray(matrix, target):
    n = len(matrix)
    m = len(matrix[0])
    i = n   #行
    j = 0  #列
    if matrix[0][0] == target or matrix[n-1][m-1] == target:
        return True
    else:
        while i >= 0 and j < m:
            print(i)
            if (matrix[i][j] == target):
                return True
            elif (matrix[i][j] < target) and i > 0:
                i-=1
            elif (matrix[i][j] < target) and i == 0:
                j-=1
            elif (matrix[i][j] > target) and i < n:
                i += 1
            elif (matrix[i][j] > target) and i == n-1:
                j += 1
        return False



matrix = [
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
print(findNumberIn2DArray(matrix,26))