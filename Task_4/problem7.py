# Problem 7: String Split and Join
# HackerRank Link: https://www.hackerrank.com/challenges/python-string-split-and-join/problem

def split_and_join(line):
    string = line.split(' ')
    return "-".join(string)
    # write your code here

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)