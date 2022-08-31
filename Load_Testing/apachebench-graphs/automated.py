#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 29 13:40:47 2022

@author: maq
"""



import subprocess 
 

for n in range(20000, 101000, 1000):
    if n==0:
        continue
    for multi in range(0, 100, 10):
        c = int(n*multi/1000)
        if c==0:
            continue
        linker = ""
        cmd = "./ab-graph.sh -u "+ linker + " -n " + str(n) + " -c " + str(c) + " -k"
        # cmd = "ab -l -n " + str(n) + " -c " + str(c) + " -k -g " + linker
        r = subprocess.check_output(cmd, shell=True, universal_newlines=True)
        print(r)

