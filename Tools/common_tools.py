# Function to determine if number is prime.
def is_prime(num):
    tmp_prime = None
    if num > 1:
        for i in range (2,num):
            if (num % i) == 0:
                tmp_prime = False
        if tmp_prime == None:
            tmp_prime = True
    return tmp_prime

# Function to generate specified number of values in  Fibonacci sequence
# Ref: https://stackoverflow.com/questions/3953749/python-fibonacci-generator
def fib_gen(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a+b
    return a,b