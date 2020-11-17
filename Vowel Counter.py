# -*- coding: utf-8 -*-
"""
Created on Fri Oct  9 16:05:42 2020

@author: anwar
"""

#Assume s is a string of lower case characters.

#Write a program that counts up the number of vowels contained 
#in the string s. Valid vowels are: 'a', 'e', 'i', 'o', and 'u'.
# For example, if s = 'azcbobobegghakl', your program should print:
    
vowelCount = 0
s = 'jaieksier'

for letter in s:
    if letter == "a":
        vowelCount += 1
    
    elif letter == "e":
        vowelCount += 1
        
    elif letter == "i":
        vowelCount += 1
    
    elif letter == "o":
        vowelCount += 1
    
    elif letter == "u":
        vowelCount += 1

print("Number of vowels: " + str(vowelCount))
    
