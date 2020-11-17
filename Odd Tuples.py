# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 16:05:48 2020

@author: anwar
"""

# Odd Tuples

#Write a procedure called oddTuples, which takes a tuple as input, 
#and returns a new tuple as output, where every other element of the input tuple is copied,
# starting with the first one. So if test is the tuple ('I', 'am', 'a', 'test', 'tuple'), 
#then evaluating oddTuples on this input would return the tuple ('I', 'a', 'tuple').

def oddTuples(aTup):
    '''
    aTup: a tuple
    
    returns: tuple, every other element of aTup.
    '''
    # a placeholder to gather our response
    rTup = ()
    index = 0
    
    # Idea: Iterate ove the elements in aTup, county by 2
    # (every other element) and adding that element to 
    # the result
    
    while index < len(aTup):
        rTup += (aTup[index],)
        index += 2
        
    return rTup