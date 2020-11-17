# -*- coding: utf-8 -*-
"""
Created on Sun Nov 15 17:45:11 2020

@author: anwar
"""

# Generalization of Hops

# Python provides a general purpose HOP, map

# simple form - a unary funciton and a collection of 
#suitable arguments

map(abs, [1,-2,3,-4])

# produces an 'iterable', so need to walk down it

for elt in map(abs, [1,-2,3,-4]):
    print(elt)
[1,2,3,4]

#general form - an n-ary funciton and n collections
# of arguments

L1 = [1,28,36]
L2 = [2,57,9]
    for elt in map(min, L1, L2):
        print(elt)
    [1,28,9]