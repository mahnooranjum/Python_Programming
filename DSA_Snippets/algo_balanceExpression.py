# -*- coding: utf-8 -*-
"""
Created on Fri Dec 10 00:16:26 2021

@author: MAQ
"""

class Stack(object):
    def __init__(self):
        self.stack = []
        
    def push(self, value):
        self.stack.append(value)
        
    def peek(self):
        if self.stack == []:
            return None
        return self.stack[len(self.stack)-1]
    
    def pop(self):
        return self.stack.pop()

openers = '{[('
mappers = {'{':'}', '(':')', '[': ']'}

str1 = '[{()}]'
str2 = '[{())}]'



def checker(string):
    s = Stack()
    for i in string:
        if str(s.peek()) in openers and i == mappers[s.peek()]:
            s.pop()
        else:
            s.push(i)
            
    return str(s.peek()) == 'None'

checker(str2)   