# Problem: Alphabet Rangoli
# HackerRank: https://www.hackerrank.com/challenges/alphabet-rangoli/problem
import string
def print_rangoli(size):
    alphabet = string.ascii_lowercase
    width = 4 * size - 3
    lines = []
    for i in range(size):
        left = [alphabet[size - 1 - j] for j in range(i + 1)]
        row = left + left[-2::-1]
        lines.append('-'.join(row).center(width, '-'))
    print('\n'.join(lines[::-1] + lines[1:]))
if __name__ == '__main__':
    print_rangoli(int(input()))
