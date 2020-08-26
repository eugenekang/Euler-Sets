"""
Maximum Path Sum I

From a triangle of numbers, taking an adjacent route from top to bottom, find the maximum total value. 
"""
from string import digits
from Tools.common_tools import extract_q_text, create_table

# Function to find the max value path of a number triangle.
    # var tri is a tabular representation of the triangle. 
def tri_find_max(tri):
    for row in range(len(tri)-1,0,-1): #iterate through list in reverse, stop one short of "top " of pyramid
        for x in range(0, len(tri[row]) - 1): #iterate through each row of the pyramid, skipping the last element.
            if tri[row][x] > tri[row][x+1]: #if statement to compare two adjacent integers and take the highest.
                tri[row-1][x] = int(tri[row][x]) + int(tri[row-1][x]) # sum highest w the value one row up.
            else:
                tri[row-1][x] = int(tri[row][x+1]) + int(tri[row-1][x])

    return tri[0][0] #Final result will be at the "top" of the pyramid.

if __name__ == "__main__":
    # Create a tabular representation of the triangle.
    tri = create_table(extract_q_text("raw_input.txt", "E18"), 2)

    print("The max value is: " + str(tri_find_max(tri)))
