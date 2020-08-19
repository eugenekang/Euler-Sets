"""
Number letter counts
If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used? 
NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.
"""
ones = {
        1:'one',
        2:'two',
        3:'three',
        4:'four',
        5:'five',
        6:'six',
        7:'seven',
        8:'eight',
        9:'nine',
        0:''
    }
teens = {
        0:'ten',
        1:'eleven',
        2:'twelve',
        3:'thirteen',
        4:'fourteen',
        5:'fifteen',
        6:'sixteen',
        7:'seventeen',
        8:'eighteen',
        9:'nineteen'
    }

tens = {
        2:'twenty',
        3:'thirty',
        4:'forty',
        5:'fifty',
        6:'sixty',
        7:'seventy',
        8:'eighty',
        9:'ninety',
        0:''
    }

# Function that turns an integer into the written, English equivalent of that number, up to 9999.
    # Returns the English spelling of the word, without spaces or punctuation.
def integer_to_word(n):
    num_word = []
    num_list =  list(reversed(str(n)))
    placeholders = ['ones','tens','hundreds','thousands']
    num_dict = dict(zip(placeholders, num_list))

    for key in num_dict:
        if key == "ones":
            num_word.append(ones[int(num_dict[key])])
        if key == "tens":
            if int(num_dict[key]) == 1:
                num_word.pop()
                num_word.append(teens[int(num_dict['ones'])])
            else:
                num_word.append(tens[int(num_dict[key])])
        if key == "hundreds":
            if int(num_dict['hundreds']) == 0: #Should not register any characters if the hundreds col is empty
                num_word.append("")
            elif int(num_dict['ones']) == 0 and int(num_dict['tens']) == 0: # Should not include 'and' if there are zeroes in the tens and ones col.
                num_word.append(ones[int(num_dict[key])] + "hundred")
            else:
                num_word.append(ones[int(num_dict[key])] + "hundredand")
        if key == "thousands":
            
                num_word.append(ones[int(num_dict[key])] + "thousand")
    
    num_word = ''.join(list(reversed(num_word))) # Revert English word back to regular orientation for readability

    return num_word

# Function to get the sum of all total letters in the english spelling of the names of all positive integers from 0 to the limit specified.
    #Returns an int sum
def compute(limit):
    num_sum = 0
    for x in range(0, limit + 1):
        num_sum += len(integer_to_word(x)) # Get sums of lengths of all words
   
    return num_sum

if __name__ == "__main__":
    print("The sum of all letters in every number up until 1000 is: " + str(compute(1000)))
