# Link: https://www.hackerrank.com/challenges/breaking-best-and-worst-records/problem

def breakingRecords(scores):
  min_count = max_count = 0
  min_value = max_value = scores[0]

  for score in scores[1:]:
    if score < min_value:
      min_value = score
      min_count += 1
    if score > max_value:
      max_value = score
      max_count += 1
  
  return max_count, min_count

print(breakingRecords([10,5,20,20,4,5,2,25,1]))



