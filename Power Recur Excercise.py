# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 23:58:13 2020

@author: anwar
"""

#In Problem 1, we computed an exponential by iteratively executing successive multiplications. 
#We can use the same idea, but in a recursive function.

#Write a function recurPower(base, exp) which computes  baseexp  by recursively 
#calling itself to solve a smaller version of the same problem, and then multiplying the result by base to solve the initial problem.

#This function should take in two values - base can be a float or an integer;
# exp will be an integer  ≥0 . It should return one numerical value. 
#Your code must be recursive - use of the ** operator or looping constructs is not allowed.

def recurPower(base, exp):
    '''
    
    base: int or float 
    exp: int >= o
    
    returns: int or float, base^exp
   
    '''
    
    # Base case is when exp = 0
    if exp <= 0:
        return 1
    
    # Otherwise, exp must be > 0, so return 
    # base * base ^(exp-1). This is the recursive case.
    return base * recurPower(base, exp -1)
