"""
Given an array of integers of length n, containing values between 1 and n-1, find the duplicate entry.

Example Array:

[2 1 2]

Strategy:
    1. Create a set
    2. Iterate through array, adding each element to set
    3. If any duplicate is found, return that entry
"""


# Fastest
def duplicate(arr):
    seen = set()
    for i in arr:
        if i in seen:
            return i
        seen.add(i)


def bubble(arr):
    for _ in range(len(arr)):
        for i in range(len(arr) - 1):
            if arr[i] >= arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]

# O(N) space
def duplicate(arr):
    #arr.sort()
    bubble(arr)
    for i in range(len(arr) - 1):
        if arr[i] == arr[i + 1]:
            return arr[i]


if __name__ == '__main__':
    array = [2, 1, 2]

    assert duplicate(array) == 2
