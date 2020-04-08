#!/bin/python3

import math
import os
import random
import re
import sys


# What is the real problem?

# Go over it once (because the first time doens't matter)
# Then sort the array and focus on the big ones only

# I think the problem is negative numbers

"""
To get the minimum sum:

1. Sort the array first (this will matter with both huge and small K)
2. Divide each index by 2 (stop dividing if you reach negative numbers)
3. Negative numbers help the sum at the end
4. Find the index of the first negative number (or zero)
5. Only work on the positive part of the array
6. Sum the negatives first (add them later)
7. Perform the operations on the positive portion of the array
"""

def minSum(num, k):
    if len(num) == 1:
        (c,) = num
        for _ in range(k):
            c = c // 2 + (1 if c % 2 != 0 else 0)
        return c

    num.sort(reverse=True)
    if k > len(num):
        num = sorted([i // 2 + (1 if (i % 2 != 0) else 0) for i in num], reverse=True)
        ops = k - len(num)
    else:
        ops = k

    index = 0
    while ops:
        ops -= 1
        num[index] = num[index] // 2 + (1 if (num[index] % 2 != 0) else 0)

        if index == len(num) - 1:
            index = 0

        if num[index] <= 0:
            index = 0

        if num[index] <= num[index + 1]:
            index += 1

    return sum(num)


[200, 50, 50, 25, 25, 10, 10]
[50, 50, 50, 25, 25, 10, 10]
[25, 25, 25, 25, 25, 10, 10]

def minSum(num, k):
    # Make sure larger numbers are closer to the start and negatives at the end
    num.sort(reverse=True)

    # Find the start of the negative numbers (or zero)
    end_index = len(num) - 1
    for ind, el in enumerate(num):
        if el <= 0:
            end_index = ind
            break

    '''
    for kk in range(k):
        # Constrain index to only process the positive numbers in the array
        index = (kk % end_index) if end_index else 0

        # Determine adjustment for ceiling calculation
        part = 0 if num[index] % 2 == 0 else 1

        # Divide by 2 with ceiling
        num[index] = num[index] // 2 + part
    '''

    index = 0
    lowest = num[index]
    while k:
        k -= 1

        # Determine adjustment for ceiling calculation
        part = 0 if num[index] % 2 == 0 else 1

        # Divide by 2 with ceiling
        num[index] = num[index] // 2 + part

        if index >= end_index:
            index = 0
            continue

        

        if index < end_index:
            if num[index] <= lowest:
                index += 1
            else:
                pass
        else:
            if num[index] <= lowest:
                index += 1
            else:
                pass

        if index < end_index and num[index] <= lowest:
            index += 1
            lowest = num[index + 1] if index < end_index else num[end_index]
        else:
            index = 0
            lowest = num[end_index] if index == end_index else num[index + 1]
    
    return sum(num)



def minSum(num, k):
    # Exit early:
    if len(num) == 1 or num[1] <= 0:
        for _ in range(k):
            num[0] = num[0] // 2 + (1 if num[0] % 2 != 0 else 0)
        return sum(num)

    # Make sure larger numbers are closer to the start and negatives at the end
    num.sort(reverse=True)

    # Find the start of the negative numbers (or zero)
    end_index = len(num) - 1
    for ind, el in enumerate(num):
        if el <= 0:
            end_index = ind
            break

    #the_nums = num[:end_index]

    index = 0
    while k:
        k -= 1  # Should I do one more iteration after the while loop??????

        #import ipdb; ipdb.set_trace()

        # Divide by 2 with ceiling
        pre = 0 + num[index]
        num[index] = num[index] // 2 + (0 if num[index] % 2 == 0 else 1)

        if index < end_index:
            if pre == num[index + 1]:
                continue

        # If RIGHT and LEFT exist, compare them to each other
        if index < end_index and index > 0:
            right = num[index + 1]
            left = num[index - 1]
            if left > right:
                index -= 1
            elif right > left:
                index += 1
            elif right > num[index]:
                index += 1
            elif left > num[index]:
                index -= 1

        elif index < end_index:
            right = num[index + 1]
            if right > num[index]:
                index += 1

        elif index > 0:
            left = num[index - 1]
            if left > num[index]:
                index -= 1

        else:
            raise Exception('Should never get here.')
    
    return sum(num)


import heapq

def minSum(num, k):
    """
    Gets the minimum sum of an array after `k` halving operations are applied.

    Args:
        num(list): the array of numbers to work with.
        k(int): the number of times that elements in the array should be halved.

    Returns:
        The sum of the array after halving the largest element in the array `k`
        times. Note that the largest element may no longer be an item that has
        just been halved.
    """

    # Since heapq doesn't provide a max-heap, we have to negate all values to
    # emulate a max-heap's functionality.
    heap = list(map(lambda x: -x, num))
    heapq.heapify(heap)

    # Now remove each largest element, divide it by 2, and add it again
    for _ in range(k):

        # Since each element is negated when added, negate here to undo that
        element = -heapq.heappop(heap)

        # Divide by 2 with ceiling
        element = element // 2 + (1 if element % 2 != 0 else 0)

        # Make sure to keep negating each element to emulate a max-heap
        heapq.heappush(heap, -element)

    # Inverting the sum is equal to inverting each element then summing
    return -sum(heap)


if __name__ == '__main__':
    data = [int(i.strip()) for i in open('capital_one_input1.txt').readlines()]
    data.pop(0)
    k = data.pop()

    # Originally getting: 312266715
    s = minSum(data, k)
    t = 16716000
    print(s, '==', t, 'difference:', s - t)
    print(s)
    print(t)

    s = minSum([10, 20, 7], 4)
    t = 14
    print(s)
    print(t)

    s = minSum([10, -1, -2, -3], 4)
    t = -5
    print(s)
    print(t)

    s = minSum([10, 20], 4)
    t = 8
    print(s)
    print(t)

    s = minSum([-10, -20], 4)
    t = 8
    print(s)
    print(t)
