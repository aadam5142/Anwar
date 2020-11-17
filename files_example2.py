# -*- coding: utf-8 -*-
"""
Created on Tue Nov 10 22:38:31 2020

@author: anwar
"""

nameHandle = open('kids', 'r')
for line in nameHandle:
    print(line)
nameHandle.close()