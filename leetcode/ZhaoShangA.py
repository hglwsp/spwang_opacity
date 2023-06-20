# def minCake(n , a , b ):
#     # 榴莲 a， 冰淇淋b， n盘子
#     if (a + b < 2 * n or min(a, b) < 2): return 0
#     if n == 2: return min(a, b)
#     res = float('inf')
#     for i in range(1, n - 1):
#         # 榴莲 i盘子 冰淇淋 n-i
#         # 不能整除
#         if a % (i + 1) != 0 or b % (n - i - 1) != 0:
#             continue
#         if a - 2 * (i + 1) < 0 or b - 2 * (n - i - 1) < 0:
#             continue
#         res = min(res, min(a // (i + 1), b // (n - i - 1) ))
#     if res == float('inf'): return 0
#     else:return res
# n,a,b = 2,5,4
# print(minCake(n,a,b))

def maxRealValue(m , sellPrice , realValue ):
    sellPrice.sort()
    realValue.sort(reverse = True)
    index = 0
    while sum(sellPrice[:index+1]) <= m and index < len(sellPrice):
        index += 1
    return sum(realValue[:index])

m,sellPrice,realValue = 4,[6,6,1,3],[1,4,4,1]
print(maxRealValue(m,sellPrice,realValue))