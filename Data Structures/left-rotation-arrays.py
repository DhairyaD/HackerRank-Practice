# Link: https://www.hackerrank.com/challenges/array-left-rotation/problem

# take the array from index 'd' till the end and concatenate with the array from the beginning to index 'd'
def rotateLeft(d, arr):
  return arr[d:] + arr[:d]

print(rotateLeft(2, [1,2,3,4,5]))
print(rotateLeft(4, [1, 2, 3, 4, 5]))
