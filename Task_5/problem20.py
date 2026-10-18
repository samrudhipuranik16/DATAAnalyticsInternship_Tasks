# Problem Name: Piling Up!
# HackerRank Link: https://www.hackerrank.com/challenges/piling-up/problem

from collections import deque

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        blocks = deque(map(int, input().split()))
        can_pile = True
        current_max = float('inf')
        while blocks:
            left = blocks[0]
            right = blocks[-1]
            if left >= right:
                if left <= current_max:
                    current_max = left
                    blocks.popleft()
                else:
                    can_pile = False
                    break
            else:
                if right <= current_max:
                    current_max = right
                    blocks.pop()
                else:
                    can_pile = False
                    break
        print("Yes" if can_pile else "No")
