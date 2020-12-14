# Link: https://www.hackerrank.com/challenges/staircase/problem

def staircase(n):
    for i in range(n):
        print(' ' * (n-i-1) + ('#' * (i + 1)))


print(staircase(4))
