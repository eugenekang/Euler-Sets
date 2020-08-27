"""
Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. 
Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.
For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. 
So, COLIN would obtain a score of 938 × 53 = 49714.
What is the total of all the name scores in the file?
"""
from Tools.common_tools import get_sum_list

# Read and clean file, return a list of sorted names.
def read_file(f):
    name_list = []
    with open(f,"r") as filestream:
        for line in filestream:
            name_list = line.replace("\"","").split(",")
    return sorted(name_list)


# Function to get the alphabetical value of a name, given a name string.
def get_alpha_value(name):
    # List to hold alphabet, zero inserted at position zero to give all alphabet characters their value. 
    alphabet = ['0','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    a_val_arr = [] # array for holding the values of the name

    for letter in list(name):
        # Find letter in alphabet, get index
        a_val_arr.append(alphabet.index(letter.lower()))

    return get_sum_list(a_val_arr)

# Function to total all name scores
def compute_total_score(f):
    names = read_file(f)
    score = []
    for name in names:
        score.append(get_alpha_value(name) * (names.index(name)  + 1))
    
    return get_sum_list(score)

if __name__ == "__main__":
    print("The total of all names scores is: " + str(compute_total_score("p022_names.txt")))