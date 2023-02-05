# -*- coding: utf-8 -*-
"""
Created on Mon Dec 26 21:26:23 2022

@author: MAQ
"""

def func_palindrome(word, i, n):
    
    if i>=n/2:
        return True
    
    if word[i] != word[n-i-1]:
        return False
    else:
        return func_palindrome(word, i+1, n)
    

    

func_palindrome("modosm", 0, 6)
