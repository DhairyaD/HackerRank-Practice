# Link: https://www.hackerrank.com/challenges/kangaroo/problem


def kangaroo(x1, v1, x2, v2):
  if x2 > x1 and v2 > v1:
    return "NO"
    
  for i in range(10001):
    x1 += v1
    x2 += v2
    if x1 == x2:
      return "YES"
      
  return "NO"

print(kangaroo(0,3,4,2))
print(kangaroo(0,2,5,3))
