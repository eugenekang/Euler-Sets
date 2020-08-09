"""
Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""
# Function to determine the sum of squares, of a series of natural numbers.
def sum_of_squares_series(start, end):
    sum = 0
    for x in range (start, end + 1):
        sum += x * x
    return sum

# Function to determine the square of a sum of a series of natural numbers. 
def square_of_sums_series(start, end):
    square = 0
    for x in range (start, end + 1):
        square += x
    square = square ** 2
    return square

if __name__ == "__main__":
    # Get difference
    print (square_of_sums_series(1,100) - sum_of_squares_series(1,100))
