# Python from Scratch

from curses.ascii import isupper


print("Hi")

character_name = 'Promela' 
character_age = 22  # An int

print("I'm " + character_name + " and I'm " + str(character_age) + " years old.\n") 
# Convert int/float/double to a string using str().

# Strings in Python
phrase = "I love cakes."
print(phrase.isupper())
print(phrase.islower())
print(phrase.upper().isupper()) # Converts str to uppercase and then checks whether it's uppercase or not
print(len(phrase))
print(phrase[0])
print(phrase.index('c'))
print(phrase.index('love'))
print(phrase.replace("cakes", "chocolates"))
print("\n")

# Numbers in Python
from math import *

num = -5
print("Absolute value is " + str(abs(num)))
print("Floor value is " + str(floor(3.7)))
print("Ceil value is " + str(ceil(3.7)))
print("Round value is " + str(round(3.7)))

print("\nMax is " + str(max(3, 7)))
print("Min is " + str(min(3, 7)))

print("\nPower is " + str(pow(3, 3)))
print("Power is " + str(int(pow(3, 3))))
print("Square rooot is " + str(sqrt(65)))
print("Square rooot is " + str(int(sqrt(65))))
print("\n")

# Input in Python
'''name = input("\nEnter your name: ")
print("Your name is " + name)

print("The sum is " + str(3 + 5))

num1 = input("Enter a number: ")
num2 = input("Enter another number: ")

result = float(num1) + float(num2)
print(result)'''

# Lists in Python
friends = ['Kevin', 'Keira', 'Jim', 'Oscar', 'Toby']
print(friends[1])
print(friends[-1])
print(friends[1:3])
print(friends[1:])
print(friends[:1])
print(friends[-1:])
print(friends[:-1])
lucky_nums = [2, 4, 6, 7, 1, 0]
friends.extend(lucky_nums)
print(friends)
friends.append("Creed")
print(friends)
friends.insert(1, "Kelly")
print(friends)
friends.remove("Jim")
print(friends)
friends.pop()
print(friends)
print("Index is: " + str(friends.index("Kevin")))
friends.clear()
print(friends)
friends = ['Kevin', 'Keira', 'Jim', 'Jim', 'Oscar', 'Toby']
print("Count is: " + str(friends.count('Jim')))
lucky_nums.sort()
print(lucky_nums)
lucky_nums.reverse()
print(lucky_nums)
friends2 = friends.copy()
print(friends2)
print("\n")

# Tuples (Can not be modified)
coordinates = (4, 5)
print(coordinates[0])
coor = [5, 7] # List
print(coor)
coor[1] = 8 # Can be modified
print(coor[1])
coordinates = [(4, 5), (8, 9), (45, 67)] # List of Tuples
# We can't change the coordinates themselves but we can add/delete a coordinate.
print(coordinates)
print("\n")

#Functions in Python
def say_hi():
    print("Hello user")
print("Top")
say_hi()
print("Botom")

def say_hi(name, age):
    print("Hello " + name + ". You are " + age)
say_hi("Prom", "22")

def say_hi(name, age):
    print("Hello " + name + ". You are " + str(age))
say_hi("Prom", 22)

def cube(num):
    return num * num * num
# If we typed cube(3) alone, it returns the value but doesn't print it.
print(cube(3))

def cube(num):
    return num * num * num
    print("Code") # It won't print the code because after the 'return' statement, nothing is counted.
result = cube(4)
print(result)  

# If-statements in Python
is_female = True
if is_female:
    print("You are a female.")
else: 
    print("You are not a female.")

is_female = False
if is_female:
    print("You are a female.")
else: 
    print("You are not a female.")

is_female = True
is_Tall = False
if is_female or is_Tall:
    print("You are a female or tall or both.")
else: 
    print("You are not a female and neither tall.")

is_female = True
is_Tall = False
if is_female and is_Tall:
    print("You are a tall female.")
elif is_female and not(is_Tall):
    print("You are a short female.")
elif not(is_female) and is_Tall:
    print("You are not a female and are tall.")
else: 
    print("You are either not a female or not tall or both.")

print("\n")

# While loop in Python
i = 1
while i <= 10:
    print(i)
    i += 1
print("Done with loop.")

# Guessing game
'''secret_word = "Giraffe" # 1st method
guess = ""
guess_count = 0

while guess != secret_word and guess_count<3:
    guess = input("Enter secret word: ")
    if guess == secret_word:
        print("You win!")
    elif guess_count == 2 and guess != secret_word:
        print("You're out of tries.")
    guess_count += 1
   
secret_word = "Giraffe" # 2nd method
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False

while guess != secret_word and not(out_of_guesses):
    if guess_count < guess_limit:
        guess = input("Enter secret word: ")
        guess_count += 1
    elif guess_count == guess_limit:
        out_of_guesses = True

if out_of_guesses:
    print("Out of guesses, you lose!")
else:
    print("You win!")'''
print("\n")

# For Loops in Python
for index in range(10):
    print(index)
print("\n")

friends = ['Kevin', 'Keira', 'Jim', 'Jim', 'Oscar', 'Toby']

for friend in friends: # 1st method
    print(friend)
print("\n")

for index in range(len(friends)): # 2nd method
    print(friends[index])
print("\n")

for index in range(len(friends[0])):  # friends = 'Kevin'
    print(index)
print("\n")

# Exponents in Python
def raise_to_power(base_num, pow_num):
    result = 1
    for index in range(pow_num):
        result = result *base_num
    return result
    
print("The result is: " + str(raise_to_power(3, 3)))
print("\n")

# 2D lists (matrices) in Python
number_grid = [
    [0, 3, 5],
    [4, 7, 9],
    [2, 3, 6],
    [0]
]
print(number_grid[1][1])
print('\n')
for row in number_grid:
    print(row)
for col in number_grid[1]:
    print(col)
print('\n')
for row in number_grid:
    for col in row:
        print(col)

