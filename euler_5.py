"""
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20? # Find the factors?
"""
from Tools.common_tools import generate_primes

# Function to compute the smallest positive integer evenly divisible by all numbers from 1 - 20.
def solve(max):
    # Generate primes between 1 and 20. 
    # All nonprimes have prime numbers as their factors, by transivity then we can only use prime numbers between 1 and 20, and all the non primes in that range should also be factors. 
    array = list(generate_primes(max))

    # Create upper limit to search within, from product of all prime factors.
    limit = 1
    for x in array:
        limit *= x

    # Determine the smallest positive number that has all primes as a factor. 
    for x in range (array[-1], limit + 1):
        is_factor = True
        for prime in array:
            if x % prime != 0:
                is_factor = False
        if is_factor == True:
            return x       

if __name__ == "__main__":
    print("The smallest positive number that is evenly divislbe by all natural numbers in range (1,20) is: " + str(solve(20)))