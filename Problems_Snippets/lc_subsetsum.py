# -*- coding: utf-8 -*-
"""
Created on Sun Jan  1 06:27:44 2023

@author: MAQ
"""

class Solution:
    
    def call(self):
        arr = [2,3]
        n = len(arr)
        arr.sort(reverse=True)
        ans = []
        def func(idx, ds):
                       
            if idx==n:
                ans.append(sum(ds))
                return
            
            func(idx+1, ds)
            ds.append(arr[idx])
            func(idx+1, ds)
            ds.pop()
            
            
        func(0,[])
        print(ans)
        


sol = Solution()
sol.call()