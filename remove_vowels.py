# Code by Tajrina Promela
# Date 28th September 2022, 10:12 AM
# Program to remove the vowels in a string in Python

def remove_vowels(s):
    for i in s:
        if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
            s = s.replace(i, "")
        elif i == "A" or i == "E" or i == "I" or i == "O" or i == "U":
            s = s.replace(i, "")
    print(s)
    
remove_vowels(input("Enter a string: "))
