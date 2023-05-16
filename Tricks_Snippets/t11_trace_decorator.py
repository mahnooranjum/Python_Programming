# -*- coding: utf-8 -*-
"""
Created on Thu May 11 07:11:39 2023

@author: MAQ
"""

import functools 
def trace(func):
    # @functools.wraps(func)
    def wrapper(*args, **kwargs):
        """The functools wrapper copies the metadata"""
        
        print(f'TRACE: calling {func.__name__}() '
        f'with {args}, {kwargs}')
        original_result = func(*args, **kwargs)
        print(f'TRACE: {func.__name__}() '
        f'returned {original_result!r}')
        return original_result
    return wrapper



@trace
def greet(str_):
    """Returns a greetings"""
    return str_.capitalize() + "!!"


greet("hello")