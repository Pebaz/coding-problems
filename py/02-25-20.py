"""
Find the second medium element in an array

Maintain 2 variables:
- Lowest
- 2nd Lowest

Iterate through array one time: O(n)
Store only 2 numbers, regardless of input: O(1)
"""

import math

def second_min(arr):
    lowest = arr[0]
    second = arr[1]

    for i in arr[2:]:
        if i < lowest:
            lowest = i
        elif i < second:
            second = i

    return second


def second_min2(arr):
    lowest = arr[0]
    second = arr[1]

    for i in range(len(arr) // 2 + 1):
        front = arr[i]
        back = arr[-(i + 1)] if i < len(arr) // 2 else back

        if front < lowest: lowest = front
        elif front < second: second = front

        if back < lowest: lowest = back
        elif back < second: second = back

    return second


if __name__ == '__main__':
    arr = [5, 3, 4, 2, 6, 7, 8]

    print(f'Second lowest of {arr}: {second_min(arr)}')
