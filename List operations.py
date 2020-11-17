# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 16:10:47 2020

@author: anwar
"""

                    # List Operations
                    
# Operations On Lists - ADD

# add elements to end of list with L.append(element)
# Mutates the list!

L = [2,1,3]
L.append(5)

# L is now [2,1,3,5]

# to combine lists together use concatenation, '+' Operator
# mutate list with L.extend(some_list)

L1 = [2,1,3]
L2 = [4,5,6]
L3 = L1 + L2 #L3 is [2,1,3,4,5,6]
L1.extend([0,6]) #Mutated L1 to [2,1,3,0,6]

# Operations on Lists - Remove

# range(5) -> equivalent to tuple [0,1,2,3,4]
# range(2,6) -> equivalent to tuple [2,3,4,5]
# range(5,2,-1) -> equivalent to tuple [5,4,3]

# When use range in a for loop, what the loop variable iterates
#over behaves like a list!

        for var in range(5):
            <expressions>
            
# behind the scnes, get converted to something that will behave like:
    
    for var in (0,1,2,3,4):
        <expressions>
        
