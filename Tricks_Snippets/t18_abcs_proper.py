# -*- coding: utf-8 -*-
"""
Created on Tue May 16 04:42:00 2023

@author: MAQ
"""

from abc import ABCMeta, abstractmethod


class Base(metaclass=ABCMeta):
    @abstractmethod
    def foo(self):
        pass
        
    @abstractmethod
    def bar(self):
        pass
        

class Concrete(Base):
    def foo(self):
        return f"{Concrete.__name__} foo called"
    
    def bar(self):
        return f"{Concrete.__name__} bar called"
    
    

assert issubclass(Concrete, Base)
    
# b = Base()
# b.foo()

c = Concrete()
c.foo()
c.bar()