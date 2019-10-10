import math
import matplotlib.pyplot as plt

def is_prime(num):
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return num > 1

def get_primes(less_than_num):
    return [i for i in range(2, less_than_num) if is_prime(i)]

def find_gaps(nums):
    return [(nums[i] - nums[i - 1]) - 1 for i in range(1, len(nums))]

count = 1000
slice = count
primes = get_primes(count)
gaps = find_gaps(primes)
plt.plot(gaps[-slice:], color='#FFC800')
plt.legend(['Prime Gap'])
plt.xticks(range(len(gaps[-slice:])), primes[-slice:])
plt.xlabel('Prime Number')
plt.ylabel('Gap')
plt.show()
