# -*- coding: utf-8 -*-
"""
Created on Sun May  7 05:31:02 2023

@author: MAQ
"""

def check(price, discount):
    old_price= price 
    price = price * (1 - discount)
    
    assert price > 0, ("price is smaller than 0")
    assert price < old_price, ("price isn't discounted")
    return price 


check(100, -1)