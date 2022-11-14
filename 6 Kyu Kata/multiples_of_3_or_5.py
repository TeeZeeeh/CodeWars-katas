# Code by Tajrina Promela
# Date 27th October 2022, 3:00 AM
# Program to find the multiples of 3 or 5 in Python

multiples = []
def solution(number):
    i = 1
    while i < number:
        if (3*i) < number:
            n = 3*i
            multiples.append(n)
        if (5*i) < number:
            n = 5*i
            multiples.append(n)
        i += 1
    return multiples # finding multiples of 3 or 5

print(solution(20))

res = []
for p in multiples: # removing duplicates
    if p not in res:
        res.append(p)
print(res)

a = 0
for index in res: # summing multiples
        a = a + index
print(a)


'''def solution(number):
    multiples = []
    i = 1
    while i < number:
        if (3*i) < number:
            n = 3*i
            multiples.append(n)
        if (5*i) < number:
            n = 5*i
            multiples.append(n)
        i += 1
    res = []
    for p in multiples:
        if p not in res:
            res.append(p)
    a = 0
    for index in res:
        a = a + index
    return a

print(solution(5))'''


