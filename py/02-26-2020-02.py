# Bubble sort

import random

class Person:
    def __init__(self):
        self.age = random.randrange(0, 100)
    def __gt__(self, other):
        return self.age > other.age
    def __lt__(self, other):
        return self.age < other.age
    def __ge__(self, other):
        return self.age >= other.age
    def __le__(self, other):
        return self.age <= other.age
    def __repr__(self):
        return str(self.age)


def bubble(arr):
    sort = True
    while sort:
        sort = False
        for i in range(len(arr) - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                sort = True

def selection(arr):
    start = 0
    while start < len(arr):
        for i in range(start, len(arr)):
            if arr[i] < arr[start]:
                arr[i], arr[start] = arr[start], arr[i]
        start += 1

def merge(arr):
    def mergesort(arr, helper, low, hi):
        if low < hi:
            mid = (low + hi) // 2
            mergesort(arr, helper, low, mid)  # Sort left half
            mergesort(arr, helper, mid + 1, hi)  # Sort right half
            merge_them(arr, helper, low, mid, hi)     # Merge them

    def merge_them(arr, helper, low, mid, hi):
        # Copy both halves into a helper array
        for i in range(low, hi):
            helper[i] = arr[i]
        
        left = low
        right = mid + 1
        current = low

        while left <= mid and right <= hi:
            if helper[left] <= helper[right]:
                arr[current] = helper[left]
                left += 1
            else:  # Right element is smaller than left element
                arr[current] = helper[right]
                right += 1
            current += 1
        
        # Copy rest of left into target array
        remain = mid - left
        for i in range(remain):
            arr[current + i] = helper[left + i]

    helper = [None] * len(arr)
    mergesort(arr, helper, 0, len(arr) - 1)


if __name__ == '__main__':
    people = [Person() for _ in range(8)]
    print('Unsorted:'.rjust(12), people)
    #bubble(people)
    #selection(people)
    merge(people)
    print('Sorted:'.rjust(12), people)
