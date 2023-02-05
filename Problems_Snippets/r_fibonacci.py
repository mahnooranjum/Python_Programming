# -*- coding: utf-8 -*-
"""
Created on Thu Dec 29 03:26:40 2022

@author: MAQ
"""

def func_fib(n):
    if n<=1:
        return n
    
    else:
        return func_fib(n-1) + func_fib(n-2)
    
    
    
func_fib(5)