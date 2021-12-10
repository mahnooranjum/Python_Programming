# -*- coding: utf-8 -*-
"""
Created on Sat Feb  6 21:30:33 2021

@author: Mahnoor
"""

def fib(n):
    if n <= 2:
        return 1
    else: 
        return fib(n-1) + fib(n-2)
    
print(fib(20))
         