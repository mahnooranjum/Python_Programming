# -*- coding: utf-8 -*-
"""
Created on Fri Dec 10 13:05:40 2021

@author: MAQ
"""

class Node():
    def __init__(self, value):
        self.value = value
        self.next  = None
        
        
        
def checker(node):
    run1 = node
    run2 = node
    
    while (run2 != None and run2.next != None):
        run1 = run1.next
        run2 = run2.next.next
        if run1 == run2:
            return True
    return False
        
a = Node(1)
b = Node(2)  
c = Node(3)

a.next = b
b.next = c
c.next = a 


checker(a)