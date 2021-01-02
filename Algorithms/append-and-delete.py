# https://www.hackerrank.com/challenges/append-and-delete/problem

'''
You have two strings of lowercase English letters. You can perform two types of operations on the first string:

- Append a lowercase English letter to the end of the string.
- Delete the last character of the string. Performing this operation on an empty string results in an empty string.

Given an integer, , and two strings,  and , determine whether or not you can convert  to  by performing exactly  of the above operations on . If it's possible, print Yes. Otherwise, print No.
'''
def appendAndDelete(s, t, k):
  min_length = min(len(s), len(t))
  s_len, t_len = len(s), len(t)

  if s_len + t_len < k:
    return 'Yes'

  for i in range(t_len):
    if s[:i] != t[:i]:
      min_length = i-1
      break
  
  difference = (s_len - min_length) + (t_len - min_length)

  return 'Yes' if difference <= k and difference % 2 == k % 2 else 'No'



print(appendAndDelete('hackerhappy', 'hackerrank', 9))
print(appendAndDelete('aba', 'aba', 7))
print(appendAndDelete('ashley', 'ash', 2))
