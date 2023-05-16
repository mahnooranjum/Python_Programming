# -*- coding: utf-8 -*-
"""
Created on Thu May 11 20:04:01 2023

@author: MAQ
"""

class Car:
    """Doc string of car class"""
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage
        

class RedCar(Car): 
    """Doc string of red car class"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.color = 'red'
        
        
        
red_car = RedCar(color='blue', mileage=123)