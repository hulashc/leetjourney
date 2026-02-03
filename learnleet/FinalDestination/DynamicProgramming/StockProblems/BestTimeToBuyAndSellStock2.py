







#### buy and sell stocks but many time for max profit

def max_profit_2(prices):
    max_profit = 0

    for i in range(1, len(prices)):
        if prices[i] > prices[i-1]:
            max_profit += prices[i] - prices[i-1]
    return max_profit


# single pass O(n), space O(1)