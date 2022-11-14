# Code by Tajrina Promela
# Date 14th November 2022, 10:14 AM
# Program to find the difference in lists in Python

def array_diff(a, b):
    res = []
    for item in a:
        if item in b:
            continue
        else: 
            res.append(item)
    return res

print(array_diff([1,2,1], []))


# Doesn't work for cases with negative integers
'''def array_diff(a, b):
    digit = ''.join(map(str, b))
    strn = ''.join(map(str, a)) + ''.join(map(str, b))
    strn = strn.replace(digit, '') 
    res = list(map(int, str(strn)))
    return res''' 
    
# set() doesn't work because it counts duplicates that aren't to be subtracted as 1 digit
# Counter() doesn't work because it doesn't delete recurring elements 
# Method: Convert all to strings then delete and then map back (DIDN'T WORK)