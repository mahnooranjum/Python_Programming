#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(ar):
    # Write your code here
    ar = [item for sublist in ar for item in sublist]
    pivot = int(math.sqrt(len(ar)))
    count = 0
    rsum = 0
    lsum = 0
    for i in range(pivot):
        rsum = rsum + ar[(pivot*i) + i]
        lsum = lsum + ar[pivot -1 + pivot*i - i]
    return abs(rsum - lsum)
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
