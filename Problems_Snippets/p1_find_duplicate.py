# -*- coding: utf-8 -*-
"""
Created on Wed Feb  1 23:55:47 2023

@author: MAQ
"""


# Better
def find_duplicate(arr):
    hasher = {}
    for i in arr:
        try:
            if hasher[i] == 1:
                return i
        except:
            hasher[i] = 1
      
# Optimal       
def find_duplicate_o(arr):
    slow = arr[0]
    fast = arr[0]
    
    slow = arr[slow]
    fast = arr[arr[fast]]
    while slow!=fast:
        slow = arr[slow]
        fast = arr[arr[fast]]
    
    fast = arr[0]
    
    while slow!=fast:
        slow = arr[slow]
        fast = arr[fast]
        
    return slow
    
        

print(find_duplicate_o([2,5,9,6,9,3,8,9,7,1]))