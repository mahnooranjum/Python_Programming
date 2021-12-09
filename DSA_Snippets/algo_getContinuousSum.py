# -*- coding: utf-8 -*-
"""
Created on Thu Dec  9 09:31:12 2021

@author: MAQ
"""

def kadanesAlgo(arr):
    max_eh = arr[0]
    max_sf = arr[0]
    for k in range(1, len(arr)):
        max_eh = max_eh + arr[k]
        if max_eh< arr[k]:
            max_eh = arr[k]
        else:
            max_sf = max_eh

    return max_sf


arr = [-1,-2,3,-4,5,7]


kadanesAlgo(arr)