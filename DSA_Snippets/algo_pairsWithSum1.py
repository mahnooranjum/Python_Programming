
import math

def getPairsCount(arr, n, summa):
  dicto = {}
  count = 0
  for i in range(n):
      if summa - arr[i] in dicto:
          dicto[summa - arr[i]] += 1
      else:
          dicto[summa - arr[i]] = 1
  for i in range(n):
      if arr[i] in dicto:
          count += 1
      else:
          pass
 
  return math.ceil(count/2)
 
arr = [2,2,3,1]
n = len(arr)
summa = 4
getPairsCount(arr, n, summa)