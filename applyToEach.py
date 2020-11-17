# -*- coding: utf-8 -*-
"""
Created on Sun Nov 15 17:30:23 2020

@author: anwar
"""

def applyToEach(L, f):
    """assumes L is a list, f a function mutates L by 
    replacing each element, e, of L by f(e)"""
    
    for i in range(len(L)):
        L[i] = f(L[i])
        
L = [1,-2,3.4]ArithmeticError
applyToEach(L, abs)
applyToEach(L, int)
applyToEach(L, fact)
applyToEach(L, fib)

        
        