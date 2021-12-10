# -*- coding: utf-8 -*-
"""
Created on Sun Jul 25 22:52:04 2021

@author: MAQ
"""

def birthdayCakeCandles(candles):
    # Write your code here
    max_val = max(candles)
    count = 0
    for i in candles: 
        if max_val == i:
            count = count + 1
        else: 
            pass
    return count

candles = [3, 2, 1, 3]

print(birthdayCakeCandles(candles))