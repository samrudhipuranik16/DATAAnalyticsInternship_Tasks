# Problem Name: Lists
# HackerRank Link: https://www.hackerrank.com/challenges/python-lists/problem

if __name__ == '__main__':
    n = int(input())
    lst = []
    for _ in range(n):
        line = input().split()
        cmd = line[0]
        if cmd == 'insert':
            lst.insert(int(line[1]), int(line[2]))
        elif cmd == 'print':
            print(lst)
        elif cmd == 'remove':
            lst.remove(int(line[1]))
        elif cmd == 'append':
            lst.append(int(line[1]))
        elif cmd == 'sort':
            lst.sort()
        elif cmd == 'pop':
            lst.pop()
        elif cmd == 'reverse':
            lst.reverse()
