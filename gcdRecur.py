# -*- coding: utf-8 -*-
"""
Created on Fri Oct 30 19:28:37 2020

@author: anwar
"""

def gcdRecur(a, b):
    '''
    
    a, b: positive integers
    
    returns: a positve integer, the greatest common divisor of a & b.
    

    '''
    
    # Base case is when b = 0
    
    if b == 0:
        return a
    
    # Recursive case
    return gcdRecur(b, a % b)