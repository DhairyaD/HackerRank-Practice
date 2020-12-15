# Link: https://www.hackerrank.com/challenges/2d-array/problem


def hourglassSum(arr):
    result = []
    for y in range(0, 4):
        for x in range(0, 4):
            temp = arr[y][x] + arr[y][x+1] + arr[y][x+2] + arr[y+1][x+1] + arr[y+2][x] + arr[y+2][x+1] + arr[y+2][x+2]
            result.append(temp)
    return max(result)



print(hourglassSum(
    [[-9, -9, -9, 1, 1, 1],
     [0, -9, 0, 4, 3, 2],
     [-9, -9, -9, 1, 2, 3],
     [0, 0, 8, 6, 6, 0],
     [0, 0, 0, -2, 0, 0],
     [0, 0, 1, 2, 4, 0]]
))
