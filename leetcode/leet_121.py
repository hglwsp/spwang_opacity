def maxProfit(prices):
    low = 0
    fast = 1    #双指针
    money = 0
    l = len(prices)
    while low < l-1:
        if prices[fast] - prices[low] > 0 and prices[fast] - prices[low] > money:
            money = prices[fast] - prices[low]
        fast += 1
        if fast == l:
            low += 1
            fast = low + 1
    return money

prices = [7,1,5,3,6,4]
print(maxProfit(prices))