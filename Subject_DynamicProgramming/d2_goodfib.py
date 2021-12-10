# -*- coding: utf-8 -*-
"""
Created on Sun Feb  7 17:26:01 2021

@author: Mahnoor
"""

def fib(n, memo = {}):
    if n in memo:
        return memo[n]
    elif n <= 2:
        return 1
    else: 
        memo[n] = fib(n-1) + fib(n-2)
        return memo[n]
    
print(fib(50))
         