# -*- coding: utf-8 -*-
"""
Created on Wed Jan 19 19:23:24 2022

@author: MAQ
"""

def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    if b==0:
        raise ValueError('division by zero')
    return a/b