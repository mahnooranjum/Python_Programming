# -*- coding: utf-8 -*-
"""
Created on Thu Dec  9 09:06:33 2021

@author: MAQ
"""

def isAnagram1(str1, str2):
    str1 = str1.replace(' ', '')
    str2 = str2.replace(' ', '')
    return sorted(str1) == sorted(str2)


def isAnagram2(str1, str2):
    counter = {}
    for i in str1:
        if i in counter:
            counter[i] += 1
        else:
            counter[i] = 1
    for i in str2: 
        if i in counter:
            counter[i] -= 1
        else:
            counter[i] = -1
    for k, v in counter.items():
        if v != 0:
            return False
    
    return True
            
        


str1 = 'abcdefg'
str2 = 'gfdeabc'

isAnagram1(str1, str2)
isAnagram2(str1, str2)