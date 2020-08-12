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
