"""
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:
13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
"""
# Function to apply the Collatz Function to an integer n.
def collatz_function(n):
    chain = []
    while n > 1:
        if n % 2 == 0: # if n is even
            n = n//2 
            chain.append(n)
        else: 
            n = 3 * n + 1
            chain.append(n)
    
    return chain

# Function to iterate Collatz Function chains until the longest is found from 2 to a given limit.
def find_longest_chain(limit):
    longest_chain = []
    lc_integer = 0
    for x in range (2, limit):
        tmp_arr = collatz_function(x)
        if len(tmp_arr) > len(longest_chain):
            longest_chain = tmp_arr
            lc_integer = x
    
    return lc_integer, longest_chain, len(longest_chain)

if __name__ == "__main__":
    print(find_longest_chain(1000000))