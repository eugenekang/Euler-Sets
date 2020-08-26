"""
Factorial Digit Sum
Find the sum of the digits in the number 100!
"""
# Simple function to produce a factorial
def factorial(n):
    fact = 1
    for x in range (1, n):
        fact *= x
    return fact

# Simple function to produce the sum of the digits in an integer.
def sum_digits_int(n):
    sum = 0
    for x in list(str(n)):
        sum += int(x)
    return sum

if __name__ == "__main__":
    print("The sum of the digits in the number 100! is: " + str(sum_digits_int(factorial(100))))