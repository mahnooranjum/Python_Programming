# -*- coding: utf-8 -*-
"""
Created on Sat May 13 06:50:10 2023

@author: MAQ
"""

import copy

x = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
y = x
z = list(x)
w = copy.deepcopy(x)

print(f"x == y = {x == y}")
print(f"x is y = {x is y}")
print(f"x == z = {x == z}")
print(f"x is z = {x is z}")
print(f"y == z = {y == z}")
print(f"y is z = {y is z}")
print(f"x == w = {x == w}")
print(f"x is w = {x is w}")

print(f"x[0] is z[0] = {x[0] is z[0]}")
print(f"y[0] == z[0] = {y[0] == z[0]}")
print(f"x[0] == w[0] = {x[0] == w[0]}")
print(f"x[0] is w[0] = {x[0] is w[0]}")


