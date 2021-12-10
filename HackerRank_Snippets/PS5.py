# -*- coding: utf-8 -*-
"""
Created on Sat Jul 24 22:25:53 2021

@author: MAQ
"""

def staircase(n):
    # Write your code here
    for i in range(1,n+1):
        space = ' ' * (n-i)
        hashes= '#' * (i)
        print(space+hashes)
        
    return 

staircase(6)
        
        