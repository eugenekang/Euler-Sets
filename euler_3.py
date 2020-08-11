"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

"""
So every integer greater than 1 is comprised of a product of prime numbers.
For example: 150 / 2 = 125
    125 / 5 = 25
    25 / 5 = 5 
So 150 is comprised of the prime factors: 5, 5, 5, 2. 
So this stands to reason that if we take the smallest prime factor of a large number and repeatedly factorize the number of times the other factor, 
we will have a list of all of the prime factors that result from the original number, which we can then order from lowest to highest. 
"""
# Function to return the smallest prime factor
def smallest_prime_factor(num):
    for i in range (2, num):
        if (num % i) == 0:
            return i

# Function returns all prime factors of given number (num)
def all_prime_factors(num):
    target = num
    pf_array = []
    while target > 0:
        pf = smallest_prime_factor(target)
        if pf != None:
            pf_array.append(pf)
            target = target // pf
        else:
            pf_array.append(target)
            break
    return pf_array

if __name__ == "__main__":
    print(sorted(all_prime_factors(600851475143), reverse=True)[0])
