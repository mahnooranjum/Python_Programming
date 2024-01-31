# -*- coding: utf-8 -*-
"""
Created on Sat Jun  3 16:24:26 2023

@author: MAQ
"""

class Person:
    def __init__(self, name, degree):
        self.name = name
        self.degree = degree
    def __repr__(self):
        return f'Person({self.name!r}, {self.degree!r})'
    
    @classmethod 
    def engineer(cls,name):
        return cls(name,'Engineer')
    
    @classmethod 
    def doctor(cls,name):
        return cls(name,'Doctor')
    
    
engr = Person.engineer("mahnoor")
        