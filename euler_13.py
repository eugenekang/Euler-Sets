"""
Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.
"""

from Tools.common_tools import extract_q_text

if __name__ == "__main__":
    table = extract_q_text("raw_input.txt","E13")
    sum = 0
    for row in table:
        sum += int(row)
    print("The value of the sum of all 100 numbers is: " + str(sum))
    print("The first ten digits of the sum are: " + str(sum)[0:10])