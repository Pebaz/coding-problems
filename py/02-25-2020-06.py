"""
This problem was asked by Spotify.

Write a function, throw_dice(N, faces, total), that determines how many ways it
is possible to throw N dice with some number of faces each to get a specific
total.

For example, throw_dice(3, 6, 7) should equal 15.

For example, throw_dice(2, 4, 4) should equal 3.

Strategy:
    1. Create a set of combinations
    2. Iterate through each dice
    3. Add combinations to set whose sum equals target
    4. Return len(set)
"""


from itertools import *


def throw_dice(dice, faces, total):
    count = 0
    for combo in combinations_with_replacement(range(1, faces), dice):
        for roll in set(permutations(combo, dice)):
            count += 1 if sum(roll) == total else 0
    return count


print(throw_dice(5, 6, 7))
