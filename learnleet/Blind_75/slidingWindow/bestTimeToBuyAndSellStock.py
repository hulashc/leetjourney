

# You are given an array prices where prices[i] is the price of a stock on day i.
# You want to maximize your profit by choosing one day to buy and one day to sell (buy before sell).
# Return the maximum profit you can achieve. If no profit is possible, return 0.


def max_profit(prices):

    min_price= float('inf')
    max_profit = 0

    for price in prices:
        if price < min_price:
            min_price = price
        elif price - min_price > max_profit:
            max_profit = price - min_price
    
    return max_profit

