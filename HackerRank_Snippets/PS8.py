# -*- coding: utf-8 -*-
"""
Created on Mon Jul 26 09:06:05 2021

@author: MAQ
"""




def gradingStudents(grades):
    # Write your code here
    return  [x + (5 - x % 5) if (x % 5) > 2 and x > 37 else x for x in grades]
    

grades = [73,67,38,33]
print(gradingStudents(grades))