#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 30 11:51:50 2022

@author: maq
"""
import os

path = './results/demo.something.com'
l_folders = list(os.listdir(path))

for i in l_folders:
    
    f = open(path+'/'+i+'/summary.txt')
    txt = f.readlines()
    for ele in txt:
        if 'Concurrency' in ele:
            c = ele
        if 'Requests per second' in ele:
            rps = ele
        if 'Complete requests' in ele:
            cr = ele
        if 'Failed requests' in ele:
            fr = ele
            
    