





### dynamic programming

def max_profit(prices):
    if not prices:
        return 0
    
    min_price = float('inf') # we put float infinity because it gurantees it will replace min
    max_profit = 0

    for price in prices:
        min_price = min(min_price, price)
        max_profit = max(max_profit, price - min_price)

    return max_profit