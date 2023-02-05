# -*- coding: utf-8 -*-
"""
Created on Sat Dec 31 07:20:48 2022

@author: MAQ
"""



class Solution:
    
    def call(self):
        arr =  [10,1,2,7,6,1,5]
        n = 7
        target = 8
        
        # Solution #####################################
        arr.sort()
        def func(target, idx, ds):
            
            if target==0:
                print(ds)
                return
            
            
            for i in range(idx, n):
                
                if i>idx and arr[i]==arr[i-1]:
                    continue
                if arr[i]>target:
                    break
                ds.append(arr[i])
                func(target-arr[i], i+1, ds)
                ds.pop()
                

            
        ################################################
        func(target, 0, [])
        
        

sol = Solution()
sol.call()