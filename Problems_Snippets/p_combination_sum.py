# -*- coding: utf-8 -*-
"""
Created on Fri Dec 30 04:25:42 2022

@author: MAQ
"""

def summa(target, arr, n, idx, ds):
    
    if target==0:
        print(ds)
        return
    if idx>=n or target<0:
        return
    
    if arr[idx]<=target:
        ds.append(arr[idx])
        summa(target-arr[idx], arr, n, idx, ds)
        ds.remove(arr[idx])
        
    summa(target, arr, n, idx+1, ds)
        
        
    


summa(7, [2,3,5,7], 4, 0, [])