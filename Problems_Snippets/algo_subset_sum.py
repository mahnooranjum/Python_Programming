# -*- coding: utf-8 -*-

l = [1,5,6,3]
s = 8

import time

tic = time.perf_counter()

def subsetsum(l, s, n):
    if (s==0):
        return True
    
    if (n==0):
        return False

    if l[n]>s:
        return subsetsum(l, s, n-1)
    else:
        return subsetsum(l, s-l[n], n-1)


subsetsum(l, s, len(l)-1)

print(time.perf_counter() - tic)

