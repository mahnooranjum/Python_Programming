# -*- coding: utf-8 -*-
"""
Created on Sat Dec 17 20:02:52 2022

@author: MAQ
"""
import time
def timeme(function):
    def wrapper(*args, **kwargs):
        before = time.time()
        rval = function(*args, **kwargs)
        after = time.time()
        print(f"[INFO] {function.__name__} executed in {after-before} seconds")
        return rval
    return wrapper


@timeme
def function1(n):
    lister = list(range(n))
    for i in lister:
        for j in lister:
            print(f"{i} and {j}")
           
            

function1(100)