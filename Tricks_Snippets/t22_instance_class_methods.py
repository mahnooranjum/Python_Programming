# -*- coding: utf-8 -*-
"""
Created on Sun May 21 15:24:05 2023

@author: MAQ
"""

class MyClass:
    def method(self):
        return 'instance method', self
    
    @classmethod
    def classmethod(cls):
        return 'class method', cls
    
    @staticmethod
    def staticmethod():
        return 'static method'
    
    
    
obj = MyClass()
obj.method()
obj.classmethod()
obj.staticmethod()
