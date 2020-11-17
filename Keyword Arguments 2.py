# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 23:04:50 2020

@author: anwar
"""

def printName(firstName, lastName, reverse = False):
    if reverse:
        print(lastName + ', ' + firstName)
    else:
        print(firstName, lastName)
    
printName('Anwar', 'Adam')
printName('Anwar', 'Adam', True)