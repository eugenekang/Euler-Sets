from math import sqrt
from string import digits 

# Function to determine if number is prime.
# A nonprime number (n) will have at least one factor, not equal to one, which is within the range between (1, sqrt(n)). 
# Therefore a prime number will have no factors between (1, sqrt(n))
def is_prime(num):
    if num < 1: 
        return False
    elif num == 2:
        return True
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

# Function to turn a string of equal-length integers into a grid of user-specificed width. Outputs an array of arrays.
    #rawstring = the original string input
    #grid_cols = number of columns in grid
    #int_size = # of digits in integers.
def create_grid(rawstring, grid_cols, int_size):
    num_grid = ''.join(c for c in rawstring if c in digits) # strip all characters except for numerals
    grid_rows = len(num_grid)//int(int_size)//int(grid_cols)
    final_table = []
    tmp_arr = []

    # Creates arrays according to specified col size and integer length.
    for i in range (0, len(num_grid), len(num_grid)//grid_rows): #step increment is equal to a whole "row"
        for x in range (0 + i, (grid_cols * int_size) + i, int_size): #steps through the values in each "row"
            tmp_arr.append(num_grid[x] + num_grid[x + 1])
        final_table.append(tmp_arr)
        tmp_arr = []

    return final_table