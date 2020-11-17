
"""
Created on Sun Oct 25 18:06:36 2020

@author: anwar
"""

epilson = 0.01
y = 24.0
guess = y/2.0
numGuesses = 0 

while abs(guess*guess - y) >= epilson:
    numGuesses += 1
    guess = guess - (((guess**2) - y)/(2*guess))
print('numGuesses = ' + str(numGuesses))
print('Square root of ' + str(y) + ' is about ' + str(guess))
