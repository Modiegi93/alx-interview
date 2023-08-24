#!/usr/bin/python3
"""Make change"""


def makeChange(coins, total):
    """ Determine the fewest number of coins
        needed to meet a given amount total.
    """
    if total <= 0:
        return 0

    few = [float('inf')] * (total + 1)
    few[0] = 0

    for coin in coins:
        for i in range(coin, total + 1):
            few[i] = min(few[i], few[i - coin] + 1)

    if few[total] == float('inf'):
        return -1
    else:
        return few[total]
