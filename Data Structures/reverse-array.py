# Link: https://www.hackerrank.com/challenges/arrays-ds/problem


def reverseArray(a):
    result = []
    for i in range(len(a)-1, -1, -1):
        result.append(a[i])
    return result


def reverseArrayOneLine(a):
    return [a[i] for i in range(len(a)-1, -1, -1)]


def reverseArrayNoLoops(a):
    return a[::-1]


print(reverseArray([1, 2, 3, 4, 5, 6]))
print(reverseArrayOneLine([1, 2, 3, 4, 5, 6]))
print(reverseArrayNoLoops([1, 2, 3, 4, 5, 6]))
