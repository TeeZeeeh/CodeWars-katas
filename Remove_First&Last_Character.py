# Code by Tajrina Promela
# Date 17th September 2022, 6:36 PM
# Program to remove the first and last characters in a string in Python

def remove_char(s):
    s = s[1:-1]
    return s

print(remove_char(input("Enter a string: ")))

# If the last character reoccurs in the string, only the first instance is removed.
'''def remove_char(s):
    s = s.replace(s[0], "", 1)
    s = s.replace(s[-1], "", 1)
    return s

print(remove_char("xofeypmzg"))'''



