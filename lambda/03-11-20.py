"""
A magic index in an array A[0...n-1] is defined to be an index such that
A[i] = i. Given a sorted array of distinct integers, write a method to find a
magic index, if one exists, in array A.

Strategy:
    1. Pick the array's middle index
    2. See if it's value is larger than it's index
    3. If so, repeat the algorithm on the left half of the array
    4. If not, repeat the algorithm on the right half of the array
"""

def magic(arr, mod=0):
    """
    Time: O(log n)
    Space: O(1)
    """
    if len(arr) == 1:
        return 0 if arr[0] == 0 else None

    index = len(arr) // 2
    index_value = index + mod

    if arr[index] == index_value:
        return index_value

    elif arr[index] > index_value:
        return magic(arr[:index], mod + len(arr) - len(arr[:index]))

    elif arr[index] < index_value:
        return magic(arr[index:], mod + len(arr) - len(arr[index:]))

if __name__ == '__main__':
    print(magic([-1, 0, 2]))
    print(magic([2, 3, 4, 5, 6, 7, 8, 9, 10]))
    print(magic([-21, -19, -18, -14, -13, -12, -11, -7, -8, -9, 10, 103]))
