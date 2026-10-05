"""Problem 4: Best Time to Buy and Sell Stock

You are given an array `prices` where `prices[i]` is the price of a given stock
on day `i`.

Find the maximum profit you can achieve by choosing a single day to buy and
another day later to sell.

Example:
    Input: [7, 1, 5, 3, 6, 4]
    Output: 5
"""


def max_profit(prices):
    """Return the maximum profit from a single buy/sell transaction."""
    if not prices:
        return 0

    min_price = prices[0]
    best_profit = 0

    for price in prices[1:]:
        min_price = min(min_price, price)
        best_profit = max(best_profit, price - min_price)

    return best_profit


if __name__ == "__main__":
    print(max_profit([7, 1, 5, 3, 6, 4]))
    print(max_profit([7, 6, 4, 3, 1]))
