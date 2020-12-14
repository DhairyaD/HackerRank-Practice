# Link: https://www.hackerrank.com/challenges/mini-max-sum/problem


def miniMaxSum(arr):
    arr_sorted = sorted(arr)
    print(sum(arr_sorted[:4]), sum(arr_sorted[1:]))


print(miniMaxSum([1, 3, 5, 7, 9]))
