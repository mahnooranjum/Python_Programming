# -*- coding: utf-8 -*-
"""
Created on Mon Jan  2 05:35:09 2023

@author: MAQ
"""


class Solution:
    
    def call(self):
        n = 4
                
        def get_valids(grid, option):
            # IF NO QUEEN PLACED, TRUE
            if len(grid)==0:
                return True
            # IF SAME ROW, RETURN FALSE
            for i in grid: 
                if option[0] == i[0]:
                    return False
            # IF SAME COLUMN, RETURN FALSE
            for i in grid: 
                if option[1] == i[1]:
                    return False
            # IF ATTACK, RETURN FALSE
            for i in grid:
                """
                F-Diag = x+y   B-Diag = x-y 
                  | 0  1  2      | 0  1  2     
                --|---------   --|---------  
                0 | 0  1  2    0 | 0  1  2    
                1 | 1  2  3    1 |-1  0  1       
                2 | 2  3  4    2 |-2 -1  0   
                """
                if (option[0] - option[1] == i[0] - i[1]):
                    return False
                if (option[0] + option[1] == i[0] + i[1]):
                    return False
            
            return True
                
                
        def func(col, grid):
        # CHECK IF GOAL REACHED
            if col==n:
                print(grid)
                return
                
            # LOOP THROUGH CHOICES
            for i in range(n):
                # CHECK ALL ROWS OF COLUMN
                option = (i, col)
                # CHECK IF VALID
                if get_valids(grid, option):
                    
                    grid.append(option)
                    # BLUEPRINT #
                    func(col+1, grid)
                    ############
                    grid.pop()
                    
                
        func(0, [])
        


sol = Solution()
sol.call()