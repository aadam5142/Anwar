# -*- coding: utf-8 -*-
"""
Created on Fri Oct 30 19:32:46 2020

@author: anwar
"""

def fib(x):
    """
    assumes x an int >= 0
    returns Fibonacci of x

    """
    if x == 0 or x == 1:
        return 1
    else:
        return fib(x-1) + fib(x-2)