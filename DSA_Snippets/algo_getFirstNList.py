# -*- coding: utf-8 -*-
"""
Created on Fri Dec 10 13:59:12 2021

@author: MAQ
"""

class Node():
    def __init__(self, value):
        self.value = value
        self.next  = None
        
        
def getfirst(node, n):
    cur = node
    for i in range(n):
        if (cur != None):
            print(cur.value)
            cur = cur.next
        
a = Node(1)
b = Node(2)  
c = Node(3)
d = Node(4)
e = Node(5)
f = Node(6)

a.next = b
b.next = c
c.next = d
d.next = e
e.next = f


getfirst(a, 8)
