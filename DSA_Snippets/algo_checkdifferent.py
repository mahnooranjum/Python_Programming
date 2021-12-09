# -*- coding: utf-8 -*-
"""
Created on Thu Dec  9 09:31:12 2021

@author: MAQ
"""

def getdifferent(arr1, arr2):
    arr1 = set(arr1)
    arr2 = set(arr2) 
    for i,j in zip(arr1, arr2):
        if i != j:
            return i
        else:
            pass
        
    return 'matched'


arr1 = [1,2,3,4,5,7]
arr2 = [6,5,4,3,2,1]

getdifferent(arr1, arr2)