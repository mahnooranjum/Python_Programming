# -*- coding: utf-8 -*-
"""
Created on Sun Jul 25 22:40:39 2021

@author: MAQ
"""

def compareTriplets(a, b):
    # Write your code here
    bools = [1 for (x,y) in zip(a,b) if x > y]
    zeros = [1 for (x,y) in zip(a,b) if x == y]
    return [sum(bools), len(a) - sum(bools) - sum(zeros)]


a = [17, 28, 30]
b = [99, 16, 8]

print(compareTriplets(a, b))