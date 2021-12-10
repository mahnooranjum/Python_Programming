# -*- coding: utf-8 -*-
"""

@author: MAQ
"""
class Deque(object):
    def __init__(self):
        self.items = []
        
    def insert_first(self, value):
        self.items.insert(0, value)
        
    def peek_first(self):
        return self.items[0]
    
    def insert_last(self, value):
        self.items.append(value)
        
    def peek_last(self):
        return self.items[len(self.items)-1]
    


s = Deque()
s.insert_first(10)
s.insert_first(20)
s.insert_last(30)
s.peek_first()
s.peek_last()


