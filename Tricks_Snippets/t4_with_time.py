# -*- coding: utf-8 -*-
"""
Created on Sun May  7 10:21:48 2023

@author: MAQ
"""


import time 
from contextlib import contextmanager


@contextmanager
def timeit():
    try: 
        t = time.time()
        yield t
        
    finally:
        print(f'Time of execution: {time.time()-t} seconds')
        
        
with timeit():
    time.sleep(1)
    
    