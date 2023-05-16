# -*- coding: utf-8 -*-
"""
Created on Fri May 12 04:50:51 2023

@author: MAQ
"""

import time

class TimeIt:
    def __init__(self):
        pass
    
    def __enter__(self):
        self.tic = time.time()
        return None
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f'Time of execution: {time.time()-self.tic} seconds')
        return None
    
with TimeIt():
    time.sleep(1)