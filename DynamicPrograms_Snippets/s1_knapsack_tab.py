# -*- coding: utf-8 -*-


import time 

pr = [60, 100, 120]
wt = [10, 20, 30]
w = 50
n = len(pr)

tic = time.perf_counter()
def knapsack(wt, pr, w, n, tab={}):
    profit = 0
    for i in range(n):
        for j in wt:
            if (i==0 or j==0):
                tab[(i, j)] = 0
            elif (wt[i-1] > j):
                tab[(i,j)] = tab[(i-1, j)]
            else:
                tab[(i,j)] = max(tab[(i-1, j)], pr[i] + tab[(i-1, j)])
    return tab 


knapsack(wt, pr, w, n)
print(time.perf_counter() - tic)