# -*- coding: utf-8 -*-
"""
Created on Fri Oct 30 00:03:41 2020

@author: anwar
"""

def mult_iter(a,b):
    result = 0
    while b > 0 :
        b -= 1
    return result 

def mult(a,b):
    if b == 1:
        return a
    else:
        return a + mult(a, b-1)