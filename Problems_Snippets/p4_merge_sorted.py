# -*- coding: utf-8 -*-
"""
Created on Sun Feb  5 20:12:36 2023

@author: MAQ
"""

def merger(arr1, arr2, n1, n2):
    
    idx1 = 0
    idx2 = 0
    
    while idx1!=n1:
        if arr1[idx1]>arr2[idx2]:
            temp = arr1[idx1]
            arr1[idx1] = arr2[idx2]
            arr2[idx2] = temp
            
            arr2.sort()
        idx1+=1
            
    
arr1 = [1,4,7,8,10]
arr2 = [2,3,9]
n1 = len(arr1)
n2 = len(arr2)

