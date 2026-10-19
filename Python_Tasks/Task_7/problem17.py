# Problem: Separate the Numbers
# HackerRank: https://www.hackerrank.com/challenges/separate-the-numbers/problem
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'separateNumbers' function below.
#
# The function accepts STRING s as parameter.
#

def separateNumbers(s):
    n = len(s)
    for i in range(1, n // 2 + 1):
        first_num_str = s[:i]
        current_num = int(first_num_str)
        built_str = first_num_str
        
        while len(built_str) < n:
            current_num += 1
            built_str += str(current_num)
            
        if built_str == s:
            print(f"YES {first_num_str}")
            return
            
    print("NO")
    # Write your code here

if __name__ == '__main__':
    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        separateNumbers(s)
