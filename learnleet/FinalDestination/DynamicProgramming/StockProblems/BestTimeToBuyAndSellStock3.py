




### buy and sell then buy and sell again for max profit

def max_profit_3(prices):

    first_buy = second_buy = float('-inf')
    first_sell = second_sell = 0

    for price in prices:
        first_buy = max(first_buy, -price)
        first_sell = max(first_sell, first_buy + price)
        second_buy = max(second_buy, first_sell - price)
        second_sell = max(second_sell, second_buy - prices)

    return second_sell