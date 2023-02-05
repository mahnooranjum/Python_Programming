# -*- coding: utf-8 -*-
"""
Created on Fri Dec 30 05:12:41 2022

@author: MAQ
"""

       
def summa(target, arr, n, idx, ds):
    if target == 0:
        print(ds)
        return
    
    for i in range(idx, n):    
        if i>idx and arr[i] == arr[i-1]:
            continue
        if arr[idx]>target:
            break
        
        ds.append(arr[i])
        summa(target - arr[i], arr, n, i+1, ds)
        ds.pop()
        


arr = [10,1,2,7,6,1,5]
arr.sort()
summa(8, arr, 7, 0, [])