# Author: Luke Thomas
# Date: 10/19/16
# Description: Methods used in wordgen.py

def get_min_max():
    # Loop until valid input
    while(True):
        # Get the lower bound of the length of the strings
        minLength = int(input("Minimum length of words: "))
        # Get the upper bound of the length of the strings
        maxLength = int(input("Maximum length of words: "))

        # If any of the input is invalid, loop again
        if(minLength < 1 or minLength > maxLength or maxLength > 20):
            print("Invalid input, try again.")
        else:
            return [minLength, maxLength]


# Write all strings of length given to the text file indicated
def write_strings(length, txtFile):
    # Initialize an array of size i filled with 'a' characters
    word = ['a'] * length

    # Write all strings of length given to the file
    while(True):
        # Cast the list to a string and write it to the file
        txtFile.write(''.join(word) + '\n')

        # Increment the rightmost character
        word[length - 1] = chr(ord(word[length - 1]) + 1)
        handle_overflow(word, length);

        # If the last character got bumped past 'z', go to next length
        if(word[0] == chr(ord('z'))):
            break


# If a letter is past 'z', set it to 'a' and increment previous letter
def handle_overflow(word, length):
    for index in range(1, length):
        if(ord(word[length - index]) == (ord('z') + 1)):
            word[length - index] = 'a'
            word[length - index - 1] = chr(ord(word[length - index - 1]) + 1)
        else:
            return word