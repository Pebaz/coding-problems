"""
This problem was asked by Glassdoor.

An imminent hurricane threatens the coastal town of Codeville. If at most two
people can fit in a rescue boat, and the maximum weight limit for a given boat
is k, determine how many boats will be needed to save everyone.

For example, given a population with weights [100, 200, 150, 80] and a boat
limit of 200, the smallest number of boats required will be three.
"""

def boats(arr, limit):
    """
    Time:
    Space:
    """
    return int(sum(arr) / limit + 1)


if __name__ == '__main__':
    print(boats([100, 200, 150, 80], 200), 3)
    print(boats([100, 100, 100], 200), 2)
    print(boats([], 200), 3)
    print(boats([], 200), 3)
