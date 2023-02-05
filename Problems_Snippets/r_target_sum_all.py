#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 29 11:35:08 2022

@author: maq
"""


def f_sum(target, coll, n, ind, arr):
    
    if ind>=n:
        if sum(arr) == target:
            print(arr)
        return
        
    arr.append(coll[ind])
    f_sum(target, coll, n, ind+1, arr)
    arr.remove(coll[ind])
    f_sum(target, coll, n, ind+1, arr)
    
    
    
arr = [10,1,2,7,6,1,5]
arr.sort()
f_sum(8,arr, 7, 0, [])
    

