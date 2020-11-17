# -*- coding: utf-8 -*-
"""
Created on Tue Nov 10 22:33:30 2020

@author: anwar
"""

nameHandle = open('kids', 'w')
for i in range(2):
    name = input('Enter name: ')
    nameHandle.write(name + '\')
nameHandle.close()
