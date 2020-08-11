from Tools.common_tools import is_prime

"""
What is the 10 001st prime number?

NOT DONE
"""

def count_to_prime(top):
    y = 0 # Counter
    x = 0 # Counter for number of primes.
    while x < top - 1:
        y += 2
        if is_prime(y) == True:
            x += 1
    return y

if __name__ == "__main__":
    print(count_to_prime(3))
    print("done")
