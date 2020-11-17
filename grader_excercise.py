# -*- coding: utf-8 -*-
"""
Created on Tue Nov 10 23:02:33 2020

@author: anwar
"""

#A regular polygon has n number of sides. Each side has length s.

#The area of a regular polygon is:  0.25∗n∗s2tan(π/n) 
#The perimeter of a polygon is: length of the boundary of the polygon
#Write a function called polysum that takes 2 arguments, n and s. This function should sum the area and square of the perimeter of the regular polygon. The function returns the sum, rounded to 4 decimal places.

import math 

def polysum(n,s):
    N = 0.25*n*(s**2)
    D = math.tan(math.pi/n)
    area = N/D
    perimeter = n*s
    return round((area + (perimeter**2)),4)
