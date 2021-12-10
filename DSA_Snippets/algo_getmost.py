# -*- coding: utf-8 -*-
"""
Created on Fri Dec 10 19:17:54 2021

@author: MAQ
"""

items = ['A', 'B', 'C', 'A']


def getmost(items):
    counter = {}
    for i in items:
        if i in counter:
            counter[i] = counter[i]+1
        else:
            counter[i] = 0
    return [max(counter, key=counter.get)]


getmost(items)