# -*- coding: utf-8 -*-
"""

@author: MAQ
"""

def seq_search_unord(l, el):
    itr = 0
    for i in l:
        itr = itr+1
        if i == el:
            return itr
    return False

def seq_search_ord(l, el):
    itr = 0
    for i in l:
        itr = itr+1
        if i > el:
            return False
        elif i == el:
            return itr
    return False


import random 
l = []
for i in range(10):
    n = random.randint(1,3000)
    l.append(n)

seq_search_unord(l, 462)

l.sort()
seq_search_ord(l, 462)
