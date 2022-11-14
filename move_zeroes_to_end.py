# Code by Tajrina Promela
# Date 13th November 2022, 2:30 PM
# Program that recursively returns the sum of digits until it's a single digit in Python

def move_zeroes(lst):
    res = []
    zeroes = []
    for item in lst:
        if item == 0:
            zeroes.append(item)
        else:
            res.append(item)
    res.extend(zeroes)
    return res      

print(move_zeroes([1, 0, 1, 2, 0, 1, 3]))