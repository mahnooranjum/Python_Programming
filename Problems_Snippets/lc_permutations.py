# -*- coding: utf-8 -*-
"""
Created on Sun Jan  1 12:03:32 2023

@author: MAQ

- with repetition
- without repetition

"""




class Solution:
    
    def call(self):
        arr = [1,2,3]
        n = len(arr)
        
        def func(idx, ds, used):
        # CHECK IF GOAL REACHED
            if idx==(n):
                print(ds)
                return
                
            # LOOP THROUGH CHOICES
            for i in range(n):
                # CHECK IF VALID
                if used[i] != 1: 
                    
                    ds.append(arr[i])
                    # BLUEPRINT #
                    used[i]+=1
                    func(idx+1, ds, used)
                    used[i]-=1
                    ############
                    ds.pop()
                    
           
        used = {k:0 for k in range(n)}
        func(0, [], used)
        


sol = Solution()
sol.call()