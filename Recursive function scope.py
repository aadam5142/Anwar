# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 23:35:28 2020

@author: anwar
"""

def fact(n):
    if n == 1:
        return 1
    else:
        return n*fact(n-1)

print(fact(4))