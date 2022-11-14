# Code by Tajrina Promela
# Date 13th November 2022, 2:18 PM
# Program that returns integers in a list occuring an odd number of times

def find_it(seq):
    freq = {} # New Dictionary
    for i in seq:
        count = freq.setdefault(i, 0)
        freq[i] += 1
    for item in freq:
        if freq[item] % 2 != 0:
            res = item
    return res
    
print(find_it([1,2,2,3,3,3,4,3,3,3,2,2,1]))
