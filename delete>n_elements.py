# Code by Tajrina Promela
# Date 7th November 2022, 5:38 PM
# Program that deletes occurrences of an element if it occurs more than N times

lis = [1,2,3,1,2,1,2,3]
count = 0
n = 2
a = 0
i = 1
j = 0

while i < len(lis):
    if lis[i] == lis[j]:
        count += 1
        while a < count:
            if count > n:
                print(lis[i])
                del lis[i]
                a += 1
        j += 1

    else:
        j += 1

    i += 1

print(lis)

