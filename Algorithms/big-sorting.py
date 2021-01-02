# Link: https://www.hackerrank.com/challenges/big-sorting/problem

'''
Consider an array of numeric strings where each string is a positive number with anywhere from  to  digits. Sort the array's elements in non-decreasing, or ascending order of their integer values and return the sorted array.

Function Description

Complete the bigSorting function in the editor below.

bigSorting has the following parameter(s):

string unsorted[n]: an unsorted array of integers as strings
Returns

string[n]: the array sorted in numerical order

Input Format

The first line contains an integer, , denoting the number of strings in .
Each of the  subsequent lines contains an integer string .

Constraints

Each string is guaranteed to represent a positive integer without leading zeros.
The total number of digits across all strings in  is between  and  (inclusive).
'''


def bigSorting(unsorted):
  unsorted.sort(key=int)
  return unsorted
  # temp = sorted([int(num) for num in unsorted])
  # return [str(num) for num in sorted([int(num) for num in unsorted])]

print(bigSorting(['31415926535897932384626433832795', '1', '3', '10', '3', '5']))
