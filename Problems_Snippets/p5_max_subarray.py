#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  6 11:03:29 2023

@author: maq
"""

def maxsubarr(arr):
    
    arr = [-2,-3,4,-1,-2,1,5,-3]
    n = len(arr)
    
    max_sum = 0
    for i in range(n):
        
        for j in range(i,n):
            sub_arr = arr[i:j+1]
            cur = sum(sub_arr)
            # print(sub_arr)
            if cur>max_sum:
                combo = sub_arr
                max_sum=cur


def kadane(arr):
    
    arr = [-2,-3,4,-1,-2,1,5,-3]
    n = len(arr)
    
    cur = 0
    max_sum = float('-inf')
    for i in range(n):
        cur = cur + arr[i]
        if cur<arr[i]:
            cur = arr[i]
            
        if max_sum < cur:
            max_sum = cur
        