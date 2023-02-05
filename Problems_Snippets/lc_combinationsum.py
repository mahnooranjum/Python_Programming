# -*- coding: utf-8 -*-
"""
Created on Sat Dec 31 06:59:38 2022

@author: MAQ
"""


class Solution:
    
    def call(self):
        arr = [2,3,6,7]
        n = 4
        target = 7
        
        # Solution #####################################
        
        def func(target, idx, ds):
            if idx>=n:
                if target==0:
                    print(ds)
                return
            
            if target>=arr[idx]:
                ds.append(arr[idx])
                func(target-arr[idx], idx, ds)
                ds.pop()
            
            func(target, idx+1, ds) 
            
        ################################################
        func(target, 0, [])
        
        

sol = Solution()
sol.call()