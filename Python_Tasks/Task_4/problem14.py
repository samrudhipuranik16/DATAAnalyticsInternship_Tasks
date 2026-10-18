# Problem 14: Set .add()
# HackerRank Link: https://www.hackerrank.com/challenges/py-set-add/problem

# Enter your code here. Read input from STDIN. Print output to STDOUT
n= int(input())
country=set()
for i in range(n):
    country.add(input().strip())
print(len(country))    
