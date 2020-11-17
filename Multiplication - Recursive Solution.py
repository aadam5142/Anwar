# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 23:34:22 2020

@author: anwar
"""

def mult(a, b):
    if b == 1:
        return a
    else:
        return a + mult(a, b-1)