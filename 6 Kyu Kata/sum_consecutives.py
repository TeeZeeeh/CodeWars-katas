# Code by Tajrina Promela
# Date 9th November 2022, 1:03 PM
# Program to find the sum of consecutive numbers


# Shorter method using itertools library
from itertools import groupby
def sum_consecutives(s):
    return [sum(group) for ele, group in groupby(s)]
    # ele: unique elements, group: unique and recurring elements in single lists

print(sum_consecutives([1,4,4,0,4,3,3,1]))


# Longer method
def sum_consecutives(s):
    res = s[:1] # Easier way to initialize a list
    cursor = s[0]
    for i in s[1:]:
        if i == cursor:
            res[-1] += i
        else:
            res.append(i)
            cursor = i
    return res
    
print(sum_consecutives([1,4,4,0,4,3,3,1]))

