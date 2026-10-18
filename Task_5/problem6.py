# Problem Name: Introduction to Sets
# HackerRank Link: https://www.hackerrank.com/challenges/py-introduction-to-sets/problem

def average(array):
    set1 = set(array)
    sum1 = sum(set1)
    heightN = len(set1)
    avg = sum1/heightN
    return round(avg,3)
    # your code goes here

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)