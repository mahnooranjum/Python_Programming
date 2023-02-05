# -*- coding: utf-8 -*-
"""
Created on Thu Dec 29 03:47:57 2022

@author: MAQ
"""

def printer(ind, arr, n, placeholder):
    
    if (ind>=n):
        print(placeholder)
        return
    
    placeholder.append(arr[ind])
    printer(ind+1, arr, n, placeholder)
    placeholder.remove(arr[ind])
    printer(ind+1, arr, n, placeholder)
    
printer(0, [3,2,1], 3, [])
    