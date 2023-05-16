# -*- coding: utf-8 -*-
"""
Created on Tue May  9 05:33:05 2023

@author: MAQ
"""

class Adder:
    def __init__(self, n):
        self.n = n
        
    def __call__(self, x):
        return self.n + x 
    

plus_4 = Adder(4)
plus_4(3)