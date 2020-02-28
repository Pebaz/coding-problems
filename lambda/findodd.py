"""
Write a function that takes an array and size as a parameter. The array
contains non-negative numbers. Every number in the array appears an even number
of times, except for one number that appears an odd number of times. The
function should return the number that appears an odd number of times.

Strategy:
    1. fn(arr, size)
    2. test it
    3. iterate through once and store all in hashmap[count]
    4. iterate through once more and return first odd one
"""

# Time: O(N)
# Space: O(N)
def find_odd(arr):
    items = {}
    for i in arr:
        items[i] = items.get(i, 0) + 1
    for key, val in items.items():
        if val % 2:
            return key

# Time: O(N)
# Space: O(N) (but mostly not)
def find_odd(arr):
    items = set()
    for i in arr:
        if i in items:
            items.remove(i)
        else:
            items.add(i)
    for i in items:
        return i

# Tests
if __name__ == '__main__':
    assert find_odd([1, 1, 2, 2, 2, 2, 3, 4, 4, 5, 5]) == 3
    assert find_odd([1]) == 1
    assert find_odd([1, 1, 1]) == 1
