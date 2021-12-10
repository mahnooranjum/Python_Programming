# -*- coding: utf-8 -*-
"""
Created on Sun Jul 25 23:05:42 2021

@author: MAQ
"""

def timeConversion(s):
    # Write your code here
    if 'PM' in s and s[:2] != '12':
        hh = int(s[:2])+12
        return str(hh)+s[2:-2]
    elif 'AM' in s and s[:2] == '12':
        return '00'+s[2:-2]        
    else:
        return s[:-2]
    
    
s = '12:05:39AM'
print(timeConversion(s))