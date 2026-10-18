# Problem 15: Word Order
# HackerRank Link: https://www.hackerrank.com/challenges/word-order/problem

# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
words = []
freq= {}            
for i in range(n):
    words.append(input().strip())
for i in words:
    freq[i]=freq.get(i,0)+1
print(len(freq))
print(*freq.values())
        