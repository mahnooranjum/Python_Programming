# -*- coding: utf-8 -*-
"""
Created on Fri Dec 10 19:21:20 2021

@author: MAQ
"""

d1 = '2021-05-01-13-23-40'
d2 = '2021-05-01-9'


def getearly(d1, d2):
    for i,j in zip(d1.split('-'), d2.split('-')):
        if i>j:
            return d2
        if j>i:
            return d1
        if i==j:
            return d2 if len(d1) > len(d2) else d1
        
        
getearly(d1, d2)
        


        