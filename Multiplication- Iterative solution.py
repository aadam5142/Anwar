# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 23:27:30 2020

@author: anwar
"""

# multiply a*b is equivalent to add a to itself b times
# capture state by
         #an itertion number(i) starts at b
         #i <- i -1 and stop when 0
# a current value of computation (result)
        # result <- result + a
        
def mult_iter(a,b):
    result = 0
    while b > 0:
        result += a
        b -= 1
    return result