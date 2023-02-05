# -*- coding: utf-8 -*-
"""
Created on Sat Feb  4 17:12:40 2023

@author: MAQ
"""


def sort012(arr, n):
    p0 = 0
    p2 = n - 1
    p1 = 0

    while p1 <= p2:
        if arr[p1] == 0:
            arr[p0], arr[p1] = arr[p1], arr[p0]
            p0 = p0 + 1
            p1 = p1 + 1
        elif arr[p1] == 1:
            p1 = p1 + 1
        else:
            arr[p1], arr[p2] = arr[p2], arr[p1]
            p2 = p2 - 1
    return arr
            
arr = [1,0,1, 0,1,0,2,2, 0]
n = len(arr)
sort012(arr,n)