"""
Write an efficient program for printing k largest elements in an array.
Elements in array can be in any order. For example, if given array is
[1, 23, 12, 9, 30, 2, 50] and you are asked for the largest 3 elements i.e.,
k = 3 then your program should print 50, 30 and 23.
"""

from tester import *

# Time: O(arr*large)
# Space: O(large)
def klarge(arr, large):
    if large < 1: raise TypeError('large argument must be greater than 1')

    largest = set()
    for i in arr:
        if len(largest) < large:
            largest.add(i)

        if i > max(largest):
            largest.remove(min(largest))
            largest.add(i)
    return largest


# Time: O(n log n)
# Space: O(n)
def klarge(arr, large):
    if large < 1: raise TypeError('large argument must be greater than 1')

    arr.sort()
    return set(arr[-large:])


# Time: O(n log n)
# Space:
def klarge(arr, large):
    if large < 1: raise TypeError('large argument must be greater than 1')


    

    return set(arr[-large:])



@test
def test_empty():
    assert klarge([], 1) == set(), 'Output should have been None.'

@test
def test_negative():
    try:
        klarge([1, 2, 3], -1)
        assert 0, 'Should have thrown error'
    except TypeError:
        pass

@test
def test_one():
    assert klarge([1], 1) == {1}
    assert klarge([10000], 1) == {10000}

@test
def test_many():
    assert klarge([1, 2, 3, 4, 5, 6, 7, 8], 3) == {6, 7, 8}





if __name__ == '__main__':
    run_tests()

