# -*- coding: utf-8 -*-
"""
Created on Thu Dec  9 09:31:12 2021

@author: MAQ
"""

def getdifferent(arr1, arr2):
    arr1.sort()
    arr2.sort()
    for i in range(len(arr1)):
        if arr1[i] != arr2[i]:
            return arr1[i]
        else:
            pass
        
    return 'matched'


arr1 = [1,2,3,4,5,7]
arr2 = [6,5,4,3,2,1]

getdifferent(arr1, arr2)