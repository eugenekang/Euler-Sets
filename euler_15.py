"""
Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.
How many such routes are there through a 20×20 grid?

Considering the references, there is no reason to create the 20x20 grid, instead we will use the binomial coefficient to determine the number of paths through a 20x20 grid.

References:
    Counting Lattice Paths: http://www.robertdickau.com/lattices.html
    Binomial Coefficient/Shortest Path Diagrams: http://www.robertdickau.com/manhattan.html
"""

from math import factorial

def binomial_coefficient(n):
    return factorial(2 * n)//factorial(n) ** 2

if __name__ == "__main__":
    print("The number of paths through a 20x20 grid is: " + str(binomial_coefficient(20)))