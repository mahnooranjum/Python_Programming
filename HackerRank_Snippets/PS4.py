# -*- coding: utf-8 -*-
"""


@author: MAQ
"""




def plusMinus(arr):
    # Write your code here
    temp = [x for x in arr if x > 0]
    temp = abs(len(temp)/len(arr))
    print(f'{temp:.6f}')
    temp = [x for x in arr if x == 0]
    temp = abs(len(temp)/len(arr))
    print(f'{temp:.6f}')
    temp = [x for x in arr if x < 0]
    temp = abs(len(temp)/len(arr))
    print(f'{temp:.6f}')


arr = [-4, 3, -9, 0, 4, 1]
plusMinus(arr)