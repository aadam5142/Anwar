# -*- coding: utf-8 -*-
"""
Created on Fri Oct  9 16:46:12 2020

@author: anwar
"""

#Assume s is a string of lower case characters.

#Write a program that prints the number of times the string 'bob' 
#occurs in s. For example, if s = 'azcbobobegghakl', then your 
#program should print

wordcount = 0
s = 'azcbobobegghakl'

for i in range(len(s)):
  # check to see if the substring accessed is equal to 'bob'
  if (s[i:i+3] == 'bob'):
      wordcount += 1
print("Number of times bob occurs is: " + str(wordcount))