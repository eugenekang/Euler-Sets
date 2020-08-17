"""
Find the sum of all the primes below two million.
"""

from Tools.common_tools import is_prime, generate_primes

if __name__ == "__main__":
    primes = list(generate_primes(2000000))
    print("The sum of all primes less than 2 million: " + str(sum(primes)))
