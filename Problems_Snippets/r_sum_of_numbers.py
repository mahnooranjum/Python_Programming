# -*- coding: utf-8 -*-
"""
Created on Sun Dec 25 13:25:29 2022

@author: MAQ
"""

def sum_parameterized(n, sum):
    if n < 1:
        print(sum)
        return
    
    sum_parameterized(n-1, sum+n)
    
    
def sum_functional(n):
    if n < 1:
        return 0
    
    return sum_functional(n-1) + n
    



sum_parameterized(3, 0)

print(sum_functional(3))


    