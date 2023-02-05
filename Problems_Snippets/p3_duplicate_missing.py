# -*- coding: utf-8 -*-
"""
Created on Sat Feb  4 19:29:17 2023

@author: MAQ
"""

def find(arr, n):

    summa = int((n*(n+1))/2)
    hasher = {}
    summer = 0
    for i in arr:
        summer+=i
        try: 
            if (hasher[i] == 1):
                duplicate = i
        except:
            hasher[i] = 1
    
    summer = summer - duplicate
    missing = summa - summer 
        
    return {"message": f"duplicate = {duplicate}, missing = {missing}"}
   

def findxor(arr, n):
    
    temp = arr[0]
    for i in arr[1:]:
        temp = temp^i
        
    xor = 1
    for i in range(2,n+1):
         xor = xor^i   
         
    xor = xor ^ temp 
    
    # bucket with set x 
    bx = []
    by = []
    for i in arr:
        if (i & xor) == xor:
            bx.append(i)
        else:
            by.append(i)
        

    yer = list(range(1, xor)) + by
    xer = list(range(xor, n+1)) + bx 

    y = yer[0]
    for i in yer[1:]:
         y = y^i   

    x = xer[0]
    for i in xer[1:]:
         x = x^i   

    return {"message": f"duplicate = {y}, missing = {x}"}
    

arr = [4,3,6,1,1,2]
n = 6
find(arr, n)
    