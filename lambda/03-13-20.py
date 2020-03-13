"""
This problem was asked by Facebook.

On a mysterious island there are creatures known as Quxes which come in three
colors: red, green, and blue. One power of the Qux is that if two of them are
standing next to each other, they can transform into a single creature of the
third color.

Given N Quxes standing in a line, determine the smallest number of them
remaining after any possible sequence of such transformations.

For example, given the input ['R', 'G', 'B', 'G', 'B'], it is possible to end up
with a single Qux through the following steps:

        Arrangement       |   Change
----------------------------------------
['R', 'G', 'B', 'G', 'B'] | (R, G) -> B
['B', 'B', 'G', 'B']      | (B, G) -> R
['B', 'R', 'B']           | (R, B) -> G
['B', 'G']                | (B, G) -> R
['R']                     |
"""


def qux(group):
    """
    Time: O(N!)
    Space: O(1)
    Stragegy: Iterative
    """

    combine = {
        (*'GB',) : 'R', (*'RB',) : 'G', (*'RG',) : 'B',
        (*'BG',) : 'R', (*'BR',) : 'G', (*'GR',) : 'B'
    }

    for _ in range(len(group)):
        combined = False
        for i in range(len(group) - 1):
            q1 = group[i]
            q2 = group[i + 1]
            if q1 != q2:
                group = [combine[q1, q2]] + group[i + 2:]
                combined = True
                break
        if not combined: break

    return len(group)


if __name__ == '__main__':
    print(qux(list('RGBGB')))
    print(qux(list('RRGG')))
    print(qux(list('BBBBBBBBBBBBBB')))
