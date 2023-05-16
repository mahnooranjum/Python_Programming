# -*- coding: utf-8 -*-
"""
Created on Wed May 10 20:43:07 2023

@author: MAQ
"""

import time
def timeit(func):
    def wrapper():
        tic = time.time()
        original = func()
        print(f'Time of execution: {time.time()-tic} seconds')
        return original
    
    return wrapper
        

@timeit
def greet():
    return "Hello"


greet()