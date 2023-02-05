# -*- coding: utf-8 -*-
"""
Created on Sun Dec 25 04:11:35 2022

@author: MAQ

Recursion:
    A function calls itself till a certain criterion is met

"""


def printer1(n, c):
    if c>n:
        return 
    
    print(f"Count {c}")
    c+=1
    printer1(n, c)
    
def printer2(n, c):
    if c>n:
        return 
    c+=1
    printer2(n, c)
    print(f"Count {c-1}")
    
    

    
    
printer2(10, 1)
    