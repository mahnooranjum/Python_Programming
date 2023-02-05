#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 29 12:34:05 2022

@author: maq
"""
def f_sum(target, coll, n, ind, arr):
    
    if ind>=n:
        # condition satisfied
        if sum(arr) == target:
            return 1
        # condition not satisfied
        else:
            return 0
        
    # all calls counter
    arr.append(coll[ind])
    l = f_sum(target, coll, n, ind+1, arr)
    arr.remove(coll[ind])
    r = f_sum(target, coll, n, ind+1, arr)
    
    # return
    return l+r
    
    
f_sum(6, [3,2,1,3], 4, 0, [])