# Problem: Funny String
# HackerRank: https://www.hackerrank.com/challenges/funny-string/problem
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'funnyString' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def funnyString(s):
    revS = reversed(s)
    list1 = [ord(i) for i in s]
    list2 = [ord(i) for i in revS]
    abs1 = []
    abs2 = []
    for i in range(len(list1)-1):
        abs1.append(abs(list1[i] - list1[i+1]))
    for i in range(len(list2)-1):
        abs2.append(abs(list2[i]-list2[i+1]))
    if abs1 ==abs2 :
        return 'Funny'        
    else:
        return "Not Funny"
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = funnyString(s)

        fptr.write(result + '\n')

    fptr.close()
