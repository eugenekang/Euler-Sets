import math
"""
There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""
# Fucntion to create a pythagorean triplet from the following criteria:
#   Reference: https://www.chilimath.com/lessons/geometry-lessons/generating-pythagorean-triples/
#   Where m > n
#   a = m**2 - n**2
#   b = 2nm
#   c = n**2 + m**2
def find_pythag_triplet(m, n):
    if m > n:
        pyth_triplet = dict([
            ('a', m**2 - n**2),
            ('b', 2 * n * m),
            ('c', n**2 + m**2)
        ])
        return pyth_triplet
    else:
        return "Error: m !> n."

# Function to return values a, b, c such that all values are part of a pythagorean triplet,
#   and a + b + c = 1000
def deliver_abc_product(sum):
    triplet = {}
    product = 0
    # Added limitation to search, since none of the pythagorean triplets can have a square > 1000
    for x in range(int(math.sqrt(sum))):
        for y in range(0,x): # Check all values less than x
            tmp = find_pythag_triplet(x+1, y)
            if tmp['a'] + tmp['b'] + tmp['c'] == 1000:
                triplet = tmp
                product = tmp['a'] * tmp['b'] * tmp['c']
    return triplet, product

if __name__ == "__main__":
    print(deliver_abc_product(1000))