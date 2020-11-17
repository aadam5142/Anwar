# -*- coding: utf-8 -*-
"""
Created on Sun Oct 25 13:09:55 2020

@author: anwar
"""

#       Approximate Solution - cube root

cube = 27
# epsilon is how close you want to get to the answer
epsilon = 0.01
# guess is where we are going to start
guess = 0.0
# increment is the size of which the guess is incremented by
increment = 0.001  
# num_guesses keeps track of how many times the code went through the loop
num_guesses = 0 
while abs(guess**3 - cube) >= epsilon:
    guess += increment
    num_guesses += 1
print('num_guesses =', num_guesses)
if abs(guess**3 - cube) >= epsilon:
    print('Failed on cube root of', cube)
else:
    print(guess, 'is close to the cube root of', cube)
    