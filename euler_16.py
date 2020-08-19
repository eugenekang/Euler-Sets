"""
2**15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
What is the sum of the digits of the number 2^1000?
"""

def sum_of_digits(n):
    sum = 0 
    num_array = list(str(n))
    for x in num_array:
        sum += int(x)
    return sum

if __name__ == "__main__":
    print("The sum of the digits of the number 2^1000 is: " + str(sum_of_digits(2**1000)))