"""
Amicable Numbers:
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.
Evaluate the sum of all the amicable numbers under 10000.
"""
# Fucntion get the proper divisors for a given number n. Returns a list of the divisors.
def get_proper_divisors(n):
    divisors = []
    for x in range(1, n):
        if n % x == 0:
            divisors.append(x)
    
    return divisors 

# Returns the sum of a list of integers.
def sum_list(n):
    sum_list = 0
    for x in n:
        sum_list += x

    return sum_list

# Computes the sum of amicable numbers in a given range.
def compute_amicable_sums(start, end):
    amicables = []
    for x in range(start, end):
        amicables.append(sum_list(get_proper_divisors(x)))
    
    return sum_list(amicables)

if __name__ == "__main__":
    print("The sum of all amicable numbers between 1 and 10000 are: " + str(compute_amicable_sums(1,10000)))