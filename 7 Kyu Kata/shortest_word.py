# Code by Tajrina Promela
# Date 28th September 2022, 10:02 AM
# Program to find the length of the shortest word in a string in Python

def shortest_word(s):
    mins = min(len(i) for i in s.split())
    print(mins)

shortest_word(input("Enter a string: "))