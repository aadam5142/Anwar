# -*- coding: utf-8 -*-
"""
Created on Sun Oct 25 17:13:34 2020

@author: anwar
"""

# Floats and Fraction

num = 19

if num < 0:
    isNeg = True
    num = abs(num)

else:
    isNeg = False
result = ''
if num == 0:
    result = '0'
while num > 0:
    result = str(num%2)+result
    num = num//2
if isNeg:
    retult = '_' + result 
    