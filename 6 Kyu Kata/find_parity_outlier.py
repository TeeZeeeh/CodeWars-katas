# Code by Tajrina Promela
# Date 28th September 2022, 10:20 AM
# Program to find the parity outlier in Python

'''def find_outlier(integers):
    if integers[0] % 2 == 0 and integers[1] % 2 == 0:
        for i in integers[2::]:
            if i % 2 == 1:
                return i      
    elif integers[0] % 2 == 1 and integers[1] % 2 == 1:
        for i in integers[2::]:
            if i % 2 == 0:
                return i
    elif integers[-1] % 2 == 0 and integers[-2] % 2 == 0:
        for i in integers[:-2]:
            if i % 2 == 1:
                return i
    elif integers[-1] % 2 == 1 and integers[-2] % 2 == 1:
        for i in integers[:-2]:
            if i % 2 == 0:
                return i
    else: 
        for i in integers:
            if (i % 2 == 0 and i % 2 != 1) or (i % 2 == 1 and i % 2 != 0):
                return None 

list = []
list = [161, 3, 1719, 19, 11, 13, -21]
print(find_outlier(list))'''


integers = []

def find_outlier(integers):
    evens = []
    odds = []
    for i in integers:
        if i % 2 > 0:
            odds.append(i)
        if i % 2 == 0:
            evens.append(i)
    if len(evens) > len(odds):
        return odds[0]
    else:
        return evens[0]

print(find_outlier([160, 3, 1719, 19, 11, 13, -21]))
print(find_outlier([2, 4, 0, 100, 4, 11, 2602, 36]))
