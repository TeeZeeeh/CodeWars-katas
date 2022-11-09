# Code by Tajrina Promela
# Date 7th November 2022, 5:38 PM
# Program that deletes occurrences of an element if it occurs more than N times

lis = [1,1,2,3,1,2,1,2,1,3]
res = []
occurrences = {}
n = 2

for i in lis:
    count = occurrences.setdefault(i, 0)
    if count >= n:
        continue
    res.append(i)
    occurrences[i] += 1
    
print(res)