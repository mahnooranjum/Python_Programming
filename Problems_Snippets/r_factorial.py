# -*- coding: utf-8 -*-
"""
Created on Mon Dec 26 02:51:08 2022

@author: MAQ
"""

def fact_parameterized(n, sum):
    if n < 1:
        print(sum)
        return
    
    fact_parameterized(n-1, sum*n)
    
    
def fact_functional(n):
    if n == 0:
        return 1
    
    return fact_functional(n-1) * n
    



fact_parameterized(10, 1)

print(fact_functional(10))
