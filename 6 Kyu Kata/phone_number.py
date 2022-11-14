# Code by Tajrina Promela
# Date 14th November 2022, 11:38 AM
# Program to create phone numbers from list of numbers in Python

def create_phone_number(n):
    return '({}{}{}) {}{}{}-{}{}{}{}'.format(*n[:])

print(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))

a = [4,3,5,7,4]
b = [4]

print([i for i in a if i not in b])
