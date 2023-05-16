# -*- coding: utf-8 -*-
"""
Created on Fri May 12 08:00:53 2023

@author: MAQ
"""

class NameTooShort(ValueError):
    pass


def validate(name):
    if len(name)<10:
        raise NameTooShort(name)
        
        
print(validate('12'))