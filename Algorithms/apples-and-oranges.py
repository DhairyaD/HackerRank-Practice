# Link: https://www.hackerrank.com/challenges/apple-and-orange/problem

def countApplesAndOranges(s, t, a, b, apples, oranges):
  count_apples = sum([1 for apple in apples if a + apple in range(s, t+1)])
  count_oranges = sum([1 for orange in oranges if b + orange in range(s, t+1)])
  print(count_apples)
  print(count_oranges)


print(countApplesAndOranges(7, 10, 4, 12, [2,3,-4], [3,-2,-4]))
