# -*- coding: utf-8 -*-
"""

@author: MAQ
"""

def reverse(str1):
    if len(str1) == 1:
        return str1
    else:
        return reverse(str1[1:]) + str1[0] 
    
    
    
reverse('helloWorld')