# -*- coding: utf-8 -*-
"""
Created on Mon Dec 26 17:29:51 2022

@author: MAQ
"""

def swap(a, l, r):
    # Stop condition
    if l==r:
        return
    
    # Functionality
    temp = a[l]
    a[l] = a[r]
    a[r] = temp
    
    # Recursion
    swap(a, l+1, r-1)
    
    
    
def swape(a, i):
    # Stop condition
    n = len(a)-1
    if i>=(n/2):
        return
    
    # Functionality
    temp = a[i]
    a[i] = a[n-i]
    a[n-i] = temp

    # Recursion
    swape(a,i+1)
    
    
arr = [1,2,3,4,5]
r = len(arr)-1
l = 0
    
print(arr)
swape(arr,0)
print(arr)