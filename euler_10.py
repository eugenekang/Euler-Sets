from Tools.common_tools import is_prime
"""
Find the sum of all the primes below two million.

Currently very slow if the start value is greater than 20000
"""
def generate_primes_in_range(start, end):
    primes = []
    primes_in_range = []

    while is_prime(start) == False:
        start = start + 1

    # build a list of primes
    for x in range(start):
        if is_prime(x) == True:
            primes.append(x)

    # generate primes
    for y in range(start, end):
        flag = True
        for prime in primes:
            if y % prime == 0:
                flag = False
                break
        if flag == True:
            primes.append(y)
            primes_in_range.append(y)

    return primes_in_range

# Function to return the answer required.
def solve(start, end):
    prime_list = generate_primes_in_range(start, end)
    comb_sum = 0
    for prime in prime_list:
        comb_sum += prime
    return comb_sum

if __name__ == "__main__":
    print(solve(4,2000000))