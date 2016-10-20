#!/usr/bin/env python3

# Author: Luke Thomas
# Date: 10/19/16
# Description:

import sys
import wordgenmethods as m

# Create file called 'words.txt' where this file is located
txtFile = open('./words.txt', 'w');

min_max = m.get_min_max();
minLength = min_max[0];
maxLength = min_max[1];

# For strings of lengths minLength to maxLength
for i in range(minLength, maxLength + 1):
    print("Generating strings of length", i)
    m.write_strings(i, txtFile);

# Close the opened file
txtFile.close()

print("Finished generating words.")
input("Press any key to exit.")