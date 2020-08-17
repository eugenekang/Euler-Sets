from math import *
# Function to determine if number is prime.
# A nonprime number (n) will have at least one factor, not equal to one, which is within the range between (1, sqrt(n)). 
# Therefore a prime number will have no factors between (1, sqrt(n))
def is_prime(num):
    if num < 1: 
        return False
    elif num % 2 == 0:
        return False
    else:
        for i in range (2,int(sqrt(num)) + 1): # Include square root of num in range bc perfect squares exist and are nonprime
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

#
def generate_primes(limit):
    x = 1
    while x < limit:
        if (is_prime(x)) == True:
            yield x
        x += 1
