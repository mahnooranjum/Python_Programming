# -*- coding: utf-8 -*-


import time 

pr = [60, 100, 120]
wt = [10, 20, 30]
w = 50
n = len(pr)-1

tic = time.perf_counter()
def knapsack(wt, pr, w, n, memo={}):
    if (w,n) in memo:
        return memo[(w, n)]
    if (w==0) or (n==0):
        return 0
    if wt[n]>w:
        return knapsack(wt,pr, w, n-1)
    else:
        memo[(w,n)] = max(knapsack(wt,pr, w, n-1),\
                   pr[n]+knapsack(wt,pr, w-wt[n], n-1))
        return memo[(w,n)]


knapsack(wt, pr, w, n)
print(time.perf_counter() - tic)