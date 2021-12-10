# -*- coding: utf-8 -*-
"""

@author: MAQ
"""

class Node():
    def __init__(self, value):
        self.value = value
        self.next  = None
        
        
        
def reverser(node):
    cur = node
    prev = None
    nexter = None
    while (cur != None):
        nexter = cur.next
        cur.next = prev 
        prev = cur 
        cur = nexter
        
    return None
        
a = Node(1)
b = Node(2)  
c = Node(3)

a.next = b
b.next = c



reverser(a)

c.next.value