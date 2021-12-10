# -*- coding: utf-8 -*-
"""
Created on Fri Dec 10 19:00:23 2021

@author: MAQ
"""

L1 = ['A', 'B', 'C']
L2 = ['A', 'C', 'D']

def getsame(arr1, arr2):
    arr1 = set(arr1)
    arr2 = set(arr2) 
    lister = []
    for i,j in zip(arr1, arr2):
        if i == j:
            lister.append(i)
        else:
            pass
        
    return lister


getsame(L1, L2)