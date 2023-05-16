# -*- coding: utf-8 -*-
"""
Created on Tue May  9 04:25:18 2023

@author: MAQ
"""

def yell(str_):
    return str_.upper() + '!!'


def greet(func):
    print(func("hello, how are you"))

yell("hello")
    
bark = yell 

bark("woof")

print(yell.__name__)
print(bark.__name__)


funcs = [yell, str.upper, str.lower, str.capitalize]
for f in funcs: 
    print(f("hello HELLO"))
    
    
funcs[0]("hello")


greet(yell)


list_ = ['hey', 'there', 'delilah']
list(map(print, list_))


def get_speaker(volume):
    def whisper(text):
        return text.lower()
    def yell(text):
        return text.upper()
    
    return yell if volume > 0.5 else whisper


get_speaker(0.4)("hello")



def get_speaker(volume, text):
    def whisper():
        return text.lower()
    def yell():
        return text.upper()
    
    return yell if volume > 0.5 else whisper


get_speaker(0.6, "hello")()