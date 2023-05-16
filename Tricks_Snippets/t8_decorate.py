# -*- coding: utf-8 -*-
"""
Created on Wed May 10 09:56:36 2023

@author: MAQ
"""



def null_decorator(func):
    print("do something here")
    return func

def caps_decorator(func):
    print("pre-wrapper")
    def wrapper():
        print("in-wrapper")
        original = func()
        modified = original.upper()
        return modified
    
    return wrapper
        

@caps_decorator
def greet():
    return "Hello"


greet()

# greet = null_decorator(greet)

