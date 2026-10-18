# Problem Name: Merge the Tools!
# HackerRank Link: https://www.hackerrank.com/challenges/merge-the-tools/problem

from collections import OrderedDict

def merge_the_tools(string, k):
    for i in range(0, len(string), k):
        segment = string[i:i+k]
        seen = OrderedDict()
        for c in segment:
            seen[c] = None
        print(''.join(seen.keys()))

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
