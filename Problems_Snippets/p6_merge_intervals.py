#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  7 10:23:07 2023

@author: maq
"""
def key(ele):
    return ele[0]


arr = [[1,3], [8,10], [2,6], [15, 18]]
n = len(arr)
arr.sort(key=key)

length = [y-x for (x,y) in arr]
start = [x for (x,y) in arr]
end = [y for (x,y) in arr]

joiner = []
final_arr = list(arr)
for i in range(n):
    pair = [start[i], end[i]]
    for j in range(i+1,n):
        if start[j] < end[i]:
            pair[1] = end[j]
            if arr[j] in final_arr:
                final_arr.remove(arr[j])
            if arr[i] in final_arr:
                final_arr.remove(arr[i])
            
    if pair[1] == end[i]:
        pair = None
    
    if pair:
        final_arr.append(pair)

print(final_arr)

