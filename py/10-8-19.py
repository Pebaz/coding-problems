"""
This problem was asked by Facebook.

Given an array of numbers representing the stock prices of a company in
chronological order and an integer k, return the maximum profit you can make
from k buys and sells. You must buy the stock before you can sell it, and you
must sell the stock before you can buy it again.

For example, given k = 2 and the array [5, 2, 4, 0, 1], you should return 3.
"""

import math

def trade(shares, trade_count):
    assert trade_count <= math.ceil(len(shares) / 2)

    # Map reversed share prices to their non-reversed indices
    data = {len(shares) - i - 1 : v for i, v in enumerate(reversed(shares))}

    profit = 0

    for _ in range(trade_count):

        # Find Lowest       
        lindex = 0
        lowest = data[0]
        for i, v in data.items():
            if v < lowest:
                lowest = v
                lindex = i
                
        # Find Highest
        hindex = lindex
        highest = lowest
        for i, v in data.items():
            if i > lindex:
                if v > highest:
                    highest = v
                    hindex = i

        profit += shares[hindex] - shares[lindex]

        #print('Lowest:', shares[lindex])
        #print('Highest:', shares[hindex])

        for index in range(lindex, hindex + 1):
            data.pop(index)

    return profit


def test_trade(shares, trade_count, should_equal):
    result = trade(shares, trade_count)
    print(result)
    assert result == should_equal

test_trade((5, 2, 4, 0, 1, 3), 2, 5)
test_trade((5, 2, 4, 0, 1), 2, 3)
test_trade((10, 0, 10, 2, 1, 2, 8), 2, 17)
test_trade((1, 0, 1, 0, 1, 0, 1), 3, 3)
test_trade((3, 0, 1, 0, 1, 0, 1), 4, 3)
