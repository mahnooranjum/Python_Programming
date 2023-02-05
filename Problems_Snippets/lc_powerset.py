# -*- coding: utf-8 -*-
"""
Created on Sat Dec 31 15:44:15 2022

@author: MAQ
"""

arr="abc"
n = 3

for i in range(0, (2**n)):
    sub = ""
    for k in range(0, n):
        if (i & (1<<k)) > 0:
            sub+=arr[k]
            
    print(sub)
    