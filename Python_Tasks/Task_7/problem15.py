# Problem: Game of Thrones - I
# HackerRank: https://www.hackerrank.com/challenges/game-of-thrones/problem
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gameOfThrones' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

from collections import Counter

def gameOfThrones(s):
    counts = Counter(s)
    odd_counts = sum(1 for count in counts.values() if count % 2 != 0)
    
    if odd_counts <= 1:
        return "YES"
    else:
        return "NO"
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = gameOfThrones(s)

    fptr.write(result + '\n')

    fptr.close()
