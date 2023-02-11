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
for i in range(n):
    for j in (range(i+1,n)):
        if end[i] > start[j]:
            joiner.append([start[i],end[j]])

