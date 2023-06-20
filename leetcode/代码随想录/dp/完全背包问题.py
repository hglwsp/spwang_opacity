# 先遍历物品，再遍历背包
def test_complete_pack1():
    weight = [1, 3, 4]
    value = [15, 20, 30]
    bag_weight = 4

    dp = [0] * (bag_weight + 1)

    for i in range(len(weight)):
        for j in range(weight[i], bag_weight + 1):
            dp[j] = max(dp[j], dp[j - weight[i]] + value[i])

    print(dp[bag_weight])


# 先遍历背包，再遍历物品
def test_complete_pack2():
    weight = [1, 3, 4]
    value = [15, 20, 30]
    bag_weight = 4

    dp = [0] * (bag_weight + 1)

    for j in range(bag_weight + 1):
        for i in range(len(weight)):
            if j >= weight[i]: dp[j] = max(dp[j], dp[j - weight[i]] + value[i])

    print(dp[bag_weight])


if __name__ == '__main__':
    test_complete_pack1()
    test_complete_pack2()

# 0-1
# // weight数组的大小 就是物品个数
# for(int i = 1; i < weight.size(); i++) { // 遍历物品
#     for(int j = 0; j <= bagweight; j++) { // 遍历背包容量
#         if (j < weight[i]) dp[i][j] = dp[i - 1][j];
#         else dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - weight[i]] + value[i]);
#
#     }
# }

# 完全
# // 先遍历物品，再遍历背包
# for(int i = 0; i < weight.size(); i++) { // 遍历物品
#     for(int j = weight[i]; j <= bagWeight ; j++) { // 遍历背包容量
#         dp[j] = max(dp[j], dp[j - weight[i]] + value[i]);
#
#     }
# }