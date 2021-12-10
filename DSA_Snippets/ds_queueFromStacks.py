# -*- coding: utf-8 -*-
"""

@author: MAQ
"""

# class Stack(object):
#     def __init__(self):
#         self.stack = []
#     def push(self, value):
#         self.stack.append(value)
#     def peek(self):
#         if self.stack != []:
#             return self.stack[len(self.stack)-1]
#         else:
#             return []
#     def pop(self):
#         return self.stack.pop()
    
    
class Queue(object):
    def __init__(self):
        self.ins = []
        self.outs = []
        
    def enqueue(self, value):
        while self.ins != []:
            self.outs.append(self.ins.pop())
        self.ins.append(value)
        while self.outs != []:
            self.ins.append(self.outs.pop())
        
    def peek(self):
        return self.ins[-1]
    
    def dequeue(self):
        return self.ins.pop()
    
    

s = Queue()
s.enqueue(10)
s.enqueue(20)
s.peek()
s.dequeue()
s.peek()        