# Problem 6: Find the Runner-Up Score!
# HackerRank Link: https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    list1 = list(sorted(set(arr)))
    print(list1[-2])