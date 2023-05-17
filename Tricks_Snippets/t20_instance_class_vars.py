# -*- coding: utf-8 -*-
"""
Created on Wed May 17 05:32:05 2023

@author: MAQ
"""

class Dog:
    num_legs = 4
    
    def __init__(self, name):
        self.name = name
        
        
jack = Dog('jack')
jill = Dog('jill')

print(jack.num_legs, jill.num_legs)

Dog.num_legs = 3

print(jack.num_legs, jill.num_legs)

Dog.num_legs = 4

print(jack.num_legs, jill.num_legs)

jack.num_legs = 6

print(jack.num_legs, jill.num_legs, Dog.num_legs, jack.__class__.num_legs)
