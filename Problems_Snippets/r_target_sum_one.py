#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 29 12:20:13 2022

@author: maq
"""
def f_sum(target, coll, n, ind, arr):
    
    if ind>=n:
        # condition true
        if sum(arr) == target:
            print(arr)
            return True
        # condition false
        else:
            return False
        
    arr.append(coll[ind])
    
    # avoid future recursion calls
    if(f_sum(target, coll, n, ind+1, arr)==True):
        return True
    
    arr.remove(coll[ind])
    
    # avoid future recursion calls
    if(f_sum(target, coll, n, ind+1, arr)==True):
        return True
    
    return False
    
f_sum(6, [3,3,2,2,2,1,5], 7, 0, [])
    