# -*- coding: utf-8 -*-
"""

@author: MAQ
"""

class Stack(object):
    def __init__(self):
        self.stack = []
    def push(self, value):
        self.stack.append(value)
    def peek(self):
        return self.stack[len(self.stack)-1]
    def pop(self):
        return self.stack.pop()

s = Stack()
s.push(10)
s.push(20)
s.peek()
s.pop()
s.peek()        