# -*- coding: utf-8 -*-
"""
Created on Sat May 20 08:36:35 2023

@author: MAQ
"""

class Counting:
    num_instances = 0
    def __init__(self):
        # self.__class__.num_instances +=1
        self.num_instances +=1
        
        

c1 = Counting()
c2 = Counting()
c3 = Counting()

c3.__class__.num_instances
c3.num_instances
Counting().num_instances
Counting.num_instances
