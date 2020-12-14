# Link: https://www.hackerrank.com/challenges/diagonal-difference/problem

def diagonalDifference(arr):
    left_diag, right_diag, count = 0, 0, 0

    for i in range(len(arr)):
        left_diag += arr[i][count]
        count += 1

    count = len(arr) - 1

    for i in range(len(arr)):
        right_diag += arr[i][count]
        count -= 1

    return abs(left_diag - right_diag)


# Shorter version:
# def diagonalDifferencee(arr):
#     left_diag = sum([arr[i][i]for i in range(len(arr))])
#     right_diag = sum([arr[i][len(arr)-1-i] for i in range(len(arr))])
#     return abs(left_diag - right_diag)


print(diagonalDifference([[11, 2, 4], [4, 5, 6], [10, 8, -12]]))
# print(diagonalDifferencee([[11, 2, 4], [4, 5, 6], [10, 8, -12]]))
