# Code by Tajrina Promela
# Date 13th November 2022, 2:30 PM
# Program that recursively returns the sum of digits until it's a single digit

def digital_root(n):
    condition = True
    sum = 0
    while condition:
        while n:
            sum += n % 10
            n //= 10
        result = sum # Return variable before next iteration 
        n = sum
        sum = 0
        condition = n > 9 # Not if there is no last digit
    return result

print(digital_root(493193))
