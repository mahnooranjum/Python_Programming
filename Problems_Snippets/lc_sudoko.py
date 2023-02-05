#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  2 11:13:14 2023

@author: maq
"""

class Solution:

    def call(self):
        board = [["5","3",".",".","7",".",".",".","."],\
                 ["6",".",".","1","9","5",".",".","."],\
                 [".","9","8",".",".",".",".","6","."],\
                 ["8",".",".",".","6",".",".",".","3"],\
                 ["4",".",".","8",".","3",".",".","1"],\
                 ["7",".",".",".","2",".",".",".","6"],\
                 [".","6",".",".",".",".","2","8","."],\
                 [".",".",".","4","1","9",".",".","5"],\
                 [".",".",".",".","8",".",".","7","9"]]

        
        def isvalid(board, idx_r, idx_c, value):
            # idx_r = 1
            # idx_c = 1            
            # if ROW has number, return FALSE
            row = board[idx_r]
            if str(value) in row:
                return False 
            
            # if COLUMN has number, return FALSE
            col = [x[idx_c] for x in board]
            if str(value) in col:
                return False
                    
            for c in range(idx_c-(idx_c%3), (idx_c-(idx_c%3))+3 ):
                for r in range(idx_r-(idx_r%3), (idx_r-(idx_r%3))+3 ):
                    if str(value) == board[r][c]:
                        return False
                
            
            return True
            
        def func(board):

            for r in range(9):
                for c in range(9):
                    if board[r][c] == ".":
                                
                        for value in range(1,10):
                            if isvalid(board, r, c, value):
                                
                                board[r][c] = str(value)
                                
                                if (func(board) == True):
                                    return True
                                
                                else:
                                    board[r][c] = "."
                    
                        return False
                                
            
            
            return True
                    

            
        
        
        func(board)
        print(board)
        


sol = Solution()
sol.call()