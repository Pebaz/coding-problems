"""
This problem was asked by Palantir.

Write a program that checks whether an integer is a palindrome. For example,
121 is a palindrome, as well as 888. 678 is not a palindrome. Do not convert
the integer into a string.
"""

# This solution is O(N * 1.5)

def get_digits(num):
	digits = []
	while num >= 10:
		digits.append(num - (num // 10) * 10)
		num //= 10
	return digits + [num]

def is_palindrome(num):
	digits = get_digits(num)
	for i in range(len(digits) // 2):
		front = digits[i]
		back = digits[len(digits) - i - 1]
		if front != back:
			return False
	return True


if __name__ == '__main__':
	assert is_palindrome(1001)
	# assert is_palindrome(101)
	# assert not is_palindrome(1012)
	# assert is_palindrome(45654)
