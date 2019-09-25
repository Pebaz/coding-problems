"""
Given an array of integers, return a new array such that each element at
index i of the new array is the product of all the numbers in the original
array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be
[120, 60, 40, 30, 24].

If our input was [3, 2, 1], the expected output would be [2, 3, 6].

Follow-up: what if you can't use division?
"""

# O(n**2)
def mularray(array):
	new = [0] * len(array)
	for i in range(len(array)):
		h = 1
		for x in range(len(array)):
			if x != i:
				h *= array[x]
		new[i] = h
	return new


# O(n)
def mularray(array):
	h = 1
	for i in array:
		h *= i
	return [int(h / i) for i in array]


result = mularray([3, 2, 1])
print(result)
assert(result == [2, 3, 6])

result = mularray([1, 2, 3, 4, 5])
print(result)
assert(result == [120, 60, 40, 30, 24])

