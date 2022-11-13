# Code by Tajrina Promela
# Date 13th November 2022, 3:42 PM
# Program to find the like count from list

# Using .format()
def likes(names): 
    n = len(names)
    return {
        0: 'no one likes this',
        1: '{} likes this', 
        2: '{} and {} like this', 
        3: '{}, {} and {} like this', 
        4: '{}, {} and {others} others like this'
    } [min(4, n)].format(*names[:3], others = n-2)

print(likes(["Alex", "Jacob", "Mark", "Max"]))


# Long method 
def likes(name):
    if len(name) == 0:
        return 'no one likes this'
    elif len(name) == 1:
        return str(name[0]) + ' likes this'
    elif len(name) == 2:
        return str(name[0]) + ' and ' + str(name[1]) + ' like this'
    elif len(name) == 3:
        return str(name[0]) + ', ' + str(name[1]) + ' and ' + str(name[2]) + ' like this'
    elif len(name) > 3:
        return str(name[0]) + ', ' + str(name[1]) + ' and ' + str(len(name)-2) + ' others like this'

print(likes(["Alex", "Jacob", "Mark", "Max"]))
