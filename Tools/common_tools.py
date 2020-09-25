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

# Function to generate prime numbers
def generate_primes(limit):
    x = 1
    while x < limit:
        if (is_prime(x)) == True:
            yield x
        x += 1

# Function to create a grid from a list of integers
    #raw_input specifies the text input
    # int size specifies how many digits each integer in each row is.
def create_table(raw_input, int_size):
    final_table = []
    tmp_arr = []

    for x in range(0, len(raw_input)):
        for y in range(0, len(raw_input[x]), int_size):
            tmp_arr.append(raw_input[x][y] + raw_input[x][y+1])
        final_table.append(tmp_arr)
        tmp_arr = []

    return final_table

# Function to extract the question text of a file and clean it. 
    # var q is the question related to the relevant text in format "E#" (ie. "E10")
    # Note that if there isn't a line for EOF, then the search for fi.index(q + ": END\n") will return an error if searching for the last E# in sequence.
    # Returns a list of values with numbers grouped into rows with no non-numeric characters and no whitespace.
def extract_q_text(filename, q):
    fi = open(filename,"r").readlines() #open textfile
    cleaned_fi = [] #create array for lines

    for line in range (fi.index(q + ": START\n") + 1, fi.index(q + ": END\n")):
        cleaned_fi.append(fi[line].strip().replace(" ","")) #append lines to new array and strip non-numerics and whitespace

    return cleaned_fi

# Function to take a list of integers and return the sum of all integers in the list.
def get_sum_list(list):
    list_sum = 0
    for n in list:
        list_sum += n
    
    return list_sum

# Function get the proper divisors for a given number n. Returns a list of the divisors.
def get_proper_divisors(n):
    divisors = []
    for x in range(1, n):
        if n % x == 0:
            divisors.append(x)
    
    return divisors 