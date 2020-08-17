"""
What is the value of the first triangle number to have over five hundred divisors?
"""

def make_tri_num(pos):
    tri_num = 0
    for x in range(1, pos + 1):
        tri_num += x
    
    return tri_num

def get_factors(num):
    target = num
    factors = [1]
    for x in range (2, target + 1): #Range is set so that it will count up to the final number.
        if target % x == 0:
            factors.append(x)

    return factors        

if __name__ == "__main__":
    factors = []
    x = 1
    while len(factors) < 50:
        x += 1
        factors = get_factors(make_tri_num(x))

    print("The value: " + str(make_tri_num(x)) + " has the following factors: ")
    print(factors)