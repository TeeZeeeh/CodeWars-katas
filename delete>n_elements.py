# Code by Tajrina Promela
# Date 7th November 2022, 5:38 PM
# Program that deletes occurrences of an element if it occurs more than N times in Python

def delete_nth(order, max_e):
    result = []
    occurrences = {} # New Dictionary
    for i in order:
        count = occurrences.setdefault(i, 0)
        if count >= max_e:
            continue
        result.append(i)
        occurrences[i] += 1
    return result
    
print(delete_nth([1,1,3,3,7,2,2,2,2], 3))