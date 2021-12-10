# -*- coding: utf-8 -*-
"""

@author: MAQ
"""

class Queue(object):
    def __init__(self):
        self.items = []
    def enqueue(self, value):
        self.items.insert(0, value)
    def peek(self):
        return self.items[len(self.items)-1]
    def dequeue(self):
        return self.items.pop()

s = Queue()
s.enqueue(10)
s.enqueue(20)
s.peek()
s.dequeue()
s.peek()        