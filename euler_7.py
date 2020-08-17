"""
What is the 10 001st prime number?
"""
from Tools.common_tools import is_prime

# Function to count to the nth prime, specifying the limit as the nth prime to count to.
# Does not count 1 as a prime number. 
def count_to_nth_prime(limit):
    num_primes = 0 
    y = 1 # ctr
    while num_primes < limit:
        y += 2
        if is_prime(y) == True:
            num_primes += 1
    return y

if __name__ == "__main__":
    print(count_to_nth_prime(10001))
