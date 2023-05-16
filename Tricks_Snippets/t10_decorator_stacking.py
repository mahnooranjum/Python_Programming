# -*- coding: utf-8 -*-
"""
Created on Thu May 11 06:40:49 2023

@author: MAQ
"""


def em(func):
    def wrapper():
        return "<em>" + func() + "</em>"
    return wrapper
    
def strong(func):
    def wrapper():
        return "<strong>" + func() + "</strong>"
    return wrapper
    
    
# @strong 
# @em 
def greet():
    return 'Hello World'

greet()

strong(em(greet))()