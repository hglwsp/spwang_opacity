def rotate(matrix):
    # 辅助数组
    # n = len(matrix)
    # matrix_new = [[0] * n for _ in range(n)]
    # for i in range(n):
    #     for j in range(n):
    #         matrix_new[i][j] = matrix[n-j-1][i]
    # matrix[:] = matrix_new
    # 不用辅助数组
    n = len(matrix)
    # 水平
    for i in range(n//2):
        for j in range(n):
            matrix[i][j],matrix[n-i-1][j] = matrix[n-i-1][j],matrix[i][j]
    # 主对角线
    for i in range(n):
        for j in range(i):
            matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]

matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(rotate(matrix))