# -*- coding: utf-8 -*-
"""
Created on Tue May 16 05:43:01 2023

@author: MAQ
"""

from collections import namedtuple


Car = namedtuple('Car', 'color model')

my_car = Car('red', 'toyota')


my_car._fields

my_car._asdict()

my_car._replace(color='blue')