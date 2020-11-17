# -*- coding: utf-8 -*-
"""
Created on Sun Nov 15 16:36:30 2020

@author: anwar
"""

# Aliases

a = 1
b = a 
print(a)
print(b)

warm = ['red', 'yellow', 'orange']
hot = warm

hot.append('pink')

cool = ['blue', 'green', 'grey']
chill = ['blue', 'green', 'grey']
print(cool)
print(chill)

# cloning

cool = ['blue', 'green', 'grey']
chill = cool[:]

chill.append('black')
print(chill)
print(cool)

# Sorting Lists

# calling sort() mutates the list, returns nothing
# calling sorted() does not mutate list, must assign
# result to a variable

warm = ['red', 'yellow', 'orange']
sortedwarm = warm.sort()
print(warm)
print(sortedwarm)


cool = ['grey', 'green', 'blue']
sortedcool = sorted(cool)
print(cool)
print(sortedcool)

# Lists of Lists (Nested Lists)

# Can have nested lists
# side effects still possible after mutation

warm = ['yellow', 'orange']
hot = ['red']
brightcolors = [warm]
brightcolors.append(hot)
print(brightcolors)

hot.append('pink')
print(hot)

print(hot+warm)

# Mutation and iteration

#avoid mutating a list as you are iterating over it

def remove_dups(L1, L2):
    for e in L1:
        if e in L2:
            L1.remove(e)
            
L1 = [1,2,3,4]
L2 = [1,2,3,4]
remove_dups(L1, L2)

def remove_dups_new(L1, L2):
    L1_copy = L1[:]
    for e in L1_copy:
        if e in L2:
            L1.remove(e)
            
            






