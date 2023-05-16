# -*- coding: utf-8 -*-
"""
Created on Sun May  7 09:01:54 2023

@author: MAQ
"""

from contextlib import contextmanager


@contextmanager
def makeafile(name : str):
    try: 
        f = open(name, "w")
        yield f
        
    finally:
        f.close()    
        
        
with makeafile("./hello.txt") as f:
    f.write("hello world\n")
    f.write("i am me\n")
    
    