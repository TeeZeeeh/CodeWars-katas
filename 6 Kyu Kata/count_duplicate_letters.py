# Code by Tajrina Promela
# Date 14th November 2022, 10:00 AM
# Program to count the number of duplicate letters in a string in Python

def duplicate_count(text):
    text = text.lower()
    freq = {}
    count = 0
    for item in text:
        freq.setdefault(item, 0)
        freq[item] += 1
    for item in freq:
        if freq[item] > 1:
            count += 1
    return count

print(duplicate_count('aabBcde'))
