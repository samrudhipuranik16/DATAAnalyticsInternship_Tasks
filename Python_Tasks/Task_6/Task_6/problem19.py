# Problem 19: Company Logo
# HackerRank: https://www.hackerrank.com/challenges/most-commons/problem

#!/bin/python3

import math
import os
import random
import re
import sys




from collections import Counter

if __name__ == '__main__':
    s = input()

    counts = Counter(s)

    result = sorted(counts.items(), key=lambda item: (-item[1], item[0]))

    for char, count in result[:3]:
        print(char, count)
