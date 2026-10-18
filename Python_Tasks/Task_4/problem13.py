# Problem 13: Symmetric Difference
# HackerRank Link: https://www.hackerrank.com/challenges/symmetric-difference/problem

# Enter your code here. Read input from STDIN. Print output to STDOUT
m= int(input())
set1 = set(map(int, input().split()))
n= int(input())
set2 = set(map(int, input().split()))
set1.symmetric_difference_update(set2)
set2 = sorted(set1)
for i in set2:
    print(i)