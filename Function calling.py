# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 21:54:59 2020

@author: anwar
"""

def g(x):
    def h():
        x = 'abc'
    x = x + 1
    print('in g(x): x =', x)
    h()
    return x

x = 3
z = g(x)