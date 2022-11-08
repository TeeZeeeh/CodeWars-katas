# Code by Tajrina Promela
# Date 6th November 2022, 3:57 PM
# Program that returns the number of bits equal to one in binary from decimal

# Method 1
b = []
def count_bits(n):
    num = n
    for i in range(n):
        rem = num % 2
        b.append(rem)
        num = num//2
        if num == 0:
            break
    b.reverse()
    print(b)
    value = ''.join(str(v) for v in b)
    print(value)
    count = 0
    for i in b:
        if i == 1:
            count += 1
    return count
print(count_bits(1234))

print("\n")

# Method 2
def count_bits(n):
    b = bin(n)[2::]
    print(b)
    s = str(b)
    count = 0
    for i in s:
        if i == '1':
            count += 1
    return count

print(count_bits(1234))
