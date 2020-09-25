"""
What is the index of the first term in the Fibonacci sequence to contain 1000 digits?
"""

def compute(limit):
    fib_seq = []
    # Generate a fibonacci sequence, store it in an array with append.
    a = 0
    b = 1
    while len(str(a)) < limit:
        fib_seq.append(b)
        a,b = b,a+b

    # check if most recent number generated is len(x) == 1000
        #if so, return that number, and the index of that number in the sequence.
    return a, fib_seq.index(a)

if __name__ == "__main__":
    print(compute(1000))
