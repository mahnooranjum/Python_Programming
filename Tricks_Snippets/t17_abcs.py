# -*- coding: utf-8 -*-
"""
Created on Tue May 16 04:34:43 2023

@author: MAQ
"""


class Base:
    def foo(self):
        raise NotImplementedError()
        
    def bar(self):
        raise NotImplementedError()
        

class Concrete(Base):
    def foo(self):
        return f"{Concrete.__name__} foo called"
    
    
# b = Base()
# b.foo()

c = Concrete()
c.foo()
c.bar()