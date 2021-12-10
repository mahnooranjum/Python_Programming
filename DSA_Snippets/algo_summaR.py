# -*- coding: utf-8 -*-
"""

@author: MAQ

"""

def getsumtill(n):
    if n == 0:
        return 0
    else: 
        return n + getsumtill(n-1)
    
    
getsumtill(4)