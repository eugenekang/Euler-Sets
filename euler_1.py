"""
Problem 1
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""
"""
if "multiple of 3 or 5" between 1, 1000;
then add to array

multiply all elements in array
"""

rng = 1000
num_array = []

for x in range(1, rng+1):
    if x % 3 == 0:
        num_array.append(x)
    elif x % 5 == 0:
        num_array.append(x)

result = sum(num_array)

print (result)
