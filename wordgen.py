#!/usr/bin/env python3

import sys

# Create file called 'words.txt' where this file is located
txtFile = open('./words.txt', 'w');

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
        break

# For strings of lengths minLength to maxLength
for i in range(minLength, maxLength + 1):
    print("Generating strings of length", i)

    # Initialize an array of size i filled with 'a' characters
    word = ['a'] * i

    # Write all strings of length i to the file
    while(True):
        # Cast the list to a string and write it to the file
        #txtFile.write(''.join(word))
        txtFile.write(''.join(word) + '\n')

        # Increment the rightmost character
        word[i - 1] = chr(ord(word[i - 1]) + 1)

        # Handle the changing of the characters sequentially
        for j in range(1, i):
            if(ord(word[i - j]) == (ord('z') + 1)):
                word[i - j] = 'a'
                word[i - j - 1] = chr(ord(word[i - j - 1]) + 1)
            else:
                break

        # If the last character got bumped past 'z', go to next length
        if(word[0] == chr(ord('z') + 1)):
            break

# Close the opened file
txtFile.close()

print("Finished generating words.")