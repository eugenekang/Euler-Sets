"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

NOT DONE
"""
def evenly_divisible(num):
    for i in range (1, 21):
        if num % i != 0:
            return False
    else: 
        return True

def solve():
    var = False
    i = 1
    while var == False:
        var = evenly_divisible(i)
        ++i # this doesn't work
    return i

if __name__ == "__main__":
    print(evenly_divisible(250822656000))
