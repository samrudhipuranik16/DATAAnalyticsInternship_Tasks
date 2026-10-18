# Problem Name: Word Order
# HackerRank Link: https://www.hackerrank.com/challenges/word-order/problem

from collections import OrderedDict

if __name__ == '__main__':
    n = int(input())
    d = OrderedDict()
    for _ in range(n):
        word = input()
        d[word] = d.get(word, 0) + 1
    print(len(d))
    print(*d.values())
