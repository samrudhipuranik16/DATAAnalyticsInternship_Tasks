# Problem: Sherlock and the Valid String
# HackerRank: https://www.hackerrank.com/challenges/sherlock-and-the-valid-string/problem
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'isValid' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

from collections import Counter

def isValid(s):
    char_counts = Counter(s)
    freq_counts = Counter(char_counts.values())
    
    if len(freq_counts) == 1:
        return "YES"
        
    if len(freq_counts) == 2:
        items = list(freq_counts.items())
        f1, c1 = items[0]
        f2, c2 = items[1]
        
        if f1 > f2:
            f1, f2 = f2, f1
            c1, c2 = c2, c1
            
        if f1 == 1 and c1 == 1:
            return "YES"
            
        if f2 - f1 == 1 and c2 == 1:
            return "YES"
            
    return "NO"
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()
