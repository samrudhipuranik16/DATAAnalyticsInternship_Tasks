# Problem 18: Lists
# HackerRank Link: https://www.hackerrank.com/challenges/python-lists/problem

if __name__ == '__main__':
    N = int(input())
    list1 = []

    for i in range(N):
        a = input().split()

        if a[0] == "insert":
            list1.insert(int(a[1]), int(a[2]))

        elif a[0] == "print":
            print(list1)

        elif a[0] == "remove":
            list1.remove(int(a[1]))

        elif a[0] == "append":
            list1.append(int(a[1]))

        elif a[0] == "sort":
            list1.sort()

        elif a[0] == "pop":
            list1.pop()

        elif a[0] == "reverse":
            list1.reverse()