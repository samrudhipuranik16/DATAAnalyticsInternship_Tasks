# Problem: Set .symmetric_difference() Operation
# HackerRank: https://www.hackerrank.com/challenges/py-set-symmetric-difference-operation/problem
n= int(input())
list1 = list(map(int, input().split()))
m = int(input())
list2 = list(map(int, input().split()))
set1 = set(list1).symmetric_difference(set(list2))
print(len(set1))
