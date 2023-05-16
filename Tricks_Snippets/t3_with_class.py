# -*- coding: utf-8 -*-
"""
Created on Sun May  7 09:07:15 2023

@author: MAQ
"""

class MakeFile:
    def __init__(self, name):
        self.name = name
        
    def __enter__(self):
        self.file = open(self.name, 'w')
        return self.file
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()   
            
with MakeFile("file.txt") as f:
    f.write("hello world\n")
    f.write("this has to end\n")