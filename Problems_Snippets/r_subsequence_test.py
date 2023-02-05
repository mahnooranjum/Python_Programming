#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 29 10:22:17 2022

@author: maq
"""



def f_seq(coll, n, ind, arr):
    
    if ind>=n:
        print(arr)
        return
        
    
    arr.append(coll[ind])
    f_seq(coll, n, ind+1, arr)
    arr.remove(coll[ind])
    f_seq(coll, n, ind+1, arr)
    

def f_seq1(coll, n, ind, arr):
    
    if ind>=n:
        print(arr)
        return
        
    f_seq(coll, n, ind+1, arr.copy())
    arr.append(coll[ind])
    f_seq(coll, n, ind+1, arr.copy())
    
    

    
f_seq1([3,2,1], 3, 0, [])