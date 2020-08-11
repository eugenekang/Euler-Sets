from Tools.common_tools import is_prime
"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

# Function to check if a number or a string is palindromic.
def check_palindrome(num):
    a = str(num)
    # reverse string
    b = a[::-1]
    if a == b:
        return True
    else:
        return False

# Function to retrieve the largest palindrome created from the product of two 3 digit numbers.
def largest_palindrome():
    tmp_array = []
    for x in range (100, 1000):
        for y in range (100, 1000):
            val = x * y
            if check_palindrome(val) == True:
                tmp_array.append(val)
    return sorted(tmp_array, reverse=True)[0]

if __name__ == "__main__":
    print(largest_palindrome())
