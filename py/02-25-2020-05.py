"""
A fixed point in an array is an element whose value is equal to its index.
Given a sorted array of distinct elements, return a fixed point, if one exists.
Otherwise, return False.

For example, given [-6, 0, 2, 40], you should return 2.
Given [1, 5, 7, 8], you should return False.

Strategy:
    1. Iterate over each item in the array
    2. Compare index to value
    3. Return first value to equal index
    4. Else return False
"""

def fixed_point(arr):
    for index, value in enumerate(arr):
        if index == value:
            return value
    return False


if __name__ == '__main__':
    arr1 = [-6, 0, 2, 40]
    arr2 = [1, 5, 7, 8]
    print(arr1, fixed_point(arr1))
    print(arr2, fixed_point(arr2))
