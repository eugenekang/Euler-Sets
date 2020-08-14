from math import *
# Function to determine if number is prime.
def is_prime(num):
    if num < 1: 
        return False
    elif num <= 3:
        return True
    elif num % 2 == 0:
        return False
    else:
        for i in range (3,num):
            if (num % i) == 0:
                return False
        return True

# Function to generate specified number of values in Fibonacci sequence
# Ref: https://stackoverflow.com/questions/3953749/python-fibonacci-generator
def fib_gen(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a+b
    return a,b

# Function to generate prime numbers up to a specified limit. Function yields a generator list.
def generate_primes(limit):
    x = 2 # Set counter to 2
    while x < limit:
        prime = True
        for y in range(2, x):
            if x % y == 0:
                prime = False
                break
        if prime:
            yield x
        x += 1 

"""
#WHY DOES THIS WORK SO GOOD?
# Returns a list of True and False indicating whether each number is prime.
# For 0 <= i <= n, result[i] is True if i is a prime number, False otherwise.
def list_primality(n):
	# Sieve of Eratosthenes
	result = [True] * (n + 1)
	result[0] = result[1] = False
	for i in range(int(sqrt(n)) + 1):
		if result[i]:
			for j in range(i * i, len(result), i):
				result[j] = False
	return result

# Returns all the prime numbers less than or equal to n, in ascending order.
# For example: listPrimes(97) = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, ..., 83, 89, 97].
def list_primes(n):
	return [i for (i, isprime) in enumerate(list_primality(n)) if isprime]

print(list_primes(200000))
"""